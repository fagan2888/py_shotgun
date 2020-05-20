#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 07:59:29 2020

@author: egorkozlov
"""

        
def target_values(mode='low education'):
    targets = dict()
        
        
    if mode=='high education':
        
        #targets['ever kids by years after marriage, 1'] = (.1901175,.0018521)
        #targets['ever kids by years after marriage, 2'] = (.3416996,.0022054)
        targets['ever kids by years after marriage, 3'] = (.4902692,.0023415)
        targets['ever kids by years after marriage, 4'] = (.6114712,.0023096)
        targets['ever kids by years after marriage, 5'] = (.7039068,.0021802)
        targets['ever kids by years after marriage, 6'] = (.7730147,.0020489)
        targets['ever kids by years after marriage, 7'] = (.8182496,.0019268)
        targets['ever kids by years after marriage, 8'] = (.8568491,.00179)
        #targets['ever kids by years after marriage, 9'] = (.8809587,.001696)
        #targets['ever kids by years after marriage, 10']= (.8978599,.0016307)
        
        
        targets['divorced by years after marriage, 1']  =  (.0084912,.0004315)
        targets['divorced by years after marriage, 2']  =  (.0199536,.0006448)
        targets['divorced by years after marriage, 3']  =  (.0345649,.0008425)        
        targets['divorced by years after marriage, 4']  =  (.0536216,.001042)
        targets['divorced by years after marriage, 5']  =  (.0683989,.0011694)
        targets['divorced by years after marriage, 6']  =  (.0807483,.0012872)
        targets['divorced by years after marriage, 7']  =  (.0879516,.0013595)
        targets['divorced by years after marriage, 8']  =  (.1011097,.0014718*(1/2))
        targets['divorced by years after marriage, 9']  =  (.1027806,.001517*(1/2))
        targets['divorced by years after marriage, 10'] =  (.116314,.0016379*(1/2))
        
        
        
        
        #targets['hazard of marriage at 22'] = (.0506949,.001038)
        targets['hazard of marriage at 23'] = (.0624283,.0011034)
        targets['hazard of marriage at 24'] = (.0787830,.0012318)
        targets['hazard of marriage at 25'] = (.0945611,.0013867)
        targets['hazard of marriage at 26'] = (.1066170,.0015351)
        targets['hazard of marriage at 27'] = (.1105425,.0016506)
        targets['hazard of marriage at 28'] = (.1181793,.0018265)
        targets['hazard of marriage at 29'] = (.1185538,.0019239)
        targets['hazard of marriage at 30'] = (.1116017,.001993)
        targets['hazard of marriage at 31'] = (.1070343,.0020717)
        targets['hazard of marriage at 32'] = (.1068933,.0022018)
        targets['hazard of marriage at 33'] = (.0913318,.0021093)
        targets['hazard of marriage at 34'] = (.0844846,.0020832)
        targets['hazard of marriage at 35'] = (.0780720,.0020774)
        
        
        #targets['k then m in population at 22'] = (.0031368,.0003093)
        targets['k then m in population at 23'] = (.0055518,.0003391)
        targets['k then m in population at 24'] = (.0080609,.000383)
        targets['k then m in population at 25'] = (.0126187,.0004615)
        targets['k then m in population at 26'] = (.0177664,.0005398)
        targets['k then m in population at 27'] = (.0214169,.0005799)
        targets['k then m in population at 28'] = (.0281133,.0006556)
        targets['k then m in population at 29'] = (.0321021,.0006961)
        targets['k then m in population at 30'] = (.0369590,.000731)
        targets['k then m in population at 31'] = (.0386226,.0007545)
        targets['k then m in population at 32'] = (.0424404,.0007881)
        targets['k then m in population at 33'] = (.0436167,.0008042)
        targets['k then m in population at 34'] = (.0483524,.0008466)
        targets['k then m in population at 35'] = (.0535521,.0008891)
        
        

        
        #targets['m then k in population at 22'] = (.0058368,.0004213)
        targets['m then k in population at 23'] = (.0150030,.0005547)
        targets['m then k in population at 24'] = (.0279987,.0007066)
        targets['m then k in population at 25'] = (.0480545,.0008848)
        targets['m then k in population at 26'] = (.0788468,.0011012)
        targets['m then k in population at 27'] = (.1209867,.0013062)
        targets['m then k in population at 28'] = (.1736392,.0015023)
        targets['m then k in population at 29'] = (.2316302,.0016661)
        targets['m then k in population at 30'] = (.2820957,.0017437)
        targets['m then k in population at 31'] = (.3449800,.0018613)
        targets['m then k in population at 32'] = (.3962855,.0019121)
        targets['m then k in population at 33'] = (.4331152,.0019509)
        targets['m then k in population at 34'] = (.4618895,.0019675)
        targets['m then k in population at 35'] = (.4719915,.0019714)
        
        
        #targets['k then m in sample at 22'] = (.3495573,.0264092)
        targets['k then m in sample at 23'] = (.2700996,.0134549/2)
        targets['k then m in sample at 24'] = (.2235426,.008985/2)
        targets['k then m in sample at 25'] = (.2079784,.0063642/2)
        targets['k then m in sample at 26'] = (.1838923,.0048233/2)
        targets['k then m in sample at 27'] = (.1503958,.0036041/2)
        targets['k then m in sample at 28'] = (.1393456,.0029425/2)
        targets['k then m in sample at 29'] = (.1217223,.0024172/2)
        targets['k then m in sample at 30'] = (.1158390,.0021046/2)
        targets['k then m in sample at 31'] = (.1006838,.0018461/2)
        targets['k then m in sample at 32'] = (.0967356,.0016985/2)
        targets['k then m in sample at 33'] = (.0914910,.001601/2)
        targets['k then m in sample at 34'] = (.0947637,.0015799/2)
        targets['k then m in sample at 35'] = (.1018985,.001609/2)
        
        #targets['hazard of new child at 22'] = (0.0136671,0.0005373)
        targets['hazard of new child at 23'] = (.0188677,.0005959)
        targets['hazard of new child at 24'] = (.0277849,.0007042)
        targets['hazard of new child at 25'] = (.0389933,.0008353)
        targets['hazard of new child at 26'] = (.0519110,.000965)
        targets['hazard of new child at 27'] = (.0661566,.0011131)
        targets['hazard of new child at 28'] = (.0813480,.0012859)
        targets['hazard of new child at 29'] = (.0893035,.0013959)
        targets['hazard of new child at 30'] = (.1023455,.0016000)
        targets['hazard of new child at 31'] = (.1039228,.0017302)
        targets['hazard of new child at 32'] = (.1029690,.0018698)
        targets['hazard of new child at 33'] = (.0970099,.0019398)
        targets['hazard of new child at 34'] = (.0884263,.0019678)
        targets['hazard of new child at 35'] = (.0799924,.0019688)
        
        
        targets['ever married at 22'] = (.0648409,.0013704)
        targets['ever married at 23'] = (.1092023,.0014232)
        targets['ever married at 24'] = (.1651963,.0015907)
        targets['ever married at 25'] = (.2321176,.0017455)
        targets['ever married at 26'] = (.3186594,.0019039)
        targets['ever married at 27'] = (.3979381,.0019605)
        targets['ever married at 28'] = (.4797466,.0019814)
        targets['ever married at 29'] = (.5492900,.0019650)
        targets['ever married at 30'] = (.6053985,.0018938)
        targets['ever married at 31'] = (.6557630,.0018604)
        targets['ever married at 32'] = (.7029164,.0017864)
        targets['ever married at 33'] = (.7277533,.0017525)
        targets['ever married at 34'] = (.7562652,.0016944)
        targets['ever married at 35'] = (.7776588,.0016421)
        
        
        
        targets['divorced by years after marriage if kids first, 1'] = (.0113142,.0020309/4)
        targets['divorced by years after marriage if kids first, 2'] = (.0216539,.0027502/4)
        targets['divorced by years after marriage if kids first, 3'] = (.0492118,.0041846/4)
        targets['divorced by years after marriage if kids first, 4'] = (.0893572,.0053861/4)
        targets['divorced by years after marriage if kids first, 5'] = (.1054101,.0058989/4)
        targets['divorced by years after marriage if kids first, 6'] = (.1386944,.0068164/4)
        targets['divorced by years after marriage if kids first, 7'] = (.1506841,.0072127/4)
        targets['divorced by years after marriage if kids first, 8'] = (.1866493,.0080136/4)
        targets['divorced by years after marriage if kids first, 9'] = (.1786823,.0078907/4)
        targets['divorced by years after marriage if kids first, 10'] = (.20118,.0084048/4)
        
        
        targets['divorced by years after marriage if marriage first, 1'] = (.000818,.0005133/2)
        targets['divorced by years after marriage if marriage first, 2'] = (.0050849,.000689/2)
        targets['divorced by years after marriage if marriage first, 3'] = (.0102901,.0007538/2)
        targets['divorced by years after marriage if marriage first, 4'] = (.0165388,.000839/2)
        targets['divorced by years after marriage if marriage first, 5'] = (.0201483,.000850/2)
        targets['divorced by years after marriage if marriage first, 6'] = (.0268928,.0009448/2)
        targets['divorced by years after marriage if marriage first, 7'] = (.0320433,.0010079/2)
        targets['divorced by years after marriage if marriage first, 8'] = (.0401776,.001116/2)
        targets['divorced by years after marriage if marriage first, 9'] = (.0479392,.0012191/2)
        targets['divorced by years after marriage if marriage first, 10'] = (.0602147,.0013719/2)
        
        
        
        targets['mean x share'] = (0.4,0.001)
        targets['divorced at 30 if one marriage'] = (.0686837,.0012484)
        targets['divorced if k then m and one marriage'] = (.1480121,.0024232*(1/4))
        targets['divorced if m then k and one marriage'] = (.0536316,.0004861*(1/4))
        targets['divorced with kids at 30']      = (.0267382,.0007793)
        targets['never married with kids at 30'] = (.0463395,.0008145)      
        targets['more than one mar at 40']       = (.1190139,.0012735)
        targets['in labor force at 30 if kids'] = (.739675,.0028066*(1/4))
        
        
        
    elif mode=='low education':
    
        
        
        #targets['ever kids by years after marriage, 1'] = (.6371565, .0030758)
        #targets['ever kids by years after marriage, 2'] = (.694856, .0028766)
        targets['ever kids by years after marriage, 3'] = (.7534413, .0027062)
        targets['ever kids by years after marriage, 4'] = (.7929944, .0026026)
        targets['ever kids by years after marriage, 5'] = (.8249145, .0024629)
        targets['ever kids by years after marriage, 6'] = (.8519912, .0023541)
        targets['ever kids by years after marriage, 7'] = (.8737004, .0022449)
        targets['ever kids by years after marriage, 8'] = (.881806, .0022094)
        #targets['ever kids by years after marriage, 9'] = (.8990071, .0021148)
        #targets['ever kids by years after marriage, 10'] = (.9025669, .0020562)
        
        
        targets['divorced by years after marriage, 1'] = (.0231847, .0009513)
        targets['divorced by years after marriage, 2'] = (.0601223, .0014428)
        targets['divorced by years after marriage, 3'] = (.0943086, .0017544)
        targets['divorced by years after marriage, 4'] = (.1245948, .001997)
        targets['divorced by years after marriage, 5'] = (.153307, .0021667)
        targets['divorced by years after marriage, 6'] = (.1724024, .0022962)
        targets['divorced by years after marriage, 7'] = (.1908162, .002408)
        targets['divorced by years after marriage, 8'] = (.2068432, .002495/2)
        targets['divorced by years after marriage, 9'] = (.216311, .0025916/2)
        targets['divorced by years after marriage, 10'] = (.2174107, .0025545/2)
        
        #targets['hazard of marriage at 22'] = (.0459992, .0009848)
        targets['hazard of marriage at 23'] = (.0480085, .0010465)
        targets['hazard of marriage at 24'] = (.0507163, .0011001)
        targets['hazard of marriage at 25'] = (.0505483, .0011527)
        targets['hazard of marriage at 26'] = (.0513198, .0011989)
        targets['hazard of marriage at 27'] = (.0533364, .0012555)
        targets['hazard of marriage at 28'] = (.0534521, .0013044)
        targets['hazard of marriage at 29'] = (.0518105, .0012773)
        targets['hazard of marriage at 30'] = (.0526195, .0013629)
        targets['hazard of marriage at 31'] = (.0509349, .001358)
        targets['hazard of marriage at 32'] = (.0477095, .0013521)
        targets['hazard of marriage at 33'] = (.0461142, .0013488)
        targets['hazard of marriage at 34'] = (.0437701, .0013087)
        targets['hazard of marriage at 35'] = (.0398101, .0012805)
        
        
        #targets['k then m in population at 22'] = (.0471337, .0008786)
        targets['k then m in population at 23'] = (.0630275, .0010425)
        targets['k then m in population at 24'] = (.0765292, .001157)
        targets['k then m in population at 25'] = (.0891691, .0012334)
        targets['k then m in population at 26'] = (.0974226, .0013089)
        targets['k then m in population at 27'] = (.1065944, .0013648)
        targets['k then m in population at 28'] = (.1122013, .0013894)
        targets['k then m in population at 29'] = (.1141492, .0014134)
        targets['k then m in population at 30'] = (.1187029, .0013998)
        targets['k then m in population at 31'] = (.1203012, .0014483)
        targets['k then m in population at 32'] = (.1200893, .0014305)
        targets['k then m in population at 33'] = (.1245074, .001461)
        targets['k then m in population at 34'] = (.1270016, .0014689)
        targets['k then m in population at 35'] = (.1215744, .0014184)
        
        

        
        #targets['m then k in population at 22'] = (.0569954, .0009611)
        targets['m then k in population at 23'] = (.0745946, .0011272)
        targets['m then k in population at 24'] = (.0946999, .0012743)
        targets['m then k in population at 25'] = (.113709, .001374)
        targets['m then k in population at 26'] = (.1358313, .0015123)
        targets['m then k in population at 27'] = (.1569375, .0016087)
        targets['m then k in population at 28'] = (.1726471, .0016638)
        targets['m then k in population at 29'] = (.1872816, .001734)
        targets['m then k in population at 30'] = (.2009962, .0017343)
        targets['m then k in population at 31'] = (.2210822, .0018475)
        targets['m then k in population at 32'] = (.2294688, .0018504)
        targets['m then k in population at 33'] = (.2389265, .001887)
        targets['m then k in population at 34'] = (.2457679, .0018993)
        targets['m then k in population at 35'] = (.249713, .0018788)
        
        
        #targets['k then m in sample at 22'] = (.4526467, .0062011)
        targets['k then m in sample at 23'] = (.4579749, .0054619/2)
        targets['k then m in sample at 24'] = (.4469404, .0049857/2)
        targets['k then m in sample at 25'] = (.4395206, .0045602/2)
        targets['k then m in sample at 26'] = (.4176675, .0043115/2)
        targets['k then m in sample at 27'] = (.4044838, .0040408/2)
        targets['k then m in sample at 28'] = (.3938983, .003864/2)
        targets['k then m in sample at 29'] = (.3786911, .0037764/2)
        targets['k then m in sample at 30'] = (.3712956, .0035625/2)
        targets['k then m in sample at 31'] = (.3523933, .003516/2)
        targets['k then m in sample at 32'] = (.3435461, .0034191/2)
        targets['k then m in sample at 33'] = (.3425861, .0033878/2)
        targets['k then m in sample at 34'] = (.3406974, .0033269/2)
        targets['k then m in sample at 35'] = (.3274401, .003233/2)
        
        targets['hazard of new child at 22'] = (.0723763, .0014004)
        targets['hazard of new child at 23'] = (.0686844, .0014701)
        targets['hazard of new child at 24'] = (.0660664, .0015141)
        targets['hazard of new child at 25'] = (.0656788, .0016069)
        targets['hazard of new child at 26'] = (.0640507, .0016735)
        targets['hazard of new child at 27'] = (.0641009, .0017645)
        targets['hazard of new child at 28'] = (.0665277, .0019017)
        targets['hazard of new child at 29'] = (.0588031, .0018288)
        targets['hazard of new child at 30'] = (.0558206, .0018416)
        targets['hazard of new child at 31'] = (.0531504, .0019242)
        targets['hazard of new child at 32'] = (.0456938, .0018372)
        targets['hazard of new child at 33'] = (.0415602, .0017985)
        targets['hazard of new child at 34'] = (.0408571, .0018053)
        targets['hazard of new child at 35'] = (.0343058, .001669)
        
        
        #targets['ever married at 21'] = (.1198675, .0012708)
        targets['ever married at 22'] = (.1725177, .0015664)
        targets['ever married at 23'] = (.2182572, .0017721)
        targets['ever married at 24'] = (.2691566, .0019303)
        targets['ever married at 25'] = (.3205891, .0020199)
        targets['ever married at 26'] = (.369406, .0021304)
        targets['ever married at 27'] = (.4139921, .0021783)
        targets['ever married at 28'] = (.4536668, .0021917)
        targets['ever married at 29'] = (.4897026, .0022219)
        targets['ever married at 30'] = (.5310084, .0021597)
        targets['ever married at 31'] = (.5669783, .002206)
        targets['ever married at 32'] = (.5937097, .0021613)
        targets['ever married at 33'] = (.6194696, .0021484)
        targets['ever married at 34'] = (.6386038, .0021192)
        targets['ever married at 35'] = (.6639089, .0020503)
        
        
        
        targets['divorced by years after marriage if kids first, 1'] = (.0201514, .0017159/4)
        targets['divorced by years after marriage if kids first, 2'] = (.0471255, .0025286/4)
        targets['divorced by years after marriage if kids first, 3'] = (.0813251, .0032273/4)
        targets['divorced by years after marriage if kids first, 4'] = (.1166151, .0038275/4)
        targets['divorced by years after marriage if kids first, 5'] = (.1376778, .0041438/4)
        targets['divorced by years after marriage if kids first, 6'] = (.1580319, .0044724/4)
        targets['divorced by years after marriage if kids first, 7'] = (.1836251, .0047913/4)
        targets['divorced by years after marriage if kids first, 8'] = (.2043214, .0049916/4)
        targets['divorced by years after marriage if kids first, 9'] = (.2066351, .0051605/4)
        targets['divorced by years after marriage if kids first, 10'] = (.2115082, .0050606/4)
        
        
        targets['divorced by years after marriage if marriage first, 1'] = (.010328, .0022173/2)
        targets['divorced by years after marriage if marriage first, 2'] = (.0289688, .002371/2)
        targets['divorced by years after marriage if marriage first, 3'] = (.0505473, .0025391/2)
        targets['divorced by years after marriage if marriage first, 4'] = (.0645814, .0025787/2)
        targets['divorced by years after marriage if marriage first, 5'] = (.0918597, .0028409/2)
        targets['divorced by years after marriage if marriage first, 6'] = (.105973, .0029251/2)
        targets['divorced by years after marriage if marriage first, 7'] = (.113954, .0029394/2)
        targets['divorced by years after marriage if marriage first, 8'] = (.1333069, .0030814/2)
        targets['divorced by years after marriage if marriage first, 9'] = (.1407658, .0031131/2)
        targets['divorced by years after marriage if marriage first, 10'] = (.1443613, .0030424/2)
        
        
    
        
        targets['mean x share'] = (0.4,0.001)
        targets['divorced at 30 if one marriage'] = (.1691302,.0023003)
        targets['divorced if k then m and one marriage'] = (.1727448,.0014886*(1/4))
        targets['divorced if m then k and one marriage'] = (.1394705,.000983*(1/4))
        targets['divorced with kids at 30']      = (.1066072,.0017801)
        targets['never married with kids at 30'] = (.2368133,.0018398)      
        targets['more than one mar at 40']       = (.1714891,.0015326)
        targets['in labor force at 30 if kids'] = (.5466037,.0033879*(1/4))
        
        
    else:
        raise Exception('this mode for targets is not found')
    
    return targets

    
