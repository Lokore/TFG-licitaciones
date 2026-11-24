# Bitácora de decisiones compartida — Claude Code ↔ Codex

Este archivo es el canal de comunicación entre Claude Code y Codex (ChatGPT) mientras ambos trabajan sobre los archivos de `C:/TFG`. No hay forma de que las dos herramientas se mensajeen directamente, así que coordinan acá, por escrito, antes de actuar.

## Protocolo

1. **Antes** de aplicar un cambio de fondo (contenido, estructura, citas, redacción, formato del anteproyecto — no aplica a tareas triviales como typos obvios), la herramienta que va a actuar agrega una entrada nueva al final de este archivo con el formato de abajo, y **espera** una revisión antes de ejecutar si el cambio es grande/riesgoso, o ejecuta y dejar constancia si es menor.
2. La **otra** herramienta, en su próximo turno, lee las entradas con estado `PENDIENTE` o `EJECUTADO`, y agrega su veredicto: `✅ DE ACUERDO`, `⚠️ OBJECIÓN` (con el motivo), o `❓ PREGUNTA` (si necesita más contexto).
3. Si hay una `⚠️ OBJECIÓN`, la herramienta que propuso el cambio original debe responder antes de que cualquiera vuelva a tocar esa parte del documento — no se resuelve por mayoría ni se ignora.
4. Nunca editar o borrar una entrada de otro; solo agregar entradas nuevas debajo.
5. El usuario es el árbitro final si las dos herramientas no llegan a acuerdo.

## Formato de entrada

```
### [FECHA HORA] — [Claude Code | Codex] — [PENDIENTE | EJECUTADO]
**Decisión/cambio propuesto:** ...
**Por qué:** ...
**Archivo(s) afectado(s):** ...
**Veredicto de la otra herramienta:** (se completa después)
```

---

### 2026-11-17 14:50 — Claude Code — EJECUTADO
**Decisión/cambio propuesto:** Se crea este canal de coordinación a pedido del usuario, que va a trabajar con Codex en paralelo sobre la misma carpeta.
**Por qué:** Evitar que ambas herramientas editen el mismo contenido sin que la otra lo sepa, y permitir revisión cruzada de decisiones de fondo sobre el anteproyecto.
**Archivo(s) afectado(s):** Ninguno del proyecto todavía; este archivo es nuevo.
**Veredicto de la otra herramienta:** (pendiente)
