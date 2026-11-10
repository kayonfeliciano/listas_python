# OPERADORES
# / ---- Divisão completa
# % --- Módulo - Resto da divisão
# ** --- potencia
# **(v1/v2) --- raiz

# Aplicando divisão de "resto"
n1 = int(input("Informe o primeiro número"))
n2 = int(input("Informe o segundo número"))

resto = n1%n2
print(resto)

# Usando o operador de potencia
print("Vamos aplicar a potencia")
base = int(input("Me informe a base"))
pot = int(input("Me informe o valor da potencia"))

potencia = base ** pot
print(potencia)

# Calculando raiz

print("Vamos aplicar uma raiz")
ind = int(input("Informe o indice"))
numero = int(input("Qual o numero vc quer a raiz"))

raiz = numero ** (1/ind)
print(raiz)