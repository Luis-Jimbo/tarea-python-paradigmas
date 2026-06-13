# Carpeta: programacion_poo | Archivo: main.py
from mascota import Mascota

if __name__ == "__main__":
    print("--- Gestión de Mascotas (Enfoque POO) ---\n")

    # Creación de dos objetos distintos
    mascota_1 = Mascota("Thor", "Perro", 4)
    mascota_2 = Mascota("Clara", "Gato", 2)

    print("Ejecutando Métodos para Mascota 1:")
    mascota_1.mostrar_informacion()
    mascota_1.hacer_sonido()
    print("-" * 40)

    print("Ejecutando Métodos para Mascota 2:")
    mascota_2.mostrar_informacion()
    mascota_2.hacer_sonido()