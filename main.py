#Funções-------------------------------------
def cria():
    control = 0
    lista = []
    while control != 1:
        key = int(input('Digite o número que quer adicionar a lista'))
        lista.append(key)
        resp = str(input('Deseja continuar com a adição de valores?(s/n): '))
        if resp == 's':
            print('continuando...')
        elif resp == 'n':
            print('fechando')
            control = 1
        else:
            print('Valor inválido')
    return lista

def alte(lista):
    print('Digite os valores que deseja alterar. Serão alterado o primeiro e último valor')
    key = [int(input('1: ')), int(input('2: '))]
    lista[0] = key[0]
    lista[-1] = key[1]
    return lista

#main_code-----------------------------------
control = 0 

while control != 1:
    print('1-Criar lista\n2-alterar lista')
    key = int(input('Digite a opção que deseja'))
    if key == 1:
        lista = cria()
        print('Lista criada %s' % lista)
    elif key == 2:
        lista = alte(lista)
        print(lista)
    else:
        print("Valor inválido")
