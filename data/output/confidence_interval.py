import matplotlib.pyplot as plt
import sys
import glob
import os
import numpy as np

#z_value = 1.96 # 95%

#v = mean + z_value * std/math.sqrt(len(values)) 

#run = '0'

#Reading data:
root_folder = "random/Function0/"
files = os.listdir(root_folder)

y_values = []
for file in files:

    with open(root_folder + file, "r") as f:
        data = f.read()

    data = data.split("\n")
    min_value = float(data[1])
    y_values.append(np.array([float(item) for item in data[3:]]))

y_values = np.array(y_values).T


def plot_confidence_interval(values):

    #Mean of y_values:
    mean_y_values = y_values.mean(axis=1)

    #Confidence Interval:
    z_value = 1.96 # 95%
    confidence_interval = z_value * y_values.std(axis=1)/np.sqrt(y_values.shape[1]) 

    # plot the shaded range of the confidence intervals
    ub = mean_y_values + confidence_interval
    lb = mean_y_values - confidence_interval

    plt.fill_between(range(y_values.shape[0]), ub, lb,
                         color='b', alpha=.5)
    # plot the mean on top
    plt.plot(mean_y_values, 'b')

    plt.show()


plot_confidence_interval(y_values)



exit()


plt.plot(step, new_y_value, label=file_path)


plt.legend(loc='upper left')
plt.savefig(str(run) + '.png', bbox_inches='tight')
plt.clf()
