#checar se o array B contém os mesmos itens que o array A, ao quadrado, independentemente da ordem
array1 = [10, 4, 5, 8, 20]
array2 = [100, 25, 64, 400]
same = True
for i in range(0, len(array1) - 1):
    for j in range(0, len(array1) - 1):
        if array1[i] ** 2 == array2[j]:
            print(array1[i] ** 2)
            print(array2[j])
            same = True
            break
        elif array1[i] ** 2 != array2[j]:
            same = False            
    if same == False:
        break
print(same)
