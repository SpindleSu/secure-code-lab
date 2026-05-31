from abc import ABC, abstractmethod
import ast

from motor_core.hallazgos import Hallazgo


class ReglaSeguridad(ABC):
    """
    Contrato base para todas las reglas de seguridad.
    """

    @abstractmethod
    def evaluar(self, arbol_ast: ast.AST) -> list[Hallazgo]:
        """
        Analiza un árbol AST y devuelve los hallazgos encontrados.
        """
        pass