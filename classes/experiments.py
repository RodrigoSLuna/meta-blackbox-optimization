from abc import ABC, abstractmethod
class Experiment(ABC):
  
    def __init__(self):
        pass

    @abstractmethod
    def run(self, f):
        pass

class MetaLearningExperiment(Experiment):
    
    def __init__(self, runs, test_interval, function, optimizer, trainer, evaluator, visualizer):
        self.runs           = runs
        self.test_interval  = test_interval
        self.function       = function
        self.optimizer      = optimizer
        self.trainer        = trainer
        self.evaluator      = evaluator
        self.visualizer     = visualizer
    
    def run(self):
        print("running")

