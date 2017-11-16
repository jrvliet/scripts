
from __future__ import print_function
import pandas as pd
import sys


for filename in sys.argv[1:]:

    print('\nColumns in {0:s}:'.format(filename))
    with pd.HDFStore(filename) as store:
        key = store.keys()[0]

        df = store.select(key)
        for label in df.axes[1]:
            print('\t{0:s}'.format(label))

