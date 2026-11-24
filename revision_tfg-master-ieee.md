# Revisión crítica del Anteproyecto: «Implementación de métodos multicriterio para la evaluación de licitaciones»

**Agente:** tfg-master-ieee
**Documento revisado:** `Anteproyecto_licitaciones_Ivan_Alex.docx` (44 páginas, unas 19 100 palabras, portada fechada el 2/11/2026)
**Criterios aplicados:** mi síntesis previa del material de la cátedra (`analisis_tfg-master-ieee.md`): la plantilla `ptfg_ieee` como esqueleto obligatorio, el Reglamento (Res. 143/2022), las diapositivas 2025 de la Prof. Bobadilla y las guías IEEE solo para la mecánica de citas. La escala de severidad es la de §3.3 de esa síntesis. Recuerdo que **es criterio mío y no una rúbrica de la cátedra**, porque esa rúbrica escrita no existe.
**Fecha:** 17/11/2026

---

## Veredicto global

**En su estado actual no está en condiciones de ser aprobado.** El motivo no es la falta de trabajo, que sobra, sino la cadena lógica: **problema → preguntas → objetivos → hipótesis → variables → método**. Esa cadena está rota en varios eslabones que la plantilla considera obligatorios:

- No hay enunciado formal del problema.
- La hipótesis afirma cosas que ningún objetivo persigue y ninguna variable mide.
- Una variable no tiene estimador ("pendiente de definición").
- La comparación central, manual contra prototipo, está diseñada de un modo que casi garantiza el resultado que se quiere probar.

A eso se suma una tensión conceptual que el documento nunca resuelve: **si las ponderaciones y las reglas se toman del pliego, ¿qué decide realmente la "comparación de métodos"?**

La base es recuperable: las referencias son de buena calidad, las tareas están bien formuladas, el cronograma es correcto y el marco teórico es sofisticado. El problema es de **coherencia y de foco**, no de esfuerzo. Con una iteración seria se puede corregir.

---

## 1. Checklist de cumplimiento estructural

Contrasto el documento con la plantilla `ptfg_ieee`, que es la fuente de la estructura. El Reglamento solo exige "Proyecto de TFG" más el ANEXO II.

### 1.1 Portada e índice

| Elemento exigido | Estado | Observación |
|---|---|---|
| Universidad, Facultad, rótulo "Anteproyecto de TFG", Carrera, Cátedra | ✅ Presente | Correcto. |
| Título | ⚠️ Inconsistente | El de la portada ("…de **métodos** multicriterio…") no coincide con el que se repite al inicio del cuerpo ("…de **un método** multicriterio…"). Ninguno de los dos menciona el prototipo web, Paraguay ni el periodo, aunque el objetivo general sí lo hace. La plantilla dice que el objetivo general "engendra" el título. |
| "Por:" con los graduandos y **nota al pie** con teléfono y correo | ❌ Formato incorrecto | Los contactos van en una tabla suelta, sin indicar a quién pertenece cada dato y sin notas al pie (el documento no tiene ninguna). |
| Profesor Orientador con nota al pie de contacto | ❌ Falta | No figura el contacto del Orientador. |
| Profesor de la Cátedra, lugar y fecha | ✅ Presente | — |
| Índice paginado; portada sin número visible e índice como pág. 1 | ⚠️ Desactualizado | Ver la tabla 1.3. La numeración de páginas no se puede verificar sin renderizar el documento; hay que comprobarla. |

### 1.2 Cuerpo: presencia y orden

| # | Sección (plantilla) | Presente | Orden | Observación clave |
|---|---|---|---|---|
| — | Título repetido al inicio del cuerpo | ✅ | ✅ | No coincide con el de la portada. |
| 1 | Definición del problema | ⚠️ Parcial | ✅ | Tiene contexto y preguntas, pero **falta el rótulo "Definición del problema:" con el enunciado en cursiva**, que la plantilla exige como cierre obligatorio de la sección. No distingue el problema real del problema de conocimiento. |
| 2 | Delimitación del trabajo | ✅ | ✅ | Delimita espacio, tiempo y unidad de comparación. Faltan las dimensiones de **recursos** y **formación del investigador** que pide la plantilla. |
| 3 | Objetivos (3.1 y 3.2) | ✅ | ✅ | Ver §3: OE5 casi repite el objetivo general, OE1 y OE4 son actos y no procesos, y OE6 no cubre la hipótesis. |
| 4 | Hipótesis | ✅ | ✅ | Es incoherente con el alcance declarado y con los objetivos (§3). |
| 5 | Fundamentación | ✅ | ✅ | Sigue el esquema 2025 (justificación, revisión de literatura, pertinencia). **Falta la dimensión personal**, obligatoria en la plantilla. |
| 6 | Impacto de la investigación | ✅ | ✅ | Incluye los impactos individual, institucional, social y en la comunidad de investigación. **Falta el impacto ecológico**, obligatorio en la plantilla. No cuantifica nada, como piden las diapositivas 2025. |
| 7 | Marco teórico (7.1 y 7.2) | ✅ | ✅ | Ocupa **unas 16 páginas** frente a las ~3 de referencia. Desarrolla ideas propias del proyecto, lo que la plantilla prohíbe (§3.6). No teoriza el constructo central del objetivo: el **sistema o prototipo de soporte a la decisión**. |
| 8 | Método (8.1, 8.2 y 8.3) | ✅ | ✅ | Completo en forma. "Tipo de investigación" y "Enfoque" son párrafos sueltos sin numerar antes de 8.1. |
| — | Diagrama funcional y diagrama de flujo | ✅ | — | Figuras 1 y 2, con epígrafe y referencia cruzada en el texto. Correcto. |
| — | Cronograma en tabla con fecha de inicio | ✅ | — | Tabla 1: 16 quincenas, del 01/01/2027 al 31/08/2027. Correcto. |
| — | Tabla de operacionalización | ✅ | — | Tabla 2 con el esquema de 4 columnas de la plantilla. |
| — | Referencias bibliográficas | ✅ | ✅ | La [43] no está citada (§2). |

