#acaban de tener y les solicita realizar un programa en python que entrege a los clientes y para ello comezamos slicitando a los usuarios su numero de rut el cual debe validar los 8 digitos del mismo en una casilla validar codigo de verificacion
#posteriormente deben preguntar el nombre del cliente el monto de la compra para saber si tiene el descuento
#toda compra menor a diez mil peso no obtiene descuento, toda compra mayor a 10 diez mil peso hasta 50 mil peso obtines 10% de descunto
# toda compra mayor a 50 mil peso obtiene 20% de descunto
#que deberia calcular mi programa monto de descuento, total a pagar y deberia mostrar en la pantalla nombre, rut y monta de la compra descuento aplicado y total a pagar

print("\n === Bienvenido al sistema de descuento === ")

def verificar_rut(rut,digito):
    suma = 0
    sec = 2

    for numero in reversed (str(rut)):
        suma += int(numero) * sec
        sec += 1
        if sec > 7:
            sec = 2

    resto = 11 - (suma % 11) 

    if resto == 11:
        calculando = "0"
    elif resto == 10:
        calculando = "k"
    else:
        calculando = str(resto)

    return calculando == digito.lower()


nombre = input("Ingresa tu nombre: ")

while True:
    rut = input("Ingresa tu rut sin codigo verificador: ")
    digito = input("Ingresa el codigo verificador: ")

    if len(rut) < 7 or len (rut) > 8:
        print(f"rut invalido, ingresate muy pocos o demasiados caracteres {len(rut)} ")
    if not rut.isdigit():
        print(f"rut invalido, ingresaste una letra en medio del rut ")
    elif verificar_rut(rut,digito):
            print("rut valido")
            break
    else:
        print("digito verificador incorrecto")
        

#cálculos  

monto = float(input("Ingresa el monto de tu compra: "))

if monto < 10000:
    descuento = 0.00
    print("no tienes descuento")
elif monto <= 50000:
    descuento = 0.10
    print("tienes un descuento de 10%")
elif monto > 50000:
    descuento = 0.20
    print("obtines un descuento de 20%")

    monto_des = monto -  monto * descuento



#Resulatado

print("\n === Resultado de tu descuento ===")
print(f"nombre: {nombre}")
print(f"rut: {rut}-{digito}")
print(f"monto original: {monto}")
print(f"descuento aplicado: {descuento}%")
print(f"monto final con descuento {monto_des:.0f}")

