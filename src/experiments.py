import numpy as np

from abc import ABC, abstractmethod
class Experiment(ABC):
  
    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        pass

class CEU(Experiment):
    '''choose -> evaluate -> update'''


    def __init__(self, runs, test_interval, max_evaluations, functions, optimizer, trainer, evaluator, visualizer):
        self.runs            = runs
        self.test_interval   = test_interval
        self.max_evaluations = max_evaluations

        self.functions       = functions
        self.optimizer       = optimizer
        self.trainer         = trainer
        self.evaluator       = evaluator
        self.visualizer      = visualizer

        #self.meta_points = []  self or not?
        #self.curr_hf = []      self or not?
    
    def run(self):

        for function in self.functions:

            self.curr_function = function
            
            #RESET
            self.reset()

            for i in range(self.runs):

                print("function: " + "-" + ", run:" + str(i))
                evaluations = self._run()
                print("evaluations: " + str(evaluations))
                print("best y: " + str(self.best_y))
                print("best x: " + str(self.best_x))

                #Trainer:
                try:
                    self.save_data()
                    self.trainer.fit()
                except:
                    pass

                #Evaluator:
                try:
                    y_values = self.steps[:, -1]
                    self.evaluator.write(self.curr_function.f.fopt, y_values)
                except:
                    pass

                print("END")

                #if self.test_interval > 0 and i % self.test_interval == 1:
                #   self.test()

    def _run(self):

        for i in range(self.max_evaluations):

            #CHOOSE POINT:
            new_x, hf = self.optimizer.next_point(self.curr_function.dimension, self.steps)
            new_x = self.curr_function.denormalize_x(new_x)

            #EVALUATE IN F(X):
            new_y = self.curr_function(new_x)

            #UPDATE STEP:
            self.steps.append([*new_x, new_y])
            self.info.append(hf)

            #STOP CONDITION:
            if self.stop_condition(new_x, new_y):
                return i

        return self.max_evaluations

    def stop_condition(self, new_x, new_y):
        if new_y < self.best_y: 
            self.best_x = new_x
            self.best_y = new_y

    def save_data(self):
        
        #Info:
        self.info = np.array(self.info)
        info_shape = self.info.shape
        self.info = self.info.reshape((info_shape[0], info_shape[1]*info_shape[2]))
                       
        #Steps:
        self.steps = np.array(self.steps)

        #Concatenate:
        data = np.concatenate((self.steps, self.info), axis=1)

        #Save:
        np.save(self.data_path, data)


    def reset(self):
        self.steps = []
        self.info  = []

        self.best_x = [None] * self.curr_function.dimension 
        self.best_y = 9999999.0

    def test(self):
        print("testing")



# class MetaLearningExperiment(Experiment):
    
#     def __init__(self, runs, test_interval, max_evaluations, function, optimizer, trainer, evaluator, visualizer):
#         self.runs           = runs
#         self.test_interval  = test_interval
#         self.function       = function
#         self.optimizer      = optimizer
#         self.trainer        = trainer
#         self.evaluator      = evaluator
#         self.visualizer     = visualizer

#         self.steps = []

#         #self.meta_points = []  self or not?
#         #self.curr_hf = []      self or not?
    
#     def run(self):
#         for i in range(self.runs):
#             self._run()

#             if self.test_interval > 0 and i % self.test_interval == 1:
#                 self.test()

#     def _run(self):
#         print("running")

#         for i in range(10):

#             #CHOOSE POINTS:
#             meta_points = self.optimizer.meta_points()

#             #CHOOSE CURR_HISTORY:
#             curr_hf = self.optimizer.hf()

#             #PROCESS META-MODEL:
#             meta_evaluations = self.optimizer.predictions(meta_points, curr_hf)

#             #SELECT BEST POINT:
#             new_x = self.optimizer.best_point(meta_points, meta_evaluations)
#             new_x = (2,3)

#             #EVALUATE IN F(X)
#             new_y = self.function(new_x)

#             #UPDATE HISTORY
#             self.optimizer.update([new_x, new_y])

#             #END

#     def test(self):
#         print("testing")

