# Síntesis crítica del material de guía: TFG I (FPUNE)

**Agente:** tfg-master-ieee
**Alcance de este análisis:** solo el material de guía de la cátedra. El anteproyecto del estudiante queda fuera, para una fase posterior.
**Fecha:** 17/11/2026

---

## 0. Inventario y valor normativo de las fuentes

Antes de usar cualquier regla conviene saber de dónde sale y cuánto pesa. El material es heterogéneo: mezcla normas de la facultad, la plantilla oficial, diapositivas de clase y una guía de **otra institución**.

| Archivo | Naturaleza real | Peso normativo |
|---|---|---|
| Reglamento de TFG.pdf | Diapositivas que **resumen** la Res. N° 143/2022 (enlazada, pero sin el texto completo). Recoge los Arts. 1–12 y 16; **faltan los Arts. 13–15 y del 17 en adelante**. | Máximo, aunque incompleto |
| ptfg_ieee.pdf | Plantilla oficial en **LaTeX** (A4, Computer Modern), fechada el 12/09/2021, de 17 páginas. | Máximo para estructura y forma |
| ANEXO II.docx | Nota de conformidad del Profesor Orientador (formulario). | Obligatorio (Arts. 11 y 16) |
| ANEXO IV.docx | Solicitud de respaldo institucional (formulario). | Obligatorio si hay trabajo con entes externos (Art. 8) |
| Presentacion de la Materia.pdf | Programa resumido: contenidos, bibliografía y ponderación. | Alto (contrato de la materia) |
| Criterios evaluación 2do parcial-TFG I.pdf | Rúbrica de la **defensa oral** del 2do parcial. | Alto, pero **solo para lo oral** |
| AGENDA.pdf | Orden de exposición del 2do parcial (2 y 3/11/2026). | Logístico |
| FORMATO-Marco Teórico, Planteamiento, Delimitación, objetivos-2025, Alcance-1-2025, Fundamentación-Impacto, Diseño-25, Operacionalización-25, Preguntas, Análisis-antecedente, leer_art_cientifico | Diapositivas y ejemplos de la Prof. Bobadilla (2025). | Medio: interpretan la plantilla y a veces la contradicen |
| Ejemplo-operacionalizacion.pdf | Ejemplo de tabla de operacionalización. | Medio (modelo práctico) |
| Guía-uso-de-norma-IEEE-y-más.pdf | Guía del **Sistema Bibliotecario ITCA-FEPADE (El Salvador)**, abril de 2021. | **Bajo:** es ajena a la FPUNE. Sirve para la mecánica de citas, no para el formato de página |
| Formato IEEE-resumido.pdf | Versión recortada de la guía anterior, adaptada a la FPUNE (añade la licencia CC BY-NC-SA del Reglamento de Investigación de la FPUNE). **Elimina márgenes y tipografías.** | Medio para citas y referencias |

No estaba en la lista, pero existe en la carpeta: `PLANTILLA_PRESENTACION_PARCIAL.pptx`, la plantilla de diapositivas de la defensa oral. Le eché un vistazo solo porque afecta a la rúbrica oral (ver §3 y §5).

**Jerarquía que propongo al equipo para resolver conflictos:**
1. Reglamento y anexos.
2. `ptfg_ieee.pdf`, la plantilla "establecida en el reglamento", según la Presentación de la Materia.
3. Diapositivas 2025 de la profesora: son más recientes, así que cuando no contradicen la plantilla sino que **añaden** requisitos, conviene cumplir ambas fuentes a la vez.
4. Guía ITCA: solo para la mecánica de cita y referencia. **Nunca** para márgenes, tipografía ni interlineado.

---

## 1. Checklist estructural del Anteproyecto (PTFG)

**Fuente principal:** la plantilla `ptfg_ieee`. El Reglamento solo exige presentar "Proyecto de TFG" y "Nota de conformidad del Profesor Orientador" (Art. 16). **Ni el ANEXO II ni el ANEXO IV definen la estructura del documento**: son formularios administrativos. La estructura sale exclusivamente de la plantilla.

### 1.0 Requisitos previos y administrativos
- [ ] Hasta **2 autores** (Art. 7). Si la dupla se disuelve, el que abandona firma el ANEXO IX, **que no está en el material**.
- [ ] Profesor Orientador de la FPUNE con formación afín (Art. 7). Puede haber co-tutor externo experto.
- [ ] **ANEXO II** firmado por el Orientador. Con esa nota se compromete además a enviar al menos dos informes de avance durante la ejecución.
- [ ] **ANEXO IV**, dirigido al Coordinador de Carrera y firmado por el alumno y el Orientador, **si el TFG requiere** trabajo de campo, acceso a datos o cualquier contacto con instituciones o empresas externas (Art. 8). Toda gestión externa debe hacerse mediante nota oficial de la FPUNE, no de forma particular.
- [ ] Tema vinculado al currículo, de complejidad acorde al grado y **con originalidad** (Art. 4).

### 1.1 Portada (según la plantilla)
- [ ] Universidad Nacional del Este, Facultad Politécnica.
- [ ] Rótulo: "Anteproyecto de Trabajo Final de Grado".
- [ ] Carrera y Cátedra.
- [ ] Título del anteproyecto.
- [ ] "Por:" con el nombre de los graduandos. Cada uno lleva una **nota al pie** con teléfono y correo.
- [ ] Profesor Orientador, también con nota al pie de teléfono y correo.
- [ ] Profesor de la Cátedra.
- [ ] Lugar ("Ciudad del Este, Alto Paraná – Paraguay") y fecha.

### 1.2 Índice
- [ ] Índice paginado. La portada no se numera de forma visible y el índice es la página 1.

### 1.3 Cuerpo, en este orden obligatorio
Al inicio del cuerpo se repite el título. Las secciones se numeran con arábigos y las subsecciones de forma decimal (3.1, 8.1.1…).

| # | Sección | Qué debe contener (síntesis) |
|---|---|---|
| 1 | **Definición del problema** | Introducción que contextualiza el problema. Preguntas de investigación: "se acostumbra" incluirlas, y de **cada pregunta debe derivar al menos un objetivo específico**. Hay que distinguir el *problema de conocimiento* (el que se investiga) del *problema real* (cuya solución suele quedar fuera del alcance). La sección **termina obligatoriamente** con el rótulo "Definición del problema:" seguido del enunciado **en cursiva**. |
| 2 | **Delimitación del trabajo** | Límites por recursos, espacio, tiempo y formación del investigador. El documento de Delimitación añade espacio, tiempo y **circunstancia**, e identificar qué recursos y procesos entran y cuáles se aíslan. |
| 3 | **Objetivos** | 3.1 Objetivo general: deriva del enunciado del problema y "engendra" el título. 3.2 Objetivos específicos: **lista numerada en orden cronológico de abordaje**; mutuamente excluyentes y de complejidad similar; expresan **procesos**, no actos (p. ej., no "entregar un informe"); ninguno repite el general. Todo el PTFG se redacta **en futuro**. |
| 4 | **Hipótesis** | Solución provisoria verificable, ligada a un resultado que se obtendrá. Puede haber varias. En investigación aplicada puede reducirse a afirmar que siguiendo el método X se obtiene el producto Y. **Ver el conflicto con Alcance en §5.** |
| 5 | **Fundamentación** | Tres dimensiones: **académica** (aporte al campo), **social** (beneficio, con el objeto circunscrito a un **contexto próximo** al investigador) y **personal** (motivación). |
| 6 | **Impacto de la investigación** | Diferencia antes/después causada por el trabajo. La plantilla exige mencionar el impacto **ecológico** (relación humano-ambiente) y el **social** (relación humano-humano). Las diapositivas 2025 añaden el académico y el institucional, y piden cuantificar. |
| 7 | **Marco teórico** (unas **3 páginas** de referencia) | 7.1 Conceptos e ideas fundamentales, estructurados **por ejes teóricos**. Un subnivel solo se abre si tiene **al menos 2 tópicos**, sin exceso de niveles. 7.2 Antecedentes: de lo antiguo a lo actual y de lo amplio a lo específico, explicando la relación de cada uno con el trabajo y cerrando con el estado del conocimiento frente a las preguntas de investigación. **No** se desarrollan aquí las ideas propias del proyecto. |
| 8 | **Método** | 8.1 Especificaciones de diseño: declarar y **fundamentar** si la investigación es básica o aplicada, y desarrollar la rama que corresponda (§4). 8.2 Lista de tareas: numerada, cronológica, **cada tarea empieza con un sustantivo** (el infinitivo queda reservado a los objetivos), y cierra con el **cronograma** en tabla (detalle en §2). 8.3 Operacionalización de variables: lista en prosa y tabla OE–Tarea–Variable–Estimador (§4). |
| — | Elementos gráficos | "Recomendable": **diagrama de flujo del método** y, si es un desarrollo tecnológico o un servicio, **diagrama funcional** del producto, con referencia cruzada en el texto. |
| — | **Referencias bibliográficas** | Lista IEEE numerada por orden de aparición en el texto. |

### 1.4 Lo que la plantilla prohíbe expresamente (útil para revisar)
- Redactar en pasado.
- Que un objetivo específico eclipse al general.
- Objetivos que sean actos o entregables.
- Desarrollar el trabajo mismo dentro del PTFG: debe quedarse en la hoja de ruta.
- Limitar 8.1 al diseño del *producto*, en vez de describir el diseño de *todo el TFG*.
- Incluir en el cronograma tareas de elaboración del propio PTFG.
- Un cronograma sin fecha de inicio ("flotando en el tiempo").
- Escribir expresiones matemáticas fuera de un entorno matemático.

---

## 2. Reglas de formato que exige esta cátedra

### 2.1 Lo que la plantilla oficial fija (y lo que no)
| Aspecto | Regla de la plantilla | Comentario |
|---|---|---|
| Herramienta | LaTeX. La Presentación de la Materia habla de "un procesador de texto científico". | **No consta si se acepta Word.** Hay que confirmarlo con la profesora (ver §5). |
| Papel | A4 (deducido de la MediaBox del PDF). | La plantilla no lo declara explícitamente. |
| Tipografía | Computer Modern (LaTeX por defecto). El cuerpo parece de 12 pt, pero **no puedo verificarlo con exactitud** desde el PDF. | **No hay ninguna regla escrita de fuente ni de tamaño.** |
| Márgenes e interlineado | **No especificados** en ningún documento propio de la FPUNE. | Vacío normativo. |
| Columnas | Una sola columna (formato de informe). | **No** es el formato de artículo IEEE a dos columnas. |
| Numeración de secciones | Arábiga decimal: 1, 3.1, 8.1.1. | Se aparta del IEEE de artículo, que usa romanos (I, II) y letras (A, B). La cátedra manda. |
| Tablas | "Tabla N:" con **numeración arábiga** y **epígrafe encima** de la tabla. Deben ir en un entorno de tabla, aunque sean imágenes, para que se numeren como tablas. | El IEEE canónico usa "TABLA I" en romanos y versalitas. **Seguir la plantilla.** |
| Figuras | "Figura N:" con **epígrafe al pie** y referencia cruzada obligatoria en el texto. | El IEEE canónico usa "Fig. 1.". **Seguir la plantilla.** |
| Ecuaciones | Siempre en entorno matemático. Las numeradas llevan (n) a la derecha y se citan como "Ec. n". Las variables se explican después con "donde:". | — |
| Notas de pie de tabla | Admitidas (p. ej., la aclaración de "Estimador*" en la Tabla 3). | — |
| Listas | Objetivos, tareas y variables siempre en listas **numeradas**. | — |
| Variables (prosa) | Formato "**Nombre:** Definición. Estimador." con oraciones simples separadas por punto y seguido. | — |
| Título de la lista final | "Referencias bibliográficas". La guía ITCA usa "Referencias". | Menor. Usar el de la plantilla. |

### 2.2 Citas en el texto (de las dos guías IEEE, que coinciden en esto)
- Número entre corchetes **dentro de la línea**, con un espacio antes: "… consultada [6]".
- **El mismo número para la misma fuente** durante todo el documento.
- Para varias fuentes es preferible citarlas por separado ("[1], [3], [5]") o con rango ("[1]–[5]"). La guía también tolera agruparlas ("[1, 5, 7]"), que **no** es la forma canónica del IEEE; recomiendo evitarla.
- No mencionar autor ni año salvo que sea necesario para el sentido. Si se menciona, va antes del corchete: "Sinisterra [3]…".
- Escribir "En [9]" o "Ver [9]", no "en la referencia [9]", salvo al inicio de oración.
- **No se admite la cita de cita** (fuente secundaria): si no se accede al original, no se cita.

