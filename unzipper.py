import pandas as pd
from ast import literal_eval
from datetime import datetime

df = pd.read_excel('combine_clean2.xlsx')

li = list()

for item in df['question']:
    x = literal_eval(item)
    print(x)
    li.append(x)

li2 = list()

for item in df['author']:
    x = literal_eval(item)
    print(x)
    li2.append(x)

q = pd.DataFrame(li)
a = pd.DataFrame(li2)

li3 = list()

for item in a['badge']:
    if item == []:
        x = {'type': '', 'description': '', 'topics': []}
    else:
        x = item[0]
    li3.append(x)

b = pd.DataFrame(li3, columns=['badge_type', 'badge_description', 'topics'])
print(b)

li4 = list()

for item in q['updated_time']:
    x = datetime.fromtimestamp(item)
    print(x)
    # if y > 1546300800:
    li4.append(x)

q['question_updated'] = li4


li5 = list()

for item in q['created']:
    x = datetime.fromtimestamp(item)
    print(x)
    # if y > 1546300800:
    li5.append(x)

q['question_created'] = li5



print(q.dtypes)
print(a.dtypes)
q.rename({'id':'question_id', 'title': 'question_title', 'created': 'question_created_time', 'updated_time': 'question_updated_time'}, inplace=True, axis=1)
a.rename({'id': 'author_id', 'name': 'author_name'}, inplace = True, axis=1)
print(q['question_id'])

# df3 = pd.concat([df,q,a], axis=1)
# df3.to_excel('clean_full.xlsx')

print(q[['question_id', 'question_title']])



df2 = pd.concat([df, q[['question_id', 'question_title', 'question_created', 'question_created_time', 'question_updated', 'question_updated_time']], a[['author_id', 'author_name', 'is_org', 'headline','user_type' , 'gender', 'is_advertiser']], b[['badge_type', 'badge_description']]], axis=1)
df2.drop(['question', 'author'], axis=1, inplace=True)
print(df2.columns)

df2.to_excel('clean_extract.xlsx')






