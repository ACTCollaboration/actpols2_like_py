# this file, along with actpols2_like_py.data, allows you 
# to use this likelihood for Monte Python. 
# 

import os
import numpy as np
from montepython.likelihood_class import Likelihood

import act_like # our likelihood

class actpols2_like_py(Likelihood):

    # initialization routine

    def __init__(self, path, data, command_line):

        Likelihood.__init__(self, path, data, command_line)

        self.need_cosmo_arguments(
            data, {
                'lensing': 'yes', 
                'output': 'tCl lCl pCl', 
                'l_max_scalars': 6000,
                'modes': 's',
                'non linear': 'halofit'
                })

        self.need_update = True
        self.use_nuisance = ['yp']
        self.nuisance = ['yp']
        
        print "PATH", self.path
        self.act = act_like.ACTPol_s2(self.actdata)

        # \ell values 2, 3, ... 6000
        self.xx = np.array(range(2,6001))

    # compute likelihood

    def loglkl(self, cosmo, data):

        
        # print "STARTING LIKELIHOOD------------ ", data.cosmo_arguments

        lkl = 0.0
        try:
        	# call CLASS
            cl = self.get_cl(cosmo, 6000)

            # we follow the convention of operating with (l(l+1)/2pi) * C_l
            ee = cl['ee'][2:]
            te = cl['te'][2:]
            tt = cl['tt'][2:]
            tt =  ((self.xx)*(self.xx+1) * tt / (2 * np.pi))
            te =  ((self.xx)*(self.xx+1) * te / (2 * np.pi))
            ee =  ((self.xx)*(self.xx+1) * ee / (2 * np.pi))

            yp = data.mcmc_parameters['yp']['current']
            lkl = -self.act.loglike(tt, te, ee, yp)

        except:
            lkl = -np.inf

        return lkl

