# Análisis del material de guía: protocolo de citación y verificación

**Agente:** citation-verifier-master
**Cátedra:** Trabajo Final de Grado I, FPUNE
**Alcance:** solo el material de guía de la cátedra. El TFG del estudiante (`Anteproyecto_licitaciones_Ivan_Alex.docx`) queda **excluido** de esta fase.
**Fecha del análisis:** 17-11-2026

---

## 0. Fuentes analizadas y qué aporta cada una

| Archivo | Tipo | ¿Trae reglas o ejemplos de citación? |
|---|---|---|
| `ptfg_ieee.pdf` | Plantilla oficial del anteproyecto (LaTeX, 2021) | **Sí.** Citas en el cuerpo y 11 referencias de ejemplo. Es lo que el docente ve como "modelo", pero sus referencias tienen defectos (ver 1.3). |
| `Formato IEEE-resumido.pdf` | Versión de la guía IEEE adaptada a la FPUNE (9 diapositivas) | **Sí.** Reglas de cita en el texto, cita textual o parafraseada, 2 referencias de ejemplo y una mención a la licencia CC BY-NC-SA de la FPUNE. |
| `Guía-uso-de-norma-IEEE-y-más.pdf` | Guía extendida del Sistema Bibliotecario ITCA-FEPADE (abril de 2021, 41 diapositivas) | **Sí, es la fuente más completa.** Normas para citar y referenciar, y esquemas con ejemplo por tipo de fuente. |
| `Reglamento de TFG.pdf` | Presentación resumida del Reglamento (Res. 143/2022) | Indirectamente: exige originalidad (Art. 4). No regula citas ni sanciones en la versión resumida. |
| `ANEXO II.docx` | Nota de conformidad del Profesor Orientador | **No.** Solo es un formulario administrativo, sin citas ni referencias (revisé también encabezados, pies y notas). |
| `ANEXO IV.docx` | Solicitud de respaldo institucional | **No.** Igual que el anterior. |
| `Analisis-antecedente.pdf` | Ejemplo de cómo redactar un antecedente | **Sí.** Muestra el patrón que la cátedra espera para citar un antecedente: título del trabajo y [n]. |
| `leer_art_cientifico.pdf` | Cómo buscar y leer artículos científicos | Indirectamente: buscadores (Google Scholar, CICCO-CONACYT), búsqueda por DOI y criterios de calidad de fuentes. |
| `Criterios evaluación 2do parcial-TFG I.pdf` | Rúbrica de la defensa oral del 2.º parcial | **No.** Solo puntúa la presentación en PowerPoint y la exposición oral. **No contiene ningún criterio sobre citas** (ver sección 3). |

**Limitaciones técnicas:** extraje el texto con `pdftotext`. Algunos PDF contienen imágenes (13 en la guía extendida, 6 en la de lectura de artículos, 4 en el Reglamento y 1 en el formato resumido) que no pude renderizar. Por el contexto parecen logos o elementos decorativos, pero **no puedo descartar** que alguna diapositiva tenga un ejemplo solo en imagen.

---

## 1. Protocolo de citación y referenciación que exige la cátedra

### 1.1 Citas en el cuerpo del texto

Coinciden con el IEEE genérico, salvo las particularidades marcadas con **[≠]**:

1. **Número entre corchetes** `[n]` según el orden de primera aparición. Las citas no distinguen entre fuentes impresas y electrónicas.
2. **Una fuente, un número.** El mismo identificador se usa en todas las menciones de esa fuente. *(Ver la contradicción de la plantilla en 1.3-a.)*
3. **El corchete va en la línea de texto, con un espacio antes**, integrado en la oración y antes del signo de puntuación (`... la temática consultada [6].`).
4. **Varias fuentes a la vez [≠]:** la guía de la cátedra *prefiere* corchetes separados (`[1], [3], [5]` y `[1]-[5]`), pero **también acepta agrupar** (`[1, 5, 7]` y `[1-5]`). La propia plantilla oficial usa `[1, 2]`. La regla de la UAM ("usar corchetes separados") es por tanto **más estricta** que lo que tolera la cátedra.
5. **Autor en el texto** solo si es relevante para la oración, y siempre **antes** del corchete (`Sinisterra [3] elaboró...`). Se desaconseja `En Smith [1]` cuando basta `En [1]`.
6. **No mencionar la fecha** de la obra citada, salvo que sea relevante.
7. **No escribir "la referencia [9]"** a mitad de oración (se usa `En [9]` o `Ver [9]`). Se admite al **comienzo** de una oración (`La referencia [9] muestra...`).
8. **Se prohíbe la cita de cita (fuente secundaria) [≠, explícito]:** "si no encuentra la fuente original, no debe citar". La UAM no lo menciona y para mi verificación es **una regla clave**.
9. **Cita textual:** fragmento exacto entre comillas, y las omisiones se marcan con puntos suspensivos. La cátedra **no exige número de página** en la cita textual; la plantilla cita textualmente con `[11]` sin página. *(Ver ambigüedad A5.)*
10. **Paráfrasis** admitida cuando el texto es muy técnico, está en otro idioma o pierde claridad si se copia literalmente. Lleva cita igualmente.
11. **Antecedentes [≠, patrón propio]:** según `Analisis-antecedente.pdf`, en esta sección el título del trabajo previo se menciona en el cuerpo y se vincula con su número, por ejemplo `El trabajo de <Título> [15], presentó...`. Luego se resume, se indica el aporte y se marca la diferencia (brecha). Se admite nombrar la obra en el texto.
12. **Las notas al pie no sustituyen a las citas.** La plantilla las usa solo para aclaraciones, como desarrollar la sigla IEEE.

### 1.2 Lista de referencias

1. **Ubicación y título [≠]:** va al final del documento. La plantilla titula la sección **"Referencias Bibliográficas"**; la guía la llama "Referencias". Acepto ambos títulos, pero en todo el documento debe usarse uno solo.
2. **Orden numérico de aparición, nunca alfabético.** El número va en una columna a la izquierda y coincide con el usado en el texto.
3. **Correspondencia biunívoca:** toda cita tiene su referencia y toda referencia está citada al menos una vez.
4. **Datos en el idioma original** de la fuente (el título no se traduce).
5. **Autores:** iniciales del nombre seguidas del apellido o apellidos completos, con espacio entre iniciales (`C. A. Molinés`).
   - Se enumeran todos los autores hasta seis; si son **más de seis**, se escribe el primero y `et al.`
   - Si el autor es una institución, se escribe tal como aparece en la fuente. Si la obra es anónima, empieza por el título.
   - **[≠]** La plantilla une autores con "**y**" (español) y no con "and". Lo acepto si es consistente.
6. **Mayúsculas:**
   - Título de libro, revista, conferencia o congreso: inicial mayúscula en cada palabra importante.
   - Título de artículo, tesis o capítulo: solo la primera palabra (más nombres propios y siglas).
7. **Formato tipográfico:** títulos de libro y de revista en *cursiva*; títulos de artículo y de capítulo "entre comillas".
8. **Páginas:** `p. 111` para una sola página y `pp. 11-120` para un rango.
9. **Volumen [≠, rareza de la guía]:** "V" mayúscula si es libro y "vol." en minúscula si es revista.
10. **Meses [≠]:** la guía propone abreviaturas en español (`en.`, `febr.`, `mzo.`, `abr.`, `my.`, `jun.`, `jul.`, `ag.`, `sept.`, `oct.`, `nov.`, `dic.`). Sus propios ejemplos no las respetan (ver A3).
11. **Obras no publicadas:** se indica "en prensa", "inédito", "enviado para evaluación", etc.
12. **Recursos en línea:** se referencian según su tipo de fuente y se añade `[En línea]` + `Disponible en:` + URL o DOI.
    - **Si existe DOI, va el DOI y no la URL.**
    - **La fecha de acceso puede omitirse si hay DOI.** En cualquier otro recurso web es obligatoria.
    - Dominios en minúscula.