**No hay secciones fuera de orden.** El problema estructural no es el orden, sino el contenido obligatorio que falta dentro de las secciones 1, 2, 5 y 6.

### 1.3 Índice frente a cuerpo

El índice automático **no se actualizó** y no refleja el documento real:

| En el cuerpo | En el índice |
|---|---|
| 5. Fundamentación | **Falta** (salta de 4 a 6) |
| 8.1 Especificaciones de diseño y 8.1.1–8.1.10 | **Faltan** |
| 7.1.1.3.7 MOORA | **Falta** |
| 7.1.3.1.5 Contrataciones del PTI | **Falta** |
| 7.2.2 "…a decisiones informáticas" | Título truncado |

Para el lector, esto es lo primero que delata un documento sin revisión final. Se arregla con F9 sobre el índice, pero hay que hacerlo.

### 1.4 Requisitos administrativos (no verificables en el .docx)

- **ANEXO II**: no forma parte del archivo. Hay que confirmar que existe y está firmado.
- **ANEXO IV**: **es obligatorio en este proyecto.** La variable 11 y el OE6 prevén una "validación de expertos" con evaluadores del PTI, es decir, contacto con una institución externa (Art. 8). Si además se van a solicitar documentos al PTI que no sean públicos, con más razón. Para los datos del portal de la DNCP, que son públicos, hay que confirmarlo con la docente (pendiente (e) de mi síntesis).

---

## 2. Evaluación del formato IEEE

### 2.1 Uso de Word: es un riesgo que hay que confirmar

La plantilla oficial está en LaTeX y el programa pide "un procesador de texto científico". **No consta en ningún lugar que Word sea aceptable.** El documento está hecho en Word, así que hay que preguntárselo a la docente **antes** de invertir más en maquetación. Si exige LaTeX, la migración es mecánica, porque la estructura ya sigue la plantilla, pero conviene saberlo ya.

Dentro de Word, el archivo muestra estas debilidades de producción:

- **Ecuaciones:** la única ecuación (el modelo aditivo V(a), en 7.1.1.3.1) está escrita como texto plano con subíndices Unicode, no con el editor de ecuaciones de Word. No está numerada y se la cita como "la expresión de V(a)". La plantilla exige un entorno matemático, el número (n) a la derecha y la cita "Ec. n". La ecuación debe numerarse como Ec. 1 y citarse así en 7.1.2.4 y 7.1.2.7.
- **Epígrafes y referencias cruzadas escritos a mano**, sin campos SEQ ni REF. Cualquier inserción de una tabla o figura descuadra la numeración.
- **Tipografía mezclada:** el estilo Normal usa Arial 11, el valor por defecto del documento es Aptos 12, cientos de fragmentos están en 9,5 pt y la ecuación en Cambria Math. Ninguna regla de la FPUNE fija la fuente, pero la mezcla se nota.
- **Idioma del estilo Normal en inglés (en-US).** Por eso el corrector ortográfico no detectó errores como "¿En que medida…" o "los método" (ver M-3).
- **Cuerpo alineado a la izquierda**, no justificado como la salida de la plantilla. Es menor.
- Los **metadatos** del archivo muestran un autor ajeno a los graduandos. Conviene corregirlos antes de entregar.
- Página A4 y márgenes de 3/3/2,2/2 cm. No hay norma de la FPUNE que contradiga esto.

### 2.2 Citas en el texto

| Regla | Estado |
|---|---|
| Numeración por orden de primera aparición | ✅ **Perfecta**: del [1] al [42] en orden estricto. |
| Correspondencia 1:1 entre citas y referencias | ❌ La **[43]** (sitio de procesos del PTI) **no se cita en ningún lugar del texto**. |
| Un único número por fuente | ✅ No se repite el error de la plantilla (Sampieri con tres entradas). |
| Varias citas por separado ("[3], [6]") | ✅ Correcto. |
| Autor antes del corchete solo cuando hace falta | ⚠️ Se abusa de listar a todos los autores ("Cinelli, Kadziński, Gonzalez y Słowiński [10]", repetido unas cinco veces). Con más de dos autores, lo legible es "Cinelli *et al.* [10]". |
| Antecedentes identificados por el **título del artículo** ("El artículo “…” [8]") | ⚠️ No es un error IEEE, pero resulta monótono (11 veces) y omite autor y año, que la estructura de 4 partes del análisis de antecedentes pide para la identificación. |
| Sin cita de cita | ✅ No se detecta ninguna. |

### 2.3 Lista de referencias

**Lo que está bien:** el patrón dominante (unas 35 entradas) es IEEE correcto. Tiene iniciales con espacio, título del artículo entre comillas, revista abreviada en cursiva, "vol.", "no.", "pp." y "art. no.", meses abreviados en español, DOI resuelto y hasta 6 autores. Para un anteproyecto de grado, el nivel es alto.

**Defectos:**

