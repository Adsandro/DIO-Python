def contadorLetras (lista_palavra):
    contador = []
    for x in lista_palavra:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

if __name__ == '__main__':
    lista = ['cachorro', 'gato', 'jacaré']
    print(contadorLetras(lista))