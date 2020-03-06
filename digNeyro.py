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


#Создаём файл с весами
import json
# weight=[]
# for i in range(784):
#     weight.append(0.0)
# with open("weight.txt", "w") as write_file:
#     json.dump(weight, write_file)


# from sklearn.datasets import fetch_openml
# mnist = fetch_openml('mnist_784')
# print(len(mnist['data']))
# for i in range(len(mnist['data'])):
#     input = mnist['data'][i]

