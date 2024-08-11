"""
    Verifica se um ano é bissexto.
"""
def is_year_leap(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
"""
    Retorna o número de dias em um mês específico de um ano.
"""
def days_in_month(year, month):
    
    # Verificar se o mês está dentro do intervalo válido
    if month < 1 or month > 12:
        return None
    
    # Lista com o número de dias em cada mês
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Ajustar o número de dias para fevereiro em caso de ano bissexto
    if month == 2 and is_year_leap(year):
        return 29
    
    # Retornar o número de dias do mês especificado
    return days_in_months[month - 1]


# Dados de teste
test_years = [1900, 2000, 2016, 1987, 2024, 2100, 2020, 2019]
test_months = [2, 2, 1, 11, 2, 2, 2, 2]
test_results = [28, 29, 31, 30, 29, 28, 29, 28]

# Teste da função
for i in range(len(test_years)):
    
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")