import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num_1 = 1
num_2 = 2
soma_int = num_1 + num_2
print("1) A soma é: ", soma_int)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num = 12
resto_div = num % 5
print("2) O resto da divisão por 5 é:", resto_div)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
num_1 = 3
num_2 = 4
multiplicacao = num_1 * num_2
print("3) O resultado da multiplicação é: ", multiplicacao)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
num_1 = 20  # Exemplo de entrada -> int(input("Digite o primeiro número inteiro: "))
num_2 = 3  # Exemplo de entrada -> int(input("Digite o segundo número inteiro: "))
resultado_divisao_inteira = num_1 // num_2
print("4) O resultado da divisão inteira é:", resultado_divisao_inteira)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
num = 5
quadrado = num**2
print("5) O quadrado do número é: ", quadrado)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
num_1 = 2.5  # Exemplo de entrada -> float(input("Digite o primeiro número flutuante: "))
num_2 = 4.5  # Exemplo de entrada -> float(input("Digite o segundo número flutuante: "))
soma_float = num_1 + num_2
print("6) A soma é:", soma_float)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num_1 = 4
num_2 = 6
media = (num_1 + num_2) / 2
print("7) A média é: ", media)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = 2.0 # Exemplo de entrada -> float(input("Digite a base: "))
expoente = 3.0 # Exemplo de entrada -> float(input("Digite o expoente: "))
potencia = base ** expoente
print("8) A potência é: ", potencia)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = 30.0
fahrenheit = (celsius * 9/5) + 32
print(f'9) {celsius}°C equivale à {fahrenheit}°F.')

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = 5.0 # Exemplo de entrada -> float(input("Digite o raio: "))
area = math.pi * raio ** 2
print(f'10) A área do círculo é: {area:.2f}')

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
texto = "Olá, mundo!" # Exemplo de entrada -> input("Digite um texto: ")
texto_maiusculo = texto.upper()
print("11) Texto em maiúscula: ", texto_maiusculo)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = "Leonardo Mafra Salin" # Exemplo de entrada -> input("Digite seu nome completo: ")
nome_minusculo = nome.lower()
print("12) Nome em minúsculo: ", nome_minusculo)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = "  Olá, mundo!  a" # Exemplo de entrada -> input("Digite uma frase: ")
frase_sem_espacos = frase.strip()
print("13) Frase sem espaços no início e no final:", frase_sem_espacos)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = "18/01/2001" # Exemplo de entrada -> input("Digite uma data no formato dd/mm/aaaa: ")
dia_mes_ano = data.split("/")
print(f'14) Dia: {dia_mes_ano[0]}, mês: {dia_mes_ano[1]}, ano: {dia_mes_ano[2]}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
texto1 = "Ara"
texto2 = "ra"
texto_concatenado = texto1 + texto2
print("15) Texto concatenado: ", texto_concatenado)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
valorA = True
valorB = False
tabela_verdade_and = valorA and valorB
print("16) True AND False: ", tabela_verdade_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
tabela_verdade_or = valorA or valorB
print("17) True OR False: ", tabela_verdade_or)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
tabela_verdade_not = not valorA
print("18) NOT True:", tabela_verdade_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num_1 = 2
num_2 = 2
igualdade = (num_1 == num_2)
print(f"19) Os números {num_1} e {num_2} são iguais? {igualdade}")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
diferenca = (num_1 != num_2)
print(f"20) Os números {num_1} e {num_2} são diferentes? {diferenca}")

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação