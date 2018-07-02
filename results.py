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

#Optimizers:
random_search = opt.Random_Search_Optimizer(verbose=0)
meta_random_search = opt.Meta_Search_Optimizer(metamodel, best_meta_point_strategy="random", verbose=0)
meta_search = opt.Meta_Search_Optimizer(metamodel, best_meta_point_strategy="lowest", verbose=0)

#Optimize:
#steps, done = random_search.optimize(f)
#steps, done = meta_random_search.optimize(f)
#steps, done = meta_search.optimze(f)

#Evaluator:
evaluator = ev.Absvalue_Evaluator(nb_trials=100)

#Evaluate:
d_random = evaluator.evaluate(f, random_search)
d_random_meta = evaluator.evaluate(f, meta_random_search)
d_meta = evaluator.evaluate(f, meta_search)

#Results
print(f.fopt)
print()
print(d_random)
print()
print(d_random_meta)
print()
print(d_meta)

