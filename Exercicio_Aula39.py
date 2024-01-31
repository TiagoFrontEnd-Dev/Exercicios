"""
Iterando strings com while
"""

name = 'Tiago Oliveira'
indice = 0
new_name = ''

while indice < len(name):
    letra = name[indice]
    new_name += f'*{letra}'
    indice += 1 


new_name += '*'
print(new_name)



    
