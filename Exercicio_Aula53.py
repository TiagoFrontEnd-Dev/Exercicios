"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['tiago', 'victoria', 'hatch']
lista.append('matheo')

ids = range(len(lista))

for i in ids:
    print(i, lista[i], type(lista[i]))
