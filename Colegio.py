class Persona:

    def __init__(self, nombre, usuario, correo, contraseña, materia):
        self.nombre = nombre
        self.usuario = usuario
        self.correo = correo
        self.contraseña = contraseña
        self.materia = materia

class Estudiante(Persona):
    def __init__(self, nombre, usuario, correo, contraseña, materia, grado, puntos, cantActividades, ActividadesREP, ActividadesAP ):
        super().__init__(self, nombre, usuario, correo, contraseña, materia)
        self.grado=grado
        self.puntos = puntos
        self.cantActividades = cantActividades
        self.ActividadesREP = ActividadesREP
        self.ActividadesAP = ActividadesAP

class Profesor(Persona):
    def __init__(self,nombre, usuario, correo, contraseña, materia,verificar):
        super().__init__(self, nombre, usuario, correo, contraseña, materia)
        self.verificar=verificar



