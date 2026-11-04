
# ============================================================
# TAREA: ENTRADA Y SALIDA DE ARCHIVOS
# PARTE 3: FORMATO JSON
# ============================================================

# PREGUNTA 11:
# ¿Qué hace la función json.dump()?
#
# RESPUESTA:
# La función json.dump() convierte un objeto de Python,
# como un diccionario o una lista, a formato JSON
# y lo escribe directamente en un archivo.
#
# Esto permite guardar información de manera
# estructurada y utilizarla posteriormente.


# PREGUNTA 12:
# ¿Cuál es la ventaja de usar with open(...)
# en lugar de .close()?
#
# RESPUESTA:
# La ventaja es que with open() cierra el archivo
# automáticamente cuando termina el bloque de código.
#
# Esto sucede incluso si ocurre una excepción.
# De esta manera evitamos olvidar cerrar el archivo,
# mejoramos la seguridad y administramos mejor
# los recursos del programa.


# ============================================================
# CÓDIGO FUNCIONAL - PARTE 3
# ============================================================

import json

# Crear diccionario con información del usuario
usuario = {
    "nombre": "Estudiante",
    "habilidades": ["Python", "HTML"],
    "activo": True
}

# GUARDAR INFORMACIÓN EN JSON
with open('datos.json', 'w') as f:
    json.dump(usuario, f, indent=4)

print("Datos guardados correctamente.")


# LEER INFORMACIÓN DESDE JSON
with open('datos.json', 'r') as f:
    datos = json.load(f)

    print(f"Usuario: {datos['nombre']}")
