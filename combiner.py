import pandas as pd
import glob

# path = r'output' # use your path
path = r'comments' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    print(filename)
    df = pd.read_csv(filename, index_col=None, header=0)
    df['filename'] = filename
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

print(frame)

frame.to_csv (r'comments.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path

print (df)


# Reference: https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe