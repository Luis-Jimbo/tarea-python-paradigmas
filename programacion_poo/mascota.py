# Carpeta: programacion_poo | Archivo: mascota.py

class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Mascota: {self.nombre} | Especie: {self.especie} | Edad: {self.edad} años")

    def hacer_sonido(self):
        esp = self.especie.lower()
        if "perro" in esp:
            print(f"{self.nombre} dice: ¡Guau guau!")
        elif "gato" in esp:
            print(f"{self.nombre} dice: ¡Miau miau!")
        else:
            print(f"{self.nombre} hace un sonido de su especie.")