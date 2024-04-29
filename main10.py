i = 0
while True:
    try:
        nome = input('Por favor digite o seu nome: ')
        ind = int(input('Digite um índice do seu nome digitado: '))
        print(nome[ind])
        break
    except ValueError:
        print('Ooops! nome inválido. Tente novamente...')
    except IndexError:
        print('Ooops! índice inválido. Tente novamente...')
print('Encerrando programa.')