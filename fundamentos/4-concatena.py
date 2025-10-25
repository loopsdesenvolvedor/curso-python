# Concatenação de valor.

name = input('Digite o nome de filme:\n')
yearLaunch = int(input('Digite o ano de lançamento: \n'))
noteMovie = float(input('Digite a nota do filme: \n'))

# Primeira forma de juntar (virgula).
print('Filme ', name,'lançado em ', yearLaunch,'nota ', noteMovie)
print('===========================================================')

# Segunda forma de juntar (f"" string).
print(f'Nome do filme {name}, lançamento {yearLaunch} com nota: {noteMovie}')