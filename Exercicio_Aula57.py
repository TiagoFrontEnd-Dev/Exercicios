"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []


while True:
    print('\nSelecione uma opção')
    opcao = input('[i]nserir, [a]pagar, [l]istar: \n')

    if opcao == 'i':
        os.system('cls')
        valor = input('Item: ')
        lista.append(valor)

    elif opcao == 'a':
        indice_str = input(
            'escolha o item para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor, digite número inteiro. ')
        except IndexError:
            print('Indice não existe na lista. ')
        except Exception:
            print('Erro desconhecido.')

    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Não a nada para listar. ')
        
        for i, valor in enumerate(lista, start=1):
            print(i, valor)
        
    else:
        print('Por favor, escolha uma das opção [i]nserir, [a]pagar, [l]istar : \n')