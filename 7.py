class EventDispatcher:

    def __init__(self):
        self.eventos = {}

    def registrar(self, nombre, funcion):

        self.eventos[nombre] = funcion

    def emitir(self, nombre, datos):

        if nombre in self.eventos:

            funcion = self.eventos[nombre]

            funcion(**datos)


def mostrar_usuario(nombre, email):

    print("Nombre:", nombre)
    print("Email:", email)


evento = EventDispatcher()


evento.registrar(
    "usuario",
    mostrar_usuario
)


datos = {
    "nombre": "Carlos",
    "email": "carlos@email.com"
}


evento.emit(
    "usuario",
    datos
)
