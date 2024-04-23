from pregunta import Pregunta

class Encuesta:
    def __init__(self, nombre: str, preguntas = [], respuestas=[]):
        self.nombre = nombre
        self.__preguntas = [Pregunta(p["enunciado"], p["ayuda"], p["requerida"], p["alternativas"]) for p in preguntas]
        self.__respuestas = respuestas
        
        
    # solo el nombre puede consultarse y modificarse libremente
    @property
    def preguntas(self):
        self.__preguntas
        
    @preguntas.setter   
    def preguntas(self, preguntas):
        pass
    
    @property
    def respuestas(self):
        self.__respuestas
        
    @respuestas.setter   
    def respuestas(self, respuestas):
        pass

    def mostrar(self):
        print(f"Encuesta: {self.nombre}")
        print("***Preguntas***")
        for pregunta in self.__preguntas:
            pregunta.mostrar()

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, edad_minima: int, edad_maxima: int, preguntas=[], respuestas=[]):
        super().__init__(nombre, preguntas, respuestas)
        self.__edad_minima = edad_minima
        self.__edad_maxima = edad_maxima
        
    @property
    def edad_minima(self):
        return self.__edad_minima
    
    @edad_minima.setter
    def edad_minima(self, edad_minima):
        self.__edad_minima = edad_minima
        
    @property
    def edad_maxima(self):
        return self.__edad_maxima
    
    @edad_maxima.setter
    def edad_maxima(self, edad_maxima):
        self.__edad_maxima = edad_maxima
        
    def agregar_respuestas(self, respuestas: list, edad_usuario: int):
        if self.edad_minima <= edad_usuario <= self.edad_maxima:
            self.respuestas.append(respuestas)
        else:
            print("La edad del usuario no está dentro del rango permitido para esta encuesta.")

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, regiones, preguntas=[], respuestas=[]):
        super().__init__(nombre, preguntas, respuestas)
        self.__regiones = regiones
        
    @property
    def regiones(self):
        return self.__regiones
    
    @regiones.setter
    def regiones(self, regiones):
        self.__regiones = regiones
        
    def agregar_respuestas(self, respuestas: list, region_usuario: int):
        if region_usuario in self.regiones:
            self.respuestas.append(respuestas)
        else:
            print("La región del usuario no está permitida para esta encuesta.")
