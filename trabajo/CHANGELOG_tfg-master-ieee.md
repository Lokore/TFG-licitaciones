# CHANGELOG: tfg-master-ieee

# CONSULTA DEL ESTUDIANTE (17/11/2026): ¿"Definición del problema" está duplicado?

**Conclusión:** el patrón estructural es correcto y no es un error. Lo que sí había era una duplicación de contenido real, aunque menor, en el párrafo 4 de la sección 1. Ya la corregí en el markdown.

**Ocurrencias en `anteproyecto_borrador.md`:** las conté con búsqueda sin distinguir mayúsculas. Son exactamente 3:
1. **Línea 31, entrada del índice** "1. Definición del problema". En el .docx no se usa este texto: tfg-format-ieee lo sustituye por un campo TOC (`TOC \o "1-4"`), que genera la entrada a partir del título. Este índice estático solo vive en el markdown.
2. **Línea 82, título de la sección 1** (`# 1. Definición del problema`). La plantilla `ptfg_ieee.pdf` lo trae con ese mismo nombre, en `ptfg_ieee_texto.txt` líneas 23 (índice) y 45 (cuerpo).
3. **Línea 97, rótulo de cierre** "**Definición del problema:**" seguido del enunciado *en cursiva*. Es obligatorio según la plantilla, líneas 58–61: "Esta sección debe concluir enunciando concreta y explícitamente el problema de investigación, así: *Definición del problema:* [enunciado en cursiva]". La plantilla repite el nombre de la sección como rótulo a propósito. Quitarlo incumpliría la plantilla.

No hay otra repetición: el título no aparece en otro lugar del cuerpo y el enunciado formal aparece una sola vez. El título del trabajo también se repite (portada, línea 13, y línea 81, antes de la sección 1), pero eso también lo pide la plantilla, línea 43.

**Duplicación real corregida (párrafo 4 de la sección 1, "Conviene distinguir dos planos…"):** en la ronda 1 yo mismo añadí la distinción entre problema real y problema de conocimiento. La última oración ("El problema de conocimiento… consiste en determinar si un prototipo web que aplique de forma trazable la regla y las ponderaciones fijadas en el pliego de cada licitación reduce el tiempo y los errores de cálculo y mejora la trazabilidad respecto de la evaluación manual, y en qué medida la clasificación resultante cambia…") repetía casi palabra por palabra el enunciado formal de la línea 97, unas diez líneas más abajo. En la práctica, el problema quedaba enunciado dos veces dentro de la sección. Es probable que el estudiante haya percibido esto como "duplicado". La plantilla exige distinguir los dos planos para no confundirlos, pero no pide anticipar el enunciado.
- **Cambio:** reemplacé esa oración por una caracterización breve del problema de conocimiento: falta de evidencia sobre los efectos de automatizar de forma trazable la evaluación de cada pliego y sobre la dependencia de la clasificación respecto del método de agregación. Añadí una remisión: "Su enunciado formal se presenta al cierre de esta sección". La distinción real/conocimiento se conserva (C-1 de la ronda 1) y el PENDIENTE de evidencia local no cambia.
- **No toqué:** el título, el rótulo, el enunciado en cursiva, las preguntas ni el índice.

**Limitación de la verificación del .docx:** en esta consulta no tuve shell para descomprimir el `.docx`. No lo abrí directamente. Lo verifiqué de forma indirecta:
- `md_to_docx_v2.py` convierte `#` en Heading y el resto en Normal.
- El CHANGELOG de tfg-format-ieee (secciones 1.8 y RONDA 2 §4) registra que eliminó las líneas del índice estático y las sustituyó por un único campo TOC.
- El recuento de párrafos que informa (350) concuerda con esa eliminación. Si el índice estático hubiera quedado junto al campo, serían unos 38 más.
- El rótulo de la línea 97 es un párrafo Normal (negrita + cursiva), no un Heading, así que no puede aparecer en el TOC.

**Pendiente para tfg-format-ieee:** regenerar el `.docx` desde el markdown actualizado. Después, en Word, F9 sobre el índice, confirmando que "1. Definición del problema" figura una sola vez.

# RONDA 2 (17/11/2026): devolución real de la profesora (GB1–GB24, nota 77,05/100)

**Fuente:** comentarios de `C:/TFG/Anteproyecto_licitaciones_Ivan_Alex-verificado.pdf`, extraídos en `C:/TFG/trabajo/verificado_texto.txt`. Allí está el texto **completo** de cada comentario y su página de anclaje. Las páginas que cito son del PDF; la numeración impresa es la del PDF menos 2.
**Método:** ediciones puntuales con Edit. No reescribí el archivo entero. No toqué la lista de referencias, el formato de las citas, ni las secciones 2, 5, 6, 7.1.1–7.1.3 ni 8.1.3–8.1.11, salvo lo que se indica abajo.

