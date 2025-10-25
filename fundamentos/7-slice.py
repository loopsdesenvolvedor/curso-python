# Oprações e métodos de string.

movieName = 'Top Gun'

# string[inicio:fim] -  indice começa na posição 0 | indice final -1

# Buscando toda a string a partir da primeira posição.
print(movieName[0:3]) # Da primeira a 3 posição.
print(movieName[:-1]) # Recuperando a string menos a ultima posição.

# Buscar toda a string da terceira até a ultima posição.
print(movieName[2:])

# string[inicio:fim:passo] - passo determina o inclemento. Por padrão esse número 1.

# Buscar toda a string de 2 em e caracteres.
print(movieName[::2]) # Retonro TpGn.

# Buscar toda a string nos indices impares.
print(movieName[1::2])

# Inverter a string.
print(movieName[::-1]) # Retorno nuG poT

