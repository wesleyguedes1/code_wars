numbers = [1, 2, 2, -56, 8, 12, 65, 34, 14]
soma = 0
for i in range(len(numbers)):
    soma+=numbers[i]
print(soma)
if soma % 2 == 0:
    print('par')
else:
    print('ímpar')