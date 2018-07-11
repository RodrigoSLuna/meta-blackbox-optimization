import argparse
import json

#Parser flags
parser = argparse.ArgumentParser()
parser.add_argument("-f", help="configuration.json path")
args = parser.parse_args()

#get file_path:
file_path = args.f or "data/configuration.json"

#try to load file:
try:
    with open(file_path, 'r') as f:
        configuration = json.load(f)
except:
    print('[Errno 2] No configuration.json file in this path: \'' + file_path + '\'')
    print("END")
    exit()

#try to begin experiment
try:
    experiment_type = configuration["experiment"]["type"]
except:
    print("experiment->type is not defined")

#try to __init__ experiment
try:
    if experiment_type == "meta_online_learning":
        
        
        experiment = MetaLearningExperiment(runs, test_interval, function, optimizer, trainer, evaluator, visualizer)
except:
    print("experiment __init__ not possible")
    exit()









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