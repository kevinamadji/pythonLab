x = float(input("Entrez le premier nombre: "))
y = float(input("Entrez le deuxième nombre: "))
z = float(input("Entrez le troisième nombre: "))
if x < y:
    max_number = y
elif x<z:
    max_number = z
else:
    max_number = x

print(max_number)
