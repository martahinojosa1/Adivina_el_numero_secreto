# PASOS:
# Importar numpy
# Generar número secreto
# Bucle while con 10 intentos y todos los prints según el intento

import numpy as np

def play():
    # Generar número aleatorio a adivinar entre 0 y 100
    numero_secreto = np.random.randint(1,101)
    numero_secreto

    # Bucle while con 10 intentos para el usuario
    intentos = 10
    while intentos > 0:
        intento = input("Adivina un número entero entre 0 y 100, ¡tienes 10 intentos!\n")
        
        if intento.lower() == 'exit':
            break
        
        if intento == '':
            continue
        
        if not intento.isdigit():
            print("Error. Ingresa un número entero entre 0 y 100.")
            continue
        
        intento_int = int(intento)
        if intento_int == numero_secreto:
            print("¡Lo has adivinado! El número secreto es", numero_secreto)
            break   
        else:
            intentos -= 1  # Se resta un intento
            if intentos > 0:  # Mientras los intentos sigan siendo > 0 se continúa. Cuando intentos = 0, se para.
                print("¡Error, sigue intentándolo! Te quedan {} intentos.".format(intentos))
                if intento_int > numero_secreto:
                    print("Pista: el número es menor que ", intento_int)
                elif intento_int < numero_secreto:
                    print("Pista: El número es mayor que ",intento_int)
                else:
                    continue
            else:
                print("¡Fin del juego, has agotado todos los intentos. El número era el ", numero_secreto)
                
                
if __name__ == "__main__":
    play()