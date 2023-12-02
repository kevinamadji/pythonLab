a = int(input('Entrez le promier nomnre: '))
b = int(input('Entrez le second nombre: '))

if b !=0:
    print(f"{a // b}, {a%b}")
else:
    print("Le dénominateur doit être différent de 0")