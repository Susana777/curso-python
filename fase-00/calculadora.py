
def calculadora():
    '''Pide al usuario dos numeros, la operacion a realizar y la ejecuta'''
    
    while True:
        try:
            num1 = float(input("Ingresa el primer numero: "))
            operador = input("Ingresa el operador +, -, *, / :")
            num2 = float(input("Ingresa el segundo numero: "))
            
            if operador == "+":
                resultado = num1 + num2
            elif operador == "-":
                resultado = num1 - num2
            elif operador == "*":
                resultado = num1 * num2
            elif operador == "/":
                if num2 == 0:
                    print("No se puede dividir entre cero")
                else:
                    resultado = num1 / num2
            else:
                print("Operador invalido")
                
            print(f"El resultado es: {resultado}")
                
            continuar = input("Quieres hacer otra operacion? (s/n): ")
            if continuar.lower() != "s":
                break
        except ValueError:
            print("Ingresa solo numeros")

calculadora()

