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

weights = [[0.1, 0.2, -0.1],[0.1, 0.2, -0.1]]
input= [8.5, 0.65, 1.2] #вход
really = [2, 3] #выход
alpha = 0.01

for k in range(len(really)):
    for j in range(10):#цикл для обучения нейронов
        pred = neural_network(input, weights[k])
        delta = (pred - really[k])
        weight_deltas = ele_mul(delta, input)

        for i in range(len(weights)):
            weights[k][i] -= weight_deltas[i] * alpha
    print(pred)