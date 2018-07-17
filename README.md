# Generic Learning to Optimize Library

![Alt text](doc/GLOL_blackbox_optimizer.png?raw=true "BlackBox Optimizer")

    GLOL is a Python library that aims to easily allow evaluating different algorithms through a declarative configuration interface.

# Installation and Setup
...

# Running

```
python3 main.py random.json
```

# Further reading  

##### Configuration file:
More information in [cfg_readme.md](https://github.com/Hugodovs/meta-blackbox-optimization/blob/master/doc/cfg_readme.md)

##### Flow diagram:
![Alt text](doc/GLOL_diagram_flow.png?raw=true "Flow diagram of GLOL")

##### Directory Structure:

```
.
├── cfg
│   ├── meta.json
│   └── random.json
├── data
│   ├── dataset
│   │   └── experiment0
│   │       ├── description.txt
│   │       └── steps.npy
│   └── dnn
│       ├── generate_dnn.py
│       └── metamodel.h5
├── doc
│   ├── configuration_explained.txt
│   ├── GLOL_blackbox_optimizer.png
│   ├── GLOL_diagram_flow.png
│   ├── GLOL_steps.png
│   └── simple_example.py
├── main.py
├── README.md
├── results
│   ├── index.html
│   └── Results.ipynb
├── src
│   ├── coco_functions.py
│   ├── evaluators.py
│   ├── experiments.py
│   ├── functions.py
│   ├── optimizers.py
│   ├── __pycache__
│   │   ├── coco_functions.cpython-36.pyc
│   │   ├── experiments.cpython-36.pyc
│   │   ├── models.cpython-36.pyc
│   │   ├── optimizers.cpython-36.pyc
│   │   └── representations.cpython-36.pyc
│   ├── representations.py
│   ├── trainers.py
│   └── visualizers.py
├── To be Deleted
│   ├── configuration.json
│   ├── configuration_test.json
│   ├── generate_train_data.py
│   ├── index.html
│   ├── main.py
│   ├── process_data.py
│   ├── run_results.py
│   └── test.py
└── verification.py
```

10 directories, 37 files

##### Method Pseudocode:

###### Using Metamodel:

1) Choose points
2) Choose Current History
3) Evaluate points in Metalmodel:
![Alt text](doc/meta_model.png?raw=true "Metamodel")
4) Select Best Point <img src="https://latex.codecogs.com/gif.latex?\vec{x}" title="\vec{x}" /> (lowest value)
5) Evaluate <img src="https://latex.codecogs.com/gif.latex?\vec{x}" title="\vec{x}" /> in function
6) Update your history

### Related Work:

[Learning to learn for global optimization of black box functions](http://www.cantab.net/users/yutian.chen/Publications/ChenEtAl_NIPS16Workshop_L2LBlackBoxOptimization.pdf)

[Easing non-convex optimization with neural networks](https://openreview.net/pdf?id=rJXIPK1PM)

[Neural Generative Models for Global Optimization with Gradients](https://arxiv.org/abs/1805.08594)

[An Introduction and Survey of Estimation of Distribution Algorithms](http://www.medal-lab.org/files/2011004_rev1.pdf)

[The CMA Evolution Strategy: A Tutorial](https://arxiv.org/abs/1604.00772)

[COCO (COmparing Continuous Optimisers)](http://coco.gforge.inria.fr/)

[Taking the Human Out of the Loop: A Review of Bayesian Optimization](https://ieeexplore.ieee.org/document/7352306/)

[Pratical Bayesian Optimization of Machine Learning Algorithms](https://arxiv.org/pdf/1206.2944.pdf)

[Black-Box Variational Inference for Stochastic Differential Equations](http://proceedings.mlr.press/v80/ryder18a.html)

[Guided evolutionary strategies: escaping the curse of dimensionality in random search](https://arxiv.org/abs/1806.10230)

