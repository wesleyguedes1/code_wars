#def suplicate_count(text):
text = str(input("Digita algo aí: "))
c = 0
rep = 0
while c < len(text):
	for i in range(len(text)):
		if text[c] == text[i] and i != c:
			rep+=1
			print(rep)
	c+=1