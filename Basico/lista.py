

# Lista , definido com colchetes []

lista = [1,2]
print(type(lista))

print(dir(lista))

lista = list(range(10))
print(lista)

lista = list(range(1, 10))
print(lista)

lista = list(range(1, 10, 2))
print(lista)

lista = list(range(10, 0, -2))
print(lista)

lista.sort()
print(lista)

lista.append(12)
print(lista)

lista.pop()
print(lista)

lista.extend([12, 14])
print(lista)

print(lista + [16, 18])

print([1, 2, 3]*3)

print ('python pro'.split())

print ('python-pro'.split("-"))

lista = 'python-pro'.split("-")
print(lista)

print('#'.join(lista))