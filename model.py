#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This collects routines for setting up the model.

Created on Tue Oct 29 17:01:07 2019

@author: egorkozlov
"""


#from platform import system

import numpy as np
from timeit import default_timer
#from numba import njit, vectorize
#from memory_profiler import profile
#from IPython import get_ipython
#from asizeof import asizeof
import os
import psutil


#if system() != 'Darwin':
from setup import ModelSetup
from solver_couples import v_iter_couple
from solver_singles import v_iter_single, v_iter_single_mom
from integrator_singles import ev_single, ev_single_k
from integrator_couples import ev_couple_m_c


class Model(object):
    def __init__(self,iterator_name='default',verbose=False,**kwargs):
        self.mstart = self.get_mem()
        self.mlast = self.get_mem()
        self.verbose = verbose
        self.setup = ModelSetup(**kwargs)
        self.dtype = self.setup.dtype
        self.iterator, self.initializer = self._get_iterator(iterator_name)
        self.start = default_timer()
        self.last = default_timer()        
        self.time_dict = dict()        
        self.solve()
        
    def get_mem(self):
        return psutil.Process(os.getpid()).memory_info().rss/1e6
        
        
    def time(self,whatisdone,verbose=True,time_lb=0.5):
        
        total_time = default_timer() - self.start
        last_time = default_timer() - self.last
        
        total_mem = self.get_mem()
        last_mem  = self.get_mem() - self.mlast
        
        def r(x): return round(x,2)
        
        if last_time > time_lb:
            if verbose: print('{} is done in {} sec, total {} sec, memory used is {} Mb'.format(whatisdone,r(last_time),r(total_time),r(total_mem)))
        self.last = default_timer()
        self.mlast = self.get_mem()
        
        if whatisdone in self.time_dict:
            self.time_dict[whatisdone] = self.time_dict[whatisdone] + [last_time]
        else:
            self.time_dict[whatisdone] = [last_time]
        
    def time_statistics(self,remove_worst=True,remove_single=False):
        
        print('Total time is {}'.format(default_timer() - self.start))
        for what, timelist in self.time_dict.items():
            
            if remove_single and len(timelist) == 1: continue
            
            time_arr = np.array(timelist)
            
            extra = ''
            if remove_worst and time_arr.size > 1:
                time_worst = time_arr.max()
                time_arr = time_arr[time_arr<time_worst]
                extra = ' (excl the worst)'
                
            av_time = round(np.mean(time_arr),2) 
            tot_time = round(np.sum(np.array(timelist)),2) 
            print('On average {} took {}, total {} sec'.format(what,av_time,tot_time,extra))
            
    
    def _get_iterator(self,name='default'):
        # this thing returns two functions: iterate and initialize
        # it can put a timer inside of them
        # it can also do many other things potentially
        
        
        # this is not the best organization but kind of works
        # this allows to use different methods for iteration/initialization
        # as long as they all are specified here or imported
        
        # first we define the iterator
         
        def v_iterator(setup,desc,t,EV=None):
            # this takes integrated future type-specific value function and returns
            # this period value function. Integration is done separately.
            # If None is feeded for EV this assumes that we are in the last period
            # and returns last period value
            #get_ipython().magic('reset -sf')
            
            ushift = self.setup.utility_shifters[desc]
            
            if desc == 'Female, single' or desc == 'Male, single':
                female = (desc == 'Female, single')
                
                V, c, s = v_iter_single(setup,t,EV,female,ushift)       
                assert V.dtype == c.dtype == setup.dtype
                return {desc: {'V':V,'c':c,'s':s,'x':0.0*c}}   
             
            elif desc== 'Couple and child' or desc == 'Couple, no children':
                haschild = (desc== 'Couple and child')
                
                V, VF, VM, c, x, s, fls, V_all_l = v_iter_couple(setup,t,EV,ushift,haschild)  
                assert V.dtype == VF.dtype == c.dtype == setup.dtype
                
                return {desc: {'V':V,'VF':VF,'VM':VM,'c':c,'x':x,'s':s,'fls':fls}}
            elif desc == 'Female and child':
                
                V, c, x, s, fls, V_all_l = v_iter_single_mom(setup,t,EV,ushift)
                assert V.dtype == c.dtype == setup.dtype
                return {desc: {'V':V,'c':c,'x':x,'s':s,'fls':fls}}
            else:
                raise Exception('I do not know this type...')
            
        # and the integrator   
        
        def v_integrator(setup,desc,t,V_next):
            
            if desc == 'Female, single' or desc == 'Male, single':
                female = (desc == 'Female, single')
                EV, dec = ev_single(setup,V_next,female,t)
                assert EV.dtype == setup.dtype
            elif desc == 'Couple and child':
                EV, dec = ev_couple_m_c(setup,V_next,t,True)
                assert EV[0].dtype == EV[1].dtype == EV[2].dtype ==  EV[3].dtype ==setup.dtype
            elif desc == 'Couple, no children':
                EV, dec = ev_couple_m_c(setup,V_next,t,False)
                assert EV[0].dtype == EV[1].dtype == EV[2].dtype == EV[3].dtype == setup.dtype
            elif desc == 'Female and child':
                EV, dec = ev_single_k(setup,V_next,t)
                assert EV.dtype == setup.dtype
            else:
                raise Exception('I do not know this type...')
            return EV, dec
            
        
        
        # then we wrap them into two routines  
        
        if name == 'default' or name == 'default-timed':
            timed = (name == 'default-timed')
            def iterate(desc,t,Vnext):
                EV, dec = v_integrator(self.setup,desc,t,Vnext)
                if timed: self.time('Integration for {}'.format(desc))
                vout = v_iterator(self.setup,desc,t,EV)
                if timed: self.time('Optimization for {}'.format(desc))
                
                self.wrap_decisions(desc,dec,vout)
                if timed: self.time('Wrapping at iter for {}'.format(desc))
                
                return vout, dec
            def initialize(desc,t):
                vout = v_iterator(self.setup,desc,t,None)
                if timed: self.time('Initialization for {}'.format(desc))
                dec = {}
                self.wrap_decisions(desc,dec,vout)
                if timed: self.time('Wrapping at iter for {}'.format(desc))
                
                return vout, dec
        else:
            raise Exception('unsupported name')
            
            
            
        return iterate, initialize
    
    def wrap_decisions(self,desc,dec,vout):
        # This interpolates consumption, savings and labor supply decisions
        # on fine grid for theta that is used for integration and simulations.
        pass
        '''
        v = vout[desc]
        if desc == 'Couple and child' or desc == 'Couple, no children':
            
            #cint = self.setup.v_thetagrid_fine.apply(v['c'],axis=2)
            #sint = self.setup.v_thetagrid_fine.apply(v['s'],axis=2)
            
            #Vint = self.setup.v_thetagrid_fine.apply(v['V_all_l'],axis=2)
            
            #xint = self.setup.v_thetagrid_fine.apply(v['x'],axis=2)
            #cint = self.setup.v_thetagrid_fine.apply(v['c'],axis=2)
            #assert sint.dtype == Vint.dtype == xint.dtype == self.setup.dtype
            
            #if Vint.ndim < 4: Vint = Vint[:,:,:,None]
            
            #fls = Vint.argmax(axis=3).astype(np.int8)
            
            
            
            #dec.update({'s':sint,'fls':fls,'x':v['x'],'c':v['c']})
            #del sint, fls
        elif desc == 'Female and child':
            #dec.update({'s':v['s'],'fls':v['fls'],'x':v['x'],'c':v['c']})
        else:
            #xx = np.broadcast_to(0.0,v['s'].shape) # this saves memory a bit
            #dec.update({'s':v['s'],'x':xx,'c':v['c']})
            del v
        '''
    
    def solve(self,save=False):
        
        show_mem = self.verbose
        
        T = self.setup.pars['T']
        self.V = list()
        self.decisions = list()
        
        
        for t in reversed(range(T)):
            Vnow = dict()
            decnow = dict()
            
            Vnext = self.V[0] if t<T-1 else None
            
            for desc in self.setup.state_names:
                if t == T-1:
                    V_d, dec = self.initializer(desc,t)
                else:
                    V_d, dec = self.iterator(desc,t,Vnext)   
                   
                Vnow.update(V_d)
                decnow.update({desc:dec})
                
            self.V = [Vnow] + self.V
            self.decisions = [decnow] + self.decisions
            

            
            if show_mem:
                print('The size of V is {} giga'.format(asizeof(self.V)/1000000000))
                print('The size of decisions is {} giga'.format(asizeof(self.decisions)/1000000000))
        if save:
            import pickle
            pickle.dump(self,open('model_save.pkl','wb+'))
        
        
    def x_reshape(self,x,t):
        # this reshapes couple's values to multidimensional objects
        ss = self.setup
        
        shp = (ss.na,ss.pars['n_zf_t'][t],
                              ss.pars['n_zm_t'][t],
                              ss.pars['n_psi_t'][t],
                              x.shape[-1])
        
        x_reshape = x.reshape(shp)
        return x_reshape
    
        
    #def graph(self,ai,zfi,zmi,psii,ti,thi):        
    #    #Draw some graph of Value and Policy Functions
    #    V=graphs(self,ai,zfi,zmi,psii,ti,thi)        
    #    return V
    
    def get_graph_values(self,fun='V',dec=False,iassets=slice(None),iexo=slice(None),itheta=slice(None),*,state,t):
        Vin = self.V[t][state][fun] if not dec else self.decisions[t][state][fun]
        
        if fun == 'fls': Vin = self.setup.ls_levels[state][Vin]
        
        if fun == 'thetas':
            Vin_old = Vin
            Vin = self.setup.thetagrid_fine[Vin]
            Vin[Vin_old==-1] = None
        
        
        
        has_theta = (Vin.ndim == 3)
        
        if type(iexo) is tuple:
            Vin = self.x_reshape(Vin,t)
            ind = (iassets,) + iexo
        else:
            ind = (iassets,iexo)
        
        agrid = self.setup.agrid_c if has_theta else self.setup.agrid_s
        if has_theta:
            exogrids = (self.setup.exogrid.zf_t[t],self.setup.exogrid.zm_t[t],self.setup.exogrid.psi_t[t])
        else:
            if state == 'Female, single' or state == 'Female and child':
                exogrids = (self.setup.zf_t[t],)
            else:
                exogrids = (self.setup.zm_t[t],)
        thetagrid = ((self.setup.thetagrid,) if not dec else (self.setup.thetagrid_fine,)) \
                            if has_theta else tuple()        
        grids = (agrid,) + exogrids + thetagrid
        
    
        
        if has_theta: ind = ind+(itheta,)
        
        grid_out = None
        
        for num, ii in enumerate(ind):
            if ii == slice(None): grid_out = grids[num]
        
        return grid_out, Vin[ind]
    
    
    def diagnostics(self):
        #from diagnostics import check_value_functions
        #check_value_functions(self)
        
        from graphs import v_graphs
        v_graphs(self)
        
    def mar_graphs(self):
        from mar_graphs import mar_graphs
        mar_graphs(self)
        
      
        
    
