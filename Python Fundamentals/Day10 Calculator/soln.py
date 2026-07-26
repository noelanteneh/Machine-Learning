from  art import logo
print(logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiplication(n1, n2):
    return n1 * n2
def division(n1, n2):
    if n2==0:
        print("Division by zero not possible")
    else:
        return round(n1 / n2,3)
def exponent(n1, n2):
    return n1 ** n2
number1=int(input("Enter the first number: "))
operator=input("Enter the operator:(+,-,*,/,^) ")
number2=int(input("Enter the second number: "))
result=0
if operator=="+":
    result=add(number1,number2)
elif operator=="-":
    result=subtract(number1,number2)
elif operator=="*":
    result=multiplication(number1,number2)
elif operator=="/":
    result=division(number1,number2)
elif operator=="^":
    result=exponent(number1,number2)
else:
    print("Operator not supported")
print(result)