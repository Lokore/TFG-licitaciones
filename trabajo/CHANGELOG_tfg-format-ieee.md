# CHANGELOG — tfg-format-ieee (maquetación y apariencia visual)

Archivo corregido: `C:/TFG/trabajo/Anteproyecto_licitaciones_Ivan_Alex_CORREGIDO.docx`
Copia de respaldo creada antes de tocar nada: `Anteproyecto_licitaciones_Ivan_Alex_CORREGIDO.docx.bak`
(permite comparar/revertir en caso de duda; no se modificó ninguna palabra de contenido, redacción ni citas, solo formato visual).

Herramienta: python-docx 1.2.0 + manipulación directa de XML (oxml) para lo que python-docx no cubre (lista multinivel, campo TOC, salto de sección, fldChar).

---

# AJUSTE PUNTUAL (17/11/2026): reflejar en el .docx la corrección de contenido de tfg-master-ieee (duplicación en §1, párrafo 4)

**Origen:** tfg-master-ieee corrigió en `anteproyecto_borrador.md` la última oración del párrafo 4 de la sección 1 (anticipaba casi palabra por palabra el enunciado formal del cierre de la sección). Ver su changelog, entrada "CONSULTA DEL ESTUDIANTE". El `.docx` de ronda 2 que yo había generado (14:22) es anterior a ese cambio en el markdown (14:30), así que seguía con la oración antigua.

**Respaldo:** copié el `.docx` de ronda 2 (completo, con todo el formato ya aplicado) a `Anteproyecto_licitaciones_Ivan_Alex_CORREGIDO.ronda2-pre-fix-duplicado.docx.bak` antes de tocar nada.

**Decisión de método:** no reconstruí el documento desde cero con `md_to_docx_v2.py` + reaplicación completa de todo el post-procesado de ronda 2 (tipografía, portada, numeración, TOC, secciones, tablas, etc.), porque ese único cambio de contenido no altera nada de la estructura ni de los demás párrafos, y el `.docx` de ronda 2 ya tenía todo el formato correcto y verificado. Regenerar todo el pipeline para cambiar una sola oración habría sido innecesario y más arriesgado (reintroducir un bug de formato ya resuelto) que una edición quirúrgica. Edité directamente, con python-docx, el único párrafo afectado (índice 36, "Conviene distinguir dos planos…", estilo `Normal`, un solo run, sin negrita/cursiva), reemplazando el texto interno del run por el párrafo completo con la oración ya corregida, carácter por carácter igual al markdown actualizado. No toqué el resto del párrafo (distinción real/conocimiento, el `[PENDIENTE]`) ni ningún otro párrafo.

**Verificación mecánica (reabriendo el `.docx` final con python-docx):**
- La oración antigua ("...consiste en determinar si un prototipo web que aplique de forma trazable...") tiene 0 ocurrencias en todo el documento (párrafos y celdas de tabla).
- La oración nueva ("...es de otra naturaleza: la falta de evidencia sobre los efectos de automatizar...") y la remisión ("Su enunciado formal se presenta al cierre de esta sección.") aparecen exactamente 1 vez cada una.
- El enunciado formal en cursiva del cierre de la sección 1 ("No se dispone de evidencia sobre si un prototipo web...") sigue apareciendo exactamente 1 vez, sin tocar.
- Comparación párrafo a párrafo contra el backup pre-ajuste: el único índice de párrafo con texto distinto es el 36; los 349 restantes son idénticos. Conteo total de párrafos (350), tablas (2) e imágenes (2) sin cambios.
- Formato de ronda 2 reconfirmado intacto: `Normal`/`Heading 1-4` en Times New Roman con sus tamaños y negrita/cursiva de ronda 2; los 266 párrafos `Normal` con texto (excluyendo los que solo contienen imagen) están justificados, salvo los 13 de portada/título repetido que siguen centrados a propósito (igual que en ronda 2); campo TOC presente en el XML; 2 secciones (portada sin pie, cuerpo con pie y `pgNumType start="1"`); las 2 tablas conservan encabezado en negrita y `w:tblHeader` activo; "Referencias Bibliográficas" conserva su `numPr` con `numId="0"` (sin número de sección); cero residuos de `**`, `<!--` o `[^` en todo el documento; las 19 partes XML del paquete parsean sin error con `lxml`.
- No fue necesario regenerar `trabajo/img/figura_fases.png` ni tocar `FIGURE_IMAGES` en `md_to_docx_v2.py`: ninguna de las dos figuras ni sus epígrafes se vieron afectados por este cambio.

**Limitación:** sigo sin acceso a Microsoft Word real; la verificación es estructural (XML válido + API de python-docx), no una renderización visual. Se recomienda, como en rondas anteriores, abrir el archivo en Word y actualizar campos (F9 sobre el índice) antes de imprimir o exportar a PDF.

---

# RONDA 2 (17/11/2026): devolución real de la profesora — pendientes de formato (GB4, GB17, cronograma, índice)

**Punto de partida:** el contenido se reescribió sustancialmente en `anteproyecto_borrador.md` tras la devolución real de la profesora (24 comentarios). Leí las secciones RONDA 2 de `CHANGELOG_tfg-master-ieee.md`, `CHANGELOG_citation-verifier-master.md` y `CHANGELOG_tfg-writer-formal.md` antes de tocar nada.

**Respaldo:** antes de regenerar, copié el `.docx` que dejó la ronda 1 (resultado final, ya con todas mis correcciones de ronda 1 aplicadas) a `Anteproyecto_licitaciones_Ivan_Alex_CORREGIDO.ronda1-final.docx.bak`. El `.bak` original de la ronda 1 (pre-arreglos, con fuente Aptos y sin numeración/TOC/secciones) se conserva sin tocar.

**Método:** el `.docx` final de la ronda 1 ya tenía resuelta toda la "infraestructura" de estilos (Times New Roman en `docDefaults`/`Normal`/`Heading 1-4`, lista multinivel vinculada a los estilos de título vía `numId=100`, estilo `TOC Heading`, `w:updateFields` activo, pie de página con campo `PAGE` y `pgNumType start="1"`). Usé ese `.docx` como **base de estilos** para `md_to_docx_v2.py` (actualizado, ver abajo), lo que significa que `clear_body()` preserva automáticamente toda esa infraestructura (vive en `styles.xml`, `numbering.xml`, `settings.xml`, partes que `clear_body` no toca) y solo se pierde el salto de sección de la portada (que vivía en el `pPr` de un párrafo del cuerpo, borrado junto con el resto). Después de la conversión básica, reapliqué **todas** las correcciones de la sección 1 de este changelog (ronda 1) sobre el contenido nuevo, más los 4 pendientes de esta ronda. Verifiqué cada paso reabriendo el archivo con python-docx (nunca asumí que un script hubiera funcionado sin comprobarlo), y al final parseé las 19 partes XML del paquete con `lxml` para confirmar que ninguna quedó mal formada.

## 1. GB4 — Alineación justificada en el cuerpo

- El estilo `Normal` del `.docx` base ya tenía `w:jc="both"` desde la ronda 1, pero lo reafirmé **explícitamente a nivel de párrafo** en los 278 párrafos de prosa del cuerpo (no en celdas de tabla, no en la portada/índice/título, que quedan centrados a propósito), para que la justificación no dependa solo de la herencia del estilo y sea verificable párrafo por párrafo.
- Verificación mecánica: iteré todos los `doc.paragraphs` posteriores al título repetido (inicio real del cuerpo) con estilo `Normal` y texto no vacío, excluyendo los párrafos que solo contienen una imagen; **cero** quedaron con una alineación distinta de `JUSTIFY`.
- Los encabezados (`Heading 1-4`) siguen alineados a la izquierda (como en la ronda 1) y la portada, el "Índice" y el título repetido siguen centrados: la instrucción de la profesora pide justificar la prosa, no el título.

