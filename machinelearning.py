import numpy as np
import random

def lerRosas() :
    arq = open('IrisDataAllset.txt', 'r')
    linhas = []
    texto = arq.readlines()
    for linha in texto :
        linhas.append(linha)
    arq.close()
    randomData(linhas)

def randomData(linhas) :
    choiced = []
    for i in range(0,30):
        position = random.randint(0, len(linhas)-1)
        choiced.append(linhas[position])
        del(linhas[position])
    arqTest = open('irisDataTest.txt', 'w')
    arqTest.writelines(choiced)
    arqData = open('irisData.txt', 'w')
    arqData.writelines(linhas)
    arqTest.close()
    arqData.close()

def classification() :
    arq = open('irisData.txt', 'r')
    x = []
    texto = arq.readlines()
    arq.close()
    j=0
    for linha in texto :
        x.append([])
        element = linha.split(',')
        pos = len(element)-1
        classify = element[pos];
        element.pop(pos)
        if classify == "Iris-setosa" :
            p
            classify = 1
        elif classify == "Iris-versicolor" :
            classify = -1
        else :
            classify = -1
        for i in range(0,pos) :
            element[i] = float(element[i])
        x[j].append(element)
        x[j].append(classify)
        j=j+1
    w = [[1],[1],[1],[1]]
    i=0
    wt=np.transpose(w)
    xt=np.transpose(x)
    
    print(wt)
    print(x[0][1])
    print(np.transpose(x[0][0]))
    for i in range(0, len(x)):
        res=np.dot(wt,np.transpose(x[i][0]))
        
        print("resultado ", i, res)
        print(np.sign(res[0]))
        print(x[i][1])
        if(np.sign(res[0]) == x[i][1]):
            print("YYYEEEEAAAAHHH")






        
