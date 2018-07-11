import json

with open("configuration.json", 'r') as f:
    configuration = json.load(f)

full_dict = {'experiment': configuration.keys()}
while True:
    node = configuration['experiment']
    

print(.keys())