## 2. GB17 — Figura de las 5 fases del diseño de la investigación

- tfg-master-ieee dejó en 8.1.2 un comentario HTML con la especificación completa del diagrama (5 cajas encadenadas por flechas, con sus OE/tareas/hipótesis/producto, una flecha discontinua de la Fase III a la Fase IV, y tres bandas de "componente" debajo agrupando las fases I-II, III y IV).
- **Generé la imagen** con matplotlib (instalé el paquete, no estaba disponible) en `C:/TFG/trabajo/img/figura_fases.png`: 5 cajas con flechas de secuencia, flecha discontinua naranja Fase III→IV con el rótulo "gestión institucional y selección de expertos en paralelo", y las tres bandas de componente con líneas punteadas de conexión, siguiendo el contenido del comentario al pie de la letra.
- Actualicé `FIGURE_IMAGES` en `C:/TFG/.claude/scripts/md_to_docx_v2.py`: `'Figura 1:' → figura_fases.png`, `'Figura 2:' → figura1.png` (el antiguo diagrama funcional, que pasa a ser la Figura 2). `figura2.png` (el viejo flujo de tareas) ya no se referencia desde el markdown y quedó sin usar; no lo borré del disco por si alguien quiere consultarlo.
- Verifiqué por orden real de los párrafos que la Figura 1 (nueva, fases) y la Figura 2 (diagrama funcional) quedaron en el cuerpo en ese orden, cada una con su párrafo de imagen centrado inmediatamente antes de su epígrafe "Figura N:".

## 3. Cronograma (Tabla 1): meses combinados sobre Q1/Q2

- La tabla tenía 17 columnas (1 de tareas + 16 quincenas Ene.Q1...Ago.Q2) y 34 filas de tareas/subtareas, exactamente como describe el comentario HTML dejado para mí en el markdown.
- Inserté una **fila nueva por encima** del encabezado existente, con python-docx (`table.add_row()` + reubicación del `<w:tr>` antes del primero): la celda de "Tareas" se fusionó verticalmente con la celda equivalente de la fila de abajo (`cell.merge`, con `vMerge` real en el XML), y cada par de columnas Q1/Q2 se fusionó horizontalmente bajo el nombre del mes correspondiente ("Enero 2027", ..., "Agosto 2027"; 8 fusiones, confirmé 8 `gridSpan` en el XML). La fila original se simplificó a "Q1"/"Q2" debajo de cada mes para no repetir el nombre del mes dos veces.
- Puse en negrita y centré ambas filas de encabezado, y activé `w:tblHeader` (repetir en cada página) en las dos.
- Puse en negrita las 7 filas de tarea principal (1 a 7), dejando las subtareas (1.1, 1.2, ...) sin negrita, tal como sugirió tfg-master-ieee.

## 4. Tabla 2 (operacionalización) y campo TOC

- Tabla 2 (4 columnas, 14 filas): encabezado en negrita + `w:tblHeader` activo, igual que en la ronda 1.
- **Índice:** el campo TOC (`TOC \o "1-4" \h \z \u`) se regeneró desde cero sobre la nueva estructura de encabezados (38 títulos con la jerarquía ya corregida por tfg-master-ieee: se eliminaron 7.2.1-7.2.3, se renombraron 8.1.1 y 8.1.2). Al no haber tocado la vinculación de la numeración a los estilos de título (se conserva de la ronda 1), Word recalculará automáticamente la numeración y la paginación la primera vez que se actualicen los campos.

## 5. Reaplicación del resto de correcciones de la ronda 1 sobre el contenido nuevo

