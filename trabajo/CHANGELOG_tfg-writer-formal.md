# CHANGELOG: tfg-writer-formal

# RONDA 2 (17-11-2026): revisión de fluidez tras la devolución real de la profesora

**Punto de partida:** `CHANGELOG_tfg-master-ieee.md` y `CHANGELOG_citation-verifier-master.md`, ronda 2. Leí el documento completo (451 líneas) después de sus reescrituras: preguntas de investigación reformuladas, hipótesis en presente, método reorganizado en 5 fases, variables renombradas (13 en total) y ~35 citas reformuladas a voz impersonal o "et al.".

## 1. Encargo específico de citation-verifier-master: fluidez tras el paso a voz impersonal

Revisé 7.1.1.3, 7.1.2.1, 7.1.2.2, 7.1.2.4 y 7.1.3 oración por oración.

- **7.1.1.3:** sin problemas de fluidez. El patrón "**Término.** Verbo con sujeto implícito..." se mantiene consistente en los siete métodos (MAVT, AHP, TOPSIS, VIKOR, ELECTRE, PROMETHEE, MOORA); es un recurso estilístico ya presente antes de esta ronda, no una secuela del cambio a voz impersonal, y funciona bien.
- **7.1.2.1:** sin problemas. El cambio puntual de citation-verifier-master ("exige" → "se exigen") es gramaticalmente correcto y el resto del apartado (artículos de la Ley 2051/2003, la Ley 7021/2022 y el Decreto 2264/2024 como sujetos) fluye con naturalidad.
- **7.1.2.2:** apliqué 1 corrección. La oración "Los métodos de evaluación de ofertas se han estudiado desde la relación entre precio y calidad [33] y, mediante análisis multicriterio, **para** seleccionar la oferta económicamente más ventajosa [3]" mezclaba dos nexos distintos ("desde..." y "...para...") de forma que dificultaba ver que ambos modificaban "se han estudiado". Cambié "para" por "**con el fin de**" para marcar mejor el segundo tramo de la enumeración, sin tocar las citas ni el contenido.
- **7.1.2.4:** apliqué 1 corrección. "La literatura ofrece orientaciones para relacionar métodos y problemas [14] **y** un sistema de recomendación..." podía leerse, en una primera pasada, como si "ofrece" tuviera un único objeto compuesto poco marcado. Añadí "**así como**" para separar con claridad los dos aportes que ofrece la literatura.
- **7.1.3:** apliqué 1 corrección, de alcance mayor que las anteriores. La frase que enumeraba las tres características relevantes del sistema de soporte a la decisión (trazabilidad, reproducibilidad, condición de prototipo) era una sola oración con dos puntos y dos complejas cláusulas subordinadas, trabada por el paso a voz impersonal ("que aquí se extiende a...", "orientada aquí a..."). La dividí en tres oraciones (una de anuncio de los tres elementos, y una por cada característica con cláusula propia), sin quitar ni añadir ninguna cita ([36], [9], [37] se mantienen en el mismo orden y con la misma función).

**No encontré problemas de fluidez que corregir** en el resto de las frases reformuladas a voz impersonal que menciona el changelog de citation-verifier-master (6, 7.1.2.3, 7.2, 8.1.11): todas leen con naturalidad en su forma actual.

## 2. Encargo específico de citation-verifier-master: afirmación en plural con una sola cita (sección 1)

Corregido. "Estudios sobre evaluación de licitaciones destacan la necesidad de..., y **muestran** que los enfoques multicriterio pueden representar... [3]" pasó a "**Un estudio** sobre evaluación de licitaciones **destaca**... y **muestra**... [3]", con concordancia de número ajustada en ambos verbos de la oración.

**Caso análogo que no corregí, para que lo evalúen los otros dos agentes:** en la Fundamentación académica (sección 5), "las revisiones sobre la calidad de las hojas de cálculo señalan que la mayoría de las planillas... contienen errores... [8]" tiene el mismo patrón (sustantivo plural, una sola cita). La diferencia es que [8] es en sí misma una revisión de literatura ("a literature review"), por lo que "revisiones" podría referirse, de forma legítima, a los estudios que esa revisión recoge y no al número de fuentes citadas en el cuerpo. No tengo forma de confirmar esa lectura sin leer [8] a texto completo, así que dejo la decisión (mantener el plural, pasar a singular, o verificar el contenido de [8]) a citation-verifier-master.

