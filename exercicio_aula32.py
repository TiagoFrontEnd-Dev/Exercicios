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

    print(f'o número {entrada_int} é {par_impar_texto}')
else:
    print('Voce nao digitou um número inteiro!')

"""
Faça um programa que perguinte a hora ao usuário e, baseando-se no horário
descrito, exiba a sadação apropriada. Ex
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23.
"""

entrada = input('Digite um horário: ')

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
    ...


"""
Faça um programa que peça o primeiro nome do usuário. Se o usuario Tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 a 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome =  input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome e curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome e normal')
    elif tamanho_nome >= 6:
        print('Seu nome e muito grande')
else:
    print('Por favor, digite um nome!')