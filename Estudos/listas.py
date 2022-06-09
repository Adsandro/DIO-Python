lista_animais = ["cachorro", "Gato", "Jacaré"]

animal = str(input("informe um animal: "))
if animal in lista_animais:
    print("Está aqui")
    lista_animais.remove(animal)
else:
    print("Não está aqui, estarei adicionando a lista")
    lista_animais.append(animal)
    
print(lista_animais)