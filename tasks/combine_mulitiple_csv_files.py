
#Importing packages
import pandas as pd
import glob
import os

#Change working directory
os.chdir('mydir/data')

#Generate list of csv files in the folder
all_csv_files = [f for f in glob.glob('*.csv')]

#Concatenate all the csv files
csv_union = pd.concat([pd.read_csv(f) for f in all_csv_files])

#Export the final csv
csv_union.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