1. **Dos patrones mezclados.** Las referencias [5], [35], [36] y [37] usan otra plantilla ("Autor. “Título”. sitio. URL (Accedido: …)"), distinta del "Accedido: …. [En línea]. Disponible en:" del resto. La [43] usa un tercer formato de fecha ("3 de noviembre de 2026" frente a "3-nov-2026"). En mi síntesis (§2.4) dejé dicho que hay que elegir **un patrón único**. Aquí no se hizo.
2. **Puntuación de títulos:** la coma va fuera de las comillas ("…approach”,"). El IEEE la pone dentro ("…approach,”). La [43] sí lo hace bien, lo que confirma la inconsistencia.
3. **DOI:** las guías piden, cuando hay DOI, solo "doi: 10.xxxx" y no "[En línea]. Disponible en: https://doi.org/…". Es menor, pero afecta a 34 entradas.
4. **[32] Ley 2051/2003: URL truncada** ("…/leyes-paraguayas/159/ley-"). La fuente no se puede verificar tal como está.
5. **[42] Dean:** copia el "año V" y el formato de la referencia de la plantilla, que en mi síntesis señalé como no IEEE. No tiene URL ni forma de acceso. Si no se consultó el original, es una cita heredada de la plantilla.
6. **[35] y [36] (ABC Color)** se usan para sostener una afirmación **jurídica**: que el PTI no se rige por la Ley 7021/2022. Un periódico no es fuente adecuada para eso. Hay que citar el Tratado de Itaipú, la normativa propia de compras de la FPTI o un dictamen de la DNCP. Además, el titular de [35] dice que los "datos siguen ocultos", lo cual **contradice** la premisa de que la documentación del PTI es de acceso público (ver I-7).
7. **[37] DNCP:** se declara que cubre solo los conjuntos de 2024 y 2025, mientras que el periodo de estudio es 2023–2026.
8. **Guiones:** "pp. 164-179" debería llevar raya corta ("164–179"). Es menor.
9. **Fechas de acceso posteriores a la fecha de la portada:** [5], [19], [35], [36] y [43] dicen "3-nov-2026", pero la portada está fechada el 2/11/2026. Es menor, pero un evaluador meticuloso lo verá.

> La existencia y la exactitud de cada referencia (volumen, páginas, DOI) corresponden a **citation-verifier-master**. No las he verificado una por una. Lo que sí afirmo es que el formato está mayormente bien y que la calidad de las fuentes es buena: son revisadas por pares en su mayoría (EJOR, J. Public Procure., JPSM, Omega).

### 2.4 Tablas y figuras

| Regla de la plantilla | Estado |
|---|---|
| "Tabla N:" con numeración arábiga y epígrafe **encima** | ✅ Tablas 1 y 2. |
| "Figura N:" con epígrafe **al pie** | ✅ Figuras 1 y 2. |
| Referencia cruzada en el texto | ✅ Las cuatro tienen referencia. |
| Numeración automática | ❌ Manual (ver 2.1). |

La tabla de contactos de la portada es una tabla sin epígrafe. Debería desaparecer en favor de las notas al pie.

---

## 3. Evaluación del rigor metodológico

### 3.1 Mapa de la cadena lógica tal como está

```
Problema (sin enunciado formal)
  └─ P. principal: ¿en qué medida un prototipo… [puede] apoyar la evaluación…?
       ├─ P1 (procedimientos, información, reglas) ──> OE1 (identificar licitaciones), OE2 (identificar reglas)
       ├─ P2 (métodos más apropiados) ──────────────> OE3 (comparar métodos)
       └─ P3 (implementar + evaluar + tiempo y errores frente a manual) ──> OE5 (implementar), OE6 (evaluar)
                                                     OE4 (definir herramientas): sin pregunta
OG: Desarrollar un prototipo web… ≈ OE5
Hipótesis: reducir tiempo + "seleccionar la mejor oferta" + transparencia + trazabilidad + objetividad
Método §8.0 y §8.1.10: "componentes de la hipótesis" = tiempo + errores + trazabilidad
Variables: 11; ninguna mide "transparencia", "objetividad" ni "mejor oferta"; la VI "modalidad" no está operacionalizada
```

### 3.2 Problema

- **Falta el enunciado formal en cursiva**: es CRÍTICO (C-1). La sección termina con las preguntas.
- **No distingue el problema real** (la evaluación manual es lenta, propensa a errores y poco trazable) **del problema de conocimiento** (qué método multicriterio representa adecuadamente las reglas de evaluación paraguayas, y si su automatización mejora la evaluación). La plantilla lo exige explícitamente.
- **No hay evidencia local del problema.** El problema real se apoya en una revisión genérica sobre errores en **hojas de cálculo** [7] y en literatura europea. No hay ningún dato, caso, informe de la DNCP ni protesta que muestre que en Paraguay la evaluación manual sea lenta o errónea. Además, [7] habla de planillas de cálculo, pero luego la modalidad manual del experimento usa **calculadora básica** (I-3). La evidencia y el diseño no hablan de lo mismo.
- **Pregunta principal:** está gramaticalmente rota (le falta un verbo conjugado, "puede") y su variable dependiente, "apoyar la evaluación", no se operacionaliza en ningún sitio.
- **P3 es una pregunta compuesta**: implementar, evaluar con tres propiedades y comparar tiempo y errores con la evaluación manual, todo en una oración. Viola el criterio de preguntas "enfocadas".

### 3.3 Objetivos

| Objetivo | Problema | Severidad |
|---|---|---|
| OG "Desarrollar un prototipo web…" | Es un objetivo de **producto**, no de investigación. No responde a la pregunta principal ("¿en qué medida…?"), que pide **evaluar**. Según objetivos-2025, le falta el "para qué". | Importante |
| OE1 "Identificar las licitaciones a ser abarcadas" | Es un **acto de muestreo**, no un proceso de conocimiento. Es una tarea. | Importante |
| OE4 "Definir las herramientas tecnológicas" | Es un **acto o decisión de diseño** de complejidad muy inferior a OE3 o a OE6. Rompe la exigencia de complejidad similar. | Importante |
| OE5 "Implementar un prototipo web…" | **Equivale al objetivo general** ("desarrollar" ≈ "implementar"). La plantilla prohíbe que un específico repita o eclipse al general. | **Crítico** |
| OE6 "Evaluar… escenarios controlados… validación de expertos" | **No incluye la comparación con la evaluación manual** ni el tiempo y los errores, que son el núcleo de la hipótesis y de P3. Incluye una "validación de expertos" que no tiene tareas, ni cronograma, ni método, ni estimador. Le falta un artículo ("y **la** validación…"). | **Crítico** |
| OE3 | En 3.2 dice "de **los** más adecuados" (plural); en la Tabla 2, "del más adecuado" (singular). El título dice "métodos" y el cuerpo, "un método". ¿Se implementa uno o varios? | Importante |

### 3.4 Hipótesis

Es el eslabón más débil del documento.

1. **Afirma lo que nadie mide.** "Seleccionar la mejor oferta", "transparencia" y "objetividad" no tienen variable, indicador ni tarea.
2. **Omite lo que sí se mide.** El método (§8.0 y §8.1.10) declara que los componentes de la hipótesis son el tiempo, los **errores** y la trazabilidad. La hipótesis no menciona los errores. El documento contradice su propia hipótesis.
3. **Contradice la delimitación y el marco teórico.** "Seleccionar la mejor oferta" choca con la delimitación ("no realizará adjudicaciones automáticas") y con 7.1.1.2 y 7.1.3.1.4, donde los propios autores sostienen que una clasificación multicriterio no demuestra cuál es la decisión correcta.
4. **Es incoherente con el alcance declarado.** El método dice que el alcance es **descriptivo**. Según Alcance-1-2025, un estudio descriptivo lleva hipótesis solo si pronostica un dato. Esta hipótesis es **causal y comparativa** ("permitirá reducir… comparándolos con los métodos manuales"), lo que corresponde a un alcance explicativo con diseño experimental o cuasi-experimental.
5. **Generaliza más de lo que el diseño permite.** Habla de "contrataciones públicas del Paraguay", pero el diseño usa dos evaluadores (los propios autores) y un muestreo intencional, y el propio §8.1.10 prohíbe extrapolar. Además, el PTI, que es parte de la muestra, **no** es contratación pública bajo la Ley 7021 (lo dice 7.1.3.1.5).

### 3.5 Tipo, alcance y diseño

- **Aplicada, con las etapas de Dean:** está bien declarada y fundamentada, y el mapeo de las etapas a los apartados 8.1.5–8.1.10 es correcto. Es de lo mejor del método.
- **"Descriptivo con diseño comparativo":** "diseño comparativo" no es una categoría de diseño en la tipología que enseña la cátedra (experimental frente a no experimental, transversal o longitudinal). Además, §8.1.1 describe "una comparación controlada de medidas repetidas" en la que "la modalidad de evaluación constituirá el factor de comparación". Eso es un **diseño intra-sujeto cuasi-experimental**, en el que se manipula la variable independiente "modalidad". Declararlo "descriptivo" y en parte "no experimental" es incoherente. Hay que nombrar el diseño por lo que es y asumir sus exigencias.
- **Validez interna de la comparación manual-automatizada:** es CRÍTICO (C-5).
  - **n = 2 evaluadores, que son los propios desarrolladores.** Conocen el sistema, los casos y los resultados esperados. El documento lo reconoce como limitación en §8.1.10, pero eso no lo convierte en un diseño válido para contrastar una hipótesis causal.
  - **Circularidad en los errores:** el prototipo se verifica contra los cálculos de referencia **antes** de las pruebas (§8.1.8), así que sus errores de cálculo serán ≈ 0 por construcción. Comparar eso con el cálculo manual no prueba nada que no se supiera.
  - **Circularidad en la trazabilidad:** la lista de comprobación la diseñan los mismos autores que diseñan el prototipo para cumplirla. Una ficha manual en papel no registra "operaciones necesarias para reconstruirlo" en el mismo sentido. El resultado está decidido de antemano.
  - **Hombre de paja:** la modalidad manual usa "calculadora básica". En la práctica real, y en la propia evidencia que citan [7], se usan hojas de cálculo. Comparar contra una calculadora infla artificialmente la diferencia de tiempo.
  - **Efecto de arrastre:** el mismo evaluador repite el mismo caso. Alternar el orden con dos personas no neutraliza el aprendizaje.
  - **Conclusión:** de los tres componentes, solo el **tiempo** es una medición genuina, y está contaminada por la familiaridad de los desarrolladores con su herramienta. La hipótesis es **prácticamente infalsable** tal como está diseñada.

### 3.6 La tensión conceptual no resuelta: pliego frente a comparación de métodos

Es el problema de fondo del proyecto.

1. El Decreto 2264/2024 (art. 59) exige ponderaciones relativas en el pliego, y el documento decide (7.1.2.5 y 8.1.4) que **las ponderaciones se tomarán del pliego y no se estimarán**.
2. Si el prototipo debe "configurar las reglas documentadas" (§8.1.6), entonces **el método ya lo fija el pliego**, que en la práctica será casi siempre una suma ponderada con fórmulas de puntuación.
3. En ese caso, la comparación de siete métodos (OE3) es **decorativa**: su resultado no puede cambiar lo que el prototipo implementa sin que este deje de reproducir la regla legal.
4. Si, por el contrario, el prototipo implementa el método "ganador" de OE3 (por ejemplo, MAVT con funciones de valor no lineales), **ya no aplica las reglas del pliego**. Entonces la comparación con la evaluación manual "de las mismas reglas" deja de comparar lo mismo, y el prototipo no sirve para la evaluación administrativa real.

El documento roza el problema en 7.1.3.1.3 (distingue la "representación del procedimiento documentado" de una "evaluación alternativa formulada con fines académicos"), pero **nunca dice cuál de las dos implementa el prototipo**, ni cuál se compara con la evaluación manual. Hay que resolverlo explícitamente. Lo más defendible es que el prototipo **reproduzca la regla del pliego** como modo principal y que la comparación de métodos sirva como **análisis de sensibilidad o contraste**. En ese caso, OE3 y la hipótesis deben reformularse en consecuencia.

Agravante: el marco teórico ya **anticipa el ganador** ("MAVT aditivo se perfila como el candidato…", en 7.1.2.8 y en el cierre de 7.2), lo que sesga una comparación que todavía no se hizo.

### 3.7 Marco teórico

- **Extensión desproporcionada:** unas 16 páginas frente a las ~3 de referencia de la plantilla. Junto con un método de unas 15 páginas, el documento llega a 44 páginas y ya no es una "hoja de ruta", sino un borrador del trabajo.
- **Desarrolla el trabajo dentro del PTFG**, lo que la plantilla prohíbe:
  - 7.1.2.7 **demuestra** la invariancia del modelo aditivo ("Esta demostración…").
  - 7.1.2.5 fija una decisión metodológica (no estimar pesos).
  - 7.1.2.8 formula una "hipótesis de trabajo" sobre el método ganador.
- **Contenido huérfano:** 7.1.2.5 (inferencia de preferencias), 7.1.2.6 (robustez), 7.2.3 (UTA-splines, medidas de expresividad) y las referencias [15], [20], [21] y [34] desarrollan la **estimación de funciones de valor a partir de decisiones históricas**, algo que el propio documento **descarta** en 7.1.2.5 y en 8.1.4. Es un vestigio de una versión anterior del proyecto y debe recortarse o justificarse.
- **Laguna central:** no hay ni una línea sobre **sistemas de soporte a la decisión**, prototipado, ingeniería de requisitos, trazabilidad en software, usabilidad ni comparación entre evaluación manual y automatizada. Son los constructos del **objetivo general** y de la **hipótesis**. El marco teórico cubre muy bien la mitad "multicriterio" y deja sin teoría la mitad "prototipo".
- **Evolución histórica cronológicamente engañosa:** empieza en 1979 y presenta ELECTRE como posterior a PROMETHEE (1985) y a AHP (1990), porque usa las fechas de los artículos citados en lugar del origen de cada método. ELECTRE es de finales de los años 60 y AHP de finales de los 70. Si la sección se titula "evolución histórica", tiene que respetar la historia.
- **Exceso de niveles:** llega a cinco (7.1.1.3.1, 7.1.3.1.1). La plantilla pide no abusar de los subniveles.
- **Antecedentes (7.2):** el orden cronológico dentro de 7.2.1 es correcto (2010 → 2022) y la estructura de 4 partes (identificación, resumen, aporte, diferenciación) se cumple razonablemente. Los defectos son tres:
  - Ningún antecedente trata **herramientas de software** de evaluación de ofertas (e-procurement, DSS), que es justamente lo que se va a construir.
  - 7.2.2 contiene un único antecedente, de 1999.
  - El cierre no contrasta el estado del conocimiento con **cada pregunta de investigación**, como pide la plantilla.
- **Antecedentes repetidos tres veces:** aparecen en la sección 1, en la "Revisión de literatura" de la Fundamentación y en 7.2. Es la contradicción C7 que señalé en el material de la cátedra; el documento cayó en ella.

### 3.8 Operacionalización

- **Variable 11 (validación de expertos): "Indicador: pendiente de definición"**, y en la Tabla 2 "pendiente de definición con el profesor". Es una variable sin estimador y, además, un **texto provisional dentro de un documento entregado**. CRÍTICO.
- **La variable independiente de la hipótesis ("modalidad": manual o automatizada) no figura** entre las variables.
- **Variables 1 y 4 son indicadores de gestión del proyecto**, no propiedades del fenómeno ("herramientas seleccionadas y documentadas" es un entregable). Es exactamente el error C12 del Ejemplo-operacionalización de la cátedra, que recomendé no imitar.
- **No hay clasificación** por naturaleza (cualitativa o cuantitativa, escala) ni por función (independiente o dependiente), aunque Operacionalización-25 la enseña.
- **Fila del OE6 en la Tabla 2:** agrupa seis variables y seis indicadores en una sola celda, así que el estimador deja de ser unívoco por variable. Debe desagregarse en una fila por variable.
- **Mapeo tarea-objetivo erróneo:** la Tabla 2 asigna la tarea 5 al OE4 ("definir herramientas"), pero la tarea 5 contiene la demostración de propiedades y el análisis de sensibilidad (5.2–5.4), que son trabajo del OE3, y el diseño de requisitos, arquitectura, base de datos e interfaz (5.5–5.8), que **no corresponde a ningún objetivo**. Falta un objetivo de diseño o el OE4 está mal formulado.

### 3.9 Tareas y cronograma

- Las tareas empiezan con sustantivo, están numeradas en dos niveles y siguen un orden cronológico. ✅
- El cronograma tiene fecha de inicio y fin y 16 quincenas consistentes con enero–agosto de 2027. ✅
- La "validación de expertos" no tiene **ninguna tarea**, aunque esté en el OE6 y en la variable 11. ❌
- La subtarea 10.5, "Redacción de los resultados… y conclusiones", es la redacción del libro, que ya está regulada. objetivos-2025 la desaconseja como objetivo; como tarea es tolerable, pero sobra. Es menor.
- **Viabilidad:** solo quedan 2 meses (quincenas 9–12) para desarrollar y verificar el prototipo, y no hay ningún análisis de recursos. La plantilla no lo exige como sección, pero la cátedra lo enseña.

### 3.10 Delimitación

- "Distintos sectores y objetos de contratación" es **no delimitar**. Sumado a que "la cantidad definitiva de casos se establecerá después", hoy el evaluador no puede juzgar la factibilidad.
- **Mezclar la DNCP (Ley 7021) con el PTI (régimen propio)** en un solo estudio duplica el marco normativo y debilita la hipótesis, que habla de "contrataciones públicas del Paraguay". Hay que justificar por qué se incluye al PTI. La única pista es la referencia [43], que no está citada, y la validación con expertos del PTI. O se explica esa razón o se acota el estudio a un solo régimen.
- La cobertura de los datos abiertos de la DNCP citada ([37]) no abarca 2023 ni 2026.

---

## 4. Hallazgos priorizados

### CRÍTICOS (cada uno es motivo para no aprobar)

**C-1. Falta el enunciado formal del problema.**
- *Ubicación:* final de la sección 1.
- *Qué está mal:* la sección termina con las preguntas, sin el rótulo "Definición del problema:" y el enunciado en cursiva.
- *Por qué:* la plantilla lo exige como cierre obligatorio. Sin él no hay un ancla para el objetivo general ni para el título.
- *Corrección:* redactar 2–3 líneas en cursiva que formulen el **problema de conocimiento** y relacionen al menos dos variables (Kerlinger). Por ejemplo: la ausencia de evidencia sobre qué procedimiento multicriterio representa fielmente las reglas de los pliegos y si su automatización reduce el tiempo y los errores frente a la evaluación habitual. Separarlo explícitamente del problema real.

**C-2. La hipótesis no se corresponde con los objetivos, las variables ni el método.**
- *Ubicación:* sección 4 frente a §8.0 (Enfoque), §8.1.10 y 8.3.
- *Qué está mal:* la hipótesis promete "seleccionar la mejor oferta", "transparencia" y "objetividad", que nadie mide, y omite los "errores", que el método sí trata como componente de la hipótesis.
- *Por qué:* rompe la cadena hipótesis → variables → estimadores y contradice la delimitación (no hay adjudicación automática).
- *Corrección:* reescribirla con los tres componentes medibles (tiempo, errores, trazabilidad), cada uno con su dirección esperada, el contexto exacto (casos seleccionados de la DNCP o del PTI) y sin "mejor oferta" ni "objetividad".

**C-3. El OE5 repite el objetivo general.**
- *Ubicación:* 3.1 frente a 3.2, ítem 5.
- *Qué está mal:* "Desarrollar un prototipo web…" y "Implementar un prototipo web…" son el mismo objetivo.
- *Por qué:* la plantilla prohíbe que un específico eclipse al general.
- *Corrección:* reformular el OG para que responda a la pregunta principal, por ejemplo "Evaluar en qué medida un prototipo… mejora…", y dejar OE5 como el proceso de construcción. Si el OG sigue siendo "desarrollar", el OE5 debe acotarse a un componente concreto, como el motor de evaluación trazable.

**C-4. El OE6 no cubre la comparación con la evaluación manual e incluye una validación de expertos sin método.**
- *Ubicación:* 3.2, ítem 6; Tabla 2; variable 11; lista de tareas.
- *Qué está mal:* la comparación de tiempo y errores frente a la evaluación manual, que es el núcleo de P3 y de la hipótesis, no está en ningún objetivo. La "validación de expertos" no tiene tareas, cronograma, procedimiento ni estimador.
- *Corrección:* separar dos objetivos: (a) verificar la corrección, la reproducibilidad y la trazabilidad, y (b) comparar el tiempo y los errores con la evaluación habitual. Para la validación de expertos, o se define completa (quiénes, cuántos, instrumento como SUS o una escala Likert de adecuación, tareas, quincena en el cronograma y **ANEXO IV**) o se elimina.

**C-5. El diseño de la comparación manual-automatizada no puede contrastar la hipótesis.**
- *Ubicación:* §8.1.1, §8.1.8–8.1.10; tareas 8–9.
- *Qué está mal:*
  - Hay dos evaluadores y son los propios desarrolladores.
  - Los errores del prototipo valen ≈ 0 por construcción, porque se verifica antes.
  - La trazabilidad se mide con una lista hecha a la medida del prototipo.
  - La modalidad manual usa calculadora básica en lugar de una hoja de cálculo.
  - El mismo evaluador repite el mismo caso.
- *Por qué:* el resultado está determinado por el diseño. La hipótesis es infalsable y el diseño se declara "descriptivo" cuando en realidad es cuasi-experimental.
- *Corrección (mínimo exigible):*
  - Llamar al diseño por su nombre (cuasi-experimental intra-sujeto).
  - Usar como comparador realista una **hoja de cálculo**, que es la práctica habitual.
  - Incorporar evaluadores **ajenos al desarrollo**: compañeros de la carrera con una consigna estandarizada, o personal de compras con el ANEXO IV.
  - Medir los errores también en el prototipo **durante la carga por un usuario** (transcripción y configuración), no solo los del motor ya verificado.
  - Si nada de lo anterior es viable, **bajar la hipótesis** a una de factibilidad técnica: "siguiendo el método X se obtiene un prototipo que reproduce correctamente…", que es la formulación que la plantilla admite para la investigación aplicada.

**C-6. Hay una variable sin estimador y texto provisional en el documento entregado.**
- *Ubicación:* 8.3, variable 11; Tabla 2, fila del OE6.
- *Qué está mal:* "pendiente de definición" y "pendiente de definición con el profesor".
- *Por qué:* es una variable sin estimador (está en la escala crítica) y, además, un texto provisional que un evaluador lee como documento inacabado.
- *Corrección:* definir el estimador o eliminar la variable junto con la mención en el OE6.

**C-7. La tensión entre la regla del pliego y el método seleccionado no está resuelta.**
- *Ubicación:* 7.1.2.5, 7.1.3.1.3, 8.1.4 y 8.1.6; OE3 y la hipótesis.
- *Qué está mal:* si las ponderaciones y las reglas vienen del pliego, el método ya está fijado y OE3 no decide nada. Si el prototipo implementa el método ganador, deja de aplicar las reglas del pliego y la comparación con la evaluación manual "de las mismas reglas" pierde sentido.
- *Corrección:* declarar en §8.1.4 qué implementa el prototipo. Mi recomendación es que reproduzca fielmente la regla del pliego como modo principal y ofrezca los métodos alternativos como análisis de contraste o sensibilidad. Después, reformular OE3, P2 y el título en consecuencia, y eliminar del marco teórico el veredicto anticipado a favor de MAVT.

### IMPORTANTES

| ID | Ubicación | Qué está mal | Por qué | Corrección |
|---|---|---|---|---|
| I-1 | Secc. 5 | Falta la fundamentación **personal**. | Es una de las tres dimensiones obligatorias de la plantilla. | Añadir un párrafo con la motivación y la relación de los autores con el tema; si es la relación con el PTI, decirlo. |
| I-2 | Secc. 6 | Falta el impacto **ecológico**; nada está cuantificado. | La plantilla exige el ecológico; las diapositivas 2025 piden cuantificar. | Añadir el impacto ecológico (despapelización, expedientes digitales) con alcance honesto, y estimar al menos un orden de magnitud: llamados por año en la DNCP, horas por evaluación. |
| I-3 | Secc. 1 y 5 | No hay evidencia **local** del problema real; [7] trata de hojas de cálculo, pero el comparador es una calculadora. | El problema no está demostrado en el contexto delimitado. | Aportar datos de la DNCP (volumen de llamados con evaluación por puntos, protestas por errores de evaluación) y alinear el comparador con la evidencia. |
| I-4 | Secc. 7 | El marco teórico ocupa ~16 páginas, incluye una demostración propia y una hipótesis de trabajo, y contiene material huérfano (inferencia y UTA). | La plantilla prohíbe desarrollar ideas propias en el marco teórico y fija ~3 páginas de referencia. | Recortar a unas 5–6 páginas como máximo, trasladar las demostraciones al TFG y eliminar 7.1.2.5, 7.1.2.6 y 7.2.3, o justificarlos. |
| I-5 | Secc. 7 | No hay teoría sobre **sistemas de soporte a la decisión**, prototipado, trazabilidad de software ni usabilidad. | Son los constructos del objetivo general y de la hipótesis. | Añadir un eje 7.1.x con al menos dos definiciones de DSS de autores distintos más una síntesis propia, e incluir antecedentes de herramientas de software de evaluación de ofertas. |
| I-6 | 3.2 (OE1, OE4) | Son actos o entregables, no procesos; su complejidad es desigual a la de OE3 y OE6. | Lo prohíbe la plantilla. | Convertir OE1 en tarea; convertir OE4 en "Diseñar el prototipo (requisitos, arquitectura, herramientas)" para que cubra también la tarea 5. |
| I-7 | Secc. 2, 7.1.3.1.5; [35], [36] | La inclusión del PTI no está justificada; su régimen jurídico se sustenta en notas de prensa; [35] indica que los datos están ocultos. | Afecta a la validez, a la viabilidad del acceso a datos y a la generalización de la hipótesis. | Justificar la inclusión del PTI con fuente normativa primaria y confirmar el acceso real a los documentos, o acotar el estudio a la DNCP. |
| I-8 | Tabla 2 | La tarea 5 está mapeada al OE4 aunque contiene trabajo del OE3 y diseño sin objetivo; la fila del OE6 agrupa seis variables. | Se rompe la trazabilidad OE–Tarea–Variable y el estimador deja de ser unívoco. | Remapear y desagregar en una fila por variable. |
| I-9 | 8.3 | Falta la VI "modalidad"; las variables 1 y 4 son de gestión; no hay clasificación por tipo, escala ni función. | Error C12 del material de la cátedra; la cadena está incompleta. | Añadir la VI, reformular o eliminar las variables 1 y 4 y clasificar todas. |
| I-10 | Método, "Tipo" | Declara "descriptivo con diseño comparativo", categoría que no existe en la tipología de la cátedra, y lo contradice con un diseño controlado de medidas repetidas. | Incoherencia entre alcance, diseño e hipótesis (contradicción C2 de mi síntesis). | Ver C-5. |
| I-11 | Portada y cuerpo | El título no es el mismo en la portada y en el cuerpo, y no deriva del objetivo general. | La plantilla dice que el OG engendra el título. | Unificar, por ejemplo: "Prototipo web de soporte a la decisión multicriterio para la evaluación de ofertas en licitaciones de Paraguay (2023–2026)". |
| I-12 | Secc. 1, 5 y 7.2 | Los mismos antecedentes se presentan tres veces. | Es la contradicción C7; infla el documento. | En la sección 1, un contexto breve; en la 5, solo la pertinencia; el análisis completo, solo en 7.2. |
| I-13 | Secc. 2 | No hay límite de sectores ni de número de casos; faltan los límites de recursos y de formación del investigador. | La factibilidad no se puede evaluar. | Fijar un rango de casos (mínimo y máximo) y, si es posible, una tipología de objetos de contratación. |
| I-14 | Índice | Desactualizado: faltan 5, 8.1–8.1.10, 7.1.1.3.7 y 7.1.3.1.5. | Es lo primero que ve el evaluador. | Actualizar el campo con F9 y convertir "Tipo" y "Enfoque" en subtítulos numerados. |
| I-15 | Refs. [5], [35]–[37], [43] | Tres patrones de referencia distintos. | La guía exige consistencia. | Unificar en "Autor, “Título,” *Sitio*. Accedido: dd-mmm-aaaa. [En línea]. Disponible en: URL". |
| I-16 | Ref. [43] | Referencia sin cita. | Rompe la correspondencia 1:1. | Citarla donde corresponda (delimitación o 8.1.2) o eliminarla. |
| I-17 | Ref. [32] | URL truncada. | La fuente no se puede verificar. | Completar la URL. |
| I-18 | 3.2 frente a Tabla 2 | El OE3 dice "los más adecuados" en un lugar y "el más adecuado" en otro. | Ambigüedad sobre cuántos métodos se implementan. | Decidir uno y unificar en el título, la pregunta 2, el OE3, la hipótesis y la Tabla 2. |

### MENORES

| ID | Ubicación | Hallazgo | Corrección |
|---|---|---|---|
| M-1 | 7.1.1.3.1 | La ecuación está escrita como texto plano, sin número, y se cita como "la expresión de V(a)". | Usar el editor de ecuaciones, numerarla (1) y citarla como "Ec. 1". |
| M-2 | Portada | Los contactos van en una tabla, sin notas al pie y sin el del Orientador. | Poner las notas al pie según la plantilla. |
| M-3 | Secc. 1 y método | Errores tipográficos: "¿En que medida… apoyar" (falta tilde y verbo), "los método", espacios dobles ("establecido   en", "contrastar  métodos"), "Itaipu"/"Itaipú" alternados. El estilo Normal tiene el idioma en inglés, por eso el corrector no los marcó. | Cambiar el idioma del documento a español y repasar. |
| M-4 | 7.1.1.1 | La cronología histórica es engañosa: ELECTRE y AHP aparecen como posteriores a PROMETHEE. | Fechar cada método por su origen y citar la fuente original o una revisión histórica. |
| M-5 | 7.1 | Hay cinco niveles de subtítulos. | Aplanar a cuatro como máximo. |
| M-6 | 7.2 | Los antecedentes se identifican por el título del artículo en lugar de por autor y año. | "Mateus *et al.* [8] (2010) analizan…". |
| M-7 | Texto | Se listan todos los autores en cada mención. | Usar *et al.* cuando hay más de dos. |
| M-8 | Referencias | La coma va fuera de las comillas; el DOI va como URL; "pp." lleva guion en lugar de raya. | Ajustarlo al patrón IEEE. |
| M-9 | Referencias | Hay accesos con fecha 3-nov-2026, posterior a la de la portada (2-nov-2026). | Unificar las fechas. |
| M-10 | Ref. [42] | Dean conserva el formato de la plantilla ("año V") y no tiene forma de acceso. | Verificar la fuente original y completarla. |
| M-11 | Tipografía | Se mezclan Arial, Aptos y Cambria Math y tamaños de 9,5, 11 y 12 pt; el texto está alineado a la izquierda. | Unificar estilos. Como no hay norma de la FPUNE, al menos que sea coherente. |
| M-12 | Epígrafes | Están escritos a mano, sin campos. | Usar Insertar título y Referencia cruzada. |
| M-13 | Tarea 10.5 | Incluye la redacción del libro. | Eliminarla o fundirla en "Análisis…". |
| M-14 | Metadatos | El autor del archivo no corresponde a los graduandos. | Corregirlo en Propiedades antes de entregar. |
| M-15 | General | No hay ninguna consideración ética sobre la participación de evaluadores o expertos. | Añadir el consentimiento informado si se incorporan participantes externos. |

---

## 5. Fortalezas reales

No diluyen lo anterior, pero son reales y conviene conservarlas:

1. **Bibliografía de calidad.** Más de 35 de las 43 fuentes son artículos revisados por pares en revistas de referencia (EJOR, J. Public Procure., JPSM, Omega), con DOI. Para un anteproyecto de grado, este nivel es excepcional y está muy por encima de los ejemplos de la propia plantilla.
2. **Numeración IEEE impecable.** Del [1] al [42] en orden estricto de aparición, con un número por fuente y sin citas de cita.
3. **Tareas bien formuladas.** Empiezan con sustantivo, están numeradas en dos niveles y en orden cronológico, y tienen detalle operativo. Es exactamente lo que pide la plantilla, que muchos ejemplos de la cátedra incumplen.
4. **El cronograma cumple:** tiene fecha de inicio, unidad temporal explícita y no incluye tareas del PTFG.
5. **Tiene los dos diagramas recomendados:** el funcional y el de flujo, con epígrafe y referencia cruzada correctos.
6. **La investigación aplicada está bien fundamentada,** con las etapas de Dean mapeadas a los apartados del método.
7. **Precisión conceptual poco común:**
   - Distingue los requisitos de admisibilidad de los criterios puntuables.
   - Distingue la clasificación matemática de la adjudicación administrativa.
   - Separa la propiedad demostrada de la comprobación empírica.
   - Advierte que la interpretación de los pesos depende de la regla de agregación.
   - Trata la inversión de orden.

   Revela una comprensión genuina del dominio multicriterio.
8. **Control de calidad de los datos:** extracción por un investigador y verificación por el otro, conservación de los valores originales, prohibición explícita de imputar por suposición y registro de los casos excluidos con su motivo.
9. **La unidad de análisis está bien definida:** el conjunto de ofertas que compiten por la misma unidad de adjudicación.
10. **Las limitaciones están reconocidas,** aunque el diseño no las resuelva: aprendizaje, participación de los desarrolladores, muestreo intencional, separación entre DNCP y PTI y entre casos reales y simulados.
11. **Los antecedentes de 7.2.1 están en orden cronológico** y siguen razonablemente la estructura de 4 partes.
12. **Redacción en futuro,** consistente en las secciones donde corresponde.

---

## 6. Preguntas para la docente antes de la próxima iteración

1. ¿Se acepta Word o el PTFG debe entregarse en LaTeX con la plantilla `ptfg_ieee`?
2. ¿Es aceptable un marco teórico de esta extensión, o se exige rigurosamente el orden de 3 páginas?
3. ¿Se exige el ANEXO IV por usar documentación pública de la DNCP y del PTI, o solo si hay contacto con personas o entidades?
4. ¿Qué esquema de tabla de operacionalización se quiere: el de 4 columnas de la plantilla o el de 6 columnas de 2025?
5. Para la hipótesis de una investigación aplicada, ¿se acepta una hipótesis de factibilidad técnica en lugar de una comparativa con la evaluación manual?
