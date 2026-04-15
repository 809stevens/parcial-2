usuario = input("ingresa tu nombre: ")
contraseña = int (input("ingresa tu contraseña: "))

print (f"{usuario} usted ha sido registrado correcatamente")

i = 1
while i == 1:

    usuuario = input ("ingresa tu nombre de usuario: ")
    if usuario == usuuario:
        print("nombre de usrario correcto")
        i = 2
    else:
        print("nombre de usuario incorrecto")
  
while i == 2:
    contraseñaa = int (input("ingreasa tu contraseña de usuario"))
    if contraseña == contraseñaa:
        print("contaseña correcta")
        i = 3
    else:
     print("contraseña incorrecta")
    
 