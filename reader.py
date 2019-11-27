import pandas as pd
import re
import csv

# questionID = 28997957
# filename = "output/" + str(questionID) + '.csv'

# df = pd.read_excel("combine_clean2.xlsx")
df = pd.read_csv("combine_clean.csv")

print(df.shape)

print(df['content'][21])

# print(df.shape)

# df2 = df[df['content'].str.contains('垃圾车')]

# # edited or not
# a = 0


# for index, row in df.iterrows():
#     print(row['updated_time'])
#     x = int(row['updated_time']) - int(row['created_time'])
#     if x != 0:
#         a+=1

# print(a)


# print(df2)

# with open("车.csv", "w", newline="", encoding = 'GB18030') as f:
#     writer = csv.writer(f)
#     writer.writerow(li)

# print(df2.shape)


# df2.to_csv('垃圾车.csv')
# df2.to_excel('垃圾车.xlsx')

