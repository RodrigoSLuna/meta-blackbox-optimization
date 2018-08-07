import matplotlib.pyplot as plt
import os
import numpy as np
import sys

def plot_confidence_interval(root_folder, values):

    #Mean of y_values:
    mean_y_values = values.mean(axis=1)

    #Confidence Interval:
    z_value = 1.96 # 95%
    confidence_interval = z_value * values.std(axis=1)/np.sqrt(values.shape[1]) 

    # plot the shaded range of the confidence intervals
    ub = mean_y_values + confidence_interval
    lb = mean_y_values - confidence_interval

    plt.fill_between(range(y_values.shape[0]), ub, lb, alpha=.5)
                         #color=color, alpha=.5)
    # plot the mean on top

    plt.plot(mean_y_values, label=root_folder)
    plt.legend(loc='best')

def simple_regret(min_value, y_values):
    return abs(min_value - y_values)

def best_regret(min_value, y_values):
    #best_y_values = np.array([[min(y_values[j, :i+1]) for i in range(len(y_values[0]))] for j in range(len(y_values))])

    best_y_values = np.minimum.accumulate(y_values, axis=0)
    return abs(min_value - best_y_values)

def cumulative_regret(min_value, y_values):
    s_r = simple_regret(min_value, y_values)
    return np.cumsum(s_r, axis=0)

def best_cumulative_regret(min_value, y_values):
    b_r = best_regret(min_value, y_values)
    return np.cumsum(b_r, axis=0)

def normalized_cumulative_regret(min_value, y_values):
    s_r = simple_regret(min_value, y_values)
    return np.cumsum(s_r/abs(min_value), axis=0)

def best_normalized_cumulative_regret(min_value, y_values):
    b_r = best_regret(min_value, y_values)
    return np.cumsum(b_r/abs(min_value), axis=0)

def read_data(root_folder):

    files = os.listdir(root_folder)

    y_values = []
    for file in files:

        with open(root_folder + file, "r") as f:
            data = f.read()

        data = data.split("\n")
        min_value = float(data[1])
        y_values.append(np.array([float(item) for item in data[3:]]))

    y_values = np.array(y_values).T

    return min_value, y_values


#Main:
availables_methods = ['simple_regret', 'best_regret', 'cumulative_regret',
                      'best_cumulative_regret', 'normalized_cumulative_regret',
                      'best_normalized_cumulative_regret']
available_colors = ['r', 'g', 'b']

#Method:
try:
    id_method = sys.argv[1]
    if id_method != "all":
        id_method = int(id_method)
        method = availables_methods[id_method]
    else:
        method = id_method
except:
    print("Insert a valid plot method! Availables:")
    for i, method in enumerate(availables_methods):
        print(str(i) + ". " + method)
    exit()

#Folder:
try:
    root_folders = [arg for arg in sys.argv[2:]]
except:
    print("Insert a folder path!")
    exit()

if method == "all":
    for method in availables_methods:
        for i, root_folder in enumerate(root_folders):

            min_value, y_values = read_data(root_folder)
            plot_values = eval(method + "(min_value, y_values)")
            plot_confidence_interval(root_folder, plot_values)

        plt.savefig(method + '.png', bbox_inches='tight')
        plt.clf()

else:
    for i, root_folder in enumerate(root_folders):

        min_value, y_values = read_data(root_folder)
        plot_values = eval(method + "(min_value, y_values)")
        plot_confidence_interval(root_folder, plot_values)

    plt.savefig(method + '.png', bbox_inches='tight')
    plt.clf()














#ONE FILE:

#with open("random/Function0/output0.txt", "r") as f:
#    data = f.read()

#    data = data.split("\n")
#    min_value = float(data[1])
#    y_values = np.array([float(item) for item in data[3:]])

#best_y_values = np.array([min(y_values[:i+1]) for i in range(len(y_values))])

#simple_regret                     = abs(min_value - y_values)
#best_regret                       = abs(min_value - best_y_values)

#cumulative_regret                 = np.cumsum(simple_regret)
#best_cumulative_regret            = np.cumsum(best_regret)


#normalized_cumulative_regret      = np.cumsum(simple_regret/abs(min_value))
#best_normalized_cumulative_regret = np.cumsum(best_regret/abs(min_value))

#print(simple_regret)
#print(best_regret)

#print(cumulative_regret)
#print(best_cumulative_regret)

#print(normalized_cumulative_regret)
#print(best_normalized_cumulative_regret)

#plt.plot(best_normalized_cumulative_regret)
#plt.show()
