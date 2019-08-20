

import pandas as pd
import glob
import os


os.chdir('/Users/smehta/Desktop/hps/data')

all_csv_files = [f for f in glob.glob('*.csv')]

csv_union = pd.concat([pd.read_csv(f) for f in all_csv_files])

csv_union.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
