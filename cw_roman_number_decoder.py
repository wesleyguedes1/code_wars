numeros = list()
n = str(input('Digite os algarismos romanos: '))
resultado = 0
for i in range(len(n)):
    if n[i] == 'I':
        numeros.append(1)
    elif n[i] == 'V':
        numeros.append(5)
    elif n[i] == 'X':
        numeros.append(10)
    elif n[i] == 'L':
        numeros.append(50)
    elif n[i] == 'C':
        numeros.append(100)
    elif n[i] == 'D':
        numeros.append(500)
    else:
        numeros.append(1000)
for j in range(len(numeros)):
    if j == 0:
        if numeros[j] >= numeros[j + 1]:
            resultado+=numeros[j]
        elif numeros[j] < numeros[j + 1]:
            resultado-=numeros[j]
    elif numeros[j] == numeros[-1]:
            resultado+=numeros[j]
    else:
        if numeros[j] >= numeros [j + 1]:
            resultado+= numeros[j]
        elif numeros[j] < numeros[j + 1]:
            resultado-=numeros[j]
print(resultado)
    