## 0. Correcciones al encargo (el texto fuente dice otra cosa)
1. **GB5 y GB6 corresponden a los OBJETIVOS ESPECÍFICOS 1 y 4, no a las tareas.** Están anclados en la página 6–7 del PDF, junto a los objetivos originales "1. Identificar las licitaciones…" y "4. Definir las herramientas tecnológicas…". La numeración "1-" y "4-" coincide con esos objetivos. Apliqué el texto literal a OE1 y OE4. Además reorganicé la lista de tareas para que la tarea *n* derive del OE *n*, así que las tareas 1 y 4 también llevan ese texto literal. Se cumplen las dos lecturas.
2. **GB7 y GB8 están en la página 7 del PDF (Hipótesis y comienzo de la Fundamentación), no en el marco teórico.** GB7 ("Escribir en presente: …reduce") remite a la hipótesis original "permitirá reducir…".
3. **GB24 tiene cinco ítems, no tres:** precisión de los cálculos, consistencia de resultados (reproducibilidad), nivel de trazabilidad, duración de la evaluación y frecuencia de errores. Los cinco son nombres propuestos para las variables del OE6.
4. **GB19–GB23 son nombres propuestos para las variables de los OE1–OE5**, anclados en la columna "Variable" de la Tabla 2. No son variables nuevas.
5. **GB2 y GB3 están completos en el PDF; no se cortan.** GB3 propone cuatro preguntas específicas literales.
6. **GB1** ("Titulo agregar: Ing. MSc."): lo más probable es que se refiera al **título de la propia profesora**, que en la portada figura como "Lic. Gabriela Matilde Bobadilla de Almada". El Orientador ya tiene título ("Ing. Mag."). Ver la sección 3.

## 1. Lo que resolví (por comentario)

