import json

from classes.models import Metamodel
from classes.optimizers import Random_Search_Optimizer

#Define FUNCTION
#f = bn.F1(1)
#f.domain = [-5, 5]
#f.dimension = 2


with open('data/configuration.json', 'r') as f:
    configuration = json.load(f)


#Experiment Name:
experiment_name = configuration["experiment"]["trainer"]

print(experiment_name)
#MODEL:
#model = Metamodel(configuration)

