
def calc():
    op = input("Выберите операцию (+, -, *, /): ")
    a, b = float(input("Первое число: ")), float(input("Второе число: "))

    if (op == '+'): res = a + b
    elif (op == '-'): res = a - b
    elif (op == '*'): res = a * b
    elif (op == '/'): res = a / b
    
    return res

result = calc()
print(f"Результат операции: {result}")
