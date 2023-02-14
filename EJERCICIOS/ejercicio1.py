class vehiculo:
    def __init__(self, velocidad_max, kilometraje):
        self.velocidad_max = Velocidad_maxima
        self.kilometraje = kilometraje

    def getvelocidad_max(self):
        return self.velocidad_max
    def getkilometraje(self):
        return self.kilometraje

    def Mostrarvehiculo(self):
        print("\nvelocidad_max: " +self.getvelocidad_max()+ "\nkilometraje: " +self.getkilometraje())



velocidad_max = input( "Ingrese la Velocidad maxima: ")
kilometraje = input("Ingrese el kilometraje del Vehiculo: ")

e = vehiculo(velocidad_max, kilometraje)
e.Mostrarvehiculo()
