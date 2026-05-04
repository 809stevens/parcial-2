print("="*70)
print("\n  bienvenido ")
print("="*70)

def validar_nombre():
    while True:
        nombre = input("ingresa tu nombre: ")
        if len(nombre) >= 3:
            return nombre
        else:
            print("tu nombre debe tener al menos tres caracteres")

def validar_tel():
    while True:
        tel = input("ingresa tu telefono (8 o 9 digitos): ")
        if not tel.isdigit():
            print("¡ERROR!, debes ingresar solo numeros")
        elif len(tel) == 8 or len(tel) == 9:
            return tel
        else:
            print("el telefono debe tener 8 o 9 digitos")

def validar_num_posi(mensaje):
    while True:
        valor = float(input(mensaje))
        if valor <= 0:
            print("\n el valor tiene que ser mayor a cero")
        else:
            return valor

def validar_cajas_cantidad():
    while True:
        cantidad = int(input("ingresa la cantidad de cajas: "))
        if cantidad <= 0:
            print("\n la cantidad tiene que ser mayor a cero")
        else:
            return cantidad

def camiones_nes(volumen_camiones):
    capacidad = 29.0
    camiones = int(volumen_camiones / capacidad)
    if volumen_camiones % capacidad > 0:
        camiones += 1
    return camiones

while True:
    nombre = validar_nombre()
    telefono = validar_tel()

    print("\n === COTIZACION ===")
    print("\n dimensiones de la caja (en centimetros)")
    largo = validar_num_posi("largo de la caja: ")
    ancho = validar_num_posi("ancho de la caja: ")
    alto = validar_num_posi("alto de la caja: ")

    cajas_cantidad = validar_cajas_cantidad()

    volumen_cm3 = largo * ancho * alto
    volumen_cm3 = volumen_cm3 / 1000000
    volumen_total_cm3 = volumen_cm3 * cajas_cantidad

    camiones = camiones_nes(volumen_total_cm3)

    precio_por_camion = 150000
    valor_total = camiones * precio_por_camion

    print("="*60)
    print("RESULTADO")
    print("="*60)
    print(f"Cliente             : {nombre}")
    print(f"Teléfono            : {telefono}")
    print(f"Cantidad de cajas   : {int(cajas_cantidad)}")
    print(f"Camiones necesarios : {camiones}")
    print(f"Valor total         : ${valor_total:,.0f}")
    print("="*60)

    respuesta = input("\ndesea realizar otra cotizacion? (si/no): ").lower()
    if respuesta == "si":
        print("\nreiniciando...")
    else:
        print("\ngracias por usar nuestro servicio")
        break





    