Repetí, sobre el markdown actualizado, todo lo que ya estaba documentado en la sección 1 de este changelog (ronda 1), porque el script base (`md_to_docx_v2.py`) vuelve a generar el cuerpo "en bruto" cada vez que se regenera desde markdown:
- Portada centrada y jerarquizada por tamaños (igual que 1.2 de la ronda 1), sin tocar ni una palabra — **expresamente dejé sin tocar la línea "Profesor de la Cátedra: Lic. Gabriela Matilde Bobadilla de Almada" (GB1)**, pendiente de confirmación del estudiante, verificado carácter por carácter contra el original.
- Markdown (`**negrita**`/`*cursiva*`) convertido a formato real en los 278 párrafos de prosa reconstruidos (verificación: 0 asteriscos dobles restantes en todo el documento, incluidas celdas de tabla).
- Notas al pie `[^1]`-`[^3]` convertidas a superíndice + bloque de 9 pt, igual que en la ronda 1 (verificación: 0 ocurrencias de `[^` restantes).
- Comentarios HTML (3 en esta ronda: el aviso de regenerar el índice y los dos recordatorios de figuras 1/2, ya resueltos) eliminados del texto visible (verificación: 0 ocurrencias de `<!--` restantes).
- Numeración jerárquica real: se quitó el número tipeado a mano de los 38 encabezados de esta versión (antes eran 40; la diferencia es el contenido eliminado por tfg-master-ieee en GB11/GB13, no un error de formato). "Referencias Bibliográficas" (con mayúscula) conserva su `numPr` de anulación (`numId="0"`) para no recibir número de sección, igual que en la ronda 1.
- Dos secciones (portada sin pie de página / resto con pie y `pgNumType start="1"`): verifiqué por separado que la sección 1 no tiene `footerReference` ni `pgNumType` y que la sección 2 tiene ambos.

## 6. Verificación mecánica final

- 350 párrafos, 2 tablas, 2 imágenes en el documento final; las 19 partes XML del paquete parsearon sin error con `lxml`.
- Búsqueda de `**`, `<!--` y `[^` en todo el documento (párrafos de cuerpo y celdas de tabla): cero coincidencias.
- `hash` MD5 del archivo copiado a la ruta final coincide exactamente con el último archivo verificado, para descartar un copiado corrupto o parcial.
- **Sigo sin acceso a Microsoft Word real en este entorno**: la verificación es estructural (XML válido + API de python-docx), no una renderización visual. Recomiendo, igual que en la ronda 1, abrir el archivo en Word y aceptar la actualización de campos (o F9 sobre el índice) antes de imprimir o exportar a PDF.

## 7. Pendientes que NO resolví (fuera de alcance de formato)

- **GB1** (título de la profesora en portada, "Lic." vs "Ing. MSc."): dejado exactamente como está, a la espera de que el estudiante confirme.
- Todo lo demás que tfg-master-ieee, citation-verifier-master y tfg-writer-formal dejaron pendiente de contenido/citas en sus propios changelogs de ronda 2 no me corresponde y no lo toqué.

## 0. Diagnóstico inicial (por qué "seguía con el mismo formato")

El .docx generado por el script markdown→docx heredó los estilos (Heading 1-4, Normal, Table Grid) pero **no terminó de convertir varias cosas**, y eso es lo que el usuario veía como "mismo formato de siempre":

