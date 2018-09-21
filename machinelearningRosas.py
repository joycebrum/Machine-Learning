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
        x[j].append([])
        element = linha.split(',')
        pos = len(element)-1
        classify = element[pos];
        classify=classify[0:len(classify)-1]        
        element.pop(pos)
        if classify == "Iris-setosa" :
            classify = 1
        elif classify == "Iris-versicolor" :
            classify = -1
        else :
            classify = -1
        for i in range(0,pos) :
            element[i] = float(element[i])
        x[j][0].append(element)
        x[j].append(classify)
        j=j+1
    w0 = [[1],[1],[1],[1]]
    i=0
    j=0
    while bool(1):
        sair=bool(1)
        for i in range(0, len(x)):
            
            res=np.dot(np.transpose(w0),np.transpose(x[i][0]))
            
            if(np.sign(res[0]) != x[i][1]):
                sair=bool(0)
                w0=w0+x[i][1]*np.transpose(x[i][0])
        if sair or j>100:
            break
        j=j+1

    #aqui vai começar a verificar a segunda reta

    j=0
    for linha in texto :
        element = linha.split(',')
        pos = len(element)-1
        classify = element[pos];
        classify=classify[0:len(classify)-1]
        if classify == "Iris-setosa" :
            classify = -1
        elif classify == "Iris-versicolor" :
            classify = 1
        else :
            classify = -1
        x[j].pop()
        x[j].append(classify)
        j=j+1
    w1 = [[1],[1],[1],[1]]
    i=0
    j=0
    while bool(1):
        sair=bool(1)
        for i in range(0, len(x)):
            
            res=np.dot(np.transpose(w1),np.transpose(x[i][0]))
            
            if(np.sign(res[0]) != x[i][1]):
                sair=bool(0)
                w1=w1+x[i][1]*np.transpose(x[i][0])
        if sair or j>100:
            print("aqui")
            break
        j=j+1

    print("w0= " ,w0)
    print("w1= " , w1)
    testClassification(w0,w1)

def testClassification(w0,w1):
    arq2 = open('irisDataTest.txt', 'r')
    x = []
    texto = arq2.readlines()
    arq2.close()
    j=0
    for linha in texto :
        x.append([])
        x[j].append([])
        element = linha.split(',')
        pos = len(element)-1
        classify = element[pos];
        classify=classify[0:len(classify)-1]        
        element.pop(pos)
        if classify == "Iris-setosa" :
            classify = 1
        elif classify == "Iris-versicolor" :
            classify = -1
        else :
            classify = -1
        for i in range(0,pos) :
            element[i] = float(element[i])
        x[j][0].append(element)
        x[j].append(classify)

        if classify == "Iris-setosa" :
            classify = -1
        elif classify == "Iris-versicolor" :
            classify = 1
        else :
            classify = -1
            
        x[j].append(classify)
        


        
        j=j+1
    i=0
    for i in range(0, len(x)):
        
        res0=np.dot(np.transpose(w0),np.transpose(x[i][0]))
        res1=np.dot(np.transpose(w1),np.transpose(x[i][0]))
        
        if(np.sign(res0[0]) == x[i][1] and np.sign(res1[0]) == x[i][2]):
            print("correto")
        else:
            print("ERRROOOUUU")



        
