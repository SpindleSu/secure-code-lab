from dataclasses import dataclass


@dataclass(frozen=True)
class Hallazgo:
    """
    Representa una vulnerabilidad o problema de seguridad detectado.
    """

    identificador_regla: str
    severidad: str
    linea: int
    mensaje: str