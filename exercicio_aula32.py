"""
Faça um programa que peça ao usuário para digitar o número inteiro,
informe se este número é um par ou um impar. Caso o usuário não digite um número
inteiro informe que não e um numero inteiro.
"""

entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'
    
    if par_impar:
        par_impar_texto = 'par'
        
    print(f'O número{entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro!')

"""
Faça um programa que perguinte a hora ao usuário e, baseando-se no horário
descrito, exiba a sadação apropriada. Ex
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23.
"""

# entrada = input('Digite um horário: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom Dia !!! ')
    elif hora >= 12 and hora <= 17:
        print('Boa Tarde !!! ')
    elif hora >= 18 and hora <= 23:
       print('Boa Noite !!! ')
    else:
        print('Não conheço está hora! ')
except:
    print('Por favor, digite apenas números inteiros!')