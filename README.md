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
│   README.md
│   file001.txt
│
└───classes
│   │   function.py
│   │   optimizer.py
│   │   trainer.py
│   │   evaluator.py
│   │   visualizer.py
│   │
│   └───subfolder1
│       │   file111.txt
│       │   file112.txt
│       │   ...
│
└───folder2
    │   file021.txt
    │   file022.txt
```


### Class Structure:

#####    FUNCTION:

        import bbobbenchmarks as bn     // import functions from bbob
        f = bn.F1(1)                    // define which function to optimize from bbob file
        f.domain = [-5, 5]              // define domain interval
        f.dimension = 2                 // define input dimension

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



