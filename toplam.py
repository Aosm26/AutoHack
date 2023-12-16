import pandas as pd

data=pd.read_csv('sales_datavirgul.csv')

toplam=0
satir=0
lbl=''

for i in range(1, 18):
    toplam=0
    lbl=f'{i}'
    # print(i)
    for a in data[lbl]:
        # print(a)
        toplam+=a
        # satir+=1
    # satir-=1
    # data.loc[(satir), f'{i}'] = toplam
    print(toplam)
# print(toplam)


data.to_csv("train_final2.csv",index=False)
data.head()