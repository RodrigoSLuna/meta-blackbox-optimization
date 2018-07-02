#import numpy as np
#from tqdm import tqdm

import classes.bbobbenchmarks as bn
import classes.optimizers as opt
import classes.evaluators as ev

import models.metamodel as metamodel 


#Define problem
f = bn.F1(1)
f.domain = [-5, 5]
f.dimension = 2

#NN Model:
metamodel = metamodel.Metamodel()


for i in range(10):

    #Optimizers:
    meta_search = opt.Meta_Search_Optimizer(metamodel, train=True, output_file=str(i))

    #Optimize:
    steps, done = meta_search.optimize(f)
