---
name: ahorro-tokens
description: Usar cuando una tarea implica leer o procesar documentos largos (PDF, DOCX, material de guía) o generar informes extensos, para reducir el consumo de tokens sin perder rigor: lee solo lo necesario, resume en vez de citar en extenso, evita releer archivos ya leídos, y delega trabajo pesado a subagentes en vez de cargarlo en el contexto principal.
---

# Ahorro de tokens

Esta skill no reduce la calidad del análisis; reduce el desperdicio. Aplica estas reglas siempre que trabajes con documentos largos o generes informes:

## Al leer documentos
- No leas un archivo completo si una búsqueda dirigida (Grep, búsqueda de texto, índice) puede localizar la sección relevante primero.
- Si ya leíste un archivo en esta sesión y no fue editado, no lo vuelvas a leer completo: usa lo que ya está en contexto o relee solo el rango de líneas necesario.
- Para PDFs/DOCX muy largos, procesa por secciones (capítulos, apartados) en vez de cargar el documento entero de una sola vez si solo necesitas una parte.
- Prioriza extraer texto plano sobre convertir a formatos intermedios innecesarios.

## Al escribir informes o respuestas
- No reproduzcas párrafos completos de un documento fuente: resume la idea y cita como máximo una frase corta cuando sea imprescindible para señalar un error puntual.
- No repitas en tu respuesta final algo que ya quedó guardado en un archivo de salida; referencia el archivo y da solo el resumen ejecutivo.
- Evita narrar el proceso paso a paso ("ahora voy a leer X, ahora voy a analizar Y"); ve directo al hallazgo.
- Prefiere listas y tablas compactas sobre prosa extensa cuando la información es estructurada (hallazgos, checklists, inventarios de citas).

## Al delegar trabajo
- Si una tarea requiere leer 10+ archivos o hacer muchas búsquedas web, delega a un subagente en vez de hacerlo en el hilo principal: su salida completa no vuelve a tu contexto, solo su resumen.
- No le pidas a un subagente que relea material que otro subagente ya analizó y dejó documentado en un archivo; dile que lea ese archivo de síntesis en vez de releer las fuentes originales desde cero, salvo que necesite verificar algo puntual contra la fuente primaria.
- Evita lanzar el mismo tipo de análisis dos veces sobre el mismo contenido "por si acaso"; reutiliza lo ya hecho.

## Señal de alerta
Si notas que vas a volcar más de ~2000 palabras de texto citado textualmente de una fuente en tu respuesta o en un archivo, detente: casi siempre se puede resumir en una fracción de eso sin perder la información que importa para la decisión.
