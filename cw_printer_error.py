teste = str(input('Digite as cores usadas: '))
accepted_colors = {'a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'}
errors = 0
for i in range(len(teste)):
    if teste[i] not in accepted_colors:
        errors+=1
print(errors,'/', len(teste))