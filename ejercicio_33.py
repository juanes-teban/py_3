def factorial(n):
    num = 1
    for i in range(n):
        num *= i + 1
    return num



print(factorial(5))