| GB | Ubicación actual | Cambio |
|---|---|---|
| GB2 | §1, pregunta principal | Adopté el texto literal de la profesora. Solo inserté "en términos de tiempo, errores de cálculo y trazabilidad" para enlazar con H2 y las variables 10–12. |
| GB3 | §1, preguntas secundarias | Adopté las 4 preguntas literales con adaptaciones mínimas. **P1** quedó literal. **P2:** "representar **y contrastar** … **con las ponderaciones fijadas en cada pliego**". **P3:** "el método seleccionado" pasó a "un prototipo web que aplique la regla documentada en cada pliego y los métodos seleccionados". **P4:** quité la palabra "**significativas**", porque el análisis es descriptivo, con n de 5 a 10 expertos y Wilcoxon solo complementario (8.1.11); prometer significación estadística sería incoherente con el diseño. También cambié "tiempo de ejecución" por "tiempo de evaluación", añadí la trazabilidad y la valoración de los expertos (H2, H3). La síntesis de antecedentes (final de 7.2) sigue respondiendo P1–P4 en orden. |
| GB2 (alineación) | §3.1, objetivo general | Lo reformulé con el vocabulario de GB2 ("prototipo web de soporte a la decisión basado en análisis multicriterio para la evaluación comparativa de ofertas en procesos de licitación pública en Paraguay … frente a los métodos manuales tradicionales"). Mantiene el qué, el cómo y el para qué. |
| GB5 | §3.2 OE1, tarea 1 y Tabla 2 | Texto literal. |
| GB6 | §3.2 OE4, tarea 4 y Tabla 2 | Texto literal. La especificación de procedimientos y propiedades, que antes estaba en OE4, pasa a **OE3** ("analizando su compatibilidad, sus propiedades y las clasificaciones…"), en coherencia con GB21. OE5 se reformuló con "Implementar…" (verbo del original) y "precisión" (GB24). |
| GB7 | §4, H1–H3 y párrafo de cierre | Todo en presente: "reproduce", "**reduce** el tiempo", "presenta", "alcanza", "valoran", "otorga", "se contrasta", "corresponde". |
| GB8 | §4, párrafo nuevo tras H3 | Añadí el fundamento de las hipótesis sin citas, para no alterar el orden de primera aparición, porque la sección 4 va antes de la 5. Remite a los apartados 5 y 7.1.3, y al 8.1.11 para el umbral de H3. **Ambigüedad:** "Justificar…" también puede ser una nota de alineación, igual que GB4; lo dejo anotado para tfg-format-ieee. |
| GB11 | 7.2 | Eliminé los subtítulos 7.2.1, 7.2.2 y 7.2.3. Los antecedentes quedan bajo 7.2 con una frase de orden inicial, una transición ("En el ámbito de las decisiones informáticas…") y un cierre sin título ("En síntesis…"). No reordené para no forzar una renumeración. Actualicé el índice. |
| GB12 | 7.1.2.4 | Eliminé el párrafo sobre la línea de inferencia de pesos (UTA, regresión ordinal, UTA-splines, expresividad y robustez), que equivale a la antigua 7.2.3 de la página 25 del PDF señalada por la profesora. Era contenido que el propio texto declaraba que no se usaría. **Consecuencia:** quedan sin citar [34], [35], [36] y [37] (ver la sección 2). |
| GB13 (contenido) | 8.1.1 | Eliminé el párrafo "Conforme a la metodología… de Peffers et al. [50]…". Las fases son ahora propuesta propia, sin cita, en 8.1.2. **Consecuencia:** [50] queda sin citar. |
| GB14 + GB15 | 8.1.1 y 8.1.2 | 8.1.1 pasa a llamarse "**Tipo, enfoque y alcance de la investigación**" (igual que el criterio de la rúbrica, que tuvo 6/6). Lo sinteticé en tres párrafos breves: tipo, enfoque y alcance por componente, con el tratamiento de datos. Eliminé la descripción del I+D, redundante con la Delimitación y con 8.1.7. Todo lo que es diseño (componentes, diseño no experimental o cuasi-experimental, VI/VD, aleatorización, temporalidad) pasa a **8.1.2 "Diseño de la investigación"**. La numeración 8.1.3–8.1.11 no cambia, así que ninguna referencia cruzada se rompe. |
| GB16 | 8.1.2, 8.2 y Tabla 1 | Antes, el diseño hablaba de "componentes" y "actividades DSRM", y la lista de tareas de "fases": era confuso. Ahora 8.1.2 define **cinco fases** (I Documental, II Comparación metodológica, III Desarrollo tecnológico, IV Evaluación con expertos, V Comunicación). Cada fase indica sus OE, tareas, hipótesis y producto. La lista de tareas usa esas mismas fases como rótulos de grupo, en cursiva y sin numerar. Las tareas se numeran 1–7 con subtareas, y la tarea *n* corresponde al OE *n*. |
| GB17 | 8.1.2 | Añadí la **Figura 1: Fases del diseño de la investigación**, con la especificación completa del diagrama en un comentario HTML. **No pude generar la imagen;** hay que crearla (ver la sección 3). El diagrama funcional pasa a ser la **Figura 2** (texto y pie actualizados). **Eliminé** el antiguo "diagrama de flujo de las tareas", que estaba desactualizado y quedaba redundante con la Figura 1 y la Tabla 1. |
| GB18 | 8.2 y Tabla 1 | **La lista y el cronograma coinciden 1:1:** 7 tareas y 27 subtareas, 34 filas en total, con la misma numeración. Cada subtarea empieza con una denominación corta, que es la que aparece en el cronograma. El encabezado muestra los **meses**: Ene. Q1 … Ago. Q2 (inicio 01/01/2027, cierre 31/08/2027), con la nota Q1 = días 1–15 y Q2 = del 16 a fin de mes. Comprobé que las 34 filas tienen 17 columnas. La preparación de expertos (6.1, Q10–Q11) se solapa con la Fase III, como dice 8.1.2. |
| GB19–GB23 | 8.3 y Tabla 2 | Renombré las variables: 1 → "Completitud documental de las licitaciones"; 2 → "Parámetros y reglas de evaluación"; 3 → "**Compatibilidad y comportamiento del método multicriterio**" (fusiona las antiguas 3 "Adecuación" y 5 "Propiedades", como en el original que obtuvo 100 %); 5 → "Cobertura técnica de las herramientas" (con el estimador adaptado a requisitos técnicos); 6 → "Operatividad funcional del prototipo web". La variable "Concordancia de las clasificaciones" se mantiene aparte (4), porque mide la comparación de clasificaciones de OE3. |
| GB24 | 8.3 y Tabla 2 | 7 → "Precisión de los cálculos"; 8 → "Consistencia de resultados (reproducibilidad)"; 10 → "Duración de la evaluación"; 11 → "Frecuencia de errores de cálculo" (el estimador incluye la cantidad); 12 → "Nivel de trazabilidad". Total: **13 variables** (antes 14). La Tabla 2 mapea ahora "Tarea *n* (subtareas…)" ↔ OE *n*, y los textos de OE3 y OE6 son idénticos a los de §3.2. En 8.1.11 cambié "corrección" por "precisión de los cálculos" y "reproducibilidad" por "consistencia de los resultados (reproducibilidad)". |

**Otros ajustes de coherencia:** H1 remite a 8.1.2 (antes a 8.1.1). En 7.1.4, "tarea 1.2" pasó a "tarea 1.1". En la tarea 3.1, los criterios de la matriz remiten a 8.1.5, y en la 1.3, los requisitos remiten a 8.1.3.

