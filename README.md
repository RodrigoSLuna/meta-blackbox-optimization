# Generic Learning to Optimize Library

![N|Solid](https://www.researchgate.net/profile/Nacim_Belkhir/publication/322035981/figure/fig1/AS:574906124910592@1514079709331/black-box-Optimization.png)

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

![Alt text](documentation/GLOL_diagram_flow.png?raw=true "Title")

### Directory Structure:

        ...

### Class Structure:

#####    FUNCTION:
        import bbobbenchmarks as bn     // import functions from bbob
        f = bn.F1(1)                    // define which function to optimize from bbob file
        f.domain = [-5, 5]              // define domain interval
        f.dimension = 2                 // define input dimension

####    OPTIMIZER
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
    
    ![N|Solid](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%20%5B%5Cmathrm%7Bx_0%7D%2C%20%26%20%5Cmathrm%7Bhf_0%7D%2C%20%26%20%5Cmathrm%7By_0%7D%5D%5C%5C%20%5B...%2C%20%26%20...%2C%20%26%20...%5D%20%5C%5C%20%5B%5Cmathrm%7Bx_t%7D%2C%20%26%20%5Cmathrm%7Bhf_t%7D%2C%20%26%20%5Cmathrm%7By_t%7D%5D%20%5Cend%7Bbmatrix%7D%5Cleft.%5Cbegin%7Bmatrix%7D%20%26%20%26%20%5C%5C%20%26%20%26%20%5Cend%7Bmatrix%7D%5Cright%5C%7D%20%5Cmathrm%7Bmax%5C_size%20%3D%20max%5C_steps%7D)]


####    TRAINER

- Input: model (h5 file), steps data (np.array) 
- Description: Trainer will fit the model with data
- Output: trained_model (h5 file)

####    EVALUATOR

        import classes.evaluators as ev
        evaluator = ev.Evaluator(mode="best_value_mean", folder="F1/simple_meta_search")
        
- Input: mode (string) and folder (string)
    
    "best_value": return lowest value in all files
    "best_value_mean": return mean of lowest value in all files
    "best_optimization": return best file (achieved lowest final value)

- Output: info (np.array)

####    VISUALIZER

TODO



