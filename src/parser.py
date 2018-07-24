
from src.experiments import *
from src.optimizers import *
from src.representations import *
from src.trainers import *
from src.functions import *
from src.evaluators import *

def create_experiment(configuration):

    experiment_type = configuration["experiment"]["type"]

    if experiment_type == "CEU":

        #Experiment:
        runs            = configuration["experiment"]["runs"]
        test_interval   = configuration["experiment"]["test_interval"]
        max_evaluations = configuration["experiment"]["max_evaluations"]

        #Function:
        lst_functions = configuration["experiment"]["function"]["type"]
        functions_0 = lst_functions[0]
        functions_1 = lst_functions[1]

        functions_0 = [item.split(".") for item in functions_0]
        train_functions = []
        for f, instance in functions_0:
            domain    = configuration["experiment"]["function"]["domain"]
            dimension = configuration["experiment"]["function"]["dimension"]
            function = Function(f, instance, domain, dimension)
            train_functions.append(function)
        
        functions_1 = [item.split(".") for item in functions_1]
        test_functions = []
        for f, instance in functions_1:
            domain    = configuration["experiment"]["function"]["domain"]
            dimension = configuration["experiment"]["function"]["dimension"]
            function = Function(f, instance, domain, dimension)
            test_functions.append(function)

        functions = [train_functions, test_functions]

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
        elif configuration["experiment"]["trainer"]["type"] == "episodic_dnn":
            dnn_path   = configuration["experiment"]["trainer"]["dnn_path"]
            data_path  = configuration["experiment"]["trainer"]["data_path"]
            batch_size = configuration["experiment"]["trainer"]["batch_size"]
            epochs     = configuration["experiment"]["trainer"]["epochs"]
            trainer = DNNTrainer(dnn_path, data_path, batch_size, epochs)

        #Evaluator:
        if configuration["experiment"]["evaluator"]["type"] == None:
            evaluator = None
        elif configuration["experiment"]["evaluator"]["type"] == "step_evaluator":
            root_path = configuration["experiment"]["evaluator"]["root_path"]
            evaluator = StepEvaluator(root_path)
            
        #Visualizer:
        if configuration["experiment"]["visualizer"]["type"] == None:
            visualizer = None

        #Experiment:
        experiment = CEU(configuration, runs, test_interval, max_evaluations, functions, optimizer, trainer, evaluator, visualizer)

        #Return:
        return experiment