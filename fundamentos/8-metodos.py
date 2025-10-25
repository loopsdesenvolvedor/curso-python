# Métodos de string.

movieName = 'Top Gun, n'
movieDescription = ''' 
   Top Gun Maverick é um filme de aviação e aventura 
   muito consagrado na industria.
'''

# Uppercase.
print(movieName.upper())
# Lowercase.
print(movieDescription.lower())
# Capitalize.
print(movieName.capitalize())
# Title. (parecido com capitalize mas deixa em maiusculo a primeira letra de cada palavra)
print(movieName.title())
# Center. (Preenche os lados da string com o caractere indicado)
print(movieName.center(20, '-'))
# Find. (busca uma letra na string)
print(movieName.find("u")) # Retorna o indice do caractere.
# Replace substituindo palavras.
print(movieName.replace('Top', "Matrix"))
# Split. (divide a string em substring, separado pela virgula, por exemplo)
print(movieName.split(','))
