
# Lista , definido com parênteses ()

tpl = (1,2)
print(type(tpl))

print(dir(tpl))

print(tuple(range(10)))

print ((6))
print((6,))

#desenpacotamento de tupla
registro = ('paulo', '47')
nome, idade = registro
print(registro)
print (nome)
print(idade)

nome, idade = ('ana', 31)
print (nome)
print(idade)
registro2 = nome, idade
print(registro2)

print(registro + registro2)
print(id(registro))
print(id(registro2))
print(id(registro + registro2))