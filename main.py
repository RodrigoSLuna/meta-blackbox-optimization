import json

import classes.coco_functions as coco_f

from classes.experiments import *


with open("data/configuration.json", 'r') as f:
    configuration = json.load(f)

experiment_type = configuration["experiment"]["type"]

if experiment_type == "meta_online_learning":

    runs          = configuration["experiment"]["runs"]
    test_interval = configuration["experiment"]["test_interval"]
    
    if configuration["experiment"]["function"]["type"] == "F1.1":
        function = coco_f.F1(1)
        function.domain    = (configuration["experiment"]["function"]["domain"])
        function.dimension = (configuration["experiment"]["function"]["dimension"])

    if configuration["experiment"]["optimizer"]["type"] == "meta_model":
        choose_points = configuration["experiment"]["optimizer"]["choose_points"]
        choose_curr_hist = configuration["experiment"]["optimizer"]["choose_curr_hist"]
        select_best_point = configuration["experiment"]["optimizer"]["select_best_point"]
        optimizer = None

        if configuration["experiment"]["optimizer"]["representation"]["type"] == "dnn":
            path = configuration["experiment"]["optimizer"]["representation"]["path"]
            representation = None

    if configuration["experiment"]["trainer"]["type"] == None:
        trainer = None

    if configuration["experiment"]["evaluator"]["type"] == None:
        evaluator = None

    if configuration["experiment"]["visualizer"]["type"] == None:
        visualizer = None

    experiment = MetaLearningExperiment(runs, test_interval, function, optimizer, trainer, evaluator, visualizer)

experiment.run()