### 2.3 Lista de referencias (guía ITCA y versión resumida)
- Ordenada **numéricamente por aparición**, no alfabéticamente. Correspondencia 1:1 entre citas y referencias.
- Datos en el idioma original. Autor como iniciales con espacio ("C. A. Molinés") seguidas del apellido completo.
- Hasta 6 autores se listan todos; con más de 6, el primero seguido de *et al.*
- El título de libro, revista o congreso va en cursiva y con las mayúsculas de título. El título de artículo o capítulo va entre comillas, con mayúscula solo inicial.
- "vol." en minúscula para revistas; "p." para una página y "pp." para un rango.
- Meses abreviados en español (en., febr., mzo., abr., my., jun., jul., ag., sept., oct., nov., dic.).
- Recursos en línea: "[En línea]. Disponible en: URL". Si hay DOI, **solo el DOI** y la fecha de acceso puede omitirse.

### 2.4 Contradicciones de formato entre archivos
1. **Formato de página ajeno.** La guía ITCA trae dos juegos de reglas que no son de la FPUNE. El primero es para artículos IEEE: márgenes "1.78 / 1.65" **sin unidad**, Times New Roman, cuerpo de 9 pt, títulos de 24 pt y subtítulos en romanos. El segundo son las normas internas del ITCA: 12 pt, interlineado 1,5 y márgenes de 2,5/2 cm. **Ninguno aplica a la FPUNE**, y la propia versión "resumida" adaptada a la FPUNE los eliminó. Aplicarlos sería un error.
2. **Numeración de tablas, figuras y secciones.** La plantilla usa arábigos, "Tabla 1" y "Figura 1"; el IEEE genérico usa romanos y "Fig.". Prevalece la plantilla.
3. **Las referencias de la propia plantilla no cumplen IEEE**, aunque la plantilla misma exige "ceñirse a las especificaciones de la IEEE":
   - Usa "obtenido el … de URL" en lugar de "[En línea]. Disponible en:".
   - Libros con "McGraw-Hill. pp 350-353, 2010": páginas en posición incorrecta y "pp" sin punto.
   - Una fecha corrupta típica de BibTeX ("01 2000") y un volumen "Año V".
   - **El mismo libro (Hernández Sampieri, 2010) figura como tres entradas distintas ([6], [9], [10]) que solo cambian la página.** Esto contradice la regla de las guías de un único identificador por fuente. La forma correcta es una sola entrada y la página en la cita ("[6, p. 120]").
   - Fuentes de baja calidad (blogs, definicion.de, docplayer), cuando leer_art_cientifico recomienda fuentes revisadas por pares.

   **Criterio que propongo:** la **estructura** se toma de la plantilla y la **sintaxis de cada referencia** de la guía o del IEEE Reference Guide. Los ejemplos de la plantilla no deben imitarse.
4. **Incoherencias internas de la guía ITCA:**
   - Pide un espacio entre iniciales, pero un ejemplo dice "D.L. Nelson".
   - Pide abreviar los meses como "en.", pero los ejemplos usan "Ene./Dic." y "ago.".
   - Mezcla "[Online]. Available" con "[En línea]. Disponible en".
   - Coloca "Accedido:" en posiciones distintas según el ejemplo.
   - Cierra el título de artículo con comillas y punto, cuando el IEEE pone la coma dentro de las comillas: “Título,”.

   Hay que elegir **un único patrón y aplicarlo de forma consistente** en todo el documento.

---

## 3. Criterios de evaluación que realmente se aplican

### 3.1 Lo que está escrito
**Rúbrica del 2do parcial, solo la parte oral:**

| Bloque | Ítem | Puntos |
|---|---|---|
| a) Presentación PowerPoint (TP 10) | Temas en secuencia | 3 |
| | Cantidad de texto adecuada | 4 |
| | Colores y tamaño de letra | 3 |
| b) Exposición oral (TP 25) | Dominio del tema | 6 |
| | No leer las diapositivas | 4 |
| | Lenguaje adecuado y claro | 5 |
| | Mirada y postura | 4 |
| | Respeto del tiempo (**máx. 10 min**) | 6 |

**Ponderación de la materia** (Presentación de la Materia): 1er parcial 20 %, 2do parcial 20 %. **No se exonera** (coherente con el Art. 6 del Reglamento).

**Reglamento:** el Profesor de Asignatura **evalúa los avances y aprueba** el proyecto (Art. 10). El tema debe tener originalidad, pertinencia curricular y complejidad acorde al grado (Art. 4).

### 3.2 Lo que NO está escrito (y es grave)
- **No existe en el material una rúbrica del documento escrito.** La única rúbrica evalúa la presentación oral. Cómo se califica el anteproyecto escrito (el 60 % restante, o lo que corresponda) **no consta**.
- La rúbrica oral se contradice sola (ver §5).