13. **Aspecto de formato (competencia de tfg-master-ieee):** la guía genérica sugiere la fuente Courier para las URL. La plantilla LaTeX no lo aplica.

### 1.3 Diferencias y defectos de la plantilla oficial (`ptfg_ieee.pdf`)

La plantilla es el modelo que el estudiante copiará, así que estas diferencias importan para no penalizar injustamente y para no validar errores heredados:

- **(a) Misma fuente con varios números.** El mismo libro (Hernández Sampieri et al., *Metodología de la investigación*, 5.ª ed., 2010) aparece como **tres referencias distintas** ([6], [9] y [10]), que solo difieren en las páginas, y [10] usa la raya "——" de autor repetido, típica de BibTeX (IEEEtran). Esto **contradice** la regla "una fuente, un número". En IEEE estricto sería **una sola** referencia citada como `[6, pp. 350-353]`, `[6, pp. 85-87]`, etc.
  **Mi criterio:** si el TFG hace lo mismo, lo registro como **observación**, no como error, porque es práctica avalada por la plantilla, y recomiendo la forma IEEE.
- **(b) Formato de acceso web diferente.** La plantilla usa `..., <año>, obtenido el <fecha> de <URL>.`. La guía usa `Accedido: <fecha>. [En línea]. Disponible en: <URL>` o `<URL> (Accedido: <fecha>)`. **Hay tres convenciones válidas en el material**: acepto cualquiera, pero debe usarse **una sola en todo el documento**.
- **(c) Referencias web formateadas como libros.** En la plantilla, páginas web y blogs aparecen con el título en cursiva, como si fueran libros ([1], [2], [3], [7]).
- **(d) Artefactos de BibTeX:** fecha `01 2000` (mes numérico), `vol. Año V`, `c. 2011` (circa) y libro con `pp 350-353` sin punto y sin los dos puntos entre lugar y editorial (`México D.F. McGraw-Hill.`), en contra del esquema de la guía (`Lugar: Editorial, Año`).
- **(e) Calidad de las fuentes de ejemplo:** la plantilla y la guía citan blogspot, DocPlayer, StuDocu y SlideShare. **La cátedra no prohíbe** este tipo de fuentes, pero son de baja trazabilidad (ver checklist H).
- **(f) Puntuación de comillas inconsistente:** la referencia [11] de la plantilla usa `,"` (coma dentro de las comillas, IEEE angloamericano), mientras los ejemplos de la guía usan `".` o `",` (fuera). Lo acepto si es consistente.

**Jerarquía que aplicaré cuando el material se contradiga:**
1. **Plantilla `ptfg_ieee.pdf`** para el estilo de cita en el texto y la estructura (lo que la cátedra tolera).
2. **`Formato IEEE-resumido.pdf`** (adaptación FPUNE) y **`Guía-uso-de-norma-IEEE-y-más.pdf`** para el formato de cada tipo de referencia, porque las referencias de la plantilla no sirven como modelo fiable.
3. **IEEE Reference Guide oficial / biblioguía UAM** como desempate final.

Nunca marco como error algo que la plantilla oficial hace. Lo registro como "observación: difiere del IEEE estricto".

---

## 2. Checklist operativo para verificar las citas de un TFG

> **Principio forense:** ninguna cita es VÁLIDA por defecto. Si un punto no se puede comprobar, la cita queda como **DUDOSA**, nunca como válida.