1. El índice era **texto estático tipeado a mano** (41 párrafos), no un campo de Word. Nunca se iba a sincronizar solo.
2. Había **un comentario HTML de Markdown filtrado como texto visible** justo debajo del título "Índice": `<!-- En Word: regenerar el índice automático (F9)... -->`. Y dos más, dentro del cuerpo, con instrucciones de contenido para actualizar las Figuras 1 y 2.
3. **Negrita y cursiva de Markdown nunca se aplicaron**: el documento mostraba literalmente los asteriscos, ej. `**Definición del problema:** *No se dispone de evidencia...*`, en vez de texto en negrita/cursiva real. Eran 35 párrafos así.
4. **Notas al pie en sintaxis Markdown sin convertir**: `[^1]`, `[^2]`, `[^3]` en el texto y `[^1]: Teléfono...` como párrafos sueltos, visibles tal cual.
5. **Mezcla de fuentes**: el estilo `Normal` fijaba Arial 11pt, pero los estilos Heading 1-4 no tenían fuente propia y heredaban del tema de Word ("Aptos Display"), es decir, cuerpo y títulos usaban tipografías distintas sin que se notara a simple vista hasta imprimir/revisar de cerca.
6. La **portada era texto plano sin ningún énfasis**: sin centrar, sin negrita, sin jerarquía de tamaños — todo en Arial 11pt alineado a la izquierda, indistinguible del cuerpo del documento.
7. Los encabezados ya tenían números **tipeados a mano** (correctos en este momento, pero frágiles: cualquier reordenamiento futuro los desincroniza, como ya le había pasado al índice).
8. El título final de referencias decía "Referencias bibliográficas" (b minúscula) en vez de "Referencias Bibliográficas", como exige la plantilla.
9. Numeración de página: todo el documento era una sola sección, por lo que la portada mostraba número de página visible, contra la regla de la plantilla ("la portada no se numera de forma visible y el índice es la página 1").

Lo que **ya estaba bien** y no se tocó:
- Tamaño de página: ya era A4 exacto (595.3 pt × 841.9 pt / 21 cm × 29.7 cm), confirmado contra `ptfg_ieee_texto.txt`.
- Márgenes: 3 cm izquierda/derecha, 2,2 cm superior, 2 cm inferior — no son el valor por defecto de Word, por lo que se asume que vienen del documento Word original del estudiante (posiblemente del Reglamento). Se **respetaron tal cual**, sin forzar 2,5 cm, siguiendo la instrucción de preferir los márgenes ya presentes en el original. **Queda como supuesto a confirmar**: no hay ningún documento de la cátedra que fije márgenes por escrito (así lo registra `analisis_tfg-master-ieee.md`, §2.1 y §5.1), así que si la profesora exige otro valor habrá que ajustarlo.
- Patrón de epígrafes "Tabla N" (encima de la tabla) y "Figura N" (debajo de la figura): ya estaba correctamente aplicado en los dos casos (Figura 1, Figura 2, Tabla 1, Tabla 2). Verificado por orden real de los elementos en el XML del cuerpo, no solo por posición aparente.
- Pie de página con campo `PAGE` real (no texto fijo) y centrado: ya estaba bien.
- Estilo de tabla `Table Grid` (con bordes) en ambas tablas: ya estaba aplicado.
- No se encontró ninguna ecuación en el cuerpo del documento (ni en línea ni en bloque), por lo que no aplicó el punto de formato de ecuaciones; si se agrega alguna más adelante, debe ir centrada con el número entre paréntesis alineado a la derecha, según el patrón de la plantilla (`ptfg_ieee_texto.txt`, pág. 15).

---

## 1. Correcciones aplicadas

### 1.1 Tipografía unificada
- `Normal`: Times New Roman 12 pt, justificado (antes: Arial 11 pt, sin alinear explícitamente).
- `Heading 1`: Times New Roman 16 pt negrita.
- `Heading 2`: Times New Roman 14 pt negrita.
- `Heading 3`: Times New Roman 13 pt negrita.
- `Heading 4`: Times New Roman 12 pt negrita cursiva.
- `docDefaults` del propio `styles.xml` también se llevó a Times New Roman, para que ningún texto futuro vuelva a heredar la fuente de tema ("Aptos").
- Encabezados: alineación izquierda y `keep-with-next` activado (evita que un título quede solo al final de una página).

### 1.2 Portada centrada y jerarquizada (párrafos 0-22)
Sin cambiar ni una palabra, se centró todo el bloque y se diferenciaron tamaños:
- Universidad / Facultad: 14 pt negrita, centrado.
- "Anteproyecto de Trabajo Final de Grado": 13 pt, centrado.
- Carrera / Cátedra: 12 pt, centrado.
- Título del trabajo: 16 pt negrita, centrado.
- Autores, profesor orientador, profesor de cátedra, lugar y fecha: 12 pt, centrado.
- El título repetido antes de la sección 1 (convención de la plantilla, pág. 2 del PDF original) también se centró y puso en 14 pt negrita.