## 2. Para citation-verifier-master
1. **GB9 y GB10 (error sistemático; la profesora escribió "CONSIDERAR PARA TODAS LAS CITACIONES").** Ubicación original: página 8 del PDF (página impresa 6), §5 Fundamentación, párrafo "Revisión de literatura". GB9 corresponde a "**Anelli, Morano, Acquafredda y Tajani [6] revisaron 74 estudios publicados entre 1998 y 2023…**". GB10 corresponde a otra cita del mismo párrafo con la misma forma: "Schotanus, van den Engh, Nijenhuis y Telgen [4]", "Guitouni y Martel [13] y Cinelli, Kadziński, Gonzalez y Słowiński [10]" o "Mateus, Ferreira y Carreira [8]". Esa frase ya no existe en el borrador (la condensé en la ronda 1), pero **el patrón sigue en todo el cuerpo**:
   - §6, impacto institucional ("como señalan Mateus, Ferreira y Carreira [9]");
   - 7.1.1.1–7.1.1.3, con listas completas de 3 a 5 autores;
   - 7.1.2.1–7.1.2.3 ("La República del Paraguay [32], en el artículo…", "Schotanus, van den Engh, Nijenhuis y Telgen [4]");
   - 7.1.3;
   - **todo 7.2**, donde además cada antecedente lleva "**[n] (año)**". **Ese "(año)" lo introduje yo en la ronda 1 y no es IEEE:** hay que eliminarlo. Si se quiere conservar la cronología, puede escribirse en prosa ("En 2010, Mateus et al. [9]…").
   - **Mi criterio IEEE:** en el texto se cita por número entre corchetes. Si se nombra al autor, con uno o dos autores se escriben los apellidos y con tres o más, el primero seguido de "et al.". No se escribe el año entre paréntesis. Para normas: "la Ley N.º 7021/2022 [1], en su artículo…", no "La República del Paraguay [1]". **No sé con certeza si la profesora acepta algún nombre de autor en el texto o solo "[n]".** Contrástalo con `C:/TFG/Guía-uso-de-norma-IEEE-y-más.pdf` y `C:/TFG/Formato IEEE-resumido.pdf` antes de aplicarlo a todo.
2. **GB13 (parte de cita).** En la página 26 del PDF, la profesora dice: "No se cita en este apartado ya corresponde a la propuesta del autor del proyecto". La cita era Dean [42], sustituida luego por Peffers [50]. Ya **eliminé la frase**, así que [50] queda sin citar: **elimina [50] de la lista**. Revisa también [51] (Diamond et al.) en 8.1.11. Mi recomendación es **mantenerla**, porque respalda un umbral numérico y no "propone" el método, pero conviene que lo decidas sabiendo que la profesora prefiere el método sin citas. [5] en 8.1.3 identifica una fuente de datos y puede quedarse.
3. **Referencias sin citar tras GB12 y GB13:** [34], [35], [36], [37] y [50]. Propuesta de renumeración (verifiqué que el orden de primera aparición se mantiene): [38]→[34], [39]→[35], [40]→[36], [41]→[37], [42]→[38], [43]→[39], [44]→[40], [45]→[41], [46]→[42], [47]→[43], [48]→[44], [49]→[45], [51]→[46]. **No renumeré** para no pisar tu trabajo.

## 3. Para tfg-format-ieee
1. **GB1 (portada).** Recomiendo cambiar "Profesor de la Cátedra: **Lic.** Gabriela Matilde Bobadilla de Almada" por "**Ing. MSc.** Gabriela Matilde Bobadilla de Almada", porque el comentario es suyo y el orquestador la identifica como Ing. MSc. Hay que confirmar con el estudiante si va "Profesora". El título del Orientador ("Ing. Mag.") se deja como está salvo que el estudiante indique otra cosa.
2. **GB4** ("Debe estar alineado justificado") **y posiblemente GB8:** alineación **justificada** en todo el cuerpo, incluidas las listas de objetivos, preguntas, hipótesis, tareas y variables. GB4 estaba anclado en la lista de objetivos.
3. **Figuras:**
   - Crear `trabajo/img/figura_fases.png` según el comentario HTML de 8.1.2.
   - En `C:/TFG/.claude/scripts/md_to_docx_v2.py`, cambiar FIGURE_IMAGES a `'Figura 1:' → figura_fases.png` y `'Figura 2:' → figura1.png`. **Si no se cambia, el script insertará el diagrama funcional en el lugar de la Figura 1.**
   - `figura2.png` (flujo de tareas) ya no se usa.
4. **Tabla 1:** añadir en Word una fila de meses combinada sobre cada par Q1/Q2, repetir el encabezado si la tabla ocupa más de una página y, opcionalmente, poner en negrita las filas 1–7. Los rótulos de fase de 8.2 van en cursiva.
5. **Índice:** se eliminaron 7.2.1–7.2.3 y se renombraron 8.1.1 y 8.1.2. Regenerarlo con F9.

## 4. Para tfg-writer-formal
- Prosa nueva que hay que revisar: 8.1.1, 8.1.2, el párrafo de fundamento tras H3, la frase inicial de 7.2 y las denominaciones cortas de las subtareas.
- **No reintroducir** "significativas" en P4 ni tiempo futuro en las hipótesis. **No restaurar** los subtítulos 7.2.x, el párrafo UTA/robustez ni la cita de Peffers/Dean en 8.1.1.

