conjunto = {1, 2, 3, 4, 4, 5, 5, 6, 6}
conjunto2 = {7, 8, 9, 10, 1, 2}
uniaoConjunto = conjunto.union(conjunto2)
conjuntoInterseccao = conjunto.intersection(conjunto2)
conjuntoDiferenca = conjunto.difference(conjunto2)
conjuntoDiferenca2 = conjunto2.difference(conjunto)
diferencaSimetrica = conjunto.symmetric_difference(conjunto2)


print('União dos conjuntos {}'.format(uniaoConjunto))
print('Intersecção dos conjuntos {}'.format(conjuntoInterseccao))
print('Diferença entre 1 e 2 {}'.format(conjuntoDiferenca))
print('Diferença entre 2 e 1 {}'.format(conjuntoDiferenca2))
print('Diferença simetrica {}'.format(diferencaSimetrica))

conjuntoA = {1, 2, 3}
conjuntoB = {1, 2, 3, 4, 5}
conjunto_subset = conjuntoA.issubset(conjuntoB)
conjunto_subsetA = conjunto.issubset(conjuntoA)


print('O conjunto A é um Subconjunto do conjunto B?{}'.format(conjunto_subset))
print('O conjunto B é um Subconjunto do conjunto A?{}'.format(conjunto_subsetA))

#O conjunto não pode conter mais de um elemento igual


lista = ['cachorro', 'gato', 'cachorro', 'elefante'] 
conjuntoAnimais = set(lista) #Transformando lista em conjunto
print(conjuntoAnimais)


 
