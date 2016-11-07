This is a Python port of software used by the ACTPol collaboration to compute the likelihood of cosmological models, using the small-scale CMB power spectrum from 350 < l <4000 measured by ACTPol, derived from the 2 seasons of polarization data. This spectrum has already been marginalized over SZ and foreground emission, and an overall calibration error is propagated to the covariance matrix in the likelihood code. The polarization efficiency is the only nuisance parameter required to be sampled. It is based on the WMAP and ACT team's likelihood software.

## Usage

Put the repository's code in the directory of your Python scripts, and then import it.
```python
import act_like
```

You then create an instance of the Python class, making sure to specify the directory of the ACTPol data.
```python
data_dir = '/Users/zequnl/Projects/actpol_py/data/'
act = act_like.ACTPol_s2(data_dir)
```

With some Cls in lists (default is l=2 to l=6000) and some value of the nuisance parameter `yp`, you just call the likelihood function.
```python
like = act.loglike(cell_tt, cell_te, cell_ee, yp)
```

You can make sure the likelihood code is doing things properly by running the included test function.
```python
act.test()
```

For a working example, see the heavily-commented `example_planck.py`.

## Citation

Please reference [Louis et al. 2016](https://arxiv.org/abs/1610.02360) if you use this code. 

The original Fortran code was written by E. Calabrese and J. Dunkley.
