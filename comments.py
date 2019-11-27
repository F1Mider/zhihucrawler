import zhihuapi as api
import pandas as pd


with open('cookie') as f:
    api.cookie(f.read())

df = pd.read_excel("combine_clean2.xlsx")

# Error at 723 5287 6026 6119 6127
for i in range(0,9809,1):
    if i not in (723,5287,6026,6119,6127):
        aid = df['id'][i]
        data = api.answer(df['id'][i])
        filename = 'comments/' + str(aid) + '.csv'
        run = True
        if df['comment_count'][i] == 0:
            run = False
        x = 0
        print(aid)
        print(i)
        while run:
            df2 = pd.DataFrame(data.comments(x))
            df2['answer_id'] = aid
            print(x)
            if df2.shape[0] != 20:
                run = False
            if x == 0:
                df2.to_csv(filename)
            else:
                df2.to_csv(filename, mode="a", header=False)
            x += 20


# b = pd.DataFrame(a.comments())

# ls = b['content']

# print(ls)

# print(a.comments())

# qir = qid.iterrows()
# print(qir)

# for item in qid['link']:
#     print(item)
#     i = item.split('/')
#     if i[3] == 'question':
#         questionID = i[4]
#         filename = 'output/' + questionID + '.csv'
#         data = api.question(int(questionID))
#
#         run = True
#         x = 0
#
#         while run:
#             df = pd.DataFrame(data.answers_bypage(x))
#             print(x)
#             if df.shape[0] != 20:
#                 run = False
#             if x == 0:
#                 df.to_csv(filename)
#             else:
#                 df.to_csv(filename, mode="a", header=False)
#             x += 20

# with open("out.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(data.answers_byvote())

# # Step 2
# with open("test.txt", 'wb') as config_dictionary_file:
#     # Step 3
#     pickle.dump(data.answers_byvote(), config_dictionary_file)
