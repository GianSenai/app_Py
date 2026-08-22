def calcular(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b

    return soma, subtracao, multiplicacao, divisao

resultado = calcular(10, 2)

print("Soma:", resultado[0])
print("Subtração:", resultado[1])
print("Multiplicação:", resultado[2])
print("Divisão:", resultado[3])