### A. Inventario (antes de juzgar nada)
- [ ] Extraer **todas** las citas `[n]` del cuerpo con su ubicación (sección y párrafo) y la afirmación que respaldan.
- [ ] Extraer **todas** las entradas de la lista de referencias.
- [ ] Construir una matriz: n.º, primera aparición, nº de apariciones, entrada en la lista, tipo de fuente y estado de verificación.

### B. Formato de la cita en el texto
- [ ] Va entre corchetes, con un espacio antes y antes de la puntuación.
- [ ] La numeración sigue el orden de **primera** aparición (la primera cita nueva es [1], la siguiente [2], etc.).
- [ ] Hay un solo número por fuente (la misma obra no aparece con dos números; salvo el caso 1.3-a, que es una observación).
- [ ] Las citas múltiples siguen un estilo consistente (separado o agrupado) en todo el documento.
- [ ] No aparecen autor ni fecha innecesarios, ni "la referencia [n]" a mitad de oración.
- [ ] Las citas textuales van entre comillas, con cita, y son exactas; las omisiones se marcan con "...".
- [ ] No hay párrafos sin cita que contengan datos, cifras, definiciones o ideas claramente ajenas (riesgo de plagio por omisión).
- [ ] No hay citas de cita ("según X, citado en [n]" o afirmaciones de una fuente primaria que el estudiante no consultó).

### C. Correspondencia entre texto y lista de referencias
- [ ] Toda cita `[n]` tiene su entrada `[n]` en la lista (sin **citas huérfanas**).
- [ ] Toda entrada de la lista está citada al menos una vez (sin **referencias fantasma o de relleno**).
- [ ] Los números de la lista son consecutivos y sin saltos ni duplicados.
- [ ] En los antecedentes, el título mencionado en el texto coincide con el título de la referencia `[n]`.

### D. Formato de cada referencia según su tipo (comparar con la sección 4)
- [ ] El tipo de fuente está bien identificado (libro, capítulo, artículo, conferencia, tesis, informe, norma o ley, web, video).
- [ ] Están todos los elementos obligatorios del tipo y en su orden: autor, título, edición, lugar: editorial, vol., n.º, pp., mes y año, `[En línea]`, Disponible en, fecha de acceso.
- [ ] Autores con iniciales y apellidos, más de seis autores como `et al.`, e institución tal como figura en la fuente.
- [ ] Cursiva y comillas según el tipo, y mayúsculas según la regla 1.2-6.
- [ ] Hay DOI cuando existe (y la URL sobra). Los recursos web sin DOI llevan fecha de acceso.
- [ ] La convención de acceso web (1.3-b), el uso de "y" o "and", las abreviaturas de mes y la puntuación de las comillas son uniformes en toda la lista.

### E. Existencia real de la fuente (el núcleo forense)
- [ ] **DOI:** resuelve en `doi.org` y **lleva a esa misma obra** (mismo título, autores y año). Un DOI que resuelve a otro artículo es un indicio de fabricación.
- [ ] **Artículos y conferencias:** localizados en Crossref, Google Scholar, IEEE Xplore, ScienceDirect, SpringerLink o en el sitio de la revista. Comprobar que la revista existe y que publicó ese volumen y número en ese año.
- [ ] **Libros:** ISBN o registro en WorldCat o en la editorial. La edición y el año deben ser coherentes (por ejemplo, que la 5.ª ed. exista en ese año).
- [ ] **Tesis y TFG:** localizados en el repositorio institucional de la universidad indicada.
- [ ] **Leyes, decretos y normativa:** localizados en el portal oficial del organismo emisor o en el repositorio legislativo oficial, con número y fecha exactos.
- [ ] **Páginas web:** la URL responde y el contenido coincide. Si está caída, buscar copia en Wayback Machine. Si no aparece ninguna copia, la cita queda como **DUDOSA**.
- [ ] Si la fuente no se encuentra por ninguna vía, se marca **NO VERIFICABLE / DUDOSA** y se pide al estudiante el PDF o el enlace. Nunca se presume que existe.

