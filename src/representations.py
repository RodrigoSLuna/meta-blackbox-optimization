from keras.models import load_model
import numpy as np

from abc import ABC, abstractmethod
class Representation(ABC):

    def __init__(self, configuration):
        self.configuration = configuration

    @abstractmethod
    def predict(self):
        pass

class DeepNeuralNetwork(Representation):

    def __init__(self, path):
        #super().__init__(configuration)
        self.path = path
        self.model = load_model(self.path)


    def predict(self, points, history):
        
        history = history.flatten()
        history = np.tile(history, (len(points), 1))
        x_test = np.hstack((points, history))*20
        score = self.model.predict(x_test)
        return score


    




# class Metamodel:

#     def __init__(self, model=None):
#             if model is None:
#                 self.model = Sequential()
#                 #model.add(Dense(32, activation='relu', input_dim = dimension + size_hist*(dimension+1)))
#                 self.model.add(Dense(64, activation='relu', input_dim = 17, kernel_initializer='RandomUniform', bias_initializer='zeros'))
#                 #self.model.add(Dropout(0.5))
#                 self.model.add(Dense(128, activation='relu', kernel_initializer='RandomUniform', bias_initializer='zeros'))
#                 #self.model.add(Dropout(0.5))
#                 self.model.add(Dense(1, activation='linear', kernel_initializer='RandomUniform', bias_initializer='zeros'))

#                 optimizer = keras.optimizers.Adam(lr=0.00001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=1e-6, amsgrad=False)

#                 self.model.compile(loss='mse',
#                               optimizer='adam',
#                               metrics=['accuracy'])
#             else:
#                 self.model = model
            
#     def fit_gen(self, points, Hf, y_net):
        
#         while True:
#             for i in range(len(points)):
#                 x_batch = []
#                 y_batch = []
                    
#                 for j in range(1):
#                     x_item = np.concatenate((points[i], Hf[i].flatten()))
#                     y_item = y_net[i]
#                     x_batch.append(x_item)
#                     y_batch.append(y_item)
                    
#                 yield np.array(x_batch), np.array(y_batch)
    
#     def fit(self, d):
        
#         points = d[:, 0]
#         Hf = d[:, 1]
#         y_net = d[:, 2]
        
#         gen = self.fit_gen(points, Hf, y_net)
#         self.model.fit_generator(gen, steps_per_epoch=1, nb_epoch=32,verbose=0)
        
        
#     def predict(self, points, curr_hf):
        
#         curr_hf = curr_hf.flatten()
#         curr_hf = np.tile(curr_hf, (len(points), 1))
#         x_test = np.hstack((points, curr_hf))*20
#         score = self.model.predict(x_test)
#         return score
#     