### 3.3 Escala de severidad para la futura revisión
A falta de rúbrica escrita, la derivo de lo que la plantilla y el Reglamento formulan como obligación ("debe", "se debe evitar") frente a lo que solo recomiendan. **Es mi criterio, no una norma de la cátedra.**

**CRÍTICO (motivo para no aprobar el proyecto):**
- Falta una sección obligatoria o el orden no respeta el de la plantilla.
- No hay enunciado formal del problema al final de la sección 1, o se confunde el problema real con el de conocimiento.
- Se rompe la cadena **problema → preguntas → objetivos específicos → tareas → variables → estimadores**: una pregunta sin objetivo, un objetivo sin tareas, una variable sin estimador.
- Un objetivo específico equivale al general, o los objetivos son actos o entregables.
- El método no declara ni fundamenta el tipo de investigación (básica o aplicada) ni, según corresponda, el enfoque, el nivel y el diseño, o bien las etapas de desarrollo tecnológico.
- Falta la operacionalización de variables o su tabla.
- Falta el cronograma, no tiene fecha de inicio o incluye tareas del PTFG.
- Hay citas sin referencia o referencias sin cita, **citas inexistentes o que no respaldan lo afirmado**, plagio, o citas de cita.
- Falta de originalidad o de pertinencia curricular (Art. 4).
- No hay ANEXO II, o no hay ANEXO IV cuando se trabaja con datos o entes externos.

**MAYOR:**
- La hipótesis es incoherente con el alcance declarado (§5).
- Fundamentación sin alguna de sus tres dimensiones.
- Impacto sin la dimensión ecológica o la social.
- Marco teórico sin ejes, sin al menos dos definiciones de autores distintos más una síntesis propia por concepto, o con antecedentes que no siguen la estructura de 4 partes (identificación con cita, resumen, aporte, diferenciación).
- Objetivos específicos fuera del orden cronológico o de complejidad desigual.
- Tareas que empiezan con infinitivo.
- Redacción en pasado.
- Fuentes de baja calidad.
- Una misma fuente con varias entradas.

**MENOR:**
- Posición de los epígrafes, formato de numeración, puntuación de referencias, título de la sección de referencias, subnivel con un solo hijo, errores tipográficos.

**Para la defensa oral**, el peso real está en el **tiempo (6)** y el **dominio (6)**. Superar los 10 minutos cuesta tanto como no dominar el tema.

---

## 4. Expectativas metodológicas

### 4.1 Problema y preguntas
- Los documentos de Planteamiento y Preguntas aplican los criterios de Kerlinger: el problema **relaciona 2 o más variables**, se formula **como pregunta** y es **verificable empíricamente**. Hay que identificar al menos 2 variables y la **unidad de análisis**.
- Las preguntas deben ser claras, relevantes, factibles, enfocadas y congruentes entre sí, y fijar límites de tiempo y espacio.
- El ejemplo modelo incluye una pregunta principal y preguntas secundarias. La plantilla exige que cada una genere al menos un objetivo específico.

### 4.2 Objetivos
- **General**, según la plantilla: deriva del problema y produce el título. **Según objetivos-2025** tiene 4 partes: verbo en infinitivo + **qué** + **cómo** + **para qué**.
- **Específicos**: según la plantilla, son procesos mutuamente excluyentes, de complejidad similar y en orden cronológico. Según objetivos-2025, deben ser SMART: medibles, realistas, temporales, específicos, y responder a qué, cuándo y cuánto.
- Errores que la cátedra señala:
  - Confundir objetivo general con específicos.
  - Objetivos exagerados ("eliminar" en lugar de "disminuir").
  - Objetivos desordenados o incompletos.
  - Objetivos innecesarios como "escribir el libro o artículo", que ya están en el Reglamento.

### 4.3 Tipo, enfoque, alcance y diseño
1. **Propósito.** La investigación **básica** genera conocimiento (descubrimiento); la **aplicada o tecnológica** genera un producto o servicio (invento o innovación, radical o incremental). **Hay que declararlo y fundamentarlo.**
2. **Si es básica:**
   - Método: inductivo, deductivo o hipotético-deductivo.
   - Enfoque: cuantitativo, cualitativo o mixto.
   - **Nivel o alcance**: exploratorio, descriptivo, correlacional o explicativo.
   - **Diseño**: experimental (manipula la VI) o no experimental (transversal o longitudinal: de tendencia, de cohorte o de panel). En el enfoque cualitativo: teoría fundamentada, etnográfico, narrativo o investigación-acción.
