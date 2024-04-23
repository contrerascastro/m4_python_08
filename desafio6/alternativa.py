class Alternativa():
    def __init__(self, contenido: str, ayuda: str = ''):
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar(self):
        if self.ayuda:
            print(f"{self.contenido}\nAyuda: {self.ayuda}")
        else:
            print(f"{self.contenido}")
