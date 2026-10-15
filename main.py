

def sumar (num1, num2):
    return num1 + num2
def restar (num1, num2):
    return num1 - num2
def multiplicar (num1, num2):
    return num1 * num2
def dividir (num1, num2):
    return num1 / num2
#para que el usuario pueda ingresar los números
try:
    # Capturamos la conversión a float por si ingresan texto en vez de números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    # Capturamos la conversión a float por si ingresan texto en vez de números
 
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

except ValueError:
        print(" Error: Debes ingresar un número válido (no letras ni caracteres especiales).")
        
except ZeroDivisionError:
        print(" Error: No se puede dividir por cero.")



