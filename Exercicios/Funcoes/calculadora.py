def calc(x, y, op):
    if op == "+":
        return x + y
    if op == "-":
        return x - y
    if op == "x":
        return x * y
    if op == "/":
        return x / y
    if op == "%":
        return x % y
    
    return 'Operação informada inválida.'
    
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

op = input(f"Digite a operação para fazer entre {n1} e {n2} ('+' para soma; '-' para subtração; 'x' para multiplicação, '/' para divisão; '%' para resto): ")
result = calc(n1, n2, op)

print(f'O resultado de {n1} {op} {n2} é {result}')
