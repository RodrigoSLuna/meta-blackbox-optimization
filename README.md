```python
from typing import Iterator

def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
```

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

Flow diagram:

![Alt text](doc/GLOL_diagram_flow.png?raw=true "Flow diagram of GLOL")

### Directory Structure:

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

### Class Structure:



### Experiments:

Simple Metasearch:

1) Choose points

2) Choose curr_history

3) Process Metalmodel:
            ______
    Xt -----|     |
            |     |---- M(y)   for all Xt
    Hf -----|_____|

4) Select Best Point

5) Evaluate x in f: f(x) = y

6) Update your history

### Reference:

1. http://www.cantab.net/users/yutian.chen/Publications/ChenEtAl_NIPS16Workshop_L2LBlackBoxOptimization.pdf
2. https://openreview.net/pdf?id=rJXIPK1PM
3. https://arxiv.org/abs/1805.08594

4. http://www.medal-lab.org/files/2011004_rev1.pdf

5. https://arxiv.org/abs/1604.00772
6. https://www.lri.fr/~hansen/cmaesintro.html

7. http://coco.gforge.inria.fr/

8. https://ieeexplore.ieee.org/document/7352306/
9. https://arxiv.org/pdf/1206.2944.pdf

10. http://proceedings.mlr.press/v80/ryder18a.html
