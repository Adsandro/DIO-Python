
import email
from inspect import Attribute

lista = [1, 2, 3, 4]
arquivo = open('C:\Workspace\DIO-Python\Estudos\Manipulação de arquivos\Manipulacao2.txt', 'r')
try:
    texto = arquivo.read()
    calculo = 10/2
    numero = lista[4]
    arquivo.close()

except ZeroDivisionError :
    print('Erro de calculo')
except IndexError:
    print("Erro de index")
else:
    print("Nenhum erro encontrado!!")
finally: #Dando erro ou não, sera executado
    print('Sempre executa ')
    print('Fechando arquivo')
    arquivo.close()
    

# Conceito utilizado do python
# https://docs.python.org/3/library/exceptions.html#:~:text=Exception%20hierarchy%C2%B6