## 3. Verificación de tiempos verbales (encargo sobre GB7)

Confirmé que la Hipótesis (sección 4) está enteramente en presente, como registra tfg-master-ieee. Repasé el resto del documento buscando más inconsistencias de tiempo verbal:

- **Marco teórico (7.1 y 7.2):** verbos en presente de forma consistente (analizan, estudia, examinan, proponen, comparan, aplican, desarrollan, construyen, presentan, etc.), incluso cuando describen trabajos publicados en el pasado; es el uso académico esperado ("presente histórico" o "de cita") y no requiere cambios.
- **Método (sección 8) y Lista de tareas (8.2):** verbos en futuro ("se realizará", "se seleccionará", "se examinará") de forma consistente en todo el apartado. Es correcto: describen un plan de trabajo que todavía no se ha ejecutado, a diferencia de la Hipótesis, que describe una relación que se pondrá a prueba. No encontré ninguna oración de esta sección en presente o en pasado que rompiera esa consistencia.
- **Impacto de la investigación (sección 6):** usa consistentemente el contraste "Antes del proyecto" (presente) / "Después del proyecto" (futuro: "permitirá", "podrá"), que es intencional y está bien marcado en todos los párrafos (individual, institucional, social, ecológico, académico).
- **No encontré ningún otro verbo que debiera pasar a presente por el mismo motivo que GB7** (es decir, una afirmación atemporal o definitoria redactada en futuro). El único caso de ese tipo ya fue corregido por tfg-master-ieee en la Hipótesis.

## 4. Otras verificaciones sin correcciones pendientes

- Revisé de corrido las 451 líneas buscando oraciones con sentido incompleto por ediciones concurrentes (un riesgo típico de varias rondas de edición simultánea): no encontré ninguna. Las transiciones entre objetivos, hipótesis, fases del método (8.1.2), tareas (8.2) y variables (8.3) son coherentes entre sí y las referencias cruzadas (a 8.1.2, 8.1.5, 8.1.10, 8.1.11) apuntan a los apartados correctos con la numeración actual.
- Concordancia número/género, tildes y ortografía: sin hallazgos nuevos (repetí las comprobaciones dirigidas de la ronda 1 sobre el texto ya reescrito).
- Celdas vacías detectadas por una búsqueda de espacios múltiples (líneas 333–366) corresponden a columnas sin marca "X" en la Tabla 1 (cronograma); no es un error de redacción.

## 5. Conflictos entre agentes

No encontré ningún conflicto entre una corrección de formato IEEE y una de citas que yo debiera exponer sin resolver. El único punto que dejo explícitamente a su criterio es el de la sección 5 señalado en el punto 2.

## 6. Resumen de esta ronda

- **4 correcciones de fluidez/forma aplicadas:** 7.1.2.2 (nexo "para" → "con el fin de"), 7.1.2.4 (conector "así como"), 7.1.3 (una oración larga dividida en tres, mismas citas), y sección 1 (plural → singular en "Un estudio... destaca... y muestra...").
- **0 correcciones de contenido técnico, citas o cifras.** No toqué ninguna referencia, numeración [n] ni dato.
- **1 observación de fondo sin corregir**, señalada para citation-verifier-master: el "revisiones... [8]" de la sección 5, análogo al caso de la sección 1.
- **Estado general de la redacción:** buena. Tras dos rondas de reescrituras sustanciales por parte de tfg-master-ieee y citation-verifier-master, el documento no presenta errores de concordancia, tiempos verbales inconsistentes ni oraciones truncadas por ediciones concurrentes. Las correcciones de esta ronda son menores y puntuales (4 ediciones en un documento de 451 líneas).

---

