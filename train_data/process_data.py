import sys, os
import numpy as np

folders = set(os.listdir()) - set([sys.argv[0]])

for folder in folders:
    np_files = os.listdir(folder)

    samples = []
    for np_file in np_files:
        samples.append(np.load(os.path.join(folder, np_file)))
    samples = np.array(samples)
    samples = samples.reshape((samples.shape[0]*samples.shape[1], samples.shape[2]))
    np.save(folder + ".npy", samples)