### 1.3 Markdown sin convertir → formato real de Word
35 párrafos tenían `**negrita**` y/o `*cursiva*` literal en el texto. Se reconstruyeron sus runs para que esas marcas se conviertan en negrita/cursiva real de Word y los asteriscos desaparezcan del texto visible (el contenido entre marcas no se tocó). Ejemplo verificado:
- Antes (texto plano): `**Definición del problema:** *No se dispone de evidencia...*`
- Después: "Definición del problema:" en **negrita real**, seguido del enunciado del problema en *cursiva real* — exactamente el patrón que exige la plantilla (`ptfg_ieee_texto.txt`, línea 60: "Aquí se escribe en letras cursivas el enunciado del problema").

Se verificó que no quedó ningún asterisco suelto en el documento (ni en párrafos del cuerpo ni en celdas de tabla).

### 1.4 Comentarios de edición filtrados al cuerpo visible → eliminados
Se encontraron y quitaron del texto visible 3 comentarios HTML residuales de la conversión Markdown→Word (quedaban como párrafos normales, visibles para cualquier lector):

1. `<!-- En Word: regenerar el índice automático (F9) para obtener la paginación real... -->` → ya no aplica: se reemplazó el índice estático por un campo TOC real (ver 1.6).
2. `<!-- Actualizar la Figura 1 para que muestre el modo principal (regla del pliego), el módulo de contraste y la exportación a la plantilla común de informe. -->`
3. `<!-- Actualizar la Figura 2 para reflejar las tareas 4 a 6 reorganizadas y las tareas 8 y 9 con expertos externos y cegamiento. -->`

**Los puntos 2 y 3 son pendientes de CONTENIDO, no de formato** (hay que rehacer/actualizar las figuras 1 y 2 para que reflejen el texto actual). Se los retiro de la vista porque un comentario de Markdown suelto en un documento final de Word no es aceptable visualmente, pero **no me corresponde resolverlos**: quedan señalados aquí para tfg-writer-formal / tfg-master-ieee / el equipo de diagramación.

### 1.5 Notas al pie en sintaxis Markdown → formato visual de nota al pie
`[^1]`, `[^2]`, `[^3]` en el texto de los nombres de los autores y del profesor orientador se convirtieron en números en superíndice. Los párrafos `[^1]: Teléfono...`, `[^2]: Teléfono...`, `[^3]: [PENDIENTE...]` se reformatearon como bloque de notas en fuente reducida (9 pt) con el número en superíndice al inicio, igual que en la plantilla oficial (pág. 1 del PDF: "1Tel: , correo electrónico:").

**Limitación documentada:** estas NO son notas al pie nativas de Word (no están en `word/footnotes.xml` ni usan `w:footnoteReference`), son una aproximación visual (superíndice + texto pequeño en el mismo bloque de la portada, que es donde ya estaban ubicadas). Decidí no crear notas al pie nativas vía XML crudo porque implica agregar una parte nueva al paquete (`footnotes.xml` + relación + tipo de contenido) con mayor riesgo de corromper el archivo sin poder probarlo en Word real. **Si se necesitan notas al pie nativas**, se puede rehacer manualmente en Word: Insertar → Nota al pie, pegando el texto de cada una y borrando el bloque manual que dejé.

**Pendiente de contenido (no de formato):** el dato de contacto del Profesor Orientador sigue como `[PENDIENTE: teléfono y correo electrónico del Profesor Orientador.]` — hay que completarlo con el dato real antes de entregar.

