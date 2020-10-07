n =int(input('Digite um número: '))
n = str(n)
numeros = list()
x = 0
for i in range(len(n)):
    i = int(i)
    x = int(n[i])
    numeros.append(x ** 2)
print(numeros)