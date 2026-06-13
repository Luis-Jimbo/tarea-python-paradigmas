# Carpeta: programacion_tradicional | Archivo: tradicional.py

def registrar_mascota():
    print("--- Registro de Mascota (Enfoque Tradicional) ---")
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie (ej. Perro, Gato): ")
    edad = int(input("Ingrese la edad de la mascota: "))
    return nombre, especie, edad

def mostrar_mascota(nombre, especie, edad):
    print("\n========================================")
    print("      INFORMACIÓN DE LA MASCOTA         ")
    print("========================================")
    print(f"Nombre:  {nombre}")
    print(f"Especie: {especie}")
    print(f"Edad:    {edad} años")
    print("========================================\n")

if __name__ == "__main__":
    nom, esp, ed = registrar_mascota()
    mostrar_mascota(nom, esp, ed)