#ejercicio 4
def getCMValues(nombre1, nombre2):
    import os 
    archivo1=open(nombre1,'r')#abre el archivo 
    a= archivo1.read().split() #se asigna el contendio del archivo a la variable
    archivo2=open(nombre2,'r')#abre el archivo 
    b= archivo2.read().split() #se asigna el contendio del archivo a la variable
    aEnteros = list(map(int, a))
    bEnteros = list(map(int, b))
    
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    result=()
    for i in range(0,len(bEnteros)):
        
        if aEnteros[i]==1 & bEnteros[i]==1:
            TP+=1
        else:
            if aEnteros[i]==1 & bEnteros[i]==0:
                FP+=1
            else:
                if aEnteros[i]==0 & bEnteros[i]==0:
                    TN+=1
                else:
                    if aEnteros[i]==0 & bEnteros[i]==1:
                        FN+=1
    result=(TP,FP,TN,FN)
    return result
    
print(getCMValues('datosReales.txt', 'resultadosTest.txt'))

#ejercicio 5

def getMetrics(resultadosTest):
    TP=int(resultadosTest[0])
    FP=int(resultadosTest[0])
    TN=int(resultadosTest[0])
    FN=int(resultadosTest[0])
    accuracy=(TP+TN)/(TP+FP+TN+FN)
    precision=TP/(TP+FP)
    sensiblidad=TP/(TP+FN)
    especificidad=TN/(TP+FP)
    return accuracy,precision,sensiblidad,especificidad

resultados=(getCMValues('datosReales.txt', 'resultadosTest.txt'))
print(getMetrics(resultados))