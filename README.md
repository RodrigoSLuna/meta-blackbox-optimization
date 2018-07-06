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

        ...

### Class Structure:

#####    FUNCTION:
        import bbobbenchmarks as bn     // import functions from bbob
        f = bn.F1(1)                    // define which function to optimize from bbob file
        f.domain = [-5, 5]              // define domain interval
        f.dimension = 2                 // define input dimension

#####    OPTIMIZER
- Input: configuration file (YAML)

| configuration |   type | description | possible values |
| :-----------: | :----: | :---------: | :-------------: |
| max_steps                     | int |criteria to finish | >= 1 
| nb_samples             | int | number of x sampled | >= 1 |
| size_hf | int | dimension of in_hf | >= 1 |
| init_hf_strategy | string | define how hf is initialized | "zero" |
| hf_strategy              | string |  define how in_hf is choosen | "random" or "gagne" |
| best_meta_point_strategy  | string | define how the best meta point is choosen | "random" or "lowest" |
|   meta_model  | string | load neural network from file.h5 | "file.h5" |
| generate_train_file          | string | save train_file | "file_name" or None |

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