## 5. Riesgos que señalo con franqueza
- La rúbrica dio **100 %** a objetivos, hipótesis, enfoque y operacionalización **en la versión original**. En la ronda 1 los reformulé bastante: OG con evaluación, H1–H3, 14 variables. En esta ronda los acerqué al vocabulario de la profesora (GB2, GB5, GB6, GB19–GB24), pero siguen siendo más extensos que lo que ella calificó. Si el estudiante prefiere minimizar el riesgo, la opción conservadora es simplificar el OG y unificar H1–H3 en una hipótesis en presente. **No lo hice**, porque eliminaría elementos medibles que la propia profesora pide en GB24.
- **El diseño (7/15) era lo más débil.** El cambio de más impacto es 8.1.2 junto con la Figura 1. Mientras la figura no exista como imagen, el hallazgo GB17 no está resuelto en el .docx.

---

# RONDA 1

**Archivo:** `C:/TFG/trabajo/anteproyecto_borrador.md`
**Fecha:** 17/11/2026
**Método:** reescribí el archivo entero en una sola operación. Copié literalmente la lista de referencias; no cambié ni un carácter de las entradas [1]–[43]. Ninguna cita [n] se eliminó: todas las del [1] al [42] siguen en el cuerpo, algunas en otra posición.
**Marcadores:** todo lo que no pude resolver sin datos del estudiante o sin una fuente verificable queda marcado como `[PENDIENTE: …]`. Las notas de maquetación van como comentarios HTML `<!-- … -->`, que no se ven al renderizar.

---

## AVISO PRINCIPAL PARA citation-verifier-master: hay que renumerar

Al reordenar la evolución histórica (ELECTRE → AHP → MAVT → PROMETHEE) y trasladar la línea de inferencia de pesos, **cambió el orden de primera aparición**. La correspondencia es la siguiente (posición nueva ← número actual):

| Posición | Número actual |
|---|---|
| 1–13 | Sin cambios |
| 14 | [18] |
| 15 | [17] |
| 16 | [14] |
| 17 | [16] |
| 18 | [19] |
| 19 | [22] |
| 20 | [23] |
| 21 | [24] |
| 22 | [25] |
| 23 | [26] |
| 24 | [27] |
| 25 | [28] |
| 26 | [29] |
| 27 | [30] |
| 28 | [31] |
| 29 | [32] |
| 30 | [33] |
| 31 | [15] |
| 32 | [20] |
| 33 | [21] |
| 34–42 | Sin cambios |

- La **[43]** sigue sin citarse. No la toqué: tú decides si se cita (en Delimitación o en 8.1.3) o se elimina.
- Revisa también los marcadores `[PENDIENTE]` de cita (ver la lista final).

---

## Cambios por ubicación

### Portada
- **Título** → lo unifiqué en portada y cuerpo: "Prototipo web de soporte a la decisión basado en métodos multicriterio para la evaluación de ofertas en licitaciones de Paraguay (2023–2026)". → I-11: deriva del objetivo general y resuelve la diferencia entre "métodos" y "un método".
- **Tabla de contactos** → la sustituí por notas al pie (`[^1]`–`[^3]`). → M-2 y plantilla.
  - Asigné cada teléfono y correo al graduando por el orden en que figuraban y por la dirección de correo. **Hay que confirmarlo.**
  - El contacto del Orientador queda como PENDIENTE.

### Índice
- **Índice** → lo reescribí según la estructura final: incluye la sección 5, 8.1.1–8.1.11 y los títulos ya sin truncar. → I-14.
- **Paginación** → la quité. Hay que regenerar el campo en Word con F9; lo dejé indicado en un comentario.

### Sección 1. Definición del problema
- **Párrafo 1** → añadí que el Decreto 2264/2024 exige que el pliego fije ponderaciones relativas, de modo que cada licitación tiene sus propios pesos. Es una segunda mención de [2]. → Mandato 5.
- **Párrafo 3** → corregí "los método" y lo reformulé así: aun con los pesos fijados, el método de agregación puede alterar la clasificación. → Mandato 5 y C-7.
- **Párrafo nuevo** → distingue el **problema real** del **problema de conocimiento**. Incluye un PENDIENTE de evidencia local. → C-1 e I-3.
- **Pregunta principal** → corregida ("¿En qué medida puede…") y operacionalizada con tiempo, errores y trazabilidad. → §3.2 de la revisión.
- **Preguntas secundarias** → pasaron de 3 a 4. La antigua P3, compuesta, se dividió en P3 (implementación) y P4 (comparación con expertos). P2 ahora pregunta por las diferencias de clasificación con las ponderaciones del pliego.
- **Rótulo nuevo** → añadí "**Definición del problema:**" con el enunciado *en cursiva* al cierre de la sección. → C-1.

### Sección 2. Delimitación
- Añadí un párrafo: **las ponderaciones vienen del pliego**, no se estiman, y lo que se compara entre métodos es la **clasificación resultante**. La regla del pliego es la referencia y los demás métodos sirven de contraste. → Mandato 5 y C-7.
- Añadí la participación de expertos externos. → Mandato 4.
- Añadí un párrafo sobre los límites de **recursos** y de **formación** de los investigadores. → I-13.
- Dejé PENDIENTES para: acotar los sectores, el rango de casos y la justificación de la inclusión del PTI. → I-13 e I-7.

