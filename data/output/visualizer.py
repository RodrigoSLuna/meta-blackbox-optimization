import matplotlib.pyplot as plt
import sys
import glob
import os

# First function:
for run in range(2):

    for file_path in glob.glob("*" + str(run)):
        print(file_path)

        with open(file_path, "r") as f:
            file = f.read()

        file = file.split("\n")
        min_value = float(file[0].split()[1])

        step = []
        y_value = []
        for i in range(2, 52):
            s, y = file[i].split()

            step.append(int(s))
            y_value.append(float(y))


        new_y_value = [y_value[0]]
        low_value = y_value[0]
        for i in range(1, len(y_value)):
            if y_value[i] < low_value:
                new_y_value.append(y_value[i])
                low_value = y_value[i]
            else:
                new_y_value.append(low_value)

        horiz_line_data = [min_value for i in range(len(step))]
        plt.plot(step, horiz_line_data, 'r--') 
        plt.plot(step, new_y_value, label=file_path)

    plt.legend(loc='upper left')
    plt.savefig(str(run) + '.png', bbox_inches='tight')
    plt.clf()