3. **Si es aplicada:** las etapas de Dean son (a) invención o adaptación del concepto con sus especificaciones, (b) análisis del concepto con ciclos de diseño y prueba, y (c) síntesis mediante prototipo y experimentos funcionales. El "alcance en profundidad" es la complejidad de las especificaciones del prototipo. **El diseño debe describir todo el TFG, no solo el producto.**
4. **Especificaciones de diseño** (Diseño-25), cada una justificada por un objetivo específico:
   - Análisis de datos: naturaleza y origen de los datos, métodos de procesamiento, herramientas, indicadores clave, validación.
   - Prototipo: requerimientos, arquitectura, UI/UX, lenguajes y plataformas, base de datos, plan de pruebas (funcionalidad, rendimiento, usabilidad).
5. **Hipótesis según el alcance** (Alcance-1-2025):
   - Exploratorio: no lleva hipótesis.
   - Descriptivo: solo si se pronostica un dato.
   - Correlacional: hipótesis correlacional.
   - Explicativo: hipótesis causal.
6. **Viabilidad**: recursos de información, materiales, temporales, económicos y humanos. El material la menciona, pero **no le asigna sección propia en la plantilla**.

### 4.4 Operacionalización de variables
- Variables clasificadas por naturaleza (cualitativas nominales u ordinales; cuantitativas de intervalo o razón, discretas o continuas) y por función (independiente, dependiente, interviniente).
- **Formato de la plantilla:** primero, un párrafo por variable con Denominación, Definición y **Estimador** (unidad de medida, instrumento, escala Likert, métrica de calidad, criterio experto…). Después, la **tabla OE | Tarea | Variable | Estimador**, con el epígrafe encima.
- **Formato de Operacionalización-25:** definición conceptual y operacional, con dimensiones, indicadores e índices. Tabla OG | OE | Tarea | Variable | Definición | Definición operacional/Indicador.
- **Ejemplo-operacionalizacion:** tabla OE | Tareas (numeradas 1.1, 1.2… por objetivo) | Variable | Indicador.
- La columna **Estimador/Indicador debe ser unívoca** por variable.

### 4.5 Marco teórico y antecedentes
- Estructura de la pirámide invertida, de lo general a lo específico:
  1. Conceptos principales: evolución histórica, concepto (**al menos 2 definiciones de autores distintos más una síntesis propia**), características y tipos (profundizando solo en los que se usarán), conceptos ligados a la problemática y, si aplica, **marco legal** (internacional, Constitución, ley nacional).
  2. Antecedentes.
- En cada apartado el autor hace un "aporte": valoración, relevancia para el objetivo, comparación de definiciones.
- **Análisis de cada antecedente en 4 partes:** identificación con cita, resumen, aporte o similitud, y diferenciación (la brecha).

---

## 5. Incoherencias, ambigüedades y vacíos en el material

### 5.1 Vacíos (información que falta)
1. **No hay rúbrica del documento escrito.** Solo se evalúa por escrito la parte oral del 2do parcial.
2. **El Reglamento está incompleto:** faltan los Arts. 13–15 y del 17 en adelante (plazos, aprobación formal, defensa), el ANEXO IX y probablemente los anexos con el formato del proyecto. Además, la numeración del resumen repite artículos (dos "Art. 5" y dos "Art. 7").
3. **Ningún documento de la FPUNE fija márgenes, fuente, tamaño ni interlineado.** La única fuente que da números es la guía ITCA, que es de otra institución.
4. **No consta si se acepta Word** o si es obligatorio LaTeX. La plantilla está escrita para LaTeX (con instrucciones de `\begin{table}`, `$…$`, `\[…\]`) y el programa pide un "procesador de texto científico".
5. Solo hay ponderación para el 40 % de la nota (dos parciales de 20 %). El resto no está explicado.
6. La viabilidad se enseña, pero no tiene sección en la plantilla.
7. El material es antiguo: la plantilla y la guía son de 2021, con referencias consultadas en 2020–2021.

