def div():
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        res = num1 / num2
    except ZeroDivisionError:
        print('Ooops! Erro de divisão por zero...')
    except:
        print('Algo de errado aconteceu...')
    else:
        return res
    finally:
        print('Executará sempre!')

#Programa principal
div()