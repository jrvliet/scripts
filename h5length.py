
'''
Prints size of hdf5 file
'''

from __future__ import print_function
from pandas import read_hdf
import sys

if len(sys.argv) != 2:
    print('Usage: h5length <filename')
    sys.exit()

fname = sys.argv[1]
df = read_hdf(fname,'data')
numRows = df.shape[0]
numCols = df.shape[1]
print('Number of columns: {0:d}'.format(numCols))
print('Number of rows: {0:d}'.format(numRows))