### Sección 3. Objetivos
- **Objetivo general** → "Desarrollar **y evaluar**…", con el qué, el cómo (comparación de métodos y evaluación con expertos frente al procedimiento manual) y el para qué (determinar si reduce el tiempo y los errores y mejora la trazabilidad). Incluye "con las ponderaciones fijadas en el pliego de cada licitación". → C-3 y mandato 5.
- **OE1** → "Determinar la suficiencia de la información pública…". Deja de ser un acto de muestreo. → I-6.
- **OE2** → precisa "ponderaciones fijadas en su pliego".
- **OE3** → compara las **clasificaciones** que producen los métodos con las ponderaciones del pliego y determina cuáles sirven como **métodos de contraste** (en plural, unificado en todo el documento). → Mandato 5, C-7 e I-18.
- **OE4** → "Diseñar el prototipo web…": abarca procedimientos, propiedades, requerimientos, arquitectura, base de datos, interfaz y herramientas. Cubre las tareas 5 y 6. → I-6 e I-8.
- **OE5** → "Construir el motor de evaluación trazable y los módulos de registro y consulta… verificando corrección y reproducibilidad". Es un componente acotado y ya no repite el OG. → C-3 y mandato.
- **OE6** → incluye explícitamente la **comparación con la evaluación manual** (tiempo, errores, trazabilidad), los **expertos externos**, la **valoración ciega** y la aceptación por expertos. → C-4 y mandatos 4 y OE6.
- Pasé los objetivos a lista numerada en orden cronológico.

### Sección 4. Hipótesis
Reescrita entera. → C-2 y mandato.
- **Sin hipótesis para OE3**, que es descriptivo y no pronostica un dato (criterio de Alcance-1).
- **H1 (factibilidad técnica):** el prototipo reproduce la regla del pliego con concordancia total y resultados reproducibles. Es la formulación que la plantilla admite para investigación aplicada.
- **H2 (comparativa):** con expertos externos, el prototipo da menos tiempo, menos **errores** (aritméticos, de transcripción y de configuración) y más trazabilidad que la evaluación manual con hoja de cálculo. Es coherente con un alcance explicativo y un diseño cuasi-experimental (8.1.2).
- **H3 (aceptación):** umbral de la variable "Validación de expertos".
- Eliminé "mejor oferta", "transparencia" y "objetividad", que nada medía. Eliminé también la generalización a "contrataciones públicas del Paraguay".

### Sección 5. Fundamentación
- La reorganicé en **tres bloques rotulados**: académica, social y personal. → Mandato 6 e I-1.
- **Académica** → integra el párrafo inicial, la "Justificación" y la "Revisión de literatura". Condensé la revisión para no repetir el análisis de 7.2 (I-12). Se conserva el orden de primera aparición de [5]–[13].
- **Social** → circunscribe el objeto a un contexto próximo (DNCP; PTI en Alto Paraná) y distingue beneficiarios directos e indirectos.
- **Personal** → **escrita desde cero.** No inventé ningún vínculo personal: dejé un PENDIENTE para que los graduandos lo confirmen o completen.

### Sección 6. Impacto
- **Niveles rotulados:** individual, institucional, social, **ecológico** (nuevo) y académico (antes "comunidad de investigación"). → Mandato 6 e I-2.
- **Ecológico** → escrito desde cero, con un alcance honesto: despapelización indirecta y no medida, y mención del consumo energético.
- Fusioné el segundo párrafo institucional para reducir la extensión.
- Añadí un PENDIENTE de cuantificación (diapositivas 2025).

### Sección 7. Marco teórico
Pasó de unas 16 páginas a unas 6. → I-4, I-5 y M-4/M-5.
- **7.1.1.1 Evolución histórica** → cronología corregida: ELECTRE (finales de los 60) → AHP (finales de los 70) → Dyer y Sarin (1979) → PROMETHEE (1985) → MOORA (2006) → taxonomía (2020). Hay dos PENDIENTES para verificar si [18] y [17] respaldan las fechas de origen o si deben citarse las obras originales. → M-4.
- **7.1.1.2** → pasa a llamarse "Concepto": dos perspectivas de autores distintos y una síntesis propia.
- **7.1.1.3** → eliminé el quinto nivel (7.1.1.3.1–7.1.1.3.7). Cada método es ahora un párrafo con lema en negrita e indica qué implica aplicarlo con pesos del pliego. Conservé todas las citas.
- **Ecuación** → numerada "(1)", seguida de "donde:" y citada como "Ec. 1". → M-1. En Word hay que pasarla al editor de ecuaciones.
- **7.1.2** → fusioné 7.1.2.1+7.1.2.2 y 7.1.2.3+7.1.2.4.
- **Eliminados**:
  - 7.1.2.5 (inferencia de preferencias) y 7.1.2.6 (robustez).
  - La "demostración" de 7.1.2.7 (desarrollo propio, prohibido en el marco teórico).
  - La "hipótesis de trabajo" que anticipaba a MAVT como ganador (7.1.2.8 y cierre de 7.2).
