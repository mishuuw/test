def test() :
    print("Hello, World!")
    
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def MULTIPLY(a, b):
    return a * b
def power(base, exponent):
    return base ** exponent

def root(value, n):
    return value ** (1/n)

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def modulus(a, b):
    return a % b

def floor_divide(a, b):
    return a // b