### 1.6 Numeración jerárquica real (lista multinivel de Word)
- Se quitó el número tipeado a mano de los 40 encabezados (ej. "1. Definición del problema" → "Definición del problema"; "7.1.1.1. Evolución histórica" → "Evolución histórica"). Antes de quitarlos se verificó que la jerarquía manual ya era consistente con el contenido actual (no se detectaron saltos ni duplicados).
- Se creó una lista multinivel nueva en `word/numbering.xml` (abstractNumId/numId = 100, para no chocar con los 0-15/1-16 ya existentes) con formato decimal `%1.`, `%1.%2.`, `%1.%2.%3.`, `%1.%2.%3.%4.` (con punto final en todos los niveles, igual que la plantilla).
- Se vinculó esa lista a los estilos `Heading 1` (nivel 0), `Heading 2` (nivel 1), `Heading 3` (nivel 2) y `Heading 4` (nivel 3), tal como lo hace la función nativa de Word "Lista con varios niveles → vincular nivel a estilo". Esto significa que **la numeración ahora la genera Word automáticamente** a partir del estilo de cada título; si el usuario reordena o agrega secciones, los números se recalculan solos (no puede volver a desincronizarse como pasó con el índice).
- "Referencias Bibliográficas" quedó con un `numPr` de anulación (`numId=0`) a nivel de párrafo para que, pese a ser `Heading 1`, **no** reciba número de sección — igual que en la plantilla, donde "Referencias Bibliográficas" aparece sin número en el índice.

### 1.7 Título de la sección de referencias
"Referencias bibliográficas" → **"Referencias Bibliográficas"**, como pide literalmente la plantilla.

### 1.8 Índice: de texto estático a campo real de Word
- Se eliminaron las 41 líneas de índice tipeadas a mano (ya desincronizadas de la jerarquía real tras las ediciones de contenido de los otros agentes).
- Se insertó un **campo TOC real** (`TOC \o "1-4" \h \z \u`), que toma automáticamente los párrafos con estilo Heading 1 a 4 (con sus números, gracias al punto 1.6) y genera hipervínculos + números de página reales.
- El párrafo "Índice" pasó del estilo `Normal` al estilo `TOC Heading` (así no entra en la numeración de los Heading y mantiene el aspecto de título de la plantilla).
- Se activó `w:updateFields` en `settings.xml` para que Word ofrezca actualizar los campos (incluido el TOC y el número de página del pie) la primera vez que se abra el archivo.

**Acción manual pendiente en Word:** al abrir el archivo, Word puede preguntar "¿Desea actualizar este documento con los cambios?" o similar — aceptar. Si el índice sigue mostrando el texto de relleno ("Haga clic con el botón derecho... o presione F9"), seleccionarlo y presionar **F9**, o clic derecho → Actualizar campos → Actualizar toda la tabla. Se recomienda volver a presionar F9 justo antes de imprimir/exportar a PDF, por si se movió algún contenido después.

### 1.9 Paginación: portada sin número visible, índice = página 1
La plantilla exige explícitamente que "la portada no se numera de forma visible y el índice es la página 1". El documento tenía una sola sección (todo el documento comparte el mismo pie de página con número). Se dividió en dos secciones mediante un salto de sección en el párrafo en blanco anterior a "Índice":
- **Sección 1 (portada)**: mismo tamaño de página y márgenes, pero **sin pie de página** (por lo tanto, sin número visible).
- **Sección 2 (desde "Índice" en adelante)**: conserva el pie de página con el campo `PAGE` que ya existía, y `pgNumType start="1"` (ya estaba presente en el documento original), de modo que la página del Índice se numera como "1".

**Verificación pendiente en Word:** abrir el archivo y confirmar visualmente que la portada no muestra número de página y que la página del Índice muestra "1". Si Word muestra un número distinto, revisar Diseño → Números de página → Formato del número de página de esa sección.

### 1.10 Tablas: encabezado en negrita y repetición de fila
- Las dos tablas ya usaban el estilo `Table Grid` (bordes) — se dejó así.
- Se puso en negrita el texto del renglón de encabezado de ambas tablas (antes no tenía ningún énfasis).
- Se activó "repetir fila de encabezado en cada página" (`w:tblHeader`) en ambas, porque la Tabla 1 (cronograma, 12 filas × 17 columnas) y la Tabla 2 (operacionalización, 15 filas × 4 columnas) son largas y es probable que se corten entre páginas.