- **Citas de la inferencia de pesos** → [15], [20], [21] y [34] se conservan en un párrafo de 7.1.2.4 que explica **por qué esa línea no se usará**: los pesos vienen del pliego.
- **7.1.3 Sistemas de soporte a la decisión** → **sección nueva.** Usa [11], [12], [7] y [8] según lo que ya afirmaba el documento, y deja tres PENDIENTES de cita: dos definiciones de SSD de autores distintos, y prototipado y trazabilidad en software. → I-5.
- **7.1.4 Marco normativo** → condensa 7.1.3.1.1–7.1.3.1.5 y 7.1.3.2 sin subniveles. Añadí un PENDIENTE sobre las fuentes periodísticas [35] y [36] del PTI. → I-7.
- **7.2.1** → cada antecedente se identifica ahora por autores, año y [n] (M-6) y se reduce a resumen, aporte y diferencia. Se mantiene el orden cronológico.
- **7.2.2** → conservé [41] y añadí un PENDIENTE de antecedentes sobre herramientas de software para la evaluación de ofertas.
- **7.2.3 Síntesis del estado del conocimiento** → **nuevo.** Contrasta los antecedentes con cada pregunta secundaria. Sustituye a la antigua 7.2.3 (UTA-splines y expresividad), cuyas citas pasaron a 7.1.2.4.

### Sección 8. Método
- **Tipo y Enfoque** → dejaron de ser párrafos sueltos: ahora son **8.1.1** y **8.1.2**, y el resto se renumeró de 8.1.3 a 8.1.11. Actualicé las referencias cruzadas (mapeo de Dean, marco teórico). → I-14.
- **8.1.2 Enfoque, alcance y diseño**, por componente. → I-10 y C-5.
  - Documental y comparación de métodos: descriptivo, no experimental, transversal y retrospectivo, sin hipótesis.
  - Desarrollo: etapas de Dean y H1.
  - Evaluación: **explicativo, cuasi-experimental intra-sujeto, cruzado y contrabalanceado**, con la VI "modalidad", H2 y H3.
  - Eliminé "diseño comparativo", que no existe en la tipología de la cátedra.
- **8.1.3** → la observación es "un caso por un experto"; los casos se agrupan en pares de complejidad similar.
- **8.1.5** → **reescrito**:
  - Las ponderaciones del pliego no son variable de decisión; se compara la **clasificación** de cada método con esos pesos.
  - La regla del pliego es el **modo principal** del prototipo y los demás métodos, el **módulo de contraste**.
  - La concordancia se mide con el primer lugar y el τ de Kendall.
  - Los parámetros que el pliego no proporciona se declaran como supuestos y se someten a sensibilidad. → Mandato 5 y C-7.
- **8.1.6** → la sensibilidad se hace respecto de los parámetros no fijados por el pliego; las variaciones de los pesos del pliego solo describen estabilidad y no proponen pesos alternativos.
- **8.1.7 y 8.1.8** → añadí el modo principal, el módulo de contraste y la exportación a una **plantilla común de informe**, necesaria para el cegamiento. Hay un comentario para actualizar la Figura 1. Cambié "frameworks" por "marcos de trabajo".
- **8.1.9** → pasa a llamarse "Verificación del prototipo web", porque la validación corresponde ahora a los expertos. La revisión interna de uso es preliminar.
- **8.1.10** → **reescrito.** → Mandato 4 y C-5.
  - Los **expertos externos** ejecutan ambas modalidades. Criterios propuestos: al menos 2 años en comités de evaluación; exclusión de los casos que el experto evaluó en su momento; entre 5 y 10 expertos, como PENDIENTE de confirmación.
  - ANEXO IV y consentimiento informado (M-15).
  - El comparador manual pasa a ser una **hoja de cálculo de uso general sin plantillas** de los investigadores, en lugar de la calculadora básica (evita el "hombre de paja").
  - **Diseño cruzado:** ningún experto repite caso (evita el arrastre).
  - **Doble ciego en la fase de valoración:**
    - el Orientador, a título de propuesta, codifica los informes y custodia la clave;
    - los investigadores puntúan errores y trazabilidad a ciegas;
    - los expertos valoran a ciegas la claridad y la confiabilidad de informes ajenos;
    - la clave se abre después de cerrar la base de datos.
  - Se reconoce que la modalidad no puede cegarse durante la ejecución.
  - Los errores del prototipo incluyen la carga por el usuario, lo que rompe la circularidad.
