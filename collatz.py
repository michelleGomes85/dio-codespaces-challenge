"""
    Aplica a sequência de Collatz ao número fornecido e conta o número de passos até que o número se torne 1.

    Parâmetros:
    numero (int): O número inicial para aplicar a sequência de Collatz. Deve ser maior que 0.

    Retorna:
    int: O número total de passos necessários para chegar a 1.
"""
def colllatz_passos(numero):
    
    passos = 0

    while numero != 1:
        
        if numero % 2 == 0:
            numero /= 2
        else:
            numero = 3 * numero + 1

        print(round(numero))

        passos += 1

    return passos


"""
    Função principal para interagir com o usuário e aplicar a sequência de Collatz.
"""
def main():

    while True:
        try:
            numero = int(input("Número maior que 0: "))
            if numero <= 0:
                print("O número deve ser maior que 0. Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

    passos = colllatz_passos(numero)
    print(f"Passos = {passos}")


if __name__ == "__main__":
    main()
