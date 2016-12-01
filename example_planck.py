"""
This is a simple demonstration of how to use the ACTPol likelihood.
You will need to configure data_dir for your own setup.
"""



import act_like # our likelihood
import numpy as np # need this for reading the Planck data in this example

# set up data directories and load up the C_l data
data_dir = '/Users/zequnl/Projects/actpol_py/data/'
filename = data_dir + "planck2015.dat"

# load in the data. there are some columns we don't need. 
# also we load in 5999 rows, since there is no l=1 and tt_lmax is 6000
tt_lmax = 6000
dum1, cell_tt, cell_te, cell_ee, dum2, dum3 = \
    np.genfromtxt(filename, delimiter=None, unpack=True, max_rows=tt_lmax-1)


# create the likelihood object
act = act_like.ACTPol_s2(data_dir)

# calculate the likelihood assuming yp = 1.0. 
like = act.loglike(cell_tt, cell_te, cell_ee, 1.0)

print("TT + TE + EE Likelihood")
print("Expected: 147.747797921459")
print("Found   : " + '{0:.12f}'.format(2*like))





# now suppose we want to change a configuration. let's use only the EE
act.use_tt = False
act.use_te = False
act.use_ee = True

print("\nUsing only EE.")
# calculate the likelihood assuming yp = 1.0. 
like = act.loglike(cell_tt, cell_te, cell_ee, 1.0)

print("Expected: 39.178004671647")
print("Found   : " + '{0:.12f}'.format(2*like))

