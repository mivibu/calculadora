

def sumar (num1, num2):
    return num1 + num2
def restar (num1, num2):
    return num1 - num2
def multiplicar (num1, num2):
    return num1 * num2
def dividir (num1, num2):
    return num1 / num2
#para que el usuario pueda ingresar los números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
#para que el usuario pueda ingresar la operación a realizar
operacion = input("Ingrese la operación a realizar (+, -, *, /): ")
#para que el usuario pueda ingresar la operación a realizar
if operacion == "+":
    print("El resultado es:", sumar(num1, num2))
elif operacion == "-":
    print("El resultado es:", restar(num1, num2))
elif operacion == "*":
    print("El resultado es:", multiplicar(num1, num2))
elif operacion == "/":
    print("El resultado es:", dividir(num1, num2))
else:
    print("Operación no válida")

    print("El resultado es:", dividir(num1, num2))



    print(dividir)