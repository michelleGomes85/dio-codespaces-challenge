word = input('Digite uma palavra: ')

word = word.replace(' ', '').lower()

reversed_word = word[::-1]

if word == reversed_word:
    print('A palavra é um palíndromo.')
else:
    print('A palavra não é um palíndromo.')
