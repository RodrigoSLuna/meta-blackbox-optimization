from abc import ABC, abstractmethod
class Experiment(ABC):
  
    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        pass

class CEU(Experiment):
    '''choose -> evaluate -> update'''


    def __init__(self, runs, test_interval, max_evaluations, function, optimizer, trainer, evaluator, visualizer):
        self.runs            = runs
        self.test_interval   = test_interval
        self.max_evaluations = max_evaluations
        self.function        = function
        self.optimizer       = optimizer
        self.trainer         = trainer
        self.evaluator       = evaluator
        self.visualizer      = visualizer

        self.steps = []

        #self.meta_points = []  self or not?
        #self.curr_hf = []      self or not?
    
    def run(self):
        for i in range(self.runs):
            self.reset()
            self.optimizer.reset()

            self._run()

            #if self.test_interval > 0 and i % self.test_interval == 1:
            #   self.test()

    def _run(self):
        print("running")

        for i in range(self.max_evaluations):

            #CHOOSE POINT:
            new_x = self.optimizer.next_point(self.function.dimension, self.function.domain, self.steps)
            
            #EVALUATE IN F(X):
            new_y = self.function(new_x)

            #UPDATE STEPS:
            self.steps.append([*new_x, new_y])

            #STOP CONDITION:
            if self.stop_condition(new_y):
                break

        print(self.best_x, self.best_y)

    def stop_condition(self, new_y):
        if new_y < self.best_y: 
            self.best_x = self.steps[-1][:-1]
            self.best_y = self.steps[-1][-1]
        pass

    def reset(self):
        self.best_x = [None] * self.function.dimension 
        self.best_y = 99999.0
        pass

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

