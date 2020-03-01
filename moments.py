#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:09:59 2020

@author: egorkozlov
"""
import numpy as np

def compute_moments(self):
    moments = dict()
    
    n_mark = self.state_codes['Couple and child']
    n_marnk = self.state_codes['Couple, no children']
    n_single = self.state_codes['Female, single']
    n_singlek = self.state_codes['Female and child']
    
    
    is_mar = (self.state == n_mark) | (self.state == n_marnk)
    is_mark = (self.state == n_mark)
    
    ever_mar = (np.cumsum(is_mar,axis=1) > 0)
    div_now =  (ever_mar) & ((self.state==n_single) | (self.state==n_singlek))
    ever_div = (np.cumsum(div_now,axis=1) > 0)
    ever_kid = ( np.cumsum( (self.state == n_mark) | (self.state == n_singlek),axis=1) > 0)
    ever_upp = (np.cumsum(self.unplanned_preg,axis=1)>0)
    ever_km  = (np.cumsum(self.k_m,axis=1)>0)
    
    
    nmar_cum = np.cumsum(self.agreed,axis=1)
    one_mar = (nmar_cum == 1)
    
    have_kid = (self.state == n_mark) | (self.state == n_singlek)
    num_mar = np.cumsum( self.agreed, axis = 1 )
    one_mar = (num_mar == 1)
    
    share_x = self.x / np.maximum(1e-3, self.x  + self.c)
    
    
    
    mean_x = share_x[:,0:20][is_mark[:,0:20]].mean()
    moments['mean x share'] = mean_x
    
    
    
    moments['never married at 25'] = 1-ever_mar[:,4].mean()
    moments['never married at 30'] = 1-ever_mar[:,9].mean()
    moments['never married at 35'] = 1-ever_mar[:,14].mean()
    moments['never married at 40'] = 1-ever_mar[:,19].mean()
    
    moments['more than one mar at 40'] = (num_mar[:,19]>1).mean()
    
    moments['divorced right now at 25'] = div_now[ever_mar[:,4],4].mean()
    moments['divorced right now at 30'] = div_now[ever_mar[:,9],9].mean()
    moments['divorced right now at 35'] = div_now[ever_mar[:,14],14].mean()
    moments['divorced right now at 40'] = div_now[ever_mar[:,19],19].mean()
    
    
    moments['no kids at 25'] = 1-ever_kid[:,4].mean()
    moments['no kids at 30'] = 1-ever_kid[:,9].mean()
    moments['no kids at 35'] = 1-ever_kid[:,14].mean()
    
    moments['no kids at 25 if married'] = 1-ever_kid[is_mar[:,4],4].mean() if np.any(is_mar[:,4]) else 0.0
    moments['no kids at 30 if married'] = 1-ever_kid[is_mar[:,9],9].mean() if np.any(is_mar[:,9]) else 0.0
    moments['no kids at 35 if married'] = 1-ever_kid[is_mar[:,14],14].mean() if np.any(is_mar[:,14]) else 0.0
    
    
    #mkids_0_mar = (self.state[:,1:] == n_mark)[ ~is_mar[:,0:-1] & is_mar[:,1:]].mean()
    moments['no kids 1 year after marriage'] = 1 - ( have_kid[:,2:][ ~is_mar[:,0:-2] & is_mar[:,2:] & one_mar[:,2:]] ).mean()
    moments['no kids 2 years after marriage'] = 1 - ( have_kid[:,3:][ ~is_mar[:,0:-3] & is_mar[:,3:] & one_mar[:,3:]] ).mean()
    moments['no kids 3 years after marriage'] = 1 - ( have_kid[:,4:][ ~is_mar[:,0:-4] & is_mar[:,4:] & one_mar[:,4:]] ).mean()
    
    
    in_sample = (self.k_m) | (self.m_k)
    
    
    moments['k then m at 25'] = self.k_m[in_sample[:,4],4].mean()
    moments['k then m at 30'] = self.k_m[in_sample[:,9],9].mean()
    moments['k then m at 35'] = self.k_m[in_sample[:,14],14].mean()
    
    moments['just k & m at 25'] = self.agreed_k[:,4].mean()
    moments['just k & m at 30'] = self.agreed_k[:,9].mean()
    moments['just k & m at 35'] = self.agreed_k[:,14].mean()
    
    
    moments['divorced with kids at 30']      = (div_now[:,9]     &  ever_kid[:,9])[ever_mar[:,9]].mean()
    moments['divorced never kids at 30']     = (div_now[:,9]     & ~ever_kid[:,9])[ever_mar[:,9]].mean()
    moments['never married with kids at 30'] = ((~ever_mar)[:,9] &  ever_kid[:,9]).mean()
    
    
    
    share_planned = self.planned_preg[(self.planned_preg) | (self.unplanned_preg)].mean()
    moments['share of planned pregnancies'] = share_planned
    share_rejected = self.disagreed.sum() / (self.disagreed | self.agreed).sum()
    moments['share of rejected proposals'] = share_planned
    if self.verbose: print('Rejected: {}, planned preg: {}'.format(share_rejected,share_planned))
    
    
    divorced_km = div_now[:,:20][self.k_m[:,:20]].mean()
    divorced_mk = div_now[:,:20][self.m_k[:,:20]].mean()    
    if self.verbose: print('Anything: divorced k_m = {}, divorced m_k = {}'.format(divorced_km,divorced_mk))
    moments['divorced if km (all)'] = divorced_km
    moments['divorced if mk (all)'] = divorced_mk
    
    divorced_km_1m = div_now[:,:20][self.k_m[:,:20] & one_mar[:,:20]].mean()
    divorced_mk_1m = div_now[:,:20][self.m_k[:,:20] & one_mar[:,:20]].mean()    
    if self.verbose: print('One mar: divorced k_m = {}, divorced m_k = {}'.format(divorced_km_1m,divorced_mk_1m))
    moments['divorced if k then m and one marriage'] = divorced_km_1m
    moments['divorced if m then k and one marriage'] = divorced_mk_1m
    
    e_divorced_upp  = ever_div[ever_upp[:,20],20].mean()
    e_divorced_nupp = ever_div[~ever_upp[:,20],20].mean()    
    if self.verbose: print('Ever divorced upp = {}, ever divorced nupp = {}'.format(e_divorced_upp,e_divorced_nupp))
    moments['ever divorced if had unplanned pregnancy'] = e_divorced_upp
    moments['ever divorced if no unplanned pregnancy'] = e_divorced_nupp
    
    e_divorced_ekm  = ever_div[ever_km[:,20],20].mean()
    e_divorced_nekm = ever_div[~ever_km[:,20],20].mean()    
    if self.verbose: print('Ever divorced ever km = {}, ever divorced never km = {}'.format(e_divorced_ekm,e_divorced_nekm))
    moments['ever divorced if ever km'] = e_divorced_upp
    moments['ever divorced if never km'] = e_divorced_nupp
    
    
    
    def std_pos(x):
        return np.std(x[x>0])
    
    sd_f_24 = std_pos(self.female_earnings[:,3])
    sd_f_30 = std_pos(self.female_earnings[:,9])
    
    sd_m_24 = std_pos(self.male_earnings[:,3])
    sd_m_30 = std_pos(self.male_earnings[:,9])
    
    
    
    moments['std earnings at 24, female'] = sd_f_24
    moments['std earnings at 30, female'] = sd_f_30
    moments['std earnings at 24, male'] = sd_m_24
    moments['std earnings at 30, male'] = sd_m_30
    
    if self.verbose:
        print('std of earnings is {} at 24 and {} at 30 for males'.format(sd_m_24,sd_m_30))
        print('std of earnings is {} at 24 and {} at 30 for females'.format(sd_f_24,sd_f_30))
    
    
    i25 = 4
    p25 = (self.male_wage[:,i25] > 0)
    i30 = 9
    p30 = (self.male_wage[:,i30] > 0)
    i40 = 19
    p40 = (self.male_wage[:,i40] > 0)
    
    
    
    
    
    
    
    med_25 = np.median(self.male_wage[p25,i25])
    med_30 = np.median(self.male_wage[p30,i30])    
    
    above_med_25 = ((self.male_wage[:,i25] >= med_25) & p25)
    below_med_25 = ((self.male_wage[:,i25] <= med_25) & p25)
    above_med_30 = ((self.male_wage[:,i30] >= med_30) & p30)
    below_med_30 = ((self.male_wage[:,i30] <= med_30) & p30)
    
    moments['log earnings coef at 25'] = ever_kid[above_med_25,i25].mean() - ever_kid[below_med_25,i25].mean() 
    moments['log earnings coef at 30'] = ever_kid[above_med_30,i30].mean() - ever_kid[below_med_30,i30].mean()
    
    
    moments['out of lf at 30 if mar and kids'] = (self.labor_supply[is_mark[:,9],9] == self.setup.ls_levels_k[0]).mean()
    
    moments['out of lf at 30 if mar and kids coef'] = \
        (self.labor_supply[is_mark[:,9] & above_med_30,9] == self.setup.ls_levels_k[0]).mean() - \
        (self.labor_supply[is_mark[:,9] & below_med_30,9] == self.setup.ls_levels_k[0]).mean() 
        
    
    
    
    p_1yr = (~is_mar[:,0:-2] & is_mar[:,2:] & one_mar[:,2:] & (self.male_wage[:,2:]>0))
    linc_own = np.log(self.female_wage[:,2:][p_1yr] )
    linc_sp =  np.log(self.male_wage[:,2:][p_1yr])
    
    moments['spouse log coef 1 year after'] = np.polyfit(linc_sp,linc_own,1)[0]
    
    
    if self.verbose:
        print('Coefficients are {} at 25 and {} at 30'.format(moments['log earnings coef at 25'],moments['log earnings coef at 30']))
    
    
    if self.verbose:
        print('')
        print('')
        print('Key target: km {}, mk {}, ratio {}'.format(divorced_km_1m,divorced_mk_1m,divorced_km_1m/divorced_mk_1m))


    
    return moments

