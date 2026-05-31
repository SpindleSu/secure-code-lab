import ast


def parsear_codigo_fuente(codigo_fuente: str) -> ast.AST:
    """
    Convierte código Python en un árbol AST.
    """

    return ast.parse(codigo_fuente)