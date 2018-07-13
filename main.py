import json

import src.coco_functions as coco_f

from src.experiments import *
from src.optimizers import *
from src.representations import *

with open("cfg/meta.json", 'r') as f:
    configuration = json.load(f)

experiment_type = configuration["experiment"]["type"]

if experiment_type == "CEU":

    #Experiment:
    runs            = configuration["experiment"]["runs"]
    test_interval   = configuration["experiment"]["test_interval"]
    max_evaluations = configuration["experiment"]["max_evaluations"]

    #Function:
    if configuration["experiment"]["function"]["type"] == "F1.1":
        function = coco_f.F1(1)
        function.domain    = (configuration["experiment"]["function"]["domain"])
        function.dimension = (configuration["experiment"]["function"]["dimension"])

    #Optimizer:
    if configuration["experiment"]["optimizer"]["type"] == "meta_model":
        points_strategy     = configuration["experiment"]["optimizer"]["points_strategy"]
        nb_points           = configuration["experiment"]["optimizer"]["nb_points"]
        hist_strategy       = configuration["experiment"]["optimizer"]["hist_strategy"]
        hist_init           = configuration["experiment"]["optimizer"]["hist_init"]
        size_hf             = configuration["experiment"]["optimizer"]["size_hf"]
        best_point_strategy = configuration["experiment"]["optimizer"]["best_point_strategy"]
        if configuration["experiment"]["optimizer"]["representation"]["type"] == "dnn":
            path           = configuration["experiment"]["optimizer"]["representation"]["path"]
            representation = DeepNeuralNetwork(path)
        optimizer = MetamodelOptimizer(representation, points_strategy, nb_points, hist_strategy, hist_init, size_hf, best_point_strategy)
    elif configuration["experiment"]["optimizer"]["type"] == "random":
        optimizer = RandomSearchOptimizer()

    #Trainer:
    if configuration["experiment"]["trainer"]["type"] == None:
        trainer = None

    #Evaluator:
    if configuration["experiment"]["evaluator"]["type"] == None:
        evaluator = None

    #Visualizer:
    if configuration["experiment"]["visualizer"]["type"] == None:
        visualizer = None

    #Experiment:
    experiment = CEU(runs, test_interval, max_evaluations, function, optimizer, trainer, evaluator, visualizer)

experiment.run()