### 5.2 Contradicciones de contenido
| # | Tema | Fuente A | Fuente B | Riesgo y recomendación |
|---|---|---|---|---|
| C1 | Forma del problema | Plantilla: enunciado **declarativo en cursiva**, con preguntas solo "acostumbradas" | Planteamiento y Preguntas (Kerlinger): el problema **debe formularse como pregunta** | Incluir ambas cosas: preguntas explícitas y el enunciado en cursiva al final. |
| C2 | Hipótesis | Plantilla: la sección 4 es fija y siempre está | Alcance: los estudios exploratorios **no** llevan hipótesis; los descriptivos casi nunca | Mantener la sección. Si el alcance es exploratorio, justificar la ausencia. En aplicada, usar la hipótesis de viabilidad del método. |
| C3 | Kerlinger frente a investigación aplicada | Kerlinger exige una relación entre 2 o más variables | La plantilla admite TFG tecnológicos cuyo problema es construir algo | En aplicada, las variables deben ser las de evaluación del producto (precisión, usabilidad…), no "el sistema". |
| C4 | Tres significados de "alcance" | Alcance-1: nivel (exploratorio… explicativo) | Su propia "tríada" equipara alcance con **delimitación**; la plantilla en aplicada lo define como la complejidad del prototipo | Usar "alcance" como nivel de profundidad y reservar "delimitación" para los límites. |
| C5 | Fundamentación | Plantilla: académica, social y personal | Fundamentación-25: justificación, **revisión de literatura** y pertinencia social, científica o tecnológica. Planteamiento: criterios de Sampieri | Cubrir las tres dimensiones de la plantilla e integrar los elementos de 2025, sin duplicar los antecedentes. |
| C6 | Impacto | Plantilla: **ecológico** y social, obligatorios | Impacto-25: académico, social e institucional, cuantificado; **no menciona el ecológico** | Incluir siempre el ecológico (lo exige la plantilla) más los de 2025. |
| C7 | Dónde van los antecedentes | Plantilla: en 7.2, dentro del marco teórico | Planteamiento: "Contexto y Antecedentes" dentro de la Definición del problema, y la revisión de literatura también en la Fundamentación | Riesgo de repetir lo mismo tres veces. En la sección 1 basta un contexto breve; el análisis completo va en 7.2. |
| C8 | Extensión del marco teórico | Plantilla: unas 3 páginas, sin ideas propias | Marco Teórico-25: "debe ser completo, desde la historia", con un "aporte" del autor en cada apartado | El aporte es valoración crítica, no la propuesta propia. La extensión es orientativa. |
| C9 | Esquema de la tabla de operacionalización | Plantilla: 4 columnas, con Estimador | Operacionalización-25: 6 columnas con OG y definiciones; Ejemplo: 4 columnas con "Indicador" | **Ambigüedad real.** Recomiendo el formato de la plantilla y, si se quiere, añadir la definición operacional. Conviene confirmarlo con la profesora. |
| C10 | Redacción de las tareas | Plantilla: empiezan con **sustantivo** | Operacionalización-25: "Recopilar", "Diseñar", "Aplicar" (infinitivos); objetivos-2025 también mezcla | Seguir la plantilla. El Ejemplo-operacionalización sí lo cumple ("Búsqueda", "Clasificación"). |
| C11 | Objetivos específicos | Plantilla: procesos, mutuamente excluyentes | objetivos-2025: SMART con "cuándo y cuánto", y verbos de intervención (capacitar, sensibilizar, disponibilizar) más propios de proyectos de gestión que de investigación | Procesos medibles; evitar verbos de intervención social. |
| C12 | Qué cuenta como "variable" | Plantilla y Operacionalización-25: propiedades del fenómeno estudiado | Ejemplo-operacionalización: indicadores de **gestión del proyecto** ("número de fuentes consultadas", "porcentaje de datos extraídos") | Error conceptual del ejemplo: confunde indicadores de avance con variables de investigación. No imitarlo. |
| C13 | Diseño experimental | Plantilla y Diseño-25: manipulación intencional de la VI | Diseño-25, en "Prototipo": "investigación experimental = pruebas de funcionamiento" | Las pruebas funcionales **no** convierten el diseño en experimental. |
| C14 | Nivel exploratorio | Plantilla: solo fuentes secundarias, resultado tipo monografía | Alcance-1: entrevistas y observación cualitativas | Definiciones distintas; precisar cuál se adopta. |
| C15 | Citas en la plantilla | Guías: un solo número por fuente, IEEE estricto | La plantilla: tres entradas para un mismo libro, formato no IEEE | §2.4. No imitar las referencias de la plantilla. |
| C16 | Fuentes secundarias | Guía ITCA: el IEEE **no admite** la cita de cita | Marco Teórico-25 enumera "fuentes secundarias" como tipo válido de literatura | Son cosas distintas (una obra de referencia frente a una cita indirecta), pero la terminología confunde. |

