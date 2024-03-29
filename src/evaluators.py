import numpy as np
import os
import json

from abc import ABC, abstractmethod
class Evaluator(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def write(self, y_values):
        pass

class StepEvaluator(Evaluator):

    def __init__(self, root_path):
        self.root_path = root_path


    def create_folders(self, nb_functions, configuration):
        self.folder_path = self.root_path + "/Function"

        for i in range(nb_functions):
            try:
                os.makedirs(self.folder_path + str(i))
            except:
                pass
        with open(self.root_path + "/cfg.json", "w") as f:
            json.dump(configuration, f, indent=4)

    def write(self, function_id, file_id, min_value, y_values):
        #print("WRITING")
        self.file = open(self.folder_path + str(function_id) + "/output" + str(file_id) + ".txt", "w")

        string = "min_value\n"
        string += str(min_value) + "\n"
        string += "y_values\n"

        for y in y_values:
          string += str(y) + "\n"

        self.file.write(string[:-1]) #remove \n
        self.file_id += 1        

    def dump(self):
        pass
        

# from tqdm import tqdm
# import numpy as np

# class Absvalue_Evaluator:

#     def __init__(self, nb_trials=100, verbose=1):
#         self.nb_trials = nb_trials
#         self.verbose = verbose

#     def evaluate(self, f, optimizer):
        
#         sum_x = [0, 0]
#         sum_x2 = [0, 0]
        
#         #Define Iterator:
#         if self.verbose:
#             iterator = tqdm(range(self.nb_trials))
#         else:
#             iterator = range(self.nb_trials)
        
#         #Iteration:
#         for trial in iterator:
#             steps, done = optimizer.optimize(f)

#             sum_x[0] += steps[:, 1][-1]
#             sum_x[1] += done
#             sum_x2[0] += sum_x[0]*sum_x[0]
#             sum_x2[1] += sum_x[1]*sum_x[1]

#         mean = [sum_x[0]/self.nb_trials, sum_x[1]/self.nb_trials] 
#         stdev = [np.sqrt((sum_x2[0]/self.nb_trials) - (mean[0]*mean[0])),
#                  np.sqrt((sum_x2[1]/self.nb_trials) - (mean[1]*mean[1]))]

#         return {"values": [abs(mean[0]), abs(stdev[0])], "opt": [mean[1], stdev[1]]}



# class MeanStd_Steps_Evaluator:
    
#     '''Evaluator
       
#        @init:
#        nb_trials = max number of iterations
#        verbose = True shows progress bar
       
#        @optimize:
#            *input:
#                f = function to be optimized
#                warning: 
#                    - f.opt = optimal value
#                    - f.domain = interval to search, e.g. [-5, 5]
#                    - f.dimension = dimension of the function
#                 optimizer = optimize that will be used to optimize the function
#            *output:
#                if optimal point was found in all iterations: 
#                    {"mean": mean, "stdev": stdev}
#                else: 
#                    {"mean": None, "stdev": None}
#     '''
    
#     def __init__(self, nb_trials=100, verbose=1):
#         self.nb_trials = nb_trials
#         self.verbose = verbose

#     def evaluate(self, f, optimizer):
        
#         sum_x = 0
#         sum_x2 = 0
        
#         #Define Iterator:
#         if self.verbose:
#             iterator = tqdm(range(self.nb_trials))
#         else:
#             iterator = range(self.nb_trials)
        
#         #Iteration:
#         for trial in iterator:
#             bestx, step = optimizer.optimize(f)
#             try:
#                 bestx, step = optimizer.optimize(f)
#             except:
#                 return {"mean": None, "stdev": None}
            
#             sum_x += step
#             sum_x2 += step*step

#         mean = sum_x / self.nb_trials
#         stdev = np.sqrt((sum_x2 / self.nb_trials) - (mean * mean)) 
        
#         return {"mean": mean, "stdev": stdev}