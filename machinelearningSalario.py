import numpy as np
import random

def editarArquivo():
    arq = open('salaryDataAllset.txt', 'r')
    linhas = []
    texto = arq.readlines()
    i=0
    for linha in texto :
        linha=linha[7:len(linha)]
        linha=linha.replace("    ",",")
        linhas.append(linha)
    
    arqTest = open('salaryCerto.txt', 'w')
    arqTest.writelines(linhas)
    arq.close()
    randomData(linhas)

def lerSalario() :
    arq = open('salaryCerto.txt', 'r')
    print("Ola")
    linhas = []
    texto = arq.readlines()
    i=0
    for linha in texto :
        linhas.append(linha)
    arq.close()
    print(linhas)
    randomData(linhas)

def randomData(linhas) :
    choiced = []
    for i in range(0,11):
        position = random.randint(0, len(linhas)-1)
        choiced.append(linhas[position])
        del(linhas[position])
    arqTest = open('salaryDataTest.txt', 'w')
    arqTest.writelines(choiced)
    arqData = open('salaryData.txt', 'w')
    arqData.writelines(linhas)
    arqTest.close()
    arqData.close()

def regressao():
    arq = open('salaryData.txt', 'r')
    x = []
    y = []
    texto = arq.readlines()
    arq.close()
    j=0
    for linha in texto :
        y.append([])
        element = linha.split(',')
        pos = len(element)-1
        classify = element[pos]
        classify=classify[0:len(classify)-1]        
        element.pop(pos)
        classify = float(classify)
            
        for i in range(0,pos) :
            element[i] = float(element[i])
        x.append(element)
        y[j].append(classify)
        j=j+1

    pseudoInvX = np.linalg.pinv(x)
    
    return np.dot(pseudoInvX, y), x, y

def testeRegressao() :
    arq = open('salaryDataTest.txt', 'r')
    x = []
    y = []
    texto = arq.readlines()
    arq.close()
    j=0
    for linha in texto :
        element = linha.split(',')
        pos = len(element)-1
        classify = element[pos]
        classify = classify[0:len(classify)-1]
        element.pop(pos)
        classify = float(classify)
        for i in range(0,pos) :
            element[i] = float(element[i])
        x.append(element)
        y.append(classify)
    erro = 0
    j=0
    w, xtotal, ytotal = regressao()
    n = len(x)
    for element in x :
        result = np.dot(np.transpose(w), np.transpose(element))
        print(result[0], y[j])        
        erro = pow(result[0] - y[j],2)
        j=j+1
    erro = erro/n
    return erro




        
