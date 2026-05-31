from motor_core.parser import parsear_codigo_fuente
from motor_core.hallazgos import Hallazgo
from motor_core.interfaces import ReglaSeguridad
from motor_core.reglas.regla_sql_injection import ReglaSqlInjection


class AnalizadorSeguridad:
    """
    Ejecuta reglas de seguridad sobre código fuente.
    """

    def __init__(self) -> None:

        self.reglas: list[ReglaSeguridad] = [
            ReglaSqlInjection()
        ]

    def analizar(self, codigo_fuente: str) -> list[Hallazgo]:

        arbol_ast = parsear_codigo_fuente(codigo_fuente)

        hallazgos_detectados: list[Hallazgo] = []

        for regla in self.reglas:

            hallazgos_detectados.extend(
                regla.evaluar(arbol_ast)
            )

        return hallazgos_detectados