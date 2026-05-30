# 🔐 Reglas de seguridad

## Formato

Cada regla define:

- nombre
- descripción
- severidad
- patrón de detección

---

## Reglas iniciales

### SQL Injection
Detecta concatenación de strings en queries SQL.

Severidad: CRÍTICA

---

### Credenciales hardcodeadas
Detecta strings sospechosamente sensibles.

Severidad: ALTA

---

### Command Injection (futuro)
Detecta uso inseguro de subprocess/os.system.

Severidad: CRÍTICA