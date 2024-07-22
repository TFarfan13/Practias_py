print("Calculadora ")
def calcular():
    print("Introduzca 2 números, luego seleccione la operación.")
    
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Por favor, ingrese números válidos.")
        return

    ope = input("Ingrese la operación a realizar con los signos (+) suma, (-) resta, (*) multiplicación, (/) división: ")

    if ope == "+":
        result = num1 + num2
        print(f"Resultado de la suma: {result}")
    elif ope == "-":
        result = num1 - num2
        print(f"Resultado de la resta: {result}")
    elif ope == "*":
        result = num1 * num2
        print(f"Resultado de la multiplicación: {result}")
    elif ope == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"Resultado de la división: {result}")
        else:
            print("No se puede dividir por cero.")
    else:
        print("Operación no válida. Inténtelo de nuevo.")   
        
while True:
    calcular()
    continuar = input("¿Desea realizar otro cálculo? (s/n): ")
    try:
        if continuar.lower() == 'n':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        elif continuar.lower()=="s":
            calcular()
            
        else:
            raise ValueError("Ingrese una opcion valida")  
    except ValueError as error:
        print(error)   
        