**Archivo:** `C:/TFG/trabajo/anteproyecto_borrador.md`
**Fecha:** 17-11-2026
**Punto de partida:** `CHANGELOG_tfg-master-ieee.md` y `CHANGELOG_citation-verifier-master.md`, además de mi propia revisión previa (`revision_tfg-writer-formal.md`) sobre la versión original del documento.
**Método:** leí el documento completo (líneas 1–474) después de las dos reescrituras y verifiqué, uno por uno, los puntos que había señalado en la revisión original, más una pasada general de gramática, ortografía, registro y uso del inglés.

---

## 1. Hallazgo principal: los errores de forma que había señalado originalmente ya no están

Antes de corregir nada, confirmé con grep y lectura completa el estado de cada punto de mi revisión anterior:

| Error original señalado | Estado actual |
|---|---|
| Título con espacios faltantes ("métodosmulticriterio", "evaluaciónde") | Resuelto. El título actual ("Prototipo web de soporte a la decisión basado en métodos multicriterio para la evaluación de ofertas en licitaciones de Paraguay (2023–2026)") está bien formado. |
| Título distinto en portada vs. cuerpo | Resuelto. Verifiqué carácter por carácter: línea 13 (portada) y línea 84 (apertura del cuerpo) son idénticas. |
| Pregunta principal sin tilde en "qué" y con infinitivo suelto ("apoyar") | Resuelto. La pregunta actual (línea 92) está completa y bien puntuada: "¿En qué medida puede un prototipo web de soporte a la decisión [...] reducir el tiempo [...], en licitaciones de Paraguay con adjudicaciones publicadas entre 2023 y 2026?". |
| "La elección de los método" (error de concordancia) | Resuelto. El párrafo 3 de la sección 1 fue reescrito por completo (ya no contiene esa oración ni el error). |
| Hipótesis con "comparándolos" de referente ambiguo | Resuelto de raíz: la sección 4 fue reescrita en tres hipótesis separadas (H1, H2, H3), cada una en oración acotada, sin gerundios de referente ambiguo. |
| Formato de fechas inconsistente (2023 a 2026 / 2023 y 2026 / 2023–2026) | Parcialmente heredado, corregido ahora (ver punto 2). |

No fue necesario reintroducir ninguna corrección de las que ya había pedido: las reescrituras de tfg-master-ieee absorbieron esos cambios al reformular las oraciones completas.

## 2. Correcciones de forma aplicadas en esta pasada

1. **Unifiqué el criterio de formato de fechas.** Detecté que, tras las reescrituras, el documento usa de forma mayoritaria y consistente "entre 2023 y 2026" dentro de oraciones corridas (6 apariciones) y "(2023–2026)" con guion en-dash como marca parentética junto al título o a un sustantivo (4 apariciones). Quedaba una excepción: en la tarea 1.1 ("adjudicaciones de 2023 a 2026") se usaba una tercera forma. La cambié a "adjudicaciones publicadas entre 2023 y 2026" para igualarla al resto de las apariciones en prosa.
   - **No toqué** la entrada de referencia [44] ("Conjuntos correspondientes a 2023-2026"), porque es contenido de una cita bibliográfica y corresponde a citation-verifier-master, no a mí.

2. **Actualicé la fecha de portada.** Por indicación de citation-verifier-master, la fecha de portada ("2 de noviembre de 2026") quedaba anterior a la fecha de acceso de todas las citas (17-nov-2026), lo cual es cronológicamente incoherente (el documento citaría fuentes consultadas después de su propia fecha de cierre). La actualicé a **17 de noviembre de 2026**, que es la fecha de hoy según el entorno y coincide con el día en que citation-verifier-master dejó registrada la verificación de todas las URLs. No usé una fecha posterior inventada (p. ej., 18-nov) porque no tengo forma de saber si ese es el día real de entrega; dejo a criterio del estudiante adelantarla si el anteproyecto se presenta después.

## 3. Verificaciones que no arrojaron correcciones pendientes

