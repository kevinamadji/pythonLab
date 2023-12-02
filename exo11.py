n = int(input('Entrez un nombre entier: '))
for i in range(1, n):
    if n % i == 0:
        print(f'{n} est divisible par {i}')