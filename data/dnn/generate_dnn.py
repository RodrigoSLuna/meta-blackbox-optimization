from keras.models import Model
from keras.layers import Input, Dense, LeakyReLU

a = Input(shape=(17,))
b = Dense(32)(a)
lr_b = LeakyReLU(alpha=0.3)(b)
c = Dense(64)(lr_b)
lr_c = LeakyReLU(alpha=0.3)(c)
d = Dense(32)(lr_c)
lr_d = LeakyReLU(alpha=0.3)(d)
e = Dense(1)(lr_d)
model = Model(inputs=a, outputs=e)
model.compile(optimizer='adam',
              loss='mse')

model.save("metamodel.h5")