### F. Consistencia de datos (referencia frente a fuente real)
- [ ] Coinciden con la fuente: ortografía de autores y su orden, título exacto, nombre de la revista, año, volumen, número, rango de páginas, editorial y edición.
- [ ] El rango de páginas es plausible y está dentro del volumen.
- [ ] La fecha de acceso no es anterior a la publicación ni posterior a la fecha de entrega, y no hay fechas futuras.
- [ ] El dominio de la URL corresponde al autor o institución declarados.
- [ ] El año que figura en el texto (si se menciona) coincide con el de la referencia.

### G. Fidelidad del contenido (lo que la fuente dice frente a lo que el TFG le atribuye)
- [ ] La afirmación que respalda `[n]` **está realmente en la fuente** (no la exagera, no la invierte, no la generaliza).
- [ ] Las cifras, estadísticas, fechas y definiciones atribuidas son exactas.
- [ ] Las citas textuales coinciden palabra por palabra con el original.
- [ ] En los antecedentes, el resumen, el "aporte" y la "diferencia" describen correctamente el trabajo citado (siguiendo el patrón de `Analisis-antecedente.pdf`).

### H. Calidad y pertinencia de la fuente (recomendaciones, no causa de invalidez)
- [ ] Hay preferencia por fuentes revisadas por pares y actuales, como sugiere `leer_art_cientifico.pdf`.
- [ ] Se señalan las fuentes de baja trazabilidad (blogs, DocPlayer, StuDocu, SlideShare, Wikipedia, contenido generado por IA) y se sugiere sustituirlas por la fuente original.
- [ ] La fuente es pertinente para la sección donde se usa (marco teórico, antecedentes, método).

### Señales de alerta de cita fabricada (por ejemplo, generada por IA)
- Título verosímil pero inexistente, atribuido a autores reales del área.
- DOI con un prefijo que no corresponde a la editorial declarada, o que resuelve a otra obra.
- Volumen o número inexistente para esa revista o ese año, o páginas incoherentes.
- Coautores que no aparecen en ningún registro, o un "et al." que oculta una autoría inexistente.
- URL con estructura plausible que devuelve 404 y no tiene ninguna copia archivada.
- Datos "demasiado perfectos" (cifras redondas o una cita textual que no aparece en el texto completo).

---

## 3. Qué cuenta como cita inválida o inventada y con qué severidad

### 3.1 Lo que dice (y no dice) el material
- **La rúbrica `Criterios evaluación 2do parcial-TFG I.pdf` no contiene ningún criterio sobre citas o referencias.** Solo evalúa:
  - a) la presentación en PowerPoint (10 puntos: secuencia, cantidad de texto, colores y letra);
  - b) la exposición oral (25 puntos: dominio, no leer, lenguaje, postura y tiempo de 10 minutos).
  - Además tiene incoherencias internas: el apartado b) indica "10%" pero suma 25 puntos, y la numeración salta del ítem 4 al 6.
- **El Reglamento** (versión resumida) exige que el TFG "debe contener originalidad" (Art. 4), pero **no tipifica** el plagio ni las sanciones. La resolución completa (Res. 143/2022), enlazada en el propio PDF, no está en la carpeta, así que este punto queda **pendiente de revisión**.
- **La guía** define el **plagio** como copiar total o parcialmente una obra ajena, de forma literal o simulada, sin reconocer la autoría. Pone como ejemplo insertar párrafos de otra obra sin citarlos. También **prohíbe la cita de cita**.
- **El formato resumido** recuerda que la producción de la FPUNE se publica bajo **CC BY-NC-SA**, lo que hace obligatoria la atribución.

### 3.2 Escala de severidad

Como la cátedra no fija una escala, **esta es una propuesta mía derivada de las reglas anteriores**. Debe confirmarse con el docente.

