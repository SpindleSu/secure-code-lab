# 🧠 Secure Code Lab

Sistema modular de análisis de seguridad inspirado en CodeQL, Semgrep y pipelines modernos de AppSec.

---

## 🎯 Objetivo

Detectar, analizar y ayudar a corregir vulnerabilidades en código mediante:

- Motor de análisis estático (AST + reglas)
- Motor de corrección basado en patrones seguros
- Capa de análisis con IA (multi-agente)
- Orquestación y trazabilidad completa

---

## 🏗️ Arquitectura

- motor_core → detección de vulnerabilidades
- reglas → definición de patrones de seguridad
- motor_fixes → correcciones seguras
- capa_multiagente → análisis explicativo con IA
- orquestador → pipeline completo
- tests → validación del sistema

---

## 🔐 Principios

- El análisis determinista es la fuente de verdad
- La IA no decide, solo interpreta
- Todo output es estructurado
- Todo proceso es trazable (request_id)

---

## 🚧 Estado

Fase inicial: estructura base del sistema