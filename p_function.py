#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:07:47 2019

@author: egorkozlov
"""
from time import sleep
from main import mdl_resid
import numpy as np
from tiktak import filer


#def mdl_resid(x=(0,)):
#    sleep(1)
#    print('hi, my x is {}'.format(x))
#    #if np.random.random_sample()>0.8: raise Exception('oh')
#    return sum([i**2 for i in x])


def fun(x):
    assert type(x) is tuple, 'x must be a tuple!'
    
    action = x[0]
    args = x[1]
    
    assert type(action) is str, 'x[0] should be string for action'
    assert len(x) <= 2, 'too many things in x! x is (action,agrs)'
    
    
    if action == 'test':
        return mdl_resid()
    elif action == 'compute':
        return mdl_resid(args)
    elif action == 'minimize':	
        
        import dfols
        
        i, N_st, lb, ub = args
        
        #Sort lists
        def sortFirst(val): return val[0]
        
        #Get the starting point for local minimization
        
            
        #Open File with best solution so far
        param=filer('wisdom.pkl',0,False)
             
        param.sort(key = sortFirst)
        print('f best so far is {} and x is {}'.format(param[0][0],param[0][1]))
        xm=param[0][1]
        
        #Get right sobol sequence point
        xt=filer('sobol.pkl',None,False)
        
        #Determine the initial position
        dump=min(max(0.1,((i+1)/N_st)**(0.5)),0.995)
        
        xc=dump*xm+(1-dump)*xt[:,i]
        xc=xc.squeeze()
        
        
        
        def q(pt):
            try:
                ans = mdl_resid(pt,return_format=['scaled residuals'])[0]
            except:
                print('During optimization function evaluation failed at {}'.format(pt))
                ans = np.array([1e6])
            finally:
                return ans
            
            
            
        res=dfols.solve(q, xc, rhobeg = 0.1, rhoend=1e-4, maxfun=100, bounds=(lb,ub))
        
        print(res)
        
        fbest = mdl_resid(res.x)[0] # in prnciple, this can be inconsistent with
        # squared sum of residuals
        
        
        print('fbest is {} and res.f is {}'.format(fbest,res.f))
        
        print('Final value is {}'.format(fbest))   
        
        param_new = filer('wisdom.pkl',None,False)
        
        param_write = param_new+[(fbest,res.x)]
        
        #Save Updated File
        param_write.sort(key=sortFirst)
        filer('wisdom.pkl',param_write,True)
        
        return fbest
    
    else:
        raise Exception('unsupported action or format')
    
    