class Error(Exception):
    pass
class inputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        nota = int(input('Entre com uma nota de 0 a 10: '))
        print(nota)
        if nota > 10:
            raise inputError('Valor maior que 10!')
        elif nota < 0:
            raise inputError('Nota não pode ser menor que 0!')

        break #Caso o comando anterior esteja correto caira aqui, e o programa sera parado, caso contrario entrara em looping
    except ValueError:
        print('Valor invalido, entre com um numero.')
    except inputError as ex:
        print(ex)