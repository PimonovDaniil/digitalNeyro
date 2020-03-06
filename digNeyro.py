#тупа нейрон
# input = 0.5
# weight = 0.0
# realy=0.8
# a=0.3
# for i in range(200):
#     pred=input*weight
#     weight_delta=(pred-realy)*input
#     weight-=weight_delta*a
#     print(pred)


#работа с данными обучающими
# k=0
# for i in range(28):
#     for j in range(28):
#         if mnist['data'][5][k] > 0.1:
#             print('1', end='')
#         else:
#             print('0', end='')
#         k += 1
#     print()
# print(mnist['target'][5])


import json

from sklearn.datasets import fetch_openml

#загружаем файл с весами
with open("weight.txt", "r") as write_file:
    weight= json.load(write_file)
print(weight)

#загружаем данные для обучения
mnist = fetch_openml('mnist_784')


for i in range(len(mnist['data'])):
    input = mnist['data'][i]