### 1.11 Epígrafes de tabla y figura
Verificado (no requirió corrección): "Tabla N:" aparece siempre inmediatamente ANTES de la tabla correspondiente, y "Figura N:" siempre inmediatamente DESPUÉS de la imagen correspondiente, coincidiendo con el orden real de los elementos en el cuerpo del documento (no solo con su posición aparente en pantalla).

### 1.12 Ecuaciones
No se encontró ninguna ecuación en el cuerpo del documento (ni en línea, ni en bloque, ni en notación de texto plano tipo LaTeX). No aplicó ninguna acción. Si se incorpora una ecuación más adelante, debe ir centrada, con el número entre paréntesis alineado a la derecha y citarse en el texto como "Ec. n", según el patrón de `ptfg_ieee_texto.txt` (págs. 14-15).

---

## 2. Verificación mecánica realizada

Todo lo anterior se verificó reabriendo el archivo guardado con python-docx (no se asumió que un script hubiera funcionado sin comprobarlo):
- Fuentes y tamaños de `Normal` y `Heading 1-4` reconfirmados tras guardar.
- Lista de encabezados reimpresa completa: los 40 títulos ya no llevan número tipeado, y "Referencias Bibliográficas" aparece correctamente renombrado.
- Búsqueda de `**`, `<!--` y `[^` en todo el documento (párrafos y celdas de tabla): cero coincidencias restantes.
- Orden real de los elementos del cuerpo (no solo el texto) para confirmar el patrón tabla-encima/figura-debajo.
- `numPr` de "Referencias Bibliográficas" confirmado con `numId="0"` (numeración anulada).
- Las dos secciones del documento confirmadas por separado: sección 1 (portada) sin `footerReference` ni `pgNumType`; sección 2 (desde Índice) con ambos, igual que antes.
- Las 21 partes XML internas del .docx (`document.xml`, `styles.xml`, `numbering.xml`, `settings.xml`, relaciones, etc.) se parsearon una por una con `lxml` para confirmar que ninguna quedó mal formada tras las ediciones.
- Total de párrafos, tablas e imágenes contado antes/después de cada etapa para confirmar que ninguna edición agregó o borró contenido fuera de lo esperado (41 líneas de índice + 3 comentarios eliminados, 1 párrafo de campo TOC agregado; neto: 449 → 406 párrafos, consistente con lo removido).

**No se tiene acceso a Microsoft Word en este entorno**, por lo que esta verificación es estructural (XML válido + API de python-docx), no una renderización visual real. Se recomienda que el usuario abra el archivo en Word como último paso y confirme visualmente los puntos marcados como "acción/verificación pendiente" arriba (1.8 y 1.9), además de revisar que no aparezca ningún diálogo de "contenido no legible" al abrir (no debería, dado que todas las partes XML son válidas, pero Word es más estricto que un parser XML genérico en algunos detalles de orden de elementos).

---

## 3. Pendientes para otros agentes (NO resueltos aquí, fuera de alcance de formato)

- **Contenido de la Figura 1**: actualizarla para reflejar el modo principal (regla del pliego), el módulo de contraste y la exportación a la plantilla común de informe (nota dejada por el equipo de redacción, ver 1.4).
- **Contenido de la Figura 2**: actualizarla para reflejar las tareas 4 a 6 reorganizadas y las tareas 8 y 9 con expertos externos y cegamiento (ver 1.4).
- **Dato de contacto del Profesor Orientador**: falta teléfono y correo electrónico (marcado como `[PENDIENTE: ...]` en la portada).
- **Márgenes**: confirmar con la cátedra si 3 cm (izq/der) / 2,2 cm (sup) / 2 cm (inf) son efectivamente los exigidos por el Reglamento; no hay ningún documento de la FPUNE que los fije por escrito (ver `analisis_tfg-master-ieee.md`, §2.1 y §5.1).
