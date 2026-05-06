print("="*70)
print("\n !BIENVENIDO¡ al sistema de adivinzazas")
print("="*70)



import random

while True:
    try:
        n1 = int(input("ingresa un numero: "))
        n2 = int(input("ingresa tu segundo numero (debe ser mayor a tu primer numero): "))
        if n1>n2:
            print("el numero dos debe ser mayor al primero")
        else:
            break
    except ValueError:
        print("ingresa algo valido")

numero = random.randint (n1,n2)

numero 

intento = 0


while intento < 3:
    adivinar = int(input("intenta adivar el numero: "))
    if numero == adivinar:
        print("="*60)
        print(f"bien hecho adivinate el numero {numero}")
        print("="*60)
        break   
    else:
        print("numero incorrecto, intentalo de nuevo")
        intento +=1

if intento == 3:
    print(f"lo siento no adivinaste el numero era {numero}")


if numero < n1 or numero > n2:
    print(f"numero fuera de rango se dividira por{n1}")
    numero = numero / n1
    print(f"nuevo numero {numero}")
