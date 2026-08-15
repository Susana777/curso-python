import random

def adivinar_numero ():
    
    numero_aleatorio = random.randint(1,100)
    numero_temporal = 0
    
    print("Para adivinar el numero tienes que ingresar primero un numero al azar para recibir las pistas (solo enteros)")
    
    while numero_temporal != numero_aleatorio:
        
        numero_temporal = int(input("Ingresa tu intento: "))
        
        if numero_temporal > numero_aleatorio:
            print("Ingresa un numero menor")
        elif numero_temporal < numero_aleatorio:
            print("Ingresa un numero mayor")
            
    print("Felicidades, atinaste el numero")
    
adivinar_numero()