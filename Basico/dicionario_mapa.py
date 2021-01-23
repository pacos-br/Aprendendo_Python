
# Dicionarios que junta chaves e valores, é usado chaves {}

linguas = {'br' : 'portugues', 'eua':"ingles"}
print(type(linguas))
print(linguas)
print(linguas['br'])
print("....")
print(linguas.get('es'))
print("....")
print(linguas.get('es', 'valor padrão')) #se não existir, é apresentado o valor padrão definido
print(linguas.get('br', 'valor padrão'))
print("....")
print('br' in linguas) #verifica se existe a chave
print('br' in linguas.keys())
print('portugues' in linguas.values())
print('es' in linguas) #verifica se existe a chave
print("....")
print(6 in list(range(10)))
print(11 in list(range(10)))
print("....")
linguas['es']='spanhol'
print(linguas['es'])
linguas['es']='espanhol'
print(linguas['es'])
print("....")
for chaves in linguas:
    print(chaves)
print("....")
for chaves in linguas.keys():
    print(chaves)
for valor in linguas.values():
    print(chaves)
print("....")
for chaves, valor in linguas.items():
    print(chaves, valor)
print("....")
linguas.pop('br')
print(linguas)
del linguas['eua']
print(linguas)
