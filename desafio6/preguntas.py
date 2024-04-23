# Ejemplo de lista de preguntas para una encuesta simple
preguntas_simple = [
    {
        "enunciado": "¿Cómo calificarías nuestro servicio?",
        "ayuda": "Por favor, califica nuestro servicio del 1 al 5.",
        "requerida": True,
        "alternativas": [
            {"contenido": "1", "ayuda": "Muy malo"},
            {"contenido": "2", "ayuda": "Malo"},
            {"contenido": "3", "ayuda": "Regular"},
            {"contenido": "4", "ayuda": "Bueno"},
            {"contenido": "5", "ayuda": "Excelente"}
        ]
    },
    {
        "enunciado": "¿Qué tan probable es que recomendarías nuestro servicio a un amigo?",
        "ayuda": "Por favor, indícanos en una escala del 1 al 10.",
        "requerida": True,
        "alternativas": [
            {"contenido": "1", "ayuda": "Nada probable"},
            {"contenido": "2", "ayuda": ""},
            {"contenido": "3", "ayuda": ""},
            {"contenido": "4", "ayuda": ""},
            {"contenido": "5", "ayuda": ""},
            {"contenido": "6", "ayuda": ""},
            {"contenido": "7", "ayuda": ""},
            {"contenido": "8", "ayuda": ""},
            {"contenido": "9", "ayuda": ""},
            {"contenido": "10", "ayuda": "Muy probable"}
        ]
    }
]

# Ejemplo de lista de respuestas para la encuesta simple
respuestas_simple = [
    {"pregunta": 0, "alternativa": 4},  # Primera pregunta, quinta alternativa (Excelente)
    {"pregunta": 1, "alternativa": 9}   # Segunda pregunta, décima alternativa (Muy probable)
]
