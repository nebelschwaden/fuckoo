import json
import csv
import os
import pandas as pd
from functools import reduce
from glob import glob
#Reading all the files that match a given extension from a directory recursively.
PATH = './reports/'
#PATH = '/home/nebelschwaden/Documents/Proyecto/Data/Analisis/'
result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.json'))]
with open(result[0]) as f:
		data  = json.load(f)
df_dataset = pd.DataFrame()
network_tcp = data['network']['tcp']
print(network_tcp)
print(len(network_tcp))