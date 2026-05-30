# 🏗️ Arquitectura del sistema

## Flujo

Entrada de código
   ↓
motor_core (AST + reglas)
   ↓
hallazgos estructurados
   ↓
capa_multiagente (explicación + análisis)
   ↓
motor_fixes (corrección segura)
   ↓
orquestador (validación final)

---

## Diseño

El sistema separa:

- detección (determinista)
- interpretación (IA)
- corrección (reglas)
- validación (control final)