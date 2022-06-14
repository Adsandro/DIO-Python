from classTelevisao import televisao
from contadorLetras import contadorLetras

televisao = televisao()
print(televisao.ligada)
televisao.power() # Liga a Televisao
print(televisao.ligada)

lista = ['elefante', 'minhoca', 'garanhoto']
print(contadorLetras(lista))