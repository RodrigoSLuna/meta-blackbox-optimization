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

![Flow diagram](https://www.draw.io/?title=GLOL#R7Zpdd5owGMc%2FjZfzCCEol9a5zXO6dqdvW3fTk0oKbEBYiFX36RckvAotVSN4uivJP%2BFJyO%2FJ2xN7YOKtPlMU2F%2BJid2eOjBXPfCxp6oK0BX%2BEynrWBmOYCxY1DFFoUy4dv5iIQ6EunBMHBYKMkJc5gRFcU58H89ZQUOUkmWx2BNxi7UGyMJbwvUcudvqd8dkdqyO4CDTv2DHspOalYHI8VBSWAihjUyyzElg2gMTSgiLn7zVBLtR5yX9Er%2F3qSY3bRjFPmvyAgB4bg4RNubAMBEyPggLz8hdiI%2FtqbrLbZ09EW6St5itRTfofxYkyfgQbiCNeQFe%2FSrL5E9W9Pvp9mJyM7u8SKzxJsUG42zRG6ltlZKFb%2BKolQOevbQdhq8DNI9yl9ypuGYzz%2BUpJX37GVOGV7UdoaTdy%2F0SEw8zuuZFxAuaIYisU2ZxepkBVhJqdg6uLjQkfMpKTWfdzh9EzzekoNZSCAPk707h8tvN7Ovs5%2FQqhyG22BEMwIAFDCqowKAdCwOQNBhursaziwKETo2FdLpKIGhtjgVNEoS72fXt%2BLw0GDrFAYIiB21YwQEeiwOUxGF6Nz6%2FHd9cdhaD2ikM%2Bt4YFL0KQ8hwEPb9YF2LIZYfaS0Y3nK%2BA8PHWa9LcxSAFVAGFVCgDCgjSVAYRY6PzQcv2kL3bXgibODraI42XgxJaF5F0iKA1MmTzaza5uBIdtIHXzkyxcI%2BpohhMVA2k1hWuBEf3tusCCJklPzGE%2BISyhWf%2BBG8J8d1SxJyHcvnyTmng7l%2BFrFz%2BGlxLDI8xzTdOvLF1ewA8Iel1QpuoU%2FP0Xn0QAp6ZXscmPwoLZKEMptYxEfuNFNLPZIDglcO%2BxHJfShS90mOz1uay4qS98LAL8zYWsQQ0IIRLmX1nhMSFMZd1LyXO55%2FDVnQOa775LgMQ9TCrKaMWg2QYhcx57lY%2F2F5qO%2BOh9qAh94aDyCFR3dp6A1owNZoaDJoKKdNQ2uNBnx3cxVowGPUGg%2F9nc1VRgMaYE8am1fHlKJ1rkBAHJ%2BFOcvfIiG3vddLQdJBKchfKq%2Fog5fK84e4BZlfpJ%2Byo6sM39lE2sRV9t307eQqALzNVbSXXUuCqxiyZ5W3uEPmUgWH2viXiUJ7U%2BcB%2FWbUwG%2BMQ%2FjNFmh9WOCcRggSC3GTxEuZA7zV%2F8rViNOoNHdK71UP407dmWGSI7tUV9n9vnL%2Fm7LqKNsjDtnDxuqDhzf3lCcQ%2FyxdJUOjKv4p5lnp0Td1%2F%2FuzmgDoyfBQIXwdyNHCoer%2BF2nVQPr9%2FmnwAHqneMi6UXM8ZOF%2B4FunQQWWR8moVSpSjhCdPv3DBiu8uu%2BBc3cgo%2F9AapfXVoDIOTmdPJDWwsfgsGePUwCiNQHS2u0KkHP7WIotpDiU3lbMoIPxfEkLCE9m%2F1qOT%2FLZf7%2FB9B8%3D)

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



