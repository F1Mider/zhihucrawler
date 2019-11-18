import pandas as pd

questionID = 326486872
filename = str(questionID) + '.csv'

df = pd.read_csv(filename, encoding='UTF-8')

print(df)