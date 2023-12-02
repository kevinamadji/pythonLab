s = "Python.org"
p = {}
for char in s:
    if char in p:
        p[char] += 1
    else:
        p[char] = 1

for char in p:
    print(f"Le caractère '{char}' figure {p[char]} dans la chaine de caractère s")