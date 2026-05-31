from motor_core.analizador import AnalizadorSeguridad


codigo_fuente = """
import sqlite3

def login(usuario):
    conexion = sqlite3.connect("app.db")
    cursor = conexion.cursor()

    cursor.execute(
        f"SELECT * FROM users WHERE nombre='{usuario}'"
    )
"""


analizador = AnalizadorSeguridad()

hallazgos = analizador.analizar(codigo_fuente)

print(hallazgos)