### 5.3 Errores internos de los ejemplos (que un estudiante podría copiar)
- **objetivos-2025:** exige que el objetivo general tenga "qué, cómo y para qué", pero su ejemplo ("Identificar técnicas de minería de datos que describan patrones…") **no tiene ni cómo ni para qué**. Su objetivo específico 3, "Analizar resultados", es vago y viola sus propias reglas. Además afirma que los objetivos generales "pueden admitir varias interpretaciones" al mismo tiempo que exige que sean claros.
- **Alcance-1:**
  - Propone como ejemplo descriptivo "Analizar los factores que determinan…", que tiene formulación explicativa.
  - Pone como ejemplo correlacional "Comparar Frameworks JavaScript", que no es correlacional.
  - Pone como ejemplo explicativo determinar las causas de la deserción con minería de datos sobre datos observacionales, cuando un diseño no experimental no establece causalidad.
  - En la tabla de variables, "satisfacción" aparece como independiente y como dependiente a la vez.
  - Asigna VI y VD a una hipótesis "descriptiva".
- **Operacionalización-25:** la hipótesis "el nivel socioeconómico **incide**…" es causal, sin un diseño experimental que la sostenga. Las escalas están mal agrupadas (discreta y continua aparecen solo bajo razón).
- **Marco Teórico-25:** la numeración del esquema está duplicada ("1.2" y "1.3" repetidos, "1.1.3" repetido) y abre un subnivel con un solo hijo, contra la regla de la plantilla.
- **Análisis-antecedente:** el párrafo modelo tiene una oración duplicada ("difiere de dicho trabajo El proyecto presentado difiere…") y su explicación menciona una librería que no aparece en el texto del ejemplo.
- **Planteamiento:** la pregunta modelo contiene un error gramatical ("¿Cuál es son…?").

### 5.4 Incoherencias administrativas y de evaluación
- **La rúbrica oral se contradice sola:**
  - Asigna 10 % a la presentación y 10 % a la exposición, pero al pie dice que se suma un 10 % en total.
  - Usa escalas dispares (TP 10 frente a TP 25).
  - La numeración salta del ítem 4 al 6.
  - El programa asigna 20 % al 2do parcial completo.

  Hay que aclarar qué porcentaje pesa lo oral y qué pesa lo escrito.
- **Tiempo de exposición:** la rúbrica fija un máximo de 10 minutos, pero la agenda asigna turnos de 15–20 minutos (probablemente incluyen las preguntas, pero no se dice).
- **La plantilla de diapositivas** dice "Primera Parcial" aunque se usa en el 2do. Además, su índice **omite** Definición del problema, Delimitación y Operacionalización, cuando el criterio de "secuencia de temas" y el orden de la plantilla los incluyen.
- **El ANEXO II** está redactado para un solo alumno, aunque el Reglamento admite duplas. No se sabe si se presenta una nota por alumno o una conjunta.
- **Resoluciones:** el Reglamento enlaza la Res. N° 143/2022, mientras que el pie de los anexos cita la "Resolución CD N° 487/2021". **No puedo determinar** si esta última es la de aprobación de los formularios o si es una versión anterior. Conviene verificarlo.
- **Terminología:** el mismo documento se llama "Anteproyecto" en la portada de la plantilla, "PTFG" (Proyecto) en el cuerpo y "Proyecto de TFG" en el Reglamento.

---

## 6. Recomendaciones operativas para el equipo
1. **tfg-writer-formal:** usar la plantilla como esqueleto rígido (portada, índice, las 8 secciones y las referencias, en ese orden). Aplicar la sintaxis IEEE de la guía a cada referencia. No usar márgenes ni tipografías ITCA. Redactar en futuro. Tareas con sustantivo inicial; objetivos con infinitivo.
2. **citation-verifier-master:** además de verificar que cada fuente exista, comprobar que cada número corresponda a una sola fuente, que no haya cita de cita y que las fuentes sean preferentemente revisadas por pares. Los ejemplos de la plantilla no sirven de referencia de calidad.
3. **Antes de la revisión del TFG, conviene confirmar con la profesora:**
   - (a) si se acepta Word o es obligatorio LaTeX;
   - (b) los márgenes, la fuente y el interlineado;
   - (c) qué esquema de tabla de operacionalización exige (C9);
   - (d) la rúbrica del documento escrito;
   - (e) si el ANEXO IV aplica cuando los datos provienen de portales públicos o de una institución externa.
