from alternativa import Alternativa

class Pregunta():
    def __init__(self, enunciado: str, ayuda: str = "", requerida: bool = False, alternativas: list = []):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.__alternativas = [Alternativa(alt["contenido"], alt["ayuda"]) for alt in alternativas]        
        
    @property
    def alternativas(self):
        self.__alternativas
        
    @alternativas.setter
    def alternativas(self, alternativas):
        pass

    def mostrar(self):
        print(f"Enunciado: {self.enunciado}")
        if self.ayuda:
            print(f"Ayuda: {self.ayuda}")
        print("***Alternativas***")
        for alternativa in self.__alternativas:
            alternativa.mostrar()
