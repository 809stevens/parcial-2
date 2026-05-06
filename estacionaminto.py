print("="*80)
print("calcular el valor de estacionamiento")
print("="*80)

nombre = input("Ingresa tu nombre: ")


print("el precio base para guardar tu motocicleta es de 15 mil peso")
print("el precio base del candado ed e 9 mil peso")

base_moto = 15000
base_candado = 9000


dias = int(input("cuantas dias lo utilizaste:"))
estudiante = input("eres estudiante (si/no): ").lower()

if dias > 20 and estudiante == "si":
    print("obtienes un descuento de 25%")
    descuento = 0.25
    porcentaje = 25
elif dias > 20 and estudiante == "no":
    print("obtienes un descuento de 15%")
    descuento = 0.15
    porcentaje = 15
elif dias >= 10 and dias <= 20 and estudiante == "si":
    print("obtienes un descuento de 15%")
    descuento = 0.15
    porcentaje = 15
elif dias  >= 10 and dias <= 20 and estudiante == "no":
    print("obtienes un descuento de 8%")
    descuento = 0.08
    porcentaje = 8


debito_descuento = 0
debito_porcentaje = 0


if estudiante == "si":
    debito = input("vas a pagar con tarjeta de debito (si/no): ").lower()
    if debito == "si":
        print("obtines 12% mas de descuento")
        debito_descuento = 0.12
        debito_porcentaje = 12
    elif debito == "no":
        print("usted no tiene obtines mas descuento")
        debito_descuento = 0.0
        debito_porcentaje = 0



otro_desc = 0
otro_por = 0



if dias < 10:
    print("obtienes 0% mas de descuento por ser menor a 10 dias")
    otro_desc = 0.0
    otro_por = 5
elif dias < 15:
    print("obtienes 5% mas de descuento por ser menor a 15 dias")
    otro_desc = 0.05
    otro_por = 0



#calcular

precio_base = base_moto + base_candado
descuento_total = descuento + debito_descuento + otro_desc
final_monto = precio_base - (precio_base * descuento_total)
porcentaje_total = porcentaje + debito_porcentaje + otro_por


print("="*60)
print("\n RESULTADO ")
print(f"nombre                                              : {nombre}")
print(f"monto original del motocicleta                      : ${base_moto}")
print(f"monto original del candado                          : ${base_candado}")
print(f"la suma de los precio base del candado y la moto    : ${precio_base}")
print(f"descuento aplicado al candado                       : {porcentaje_total}%")
print(f"monto final                                         : ${final_monto:,.0f}")
print("="*60)