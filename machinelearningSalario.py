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
        
            
        for i in range(0,pos) :
            element[i] = float(element[i])
        x[j][0].append(element)
        x[j].append(classify)
        j=j+1
    w = [[1],[1],[1],[1],[1]]
    i=0
    j=0
    sair=bool(1)
    for i in range(0, len(x)):
            
        res=np.dot(np.transpose(w),np.transpose(x[i][0]))
        if():
            sair=bool(0)
            w=w+x[i][1]*np.transpose(x[i][0])
        print("resultado:", w)







        
