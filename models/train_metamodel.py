import numpy as np

from keras.models import load_model


class Trainer:

    def __init__ (self, model, generator):
        self.model = model
        self.generator = generator




model = load_model('metamodel.h5')
data = np.load("0.npy")

print(data.shape)
print(data[0].shape)
#print(data[0])
#x = data[:, :2]
#y = data[:, -1]

print(x.shape)
print(y.shape)

#model.fit()

#trainer = Trainer(model, )