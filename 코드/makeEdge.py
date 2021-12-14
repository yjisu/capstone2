import pandas as pd
import numpy as np
df = pd.read_excel("C:/Users/yangj/OneDrive/바탕 화면/캡스톤2/capstone2/capstone2/분석자료/부상자test.xlsx")
#print(df)
df_list = df.values.tolist()
#print(df_list)
new=[0]
for one in range(0,len(df_list)):
    for i in range(1,8):
         new.append([df_list[one][0],df_list[one][i]])
    for j in range(2, 8):
        new.append([df_list[one][1], df_list[one][j]])
    for k in range(3,8):
        new.append([df_list[one][2], df_list[one][k]])
    for m in range(4, 8):
        new.append([df_list[one][3], df_list[one][m]])
    for s in range(5, 8):
        new.append([df_list[one][4], df_list[one][s]])
    for t in range(6, 8):
        new.append([df_list[one][5], df_list[one][t]])
    for p in range(7, 8):
        new.append([df_list[one][6], df_list[one][p]])

del(new[0])
print(new[0][1])
a=[0]
b=[0]
for i in range(len(new)):
    a.append(new[i][0])

print(a)
del(a[0])
for i in range(len(new)):
    b.append(new[i][1])
print(b)
del(b[0])
col_name =['source','target']
df_att = pd.DataFrame([ x for x in zip(a,b)],columns=col_name)
#df_att = pd.DataFrame(df_list,)
df_att.to_excel('부상자text_Edge.xlsx', index=False)
