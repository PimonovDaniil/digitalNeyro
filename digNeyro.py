import json
from sklearn.datasets import fetch_openml

def w_sum(a, b):
    assert(len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i] * b[i])
    return output

def neural_network(input, weights): #возвращает сумму перемноженных на input весов
    pred = w_sum(input, weights)
    return pred

def ele_mul(delta, input):
    output =[]
    for i in range(len(input)):
        output.append(0)
    assert (len(output) == len(input))

    for i in range(len(output)):
        output[i]= delta*input[i]
    return output

#загружаем файл с весами
with open("weight.txt", "r") as write_file:
    weights = json.load(write_file) #10*784

# #генерируем структуру
# weights=[]
# for i in range(10):
#     s=[]
#     for j in range(784):
#         s.append(1)
#     weights.append(s)
# print(weights)

#загружаем данные для обучения
mnist = fetch_openml('mnist_784')

alpha = 0.000000001 #чистая магия

#Проверка обученности нейронки
sum=0
kol=0
for i in range(10000):
    sum+=1
    print(mnist['target'][i], end=' ')
    m=[]
    for k in range(10):
        pred = neural_network(mnist['data'][i], weights[k])
        m.append(pred)
        #print(pred)
    print(m.index(max(m)))
    #ожидание - реальность
    if(int(mnist['target'][i])==m.index(max(m))):
        kol+=1
print(str((kol/sum)*100)+"% успеха")

# #обучение нейронки
# for j in range(69000):#входные даныные
#     #print(j)
#     #print(mnist['target'][j])
#     input= mnist['data'][j] #вход 784
#     really = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] #ожидаемый выход 10 нейронов
#     really[int(mnist['target'][j])] = 1.0
#     for k in range(len(really)):#обучаем один набор нейросети (k - кол-во выходов)
#         pred = neural_network(input, weights[k])
#         delta = (pred - really[k])
#         weight_deltas = ele_mul(delta, input)
#         error = (pred - really[k])**2
#         # print("error " + str(error))
#         # print("pred: " + str(pred))
#         for i in range(len(weights[k])):
#             weights[k][i] -= weight_deltas[i] * alpha
#         #print("pred: " + str(pred))
#         #print("error: "+str(error))
#     #сохраняем результат, чтобы не потерять его
#     if (j+1)%1000 == 0:
#         print("load result  j = "+str(j+1))
#         with open("weight.txt", "w") as write_file:
#             json.dump(weights, write_file)# сохраняем веса