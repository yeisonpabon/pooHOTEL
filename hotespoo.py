
# Clase Habitacion 
class Habitacion: 
    def __init__(self, numero, tipo): 
        self.numero = numero
        self.tipo = tipo 
        self.ocupada = False 
        
    def reservar(self):
        if not self.ocupada:
            self.ocupada = True 
            print(f"Habitación {self.numero} {self.tipo} ha sido reservada.")
        else: 
            print(f"Habitación {self.numero} ya está ocupada.") 
    
    def liberar(self): 
        if self.ocupada:
            self.ocupada = False
            print(f"Habitación {self.numero} ha sido liberada.")
        else:
            print(f"Habitación {self.numero} ya está libre.") 

# Clase Huesped 
class Huesped:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id

    def reservar_habitacion(self, habitacion):
        if not habitacion.ocupada:
            habitacion.reservar()
            print(f"{self.nombre} identificado con numero {self.id} ha reservado la habitación {habitacion.numero}.")
        else:
            print(f"La habitación {habitacion.numero} no está disponible.") 

hotel = Habitacion(11, 'individual')
hotel.reservar()

cliente = Huesped('yeison', 1193290165)
cliente.reservar_habitacion(hotel)

        