import matplotlib.pyplot as plt
import sys
import glob
import os

paths = ["same_functions/", "different_functions/"]

for dir_path in paths:
    for run in range(2):

        for file_path in glob.glob(dir_path + "*" + str(run)):
            

            with open(file_path, "r") as f:
                file = f.read()

            file = file.split("\n")
            min_value = float(file[0].split()[1])

            y_value = []
            for i in range(2, 52):
                s, y = file[i].split()
                y_value.append(float(y))

            print(file_path)
            print(min(y_value))
            print()