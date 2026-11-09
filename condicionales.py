animales = [ "Perro","Gato","Loro","Burro"]
contador = 1
for animal in animales:
    print("Animal",contador," ",animal)
    contador += 1

respuesta = ""
while respuesta != "salir":
    respuesta = input("Escriba algo o 'salir' para terminar: ")
    print("Ingresaste: ",respuesta)