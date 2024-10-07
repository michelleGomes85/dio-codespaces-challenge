# Código simples aprendendo o uso de dicionario
def contar_caracteres(string):
    
    contador = {}
    
    # Itera através de cada caractere na string
    for char in string:
        # Verifica se o caractere já está presente no dicionário contador
        if char in contador:
            # Se o caractere já estiver presente, incrementa o valor associado a essa chave
            contador[char] += 1
        else:
            # Caso contrário, adiciona o caractere ao dicionário com valor inicial 1
            contador[char] = 1
    
    return contador

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)
