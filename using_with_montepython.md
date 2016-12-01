To use this code with Monte Python, first go to your MontePython/montepython directory. 

```
cd /u/zequnl/Documents/montepython_public/montepython/likelihoods
```

Then clone this repository in there. Make sure not to change the folder's name.
```
git clone https://github.com/xzackli/actpols2_like_py.git
```
You're basically done! Now when you use a MontePython parameter file, you can write something like

```
data.experiments=['actpols2_like_py']
```

### tau prior
To run the ACTPol likelihood by itself, you will want to include a prior on tau_reio = 0.06 \pm 0.01. For convenience, I've included such a likelihood in the folder tau_prior. You can use it by copying it to your MontePython likelihoods folder. Since this repository should be in your likelihoods folder already, you can run

```
cp -r tau_prior ../ 
```


### example parameter file
I've included a parameter file `actpol_s2.param`, which is configured to reproduce the result of [Louis et al. 2016](https://arxiv.org/abs/1610.02360). It will run a chain with the standard CLASS LCDM parameters, and also produce the derived parameter `h`. You can copy `actpol_s2.param` to your MontePython directory and run it,

```
python montepython/MontePython.py run -p actpol_s2.param -o chains/actpol_s2 -N 1000
```
This requires the use of the tau prior likelihood.
