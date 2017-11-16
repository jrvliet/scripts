
from __future__ import print_function
import pandas as pd
import sys

filename = sys.argv[1]
group = sys.argv[2]

df = pd.read_hdf(filename, group)
header = df.columns.values.tolist()
print(header)
for i in range(len(df)):
    s = ''
    for j in range(len(header)):
        s += '{0:f}\t'.format(df[header[j]][i])
    s += '\n'
    print(s)



