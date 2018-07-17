import sys
import json

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'

from src.parser import create_experiment

try:
    cfg_path = sys.argv[1]
except:
    print("Insert a valid cfg_path!")
    exit()

with open(cfg_path, 'r') as f:
    configuration = json.load(f)

experiment = create_experiment(configuration)

experiment.run()