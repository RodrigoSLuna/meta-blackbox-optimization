# Generic Learning to Optimize Library

![Alt text](documentation/GLOL_blackbox_optimizer.png?raw=true "BlackBox Optimizer")

GLOL is a Python library that aims to easily allow evaluating different algorithms through a declarative configuration interface.

# Installation
...
# Setup
...
# Running
...
# Visualization
...
# Further reading  

Flow diagram:

![Alt text](documentation/GLOL_diagram_flow.png?raw=true "Flow diagram of GLOL")

### Directory Structure:

```
.
├── classes                         //Implementation of main classes
│   ├── evaluators.py
│   ├── functions.py
│   ├── models.py
│   ├── optimizers.py
│   ├── trainers.py
│   └── visualizers.py
├── data
│   ├── configuration.json          -> experiment configuration 
│   ├── dataset                     -> experiment output (each folder)
│   │   └── experiment0                 -> experiment name
│   │       ├── description.txt               -> experiment description
│   │       └── steps.npy                     -> optimizer output
│   └── dnn                         -> different keras dnn
│       ├── generate_dnn.py             -> run to generate nn model
│       └── metamodel.h5                -> dnn keras model
├── documentation                   -> more information
│   ├── GLOL_blackbox_optimizer.png
│   ├── GLOL_diagram_flow.png
│   ├── GLOL_steps.png
│   └── simple_example.py
├── main.py                         -> run an experiment
├── README.md                       -> README
├── results                         -> jupyter notebooks with some results
│   ├── index.html
│   └── Results.ipynb
└── To be Deleted                   -> Future versions will be deleted
    ├── generate_train_data.py
    ├── main.py
    ├── process_data.py
    └── run_results.py
```

8 directories, 23 files

### Class Structure:

#####    FUNCTION:

        ```python
        import bbobbenchmarks as bn     // import functions from bbob
        f = bn.F1(1)                    // define which function to optimize from bbob file
        f.domain = [-5, 5]              // define domain interval
        f.dimension = 2                 // define input dimension
        ```

#####    OPTIMIZER
- Input: configuration file (YAML)

| configuration            | type   | possible values      | description                               |
| :----------------------: | :----: | :------------------: | :-------------:                           |
| max_steps                | int    | >= 1                 | criteria to finish                        |
| nb_samples               | int    | >= 1                 | number of x sampled                       |
| size\_hf                 | int    | >= 1                 | dimension of in_hf                        |
| init\_hf\_strategy       | string | "zero"               | define how hf is initialized              |
| hf\_strategy             | string | "random" or "gagne"  | define how in_hf is choosen               |
| best_meta_point_strategy | string | "random" or "lowest" | define how the best meta point is choosen |
| meta_model               | string | "file.h5"            | load neural network from file.h5          |
| generate_train_file      | string | "file\_name" or None | save train_file                           |

- Output: numpy array
    
    ![Alt text](documentation/GLOL_steps.png?raw=true "steps")

#####    TRAINER

- Input: model (h5 file), steps data (np.array) 
- Description: Trainer will fit the model with data
- Output: trained_model (h5 file)

#####    EVALUATOR

        import classes.evaluators as ev
        evaluator = ev.Evaluator(mode="best_value_mean", folder="F1/simple_meta_search")
        
- Input: mode (string) and folder (string)
    
    "best_value": return lowest value in all files
    "best_value_mean": return mean of lowest value in all files
    "best_optimization": return best file (achieved lowest final value)

- Output: info (np.array)

#####    VISUALIZER

TODO

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
