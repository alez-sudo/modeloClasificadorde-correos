# 1. NUESTROS DATOS (Comentarios en una publicación)
comentarios_nuevos = [
    "¡Qué gran publicación, me encantó el contenido!",
    "Eres un idiota y no sabes nada de lo que hablas.",
    "Hola, ¿alguien sabe a qué hora abre el banco hoy?",
    "Este post es una basura, vete de las redes."
]

# 2. NUESTRO MODELO (Palabras prohibidas por la comunidad)
palabras_toxicas = ["idiota", "basura", "estúpido", "odiar"]

def modelo_ia_moderador(comentario):
    comentario_minuscula = comentario.lower()
    
    # El modelo busca si hay lenguaje ofensivo
    for palabra in palabras_toxicas:
        if palabra in comentario_minuscula:
            return "BLOQUEADO (Tóxico)" # Predicción 1
            
    return "APROBADO (Seguro)" # Predicción 2

# 3. EVALUACIÓN Y PREDICCIÓN
print("--- MODERADOR DE REDES SOCIALES ---")
for i, comentario in enumerate(comentarios_nuevos, 1):
    prediccion = modelo_ia_moderador(comentario)
    print(f"Comentario {i}: '{comentario}' -> ESTADO: {prediccion}")
