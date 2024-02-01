"""
Exercicio de fixação.
crie um programa que conte quantas vezes cada letra foi usada,
e use ele para identificar qual letra foi usada mais vezes. 

"""

frase = 'O Python e uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido Van Rossum. '.upper()

contador_letras = {}


index = 0
while index < len(frase):
    letra = frase[index]
    if letra.isalpha() or letra == 'Ã' or  letra == 'Ç':
        contador_letras[letra] = contador_letras.get(letra, 0) + 1
    index += 1
    

letra_mais_frequente = max(contador_letras, key=contador_letras.get)

print(frase)

print('Contagem de Letras: \n')
for key,value in sorted(contador_letras.items()):
    print(f'{key}={value}')


print("\nA letra mais usada é: ", letra_mais_frequente)
