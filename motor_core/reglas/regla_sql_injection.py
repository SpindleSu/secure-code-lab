import ast

from motor_core.hallazgos import Hallazgo
from motor_core.interfaces import ReglaSeguridad


class ReglaSqlInjection(ReglaSeguridad):
    """
    Detecta consultas SQL construidas mediante f-strings.
    """

    def evaluar(self, arbol_ast: ast.AST) -> list[Hallazgo]:

        hallazgos_detectados = []

        for nodo in ast.walk(arbol_ast):

            if not isinstance(nodo, ast.Call):
                continue

            if not hasattr(nodo.func, "attr"):
                continue

            if nodo.func.attr != "execute":
                continue

            for argumento in nodo.args:

                if isinstance(argumento, ast.JoinedStr):

                    hallazgos_detectados.append(
                        Hallazgo(
                            identificador_regla="SQL_INJECTION",
                            severidad="CRITICA",
                            linea=getattr(nodo, "lineno", -1),
                            mensaje="Posible inyección SQL mediante uso de f-string."
                        )
                    )

        return hallazgos_detectados