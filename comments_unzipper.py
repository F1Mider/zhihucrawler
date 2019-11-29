import pandas as pd
import re
from ast import literal_eval
from datetime import datetime

df2 = pd.read_excel("comments_unedited.xlsx")


lis = list()

for item in df2['created_time']:
    x = datetime.fromtimestamp(item)
    print(x)
    # if y > 1546300800:
    lis.append(x)

df2['created'] = lis

ls = df2['content']
lis3 = list()

for item in ls:
    print(item)
    if pd.notna(item):
        str = re.sub('<.*?>', '\n', item)
    # str = re.sub(r'[^\u0000-\u9999]+', "", str)
    # str = str.replace("\xb4", "")
        str = re.sub(r'\n\s*\n', '\n\n', str)
    else:
        str = ''
    lis3.append(str)

df2['content'] = lis3

df2.rename({'Unnamed: 0': 'no'}, axis=1, inplace=True)

print(df2.columns)



# Unnamed: 0	allow_delete	allow_like	allow_reply	allow_vote	author	can_collapse	can_recommend	collapsed
# content	created_time	disliked	featured	id	is_author	is_delete	is_parent_author	reply_to_author
# resource_type	reviewing	type	url	vote_count	voting

df10 = df2[['no', 'id', 'created', 'created_time', 'content', 'vote_count', 'featured']]
df = df2[['disliked', 'reply_to_author', 'voting', 'filename', 'author']]

df10['filename'] = 0
df10['reply_to_author'] = ''
df10['voting'] = ''
df10['author'] = df['author']
df10['disliked'] = ''

def russian_taowa(a):
    l1 = level1(a)
    l2 = level2(l1)
    l3 = level3(l2)
    print(l3)
    return l3


def level1(a):
    x = literal_eval(a)
    print(x)
    s = pd.DataFrame(x)
    print(s)
    return s


def level2(a):
    s = pd.DataFrame(a['member'])
    a1 = a.append(s)
    a2 = a1.drop('member')

    return a2


def level3(a):
    t = a['badge']
    if t == []:
        x = {'type': '', 'description': '', 'topics': []}
    else:
        x = t[0]
    s = pd.DataFrame(x)
    a1 = a.add(s)
    a2 = a1.drop('badge')

    return a2


for i, item in df.iterrows():
    filename = item['filename']
    rta = item['reply_to_author']
    voting = item['voting']
    author = item['author']
    disliked = item['disliked']

    x = re.findall(r'\d+', filename)
    # print(int(x[0]))
    df10['filename'][i] = int(x[0])

    # TODO: taowa
    # russian_taowa(author)


    if pd.isna(rta):
        df10['reply_to_author'][i] = False
    elif rta == False:
        df10['reply_to_author'][i] = False
    else:
        df10['reply_to_author'][i] = True

    if pd.isna(disliked):
        df10['disliked'][i] = False
    elif disliked == False:
        df10['disliked'][i] = False
    else:
        df10['disliked'][i] = True

    if pd.isna(voting):
        df10['voting'][i] = False
    elif voting == False:
        df10['voting'][i] = False
    else:
        df10['voting'][i] = True



print(df10['filename'])








print(df2.columns)

df2.to_excel('comments_extract.xlsx')






