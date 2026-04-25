# cajero automatico.
# estimado estudiate usted ha sido seleccionado para realizar el interfaz de usuario de los cajeros automatico del grupo santander.
# el programado debe solicitar al usuario numero de rut el cual debe ser validado con su codigo de verificacion
# posteriormente a esto el usuario debe ingresar su clave que no debe ser menor o mayor a diez digitos


print("\n ¡Bienvenido al cajero automatico de santander!")

def verificar_rut (rut, digito):
    suma = 0 
    sec = 2
    for numero in reversed(str(rut)):
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






while True:
    rut = input("ingresa tu rut y numero verificador (sin el guion): ")

    if len (rut) < 8: 
        print(f"rut invalido, ingresate muy pocos caracteres: {rut} ")
    elif len (rut) > 9:
        print(f"rut invalido, ingrsate demasiados caracteres: {rut}")
        break

numero = rut [:-1]
digito = rut [-1].lower()

if not numero.isdigit():
    print(f"rut ivalido, hay una letra entre medio de los numeros {numero}")
else:
    if verificar_rut(numero, digito):
        print("rut valido")
        print("digito verificador correcto")
    else:
        print("digito verificador incorrecto")
        



while True:
    clave = input("ingresa tu clave (no debe ser menor o mayor que diez): ")

    if len (clave) > 10:
        print(f"clave incorrecto, ingresaste {len (clave)} numeros pero deben minnimo diez ")
    elif len (clave) < 10:
        print(f"clave incorrecto, ingresaste {len (clave)} numeros pero deben ser maximo diez ")
    else:
        print("clave correcto")
        break








