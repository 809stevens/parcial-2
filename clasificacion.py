print("\n=== bienvenido al sistema de clasificación de películas ===")

def clasificar(titulo , puntaje):
        if puntaje >= 9:
            categoria = "obra maestra"
        elif puntaje >= 7:
            categoria = "buena"
        elif puntaje >= 5:
            categoria = "regular"
        else:
            categoria = "mala" 

        return titulo, categoria 

while True:
   

    titulo = input("ingresa el nombre de la pelicula: ")

    puntaje = float(input("ingresa el puntaje de la pelicula (0-10): "))



    titulo, categoria = clasificar (titulo, puntaje)
    print(f"pelicula: {titulo}")
    print(f"categoria: {categoria}")

    repetir = input("\n deseas repetir otra vez (si/no): ").lower()
    if repetir != "si":
        print("hasta luego!")
        print("cerrando sistema.....")
        break