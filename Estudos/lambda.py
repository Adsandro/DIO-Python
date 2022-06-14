contadorLetras = lambda lista: [len(x) for x in lista]
# Lambda é eficiente para resolver problemas simples em uma unica linha (funçoes anonimas, ou seja, não possui um nome, pode estar dentro de uma variavel)

listaAnimais = ['cachorro', 'gato', 'elefante']
print(contadorLetras(listaAnimais))

# EX: 2
soma = lambda a, b: a + b
print(soma(2, 3))

# EX: 3
subtracao = lambda a, b: a - b
print(subtracao(10, 4))