| Severidad | Casos | Veredicto |
|---|---|---|
| **CRÍTICA** (integridad académica) | La fuente no existe. El DOI o la URL llevan a otra obra. La combinación de autor, título y año no existe. Se atribuye a la fuente algo que no dice. Hay una cita textual sin comillas o un párrafo ajeno sin cita (plagio según la definición de la guía). Se presenta una cita de cita como fuente primaria. | **INVÁLIDA, FABRICADA o PLAGIO.** Hay que eliminarla o sustituirla. |
| **ALTA** (rompe la trazabilidad) | Cita huérfana (sin entrada en la lista). Referencia que nadie cita. Una misma fuente con números en conflicto que confunden al lector. Datos tan erróneos (autor, año, título) que la fuente no se puede localizar. URL muerta sin copia archivada. | **INVÁLIDA**, corregible. |
| **MEDIA** (incumple la norma) | Numeración fuera del orden de aparición. Lista ordenada alfabéticamente. Faltan elementos obligatorios (fecha de acceso en la web, vol., n.º, pp., editorial). Se usa el esquema de otro tipo de fuente. Se pone URL cuando existe DOI. Se usa APA u otro estilo en lugar de IEEE. | **VÁLIDA CON ERRORES DE FORMATO.** |
| **BAJA** (estilo) | Puntuación, cursivas, mayúsculas, espacio entre iniciales, abreviatura de meses, "y" o "and", estilo de citas múltiples o convención de acceso usados de forma inconsistente. Mismo libro en varias entradas por página (la práctica de la plantilla). | **OBSERVACIÓN.** |
| **SIN DETERMINAR** | La existencia o el contenido no se pudieron comprobar con los medios disponibles. | **DUDOSA / NO VERIFICABLE.** Nunca se presume válida. |

Veredictos posibles por cita: `VERIFICADA` · `VERIFICADA CON OBSERVACIONES` · `VÁLIDA CON ERRORES DE FORMATO` · `DUDOSA` · `INVÁLIDA` · `FABRICADA/INEXISTENTE`.

---

## 4. Ejemplos de referencia para comparar

> Importante: **los anexos (II y IV) no contienen ningún ejemplo de cita ni de referencia.** Los modelos están en la guía extendida, el formato resumido, la plantilla y el ejemplo de antecedente. Los ejemplos de la guía también tienen pequeños errores; los indico para no tomarlos como un patrón perfecto.

### 4.1 Esquemas por tipo de fuente (de la guía; los elementos y su orden son los exigibles)

| Tipo | Esquema |
|---|---|
| Libro impreso, 1 autor | `[#] N. Apellido, *Título del libro*, Edición. Lugar: Editorial, Año.` |
| Libro impreso, 2 autores | `[#] N. Apellido1 y N. Apellido2, *Título*, Edición. Lugar: Editorial, Año.` |
| Libro, más de 6 autores | `[#] N. Apellido1 et al., *Título*, Edición. Lugar: Editorial, Año.` |
| Capítulo de libro | `[#] N. Apellido, "Título del capítulo", en *Título del libro*, N. Apellido, Ed., Edición. Lugar: Editorial, Año, cap. x, sec. x, pp. x-x.` |
| Artículo de revista impresa | `[#] N. Apellido, "Título del artículo", *Revista (abreviada)*, vol. x, no. x, pp. x-x, Mes Año.` |
| Libro electrónico | Esquema de libro + `[En línea]. Disponible en: URL` |
| Artículo de revista electrónica | Esquema de artículo + `Accedido: fecha. [En línea]. Disponible en: URL/DOI` (sin fecha de acceso si hay DOI) |
| Página web | `[#] N. Apellido (o institución). "Título de la página". *Sitio web*. URL (Accedido: fecha).` |
| Video en línea | `[#] Creador. *Título del video*. (Fecha de publicación). Accedido: fecha. [Video en línea]. Disponible en: URL` |

