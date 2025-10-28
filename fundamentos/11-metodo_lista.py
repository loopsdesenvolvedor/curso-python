filmeList = ['Inception', 'The Shawshank Redemption',
             'The Dark Kgninth', 'Pulp Fiction', 'Interestellar'
             ]


# Vreficando o tamanho da lista. len(array)
print(len(filmeList))

# Recuperando um item da lista pelo seu índice. array.index() => indice.
print(filmeList.index('Interestellar'))

# Adicionando item ao final da lista.
filmeList.append('The Lord of the Rings')
print(filmeList)

# Ordenando a lista.
filmeList.sort()
print(filmeList)

# Copiando os items de uma lista para outra,
filmeCopy = filmeList.copy()
filmeCopy.remove('Pulp Fiction') # Removendo item da lista remove('string').
print(filmeCopy)

# Removendo todos os items da lista.
filmeList.clear()
print(filmeList)