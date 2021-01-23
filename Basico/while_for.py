
nome = 'paulo'

i = 0

while i < len(nome):
    print(nome[i])
    i += 1

print()

for v in nome:
    print(v)

print()

for v in range(len(nome)):
    print(v, nome[v])

print("....")

for i, v in enumerate(nome):
    print(i,v)

print("....")

cidade = 'Teresina'
for c, v in enumerate(cidade, start=10):
    print(c, v)