El material **no trae esquemas** para conferencias, tesis, informes técnicos, normas, leyes, patentes ni comunicaciones personales. Para esos tipos aplicaré la IEEE Reference Guide oficial y la biblioguía UAM (ver A6).

### 4.2 Ejemplos concretos del material (para comparar)

**Libro (formato resumido y guía):**
```
[1] B. Klaus and P. Horn, Robot Vision. Cambridge, MA: MIT Press, 1996.
```
Es el modelo canónico de libro en IEEE (*título en cursiva*, `Lugar: Editorial, Año`). Nota: en ambos documentos aparece escrito "Robot Visión", con una tilde errónea; aquí va corregido. En los demás ejemplos de esta sección también normalicé espacios e iniciales y lo indico en cada caso.

**Capítulo en libro editado (formato resumido y guía):**
```
[2] R. L. Myer, "Parametric oscillators and nonlinear materials," in Nonlinear Optics,
    vol. 4, P. G. Harper and B. S. Wherret, Eds. San Francisco, CA: Academic, 1977, pp. 47-160.
```

**Libro con 2 autores (guía):**
```
[2] D. L. Nelson y M. M. Cox, Lehninger Principles of Biochemistry, 6.ª ed. Nueva York,
    NY, USA: W.H. Freeman and Company, 2012.
```
En el original falta el espacio entre las iniciales ("D.L.", "M.M."), lo que contradice su propia regla.

**Artículo de revista electrónica con más de 6 autores y DOI (guía):**
```
[10] N. Akhlaghi et al., "Real-Time Classification of Hand Motions Using Ultrasound
     Imaging of Forearm Muscles", IEEE Transactions on Biomedic..., vol. 63, no. 8,
     pp. 1687-1698, ago. 2016. [Online]. Available: http://dx.doi.org/10.1109/TBME.2015.2498124
```
Es un buen modelo de estructura. Defectos del ejemplo: el nombre de la revista está truncado (*IEEE Transactions on Biomedical Engineering*), mezcla español e inglés ("ago.", "[Online]. Available") y usa el resolvedor antiguo `dx.doi.org` en lugar de `https://doi.org/`.

**Artículo de revista con handle (guía):**
```
[9] M. J. Gómez López, "Prototipo electrónico de control y monitoreo de parámetros ambientales
    implementando internet de las cosas", Revista Tecnológica, vol. 11, no. 11, pp. 11-18,
    Ene./Dic. 2018. Accedido: 20-jul-2020. [En línea]. Disponible en: http://hdl.handle.net/10972/3617
```

**Página web (guía):**
```
[11] IEEE Foundation. "Typography". ieeefoundation.org.
     https://www.ieeefoundation.org/ieee-units/brand/typography (Accessed: 30-jun-2020)
```

**Artículo de revista (plantilla oficial, estilo IEEEtran):**
```
[11] R. Dean, "La investigación tecnológica en las ciencias de la ingeniería y la innovación
     tecnológica," Revista Voces de la Universidad - Universidad Nacional de Río Cuarto - U.N.R.C.,
     vol. Año V, pp. iv – vi, 01 2000.
```
Sirve como modelo de la puntuación `,"`. La fecha y el volumen son artefactos de BibTeX y no deben imitarse.

**Libro (plantilla oficial):**
```
[6] R. Hernández Sampieri, C. Fernández Collado, y M. P. Baptista Lucio,
    Metodología de la investigación. 5a ed. México D.F. McGraw-Hill. pp 350-353, 2010.
```
Muestra el uso de "y" entre autores. Faltan los dos puntos (`México D.F.: McGraw-Hill`), no debería llevar páginas en la referencia y repite la obra en [9] y [10].

**Web (plantilla oficial, convención "obtenido el"):**
```
[7] E. Arrieta, Método inductivo y deductivo. Diferenciador.com, 2020, obtenido el
    6 de septiembre de 2021 de https://www.diferenciador.com/diferencia-entre-metodo-inductivo-y-deductivo/.
```

