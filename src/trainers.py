import numpy as np
from keras.models import load_model
import numpy as np

from abc import ABC, abstractmethod
class Trainer(ABC):

    def __init__(self, configuration):
        self.configuration = configuration
        
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def fit(self):
        pass

class DNNTrainer(Trainer):

    def __init__(self, dnn_path, data_path, batch_size, epochs):
        #super().__init__(configuration)
        self.dnn_path = dnn_path
        self.data_path = data_path
        self.batch_size = batch_size
        self.epochs = epochs

        self.model = None

    def reset(self):
        pass

    def fit(self):
        
        #Load:
        self.model = load_model(self.dnn_path)

        #Reshape:
        data = np.load(self.data_path)
        self.x = data[:, :-1]
        self.y = data[:, -1]

        #Fit:
        self.model.fit(self.x, self.y, batch_size=self.batch_size, epochs=self.epochs)
        
        #Save:
        self.model.save(self.dnn_path)

    @staticmethod
    def fit_gen(points, Hf, y_net):
        
        while True:
            for i in range(len(points)):
                x_batch = []
                y_batch = []
                    
                for j in range(1):
                    x_item = np.concatenate((points[i], Hf[i].flatten()))
                    y_item = y_net[i]
                    x_batch.append(x_item)
                    y_batch.append(y_item)
                    
                yield np.array(x_batch), np.array(y_batch)
