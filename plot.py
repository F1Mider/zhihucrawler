import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

df = pd.read_csv("combine.csv", encoding='UTF-8')

li = list()

for item in df['updated_time']:
    x = datetime.fromtimestamp(item)
    print(x)
    # if y > 1546300800:
    li.append(x)

df['new_time'] = li

print(df['new_time'])



a = plt.hist(li, bins=100)
# plt.show(a)