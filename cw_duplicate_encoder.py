def duplicate_encode(word):
	word = word.casefold()
	c = 0
	while c < len(word):
		
		for i in range(len(word)):
			if word[c] == word[i] and i != c:
				word = word.replace(word[c], "_")
		c+=1
	for j in range(len(word)):
		if word[j] != "_":
			word = word.replace(word[j], "(")
	for k in range(len(word)):
		if word[k] == "_":
			word = word.replace(word[k], ")")
duplicate_encode("FHcdwd(cTk!")

		

'''a = str(input("digita algo aí: "))
c1 = 0
rep = 0
for i in range(len(a)):
	cont = a.count(a[c1])
	if cont > 1:
		rep+=1
	c1+=1
print('Há', rep, 'repetições na palavra ',a)'''



	