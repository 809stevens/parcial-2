print("\n === binevenido al tiende de retail ===")

nombre = str(input("Ingresa tu nombre: "))

monto = int(input("Ingresa el monto de tu compra: "))

if monto <= 0:
    print("ingresa un monto valido")


if monto < 10000:
    descuento = 0
    porcentaje = "0%"
elif monto <= 50000:
    descuento = monto - monto * 0.10
    porcentaje = "10%"
else:
    descuento = monto - monto * 0.20
    porcentaje = "20%"


#resultados

print("\n === Resultado de tu compra ===")

print(f"nombre: {nombre}")
print(f"monto inicial de tu compra: {monto}")
print(f"monto con descuento: {descuento}")
print(f"porecentaje de descuento: {porcentaje}")