### 4.3 Ejemplos de cita en el texto (formas aceptadas)
- Simple: `... la temática consultada [6].`
- Con autor relevante: `Sinisterra [3] elaboró ...`
- Múltiple preferida: `En algunos estudios recientes [3], [4], [5] se ha ...`; rango `[1]-[5]`.
- Múltiple tolerada (la usa la plantilla): `... producto o servicio tecnológico [1, 2].`
- Remisión: `Ver [9]`, `En [9]`, `Como se mencionó anteriormente [2], [4]-[7], [9]`.
- Cita textual (plantilla): `a decir de [11]: la realizabilidad tecnológica "Lo es materialmente si ..."`.
- Antecedente (patrón de la cátedra): `El trabajo de <Título del trabajo> [15], presentó <qué hizo>. Con respecto al proyecto propuesto, aporta <similitud>. No obstante, difiere en <brecha>.`
  Nota: el propio ejemplo contiene una frase duplicada ("No obstante, el presente proyecto difiere de dicho trabajo El proyecto presentado difiere...") y su guía de estructura menciona la librería `face_recognition`, que no aparece en el texto del ejemplo. Esto muestra que debe verificarse que lo que se atribuye a un antecedente esté realmente en él.

---

## 5. Ambigüedades detectadas en el material

| # | Ambigüedad | Criterio que aplicaré |
|---|---|---|
| A1 | **Citas múltiples:** la guía prefiere `[1], [3]`, acepta `[1, 3]`, y la plantilla usa `[1, 2]`. La UAM exige corchetes separados. | Acepto ambas formas si son consistentes; recomiendo la separada. |
| A2 | **Misma fuente y distintas páginas:** la plantilla crea entradas separadas ([6], [9], [10]), lo que contradice "una fuente, un número". | Observación (BAJA); recomiendo `[n, pp. x-y]`. |
| A3 | **Meses:** la regla pide abreviaturas en español, pero los ejemplos usan "Ene./Dic.", "ago.", "jul" y "01". | Acepto abreviaturas en español o en inglés si son consistentes. |
| A4 | **Acceso web:** tres convenciones ("obtenido el ... de", "Accedido: ... [En línea]. Disponible en:", "URL (Accedido: ...)"). | Cualquiera, pero una sola en todo el documento. La fecha de acceso es obligatoria si no hay DOI. |
| A5 | **Cita textual:** no se exige número de página (la plantilla no lo pone). | No la invalido si falta la página, pero verifico el texto literal en la fuente y recomiendo `[n, p. x]`. |
| A6 | **Tipos sin esquema** (conferencia, tesis, informe, ley o norma, patente, comunicación personal). | IEEE Reference Guide oficial y biblioguía UAM. |
| A7 | **No hay rúbrica de citas:** la evaluación del 2.º parcial es solo oral, y el Reglamento resumido no define sanciones por plagio. | La escala de la sección 3.2 es una propuesta mía; hay que confirmarla con el docente y revisar la Res. 143/2022 completa. |
| A8 | **Título de la sección:** "Referencias Bibliográficas" (plantilla) o "Referencias" (guía). | Acepto ambos, uno solo en el documento. |
| A9 | **Fuentes de baja calidad** (blogs, DocPlayer, StuDocu, SlideShare) aparecen en los ejemplos de la propia cátedra. | No invalidan la cita; recomiendo sustituirlas por la fuente original. |
| A10 | **Conector entre autores e idioma de los elementos** ("y"/"and", "Disponible en"/"Available", "ed."). | Acepto ambos idiomas si son consistentes. |
| A11 | **Puntuación con comillas:** `,"` (plantilla) o `",` (guía). | Acepto cualquiera si es consistente. |
| A12 | **Imágenes no extraídas** en varios PDF. | Si el docente aporta una regla gráfica adicional, este protocolo se actualizará. |
