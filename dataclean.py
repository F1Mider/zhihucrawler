import pandas as pd
from datetime import datetime
import re

# df = pd.read_csv("combine.csv", encoding='UTF-8')
df = pd.read_csv("comments.csv", encoding='UTF-8')

# li = list()

# for item in df['updated_time']:
#     x = datetime.fromtimestamp(item)
#     print(x)
#     # if y > 1546300800:
#     li.append(x)
#
# df['updated'] = li

print(df)

df.to_excel('comments_unedited.xlsx')

li2 = list()

for item in df['created_time']:
    x = datetime.fromtimestamp(item)
    print(x)
    # if y > 1546300800:
    li2.append(x)

df['created'] = li2

ls = df['content']
li3 = list()

for item in ls:
    str = re.sub('<.*?>', '\n', item)
    # str = re.sub(r'[^\u0000-\u9999]+', "", str)
    # str = str.replace("\xb4", "")
    str = re.sub(r'\n\s*\n', '\n\n', str)
    li3.append(str)

df['content'] = li3

df.rename({'Unnamed: 0': 'no'}, axis=1, inplace=True)

print(df.columns)

# Unnamed: 0	allow_delete	allow_like	allow_reply	allow_vote	author	can_collapse	can_recommend	collapsed
# content	created_time	disliked	featured	id	is_author	is_delete	is_parent_author	reply_to_author
# resource_type	reviewing	type	url	vote_count	voting

# df2 = df[['no', 'id', 'created', 'created_time', 'updated', 'updated_time', 'content', 'voteup_count', 'comment_count', 'question', 'author']]
df2 = df[['no', 'id', 'created', 'created_time', 'content', 'vote_count', 'is_author', 'is_parent_author', 'filename', 'author']]

print(df2.shape)

df2.to_csv('combine_clean.csv')
df2.to_excel('comments_clean.xlsx')