- **Registro impersonal/académico:** se mantiene sin fisuras en las 474 líneas. No encontré ningún fragmento con el registro de carta/anexo (fórmulas como "manifiesto por este medio", "me dirijo a usted", "Atentamente", "Yo, [nombre], documento de identidad N.º..."); ese registro solo debería aparecer en los anexos (ANEXO II y IV), que no forman parte de este archivo.
- **Inglés en el cuerpo:** no hay ninguna oración del cuerpo en inglés. El inglés que aparece está exclusivamente en los títulos de las 51 referencias bibliográficas (esperado y correcto, según indicó el estudiante) y en nombres propios de método ("min-max", "UTA-splines"), que se mantienen como términos técnicos consolidados.
- **Concordancia número/género:** no encontré nuevos errores de concordancia en la revisión completa (grep de palabras repetidas, errores típicos de artículo+sustantivo, etc., sin resultados en el cuerpo).
- **Tildes y ortografía:** grep dirigido a palabras agudas/esdrújulas comúnmente mal escritas sin tilde (método, evaluación, información, técnico, análisis, decisión, función, etc.) no encontró ninguna instancia sin tilde en el cuerpo; todas las coincidencias correspondían a texto en inglés de las referencias.
- **Índice vs. cuerpo:** el título de la portada (línea 13) y el que abre el cuerpo (línea 84) son idénticos carácter por carácter. El índice (líneas 29–71) ahora sí incluye la sección 5 y los apartados 8.1.1–8.1.11, resolviendo la discrepancia que había señalado en la revisión original (ese era un comentario de estructura, no de redacción, y ya lo había dejado para tfg-master-ieee).
- **Hipótesis:** las tres hipótesis (H1, H2, H3) están redactadas en oraciones acotadas, sin gerundios sueltos ni referentes ambiguos. H2 en particular, que antes tenía el problema del "comparándolos", ahora compara explícitamente "la evaluación de ofertas realizada con el prototipo web [...] que la evaluación manual de las mismas reglas y ponderaciones, realizada por esos mismos expertos con una hoja de cálculo de uso general": el sujeto de la comparación es inequívoco.
- **Monotonía de apertura en antecedentes (7.2.1):** la señalé en mi revisión original como un problema de estilo (siete párrafos con la fórmula "El artículo '...' analiza..."). tfg-master-ieee resolvió esto de fondo al reescribir cada antecedente con la estructura "Autor(es) [n] (año) + verbo variado + aporte + diferencia" (p. ej., "Mayor, Botero y González-Ruiz [46] (2016) proponen...", "Stilger, Siderius y van Raaij [10] (2017) comparan..."). Ya no hay monotonía de apertura; no fue necesario intervenir.

## 4. Puntos que señalo sin tocar (no son de mi competencia)

No encontré conflictos entre una corrección de formato IEEE y una de citas que requirieran que yo arbitrara. Sí dejo constancia de dos observaciones menores para que los otros dos agentes las evalúen, por si no las habían visto:

1. **Prosa de las secciones nuevas (5, 6, 7.1.3, 8.1.5, 8.1.10):** tfg-master-ieee pidió explícitamente que yo revisara la redacción de estas secciones "palabra por palabra". Las leí completas: están bien escritas, en registro académico consistente, sin errores gramaticales ni frases huecas. No encontré nada que corregir en ellas más allá de lo ya aplicado (fechas).
2. **[13, p. 5]:** citation-verifier-master dejó a criterio de tfg-master-ieee si debe añadirse el número de página a la cita de Mavidis y Folinas [13] en el cuerpo (actualmente aparece como "[13]" sin página, por ejemplo en la línea 129 y en 135). Es una decisión de formato IEEE de citas, no de redacción; la señalo para que no se pierda entre los dos changelogs, pero no la cambié yo.

## 5. Resumen

- **2 correcciones de forma aplicadas:** unificación del formato de fechas (1 instancia) y actualización de la fecha de portada.
- **0 correcciones de contenido técnico, objetivos, hipótesis, metodología o citas.** No toqué nada de eso.
- **Todos los errores de mi revisión original ya estaban resueltos** por las reescrituras de tfg-master-ieee y citation-verifier-master; no fue necesario reintroducir ninguno.
- El documento, en su estado actual, cumple con el registro impersonal/académico esperado por la cátedra, no mezcla el tono de los anexos, no tiene inglés fuera de las referencias y mantiene terminología metodológica consistente.
