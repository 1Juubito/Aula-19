def borda(s1):
    tam = len(s1)
    #só imprime caso tenha algum caractere
    if tam:
        print('+','-' * tam,'+')
        print('|',s1,'|')
        print('+','-' * tam,'+')

#Programa Principal
borda('Bem vindo')