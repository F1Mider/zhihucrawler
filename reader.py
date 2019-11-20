import pandas as pd

questionID = 28997957
filename = "output/" + str(questionID) + '.csv'

df = pd.read_csv("combine.csv", encoding='UTF-8')

df2 = df[df['content'].str.contains('日本')]
print(df2.shape)

print(df2)

