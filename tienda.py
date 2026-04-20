print("\nbienvenido al sistema de descuentos de la tienda")

name = input("ingresa tu nombre: ")

age = int(input("Ingresa tu edad: "))

partner = input("¿tienes tarjeta de socio? (si/no): ")

price = float(input("ingresa el precio del producto:"))

#reglas de descuento
if age >= 60 and partner.lower() == "si":
    discount = 0.30
    print("eres mayor de edad y socio de la tienda, tienes un descuento del 30%")
    
elif age < 18:
    discount = 0.10
    print("eres menor de edad, tienes un descuento del 10%")

elif age >= 60:
    discount = 0.15
    print("eres mayor de edad, tienes un descuento del 15%")

elif partner.lower() == "si":
    discount = 0.20
    print("eres socio de la tienda, tienes un descuento del 20%")

else:
    discount = 0.0
    print("no cumples los requisitos para obtener un descuento")

#calculo
price_after_discount = price *  (1 - discount)

print(f"precio original: {price:.3f}")
print(f"descuento aplicado: {discount}%")
print(f"precio final: {price_after_discount:.3f}")


