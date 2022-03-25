def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
if __name__=="__main__":
    x = int(input("Enter num1"))
    y = int(input("Enter num2"))
    addition = add(x,y)
    subtraction = sub(x,y)
    multiplication = mul(x,y)
    division = div(x,y)
    print(addition)
    print(subtraction)
    print(multiplication)
    print(division)