- **8.1.11** →
  - La lista de trazabilidad se fija antes de terminar el prototipo y la revisan los expertos (rompe la circularidad).
  - Se incluyen el cuestionario Likert y el umbral, con un PENDIENTE de cita para el umbral del 80 %.
  - Se añaden diferencias por caso y por experto, y Wilcoxon como análisis complementario.
  - Las limitaciones se actualizaron.

### 8.2 Lista de tareas
- Restituí la numeración en dos niveles, que se había perdido en la conversión a markdown.
- **Tarea 4** → aplicación de los métodos con los pesos del pliego, comparación de clasificaciones y selección de los métodos de contraste.
- **Tarea 5** → solo especificación y propiedades (antes 5.1–5.4).
- **Tarea 6** → diseño (antes 5.5–5.8) más herramientas (antes tarea 6). → I-8.
- **Tarea 7** → absorbe la comprobación de corrección y reproducibilidad (OE5).
- **Tareas 8 y 9** → reescritas para expertos, ANEXO IV, consentimiento, sorteo, codificación ciega y cuestionario.
- **Antigua 10.5** ("Redacción…") → fundida en 10.6. → M-13.
- **Hay un comentario para actualizar la Figura 2.**

### Tabla 1 (cronograma)
- Filas 4, 5, 6, 8, 9 y 10 → nuevas etiquetas.
- **Fila 8** → se adelanta y amplía a las quincenas 10–13 (antes 12–13) para dar tiempo al ANEXO IV y al reclutamiento de expertos.
- Las demás quincenas no cambian.

### 8.3 Operacionalización
- Pasó de 11 a **14 variables**, en el formato "**Nombre:** Definición. Estimador. Clasificación (naturaleza; función)". → I-9.
- **Variables nuevas:**
  - 4, Concordancia de las clasificaciones (OE3, mandato 5);
  - 5, Propiedades de los procedimientos (OE4);
  - 10, **Modalidad de evaluación**, la VI que faltaba.
- **Variable 4 anterior** ("herramientas seleccionadas", de gestión) → sustituida por la 6, "Cobertura del diseño respecto de los requerimientos".
- **"Validación de expertos"** (antes la variable 11, ahora la **14**) → **indicador definido**:
  - Likert de 5 puntos en tres dimensiones (claridad, confiabilidad, utilidad), con al menos 3 ítems por dimensión.
  - Se informan la mediana y el porcentaje de expertos con media ≥ 4.
  - **Aceptación:** mediana ≥ 4 y ≥ 80 % de expertos con media ≥ 4 en cada dimensión.
  - **Justificación:** los datos Likert son ordinales, por lo que corresponden mediana y porcentaje, no media.
  - El umbral del 80 % lleva un PENDIENTE de cita. → Mandato 3 y C-6.
- **Tabla 2** → una fila por variable. Eliminé "pendiente de definición con el profesor". Remapeé las tareas a los objetivos (tarea 5 → OE4; tarea 7 → OE5). La columna pasa a llamarse "Estimador", como en la plantilla. → I-8 y C-6.

### Idioma
- No encontré oraciones del cuerpo en inglés.
- Al identificar los antecedentes por autor y año, desaparecieron del cuerpo los títulos en inglés de 7.2.
- Los términos técnicos ("min-max", "UTA-splines") se conservaron como nombres propios.

---

## Pendientes que no pude resolver (necesitan al estudiante o una fuente)

**Datos del estudiante:**
1. Contacto del Orientador y confirmación de qué contacto corresponde a cada graduando.
2. Evidencia local del problema real (sección 1) y cuantificación del impacto (sección 6).
3. Acotar los sectores, el rango de casos (mínimo y máximo) y justificar la inclusión del PTI o acotar el estudio a la DNCP (sección 2).
4. Motivación y vínculo personal con el tema (sección 5).
5. Número y disponibilidad de los expertos (8.1.10). También hay que confirmar los criterios de inclusión propuestos, la elección del Orientador como custodio de la clave y el comparador manual con hoja de cálculo.

**Citas (para citation-verifier-master):**
6. Fechas de origen de ELECTRE y AHP: ¿bastan [18] y [17] o hay que añadir las obras originales?
7. Dos definiciones de SSD.
8. Prototipado y trazabilidad en software.
9. Antecedente de herramientas de software para la evaluación de ofertas.
10. Umbral del 80 % en el juicio de expertos.
11. Fuente normativa primaria sobre el régimen del PTI.

**Word y maquetación:**
12. Regenerar el índice con F9, pasar la Ec. 1 al editor de ecuaciones, actualizar las Figuras 1 y 2 y usar epígrafes automáticos.

**Para tfg-writer-formal:**
- No pulí la prosa palabra por palabra; la de las secciones nuevas (5, 6, 7.1.3, 8.1.5, 8.1.10) debe revisarse.
- **No reintroducir:**
  - "mejor oferta", "objetividad" ni "transparencia" como resultados medidos;
  - el veredicto anticipado a favor de MAVT;
  - la "calculadora básica";
  - la idea de que el equipo elige las ponderaciones.
