import json

from classes.models import Metamodel
from classes.optimizers import Random_Search_Optimizer

#Define FUNCTION
f = bn.F1(1)
f.domain = [-5, 5]
f.dimension = 2


with open('data/configuration.json', 'r') as f:
    configuration = json.load(f)


#Carrega tudo o que é necessário:
representation = Metamodel(configuration)


#Cria um experimento:
experiment = Experiment(a, b, c, d, ...)

#roda:
experiment.run()