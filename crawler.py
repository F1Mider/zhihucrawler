import zhihuapi as api
import pickle
import csv
import pandas as pd


with open('cookie') as f:
    api.cookie(f.read())

qid = pd.read_excel('zhihuposts.xlsx', header=0)

# qir = qid.iterrows()
# print(qir)

for item in qid['link']:
    print(item)
    i = item.split('/')
    if i[3] == 'question':
        questionID = i[4]
        filename = 'output/' + questionID + '.csv'
        data = api.question(int(questionID))

        run = True
        x = 0

        while run:
            df = pd.DataFrame(data.answers_bypage(x))
            print(x)
            if df.shape[0] != 20:
                run = False
            if x == 0:
                df.to_csv(filename)
            else:
                df.to_csv(filename, mode="a", header=False)
            x += 20

# with open("out.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(data.answers_byvote())

# # Step 2
# with open("test.txt", 'wb') as config_dictionary_file:
#     # Step 3
#     pickle.dump(data.answers_byvote(), config_dictionary_file)
