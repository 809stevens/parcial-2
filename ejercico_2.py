print("\n === Renta de maquinaria ===")


nombre = input("ingresa tu nombre: ")
if len(nombre) < 3:
        print("ingresa un nombre valido")

while len(nombre) < 3:
   nombre = input("Ingresa tu nombre: ")
   if len(nombre) >= 3:
         break
    
while True:
    try:
        telefono = input("ingesa tu numero: ")
        if len(telefono) == 8 or len(telefono) == 9:
                break
        else:
            print("error el numero debe ser entre 8 u 9")
    except ValueError:
         print("ingresa un numero valido")
         continue
       



print("Seleccion de maquinaria (los precios son por hora)")

print ("1) excavadora ($200000)") 
print ("2) grua ($250000) ")
print ("3) mezcaldora (150000)")

seleccion = input("ingresa uno tu seleccion: ")


if seleccion == "1":
     precio = 200000
     horas = int(input("por cuantas horas lo utilzaste"))

elif seleccion == "2":
      precio = 250000
      horas = int(input("por cuantas horas lo utilzaste"))

elif seleccion =="3":
      precio = 150000
      horas = int(input("por cuantas horas lo utilzaste"))
else:
     print("¡Error!, el numero que seleccionaste no esta en nuestra lista")

monto = precio * horas


print("\n === compra realizada === ")

print(f"nombre: {nombre}")
print(f"telefono {telefono}")
print(f"horas utilizada {horas}")
print(f"equipo seleccionada {seleccion}")
print(f"monto a pagar {monto}")

     
    

