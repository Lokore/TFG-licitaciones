# Changelog de formato (tfg-format-ieee)

Documento generado: `trabajo/Anteproyecto_licitaciones_Ivan_Alex_CORREGIDO.docx`
Fuente: `trabajo/anteproyecto_borrador.md` (contenido ya cerrado por tfg-master-ieee,
citation-verifier-master y tfg-writer-formal).

No existía una version previa de este .docx en `trabajo/`, por lo que no hubo
archivo que respaldar antes de generar el primero. Las herramientas usadas quedan
documentadas abajo para que cualquier regeneracion futura sea reproducible.

## Herramientas usadas (Bash + python-docx + oxml)

- `.claude/scripts/make_base_template.py` (nuevo): genera un `.docx` base con
  tamano de pagina, margenes y estilos (Normal/Heading 1-5/Title/Caption/TOC
  Heading/estilos propios de portada, subtitulo sin numerar y referencias).
- `.claude/scripts/md_to_docx_v2.py` (reescrito, conservando el nombre e idea
  original de "leer el .md y convertirlo a .docx con python-docx"): ahora hace
  todo el trabajo de maquetacion fina (numeracion multinivel real, campo TOC,
  figuras/tablas con epigrafe, tablas con ancho fijo y encabezado repetido,
  ecuacion con formato visual distinguible, correccion de puntuacion de las
  referencias, eliminacion de comentarios HTML internos del borrador).
- Verificacion: reapertura con `python-docx` (prueba de integridad de zip +
  lectura de parrafos/tablas/imagenes/secciones) y renderizado real con
  LibreOffice (`soffice --headless --convert-to pdf`, mas una macro UNO que
  fuerza la actualizacion del campo TOC) para inspeccionar visualmente cada
  cambio antes de darlo por bueno. Las capturas de ese PDF de verificacion
  confirmaron cada punto marcado como "Verificado" abajo.

## Cambios aplicados

1. **Tamano de pagina y margenes.** A4 (21 x 29.7 cm). Margenes estimados por
   medicion fisica directa de `ptfg_ieee.pdf` (el Reglamento y el Formato
   IEEE-resumido no especifican margenes por escrito): 3.5 cm izquierda/
   derecha/superior, 3.0 cm inferior. Verificado con python-docx
   (`section.page_width/height/left_margin/...`) y visualmente en el PDF de
   prueba.

2. **Fuente y tamano.** Times New Roman en todo el documento (cuerpo 12 pt,
   justificado IEEE/Reglamento no lo exigen explicitamente, pero coincide con
   el cuerpo CMR12 de `ptfg_ieee.pdf` y con mi propia recomendacion). Titulos
   y portada mantienen jerarquia de tamanos (Titulo 18 pt, Heading 1 16 pt,
   Heading 2 13 pt, Heading 3-5 12 pt, Heading 4-5 en cursiva) pero en la
   misma familia tipografica. Verificado programaticamente: todo run con
   fuente explicita en el documento final usa `Times New Roman` (no se
   detecto ninguna otra familia).

3. **Numeracion de secciones.** Decimal jerarquica 1., 1.1., ..., 7.1.1.3.1.
   (5 niveles), aplicada mediante una lista multinivel real de Word
   (`numbering.xml`, `abstractNum`/`num` creados con oxml) vinculada por
   `w:numPr` a cada parrafo `Heading 1-5`; ya no es texto escrito a mano en el
   titulo (el borrador traia los numeros tecleados en el propio texto del
   encabezado, p. ej. "## 7.1. Conceptos..."; el script los detecta con una
   expresion regular, los retira del texto visible y deja que Word los vuelva
   a generar automaticamente). 54 encabezados quedaron numerados asi.
   "Índice" y "Referencias Bibliográficas" quedan **sin** numero (como en la
   plantilla oficial, que los muestra sin prefijo numerico en el indice).
   Verificado abrido el .docx y comprobando `w:numPr` en cada Heading, y
   visualmente en el PDF de prueba (aparecen "1. Definición del problema",
   "8.1.2. Fase 1: ...", etc., calculados por Word/LibreOffice, no por mi).

   Caso especial: "Tipo de investigación" y "Enfoque de la investigación"
   (dentro de la seccion 8) estaban marcados como encabezado en el borrador
   pero **sin numero** y **no figuran en el indice estatico** que el propio
   borrador traia escrito a mano. Para no romper la numeracion automatica
   (un Heading intermedio sin numero generaria un salto invalido del tipo
   "8.0.1") y para respetar que el equipo de contenido ya decidio no
   numerarlos ni listarlos en el indice, los deje como parrafos en negrita
   con un estilo propio ("TFG Subtitulo sin numerar"), igual que el
   formato de titulo-de-parrafo en negrita-cursiva que usa la plantilla
   oficial para frases como "Citas en el texto y referencias...". No forman
   parte de la jerarquia Heading ni del TOC. Esto es una decision de
   maquetacion, no de contenido: el texto de ambos subtitulos no se toco.

4. **Índice (TOC).** Se elimino la lista estatica escrita a mano en el
   borrador y se inserto un campo TOC real de Word (`{ TOC \o "1-5" \h \z \u }`
   armado con oxml: `fldChar begin/separate/end` + `instrText`), con un
   parrafo de marcador de posicion en cursiva explicando como actualizarlo.
   Se activo `w:updateFields` en `settings.xml` para que Word recalcule el
   campo al abrir/imprimir. El titulo "Índice" usa el estilo integrado
   "TOC Heading" (visualmente igual a Heading 1 pero con `outlineLvl=9`) para
   que no se liste a si mismo dentro de su propio indice, tal como en la
   plantilla oficial. **Verificado de verdad, no solo supuesto:** force la
   actualizacion del campo con una macro UNO de LibreOffice y confirme en el
   PDF resultante que el indice se genera completo, con los titulos y
   numeros de pagina correctos, reflejando la estructura final (8.1.1 a
   8.1.11 fusionadas, "Referencias Bibliográficas" al final, sin los
   subtitulos "Tipo de investigación"/"Enfoque de la investigación").
   **Limitacion que no pude resolver del todo:** LibreOffice en modo
   headless normal (`--convert-to pdf` sin macro) no recalcula el campo TOC
   por si solo, asi que el .docx tal cual queda guardado en disco contiene el
   campo con un texto de marcador de posicion hasta que alguien lo abra en
   Word (o en LibreOffice Writer) y presione F9 / actualice campos. Esto es
   exactamente la limitacion que se anticipaba en mis instrucciones de
   trabajo; lo dejo documentado para que el usuario sepa que debe actualizar
   el indice una vez al abrir el documento.

5. **Título de Referencias.** "Referencias bibliográficas" (como estaba
   escrito en el borrador) se renderiza como "Referencias Bibliográficas"
   (mayuscula en ambas palabras), igual que en `ptfg_ieee.pdf`. Es un cambio
   de capitalizacion/formato, no de contenido.

6. **Tablas.** Las 2 tablas markdown (Tabla 1: cronograma de 9 columnas;
   Tabla 2: operacionalizacion de 4 columnas) se convirtieron a tablas Word
   reales (no texto con pipes): estilo "Table Grid" con bordes, fila de
   encabezado en negrita y centrada, fila de encabezado repetida
   automaticamente si la tabla salta de pagina (`w:tblHeader`), ancho de
   columna fijo calculado a partir del ancho util de la pagina (no ancho
   automatico, que en LibreOffice generaba columnas angostisimas). Se quito
   la marca markdown `**...**` de las celdas (fases/columnas en negrita del
   cronograma) y se aplico negrita real a esas celdas en vez de dejar los
   asteriscos como texto literal. Las celdas "X" quedan centradas, el resto
   alineado a la izquierda.

   **Problema encontrado y corregido durante la verificacion:** al principio
   las columnas de mes del cronograma (Ene, Feb, ...) partian el texto letra
   por letra ("E" / "ne"). La causa real (confirmada midiendo anchos de
   fuente con fontTools, no supuesta) no era el ancho de columna sino que las
   celdas heredaban la sangria de primera linea de 1.25 cm del estilo Normal
   del cuerpo del documento, que por si sola superaba el ancho de una columna
   angosta. Se corrigio poniendo sangria 0 explicitamente en los parrafos de
   celda de tabla. Para el cronograma ademas se redujo el tamano de fuente a
   10 pt (11 pt en la tabla de operacionalizacion) y se redujeron los
   margenes internos de celda, como excepcion documentada a la unificacion
   general en 12 pt: es una practica habitual y necesaria para que 9 columnas
   quepan en el ancho util de una pagina A4 sin desbordar; la familia
   tipografica (Times New Roman) se mantuvo igual en toda la tabla.

7. **Figuras.** `<!-- FIGURA: ... -->` se resolvio con las dos imagenes
   disponibles en `trabajo/img/`: Figura 1 = `figura_fases.png` (diagrama de
   flujo de las fases del trabajo, 8.1.1), Figura 2 = `figura1.png` (diagrama
   funcional del prototipo web, 8.1.6). Ambas se insertaron centradas, con
   ancho fijo de 14 cm (el ancho util de la pagina), y con el epigrafe
   "Figura N: ..." **debajo** de la imagen, en negrita solo la etiqueta
   "Figura N:", como exige la plantilla oficial (y nunca el estilo
   "Fig./TABLA" de IEEE de conferencias). `figura2.png` (diagrama de flujo de
   tareas del borrador anterior) ya no se referencia en el texto actual y no
   se uso. No hubo ningun marcador de figura sin imagen correspondiente: las
   2 imagenes disponibles cubren las 2 figuras citadas en el texto.

8. **Tablas: epigrafe.** "Tabla N: ..." se coloca **encima** de la tabla
   (orden que ya traia el markdown de forma natural: la linea de epigrafe
   precede al bloque de pipes), en negrita solo la etiqueta, estilo Caption
   sin el color azul tematico que trae por defecto la plantilla de
   python-docx (se quito explicitamente, junto con el borde azul tematico
   que traia por defecto el estilo "Title").

9. **Ecuaciones.** Se encontro **una** ecuacion escrita como texto plano con
   simbolos unicode de sumatoria/sub-indices (seccion 7.1.1.3.1, MAVT):
   `V(a) = Σⱼ₌₁ᵐ wⱼ · vⱼ(xⱼ(a)), wⱼ ≥ 0, Σⱼ₌₁ᵐ wⱼ = 1.` No la convertí a un
   objeto OMML nativo porque transcribir una expresion matematica a mano
   conlleva riesgo real de alterar su significado (sub/super-indices,
   multiplicacion, igualdad) sin que ese riesgo corresponda a mi rol de
   formato puro; en su lugar le di el tratamiento visual alternativo que
   permiten mis instrucciones: la deje centrada horizontalmente y le agregue
   numeracion entre parentesis alineada al margen derecho, "(1)", usando
   tabuladores de parrafo (centro a medio ancho, derecha al ancho completo),
   igual que el patron de "ecuaciones numeradas" de `ptfg_ieee.pdf`. No se
   modifico ni un caracter del contenido matematico. No se encontraron mas
   ecuaciones en el documento.

10. **"Definición del problema:" en cursiva al cierre de la sección 1.**
    **No pude aplicar este punto de la plantilla porque el contenido no lo
    tiene todavia**: la sección 1 del borrador actual termina con la lista de
    4 preguntas secundarias y pasa directo a la sección 2, sin el parrafo de
    cierre "*Definición del problema: ...*" en cursiva que exige
    `ptfg_ieee.pdf`. Agregar esa frase exige redactar el enunciado formal del
    problema de investigación, lo cual es contenido/redacción (no me
    corresponde inventarlo). Dejo esto senalado explicitamente para
    tfg-master-ieee/tfg-writer-formal: cuando agreguen esa frase de cierre,
    con que quede como texto independiente y en cursiva al final de la
    sección 1 alcanza para que el formato ya definido (parrafo Normal
    justificado) se aplique solo; si prefieren que yo le de el formato una
    vez redactada, puedo hacerlo en una pasada posterior.

11. **Alineación justificada (GB4) en todo el cuerpo.** Se aplico
    `WD_ALIGN_PARAGRAPH.JUSTIFY` al estilo "Normal" (heredado por todos los
    parrafos de cuerpo, incluida la sección 2 "Delimitación del trabajo" y
    la lista de referencias). Los títulos (Heading 1-5, Title, TOC Heading)
    y la portada mantienen su alineación propia (izquierda los títulos,
    centrada la portada y el título repetido antes de la sección 1), como
    corresponde visualmente y como ya indicaba mi analisis previo.

12. **Sangría de primera línea.** 1.25 cm en los párrafos de cuerpo (estilo
    Normal), 0 en títulos, portada, celdas de tabla y epígrafes. Interlineado
    sencillo y espaciado de 6 pt después de cada párrafo en todo el
    documento, salvo las referencias (8 pt, sangría francesa de 1 cm para que
    las líneas de continuación queden alineadas bajo el texto, no bajo el
    "[N]").

13. **Punto de decisión: coma dentro o fuera de las comillas en las 42
    referencias.** **Decisión: coma DENTRO de las comillas** (estilo
    `..., título del artículo,” fuente, año.`), aplicada de forma uniforme a
    las 42 entradas (se verificó que el patrón `”,` aparecía exactamente 42
    veces, una por referencia, y solo dentro de la sección de referencias;
    se reemplazó por `,”` con una única operación de texto, documentada y
    reproducible).

    **Por qué:** el documento `Formato IEEE-resumido.pdf` de la propia
    cátedra (no la plantilla LaTeX genérica, sino la guía que describe
    explícitamente el formato IEEE de referencias que deben usar) trae como
    único ejemplo de referencia con comillas: `R. L. Myer, "Parametric
    oscillators and nonlinear materials," in Nonlinear Optics, ...` — con la
    coma **dentro** de las comillas de cierre. Esa es la fuente más
    específica y autorizada sobre este punto exacto (más que la plantilla
    `ptfg_ieee.pdf`, que de hecho no usa comillas en absoluto para los
    títulos de referencia, solo cursiva, así que no sirve de precedente
    directo para esta disyuntiva). Dado que mi rol es justamente resolver
    apariencia/formato según el material oficial de la cátedra, y que este
    es un punto de puntuación tipográfica (no de contenido ni de la cita en
    sí), prioricé el ejemplo escrito explícito de la cátedra sobre la
    instrucción verbal que recibió citation-verifier-master. Si la profesora
    confirma por escrito que prefiere la coma fuera pese a su propio
    ejemplo, es una reversión de una sola operación de texto (swap inverso
    `,”` → `”,`) sobre las 42 referencias.

## Verificación final

- `zipfile.testzip()` sobre el `.docx` final: sin archivos corruptos.
- Reapertura con `python-docx`: 388 párrafos, 2 tablas, 2 imágenes, sección
  única con A4 y márgenes 3.5/3.5/3.5/3.0 cm, 54 encabezados con `w:numPr`.
- Ningún run del documento final usa una fuente distinta de "Times New
  Roman"; no quedan marcadores `**` de markdown sin convertir en párrafos ni
  en celdas de tabla.
- Render completo a PDF con LibreOffice (con y sin actualización forzada de
  campos vía macro UNO) inspeccionado página por página para portada,
  índice, cada nivel de encabezado (1 a 5), ambas figuras, ambas tablas,
  la ecuación y la lista de referencias.

## Limitaciones no resueltas (requieren abrir el documento en Word)

- **Actualizar el campo TOC** (clic derecho → "Actualizar campos" o F9) para
  que el índice muestre los títulos y números de página reales la primera
  vez que se abra en Word; ya quedó activado `updateFields` para que Word lo
  intente automáticamente al abrir/imprimir, pero no hay garantía de que
  todas las versiones de Word lo hagan sin pedir confirmación.
- Falta el párrafo de cierre en cursiva "*Definición del problema: ...*" de
  la sección 1 (ver punto 10 arriba); es contenido pendiente, no formato.

---

## Versión LaTeX (nueva entrega, misma pasada de contenido ya cerrada)

Documento generado: `trabajo/Anteproyecto_licitaciones_Ivan_Alex_CORREGIDO.tex`
y `trabajo/Anteproyecto_licitaciones_Ivan_Alex_CORREGIDO.pdf` (50 páginas, A4).
Fuente: `trabajo/anteproyecto_borrador.md`, ya con el párrafo "Definición del
problema:" en cursiva al cierre de la sección 1 (la limitación señalada arriba
para la versión Word ya no aplica: el contenido llegó completo a esta pasada).

**Por qué existe una versión en LaTeX además del .docx:** la cátedra entregó
`ptfg_ieee.pdf` como PDF ya compilado desde una plantilla LaTeX, pero no el
código `.tex` fuente. No se pudo partir de ese archivo; se reconstruyó un
documento `.tex` desde cero que replica su apariencia (portada, índice,
numeración decimal multinivel, estilo de "Tabla N:"/"Figura N:", párrafo
"Definición del problema:" en cursiva) a partir de la medición visual del PDF
oficial (páginas renderizadas con `pdftoppm` e inspeccionadas directamente) y
de las mismas medidas ya usadas para el `.docx` (A4, márgenes 3.5/3.5/3.5/3.0
cm, Times New Roman 12 pt vía el paquete `mathptmx`).

### Herramientas usadas

- `pdftoppm` (poppler-utils) para renderizar páginas de `ptfg_ieee.pdf` a PNG
  e inspeccionarlas visualmente (portada, índice, encabezados, tablas,
  ecuación, referencias) antes de diseñar el `.tex`.
- Tres scripts Python (en el directorio de trabajo temporal de la sesión, no
  forman parte de la entrega): `md_to_tex.py` (convierte Markdown a LaTeX:
  encabezados → `\section`.`\subparagraph` con numeración automática de
  LaTeX, listas, negrita/cursiva, comillas tipográficas, la ecuación MAVT a
  notación matemática real, la lista de referencias a un entorno con sangría
  francesa), `build_tables.py` (las 2 tablas Markdown a `longtable` con
  `booktabs`), `assemble.py` (preámbulo + portada + ensamblado final).
- Compilación con `pdflatex` (3 pasadas, necesarias para resolver el índice y
  las referencias cruzadas de la ecuación). Verificación: inspección del log
  de cada pasada (sin errores, `overfull`/`underfull hbox` reducidos a menos
  de 0.5 cm tras ajustes, ver abajo) y renderizado de páginas clave a PNG con
  `pdftoppm` para confirmar visualmente portada, índice, encabezados de los 5
  niveles, ambas figuras, ambas tablas, la ecuación numerada y la lista de
  referencias.

### Decisiones de maquetación específicas de LaTeX

1. **Numeración multinivel real**: se usan los contadores nativos de LaTeX
   (`\section` … `\subparagraph`, con `secnumdepth`/`tocdepth` en 5 para
   llegar a niveles como 7.1.1.3.1 y 7.1.3.1.1) en lugar de escribir los
   números a mano; el script quita el número que traía el título en el
   Markdown y deja que LaTeX lo regenere, igual que se hizo con `numPr` en el
   `.docx`. Los 2 subtítulos sin numerar del apartado 8 ("Tipo de
   investigación", "Enfoque de la investigación") se mantienen sin número y
   fuera del índice usando la variante con asterisco (`\subsubsection*`),
   igual que la decisión ya tomada para el `.docx`.
2. **Índice**: `\tableofcontents` real (no una lista estática), con
   `\contentsname` forzado a "Índice" (babel-spanish usa por defecto "Índice
   general"). A diferencia del `.docx`, en LaTeX el índice se recalcula solo
   en cada compilación, sin pasos manuales pendientes para el usuario.
3. **"Tabla N:"**: se detectó que babel-spanish traduce el nombre del
   contador de tablas como "Cuadro" por defecto; se fuerza
   `\renewcommand{\tablename}{Tabla}` (después de `\begin{document}`, porque
   babel lo redefine justo ahí y un `\renewcommand` anterior era
   sobrescrito) para que coincida con la plantilla oficial y con el `.docx`
   ya entregado.
4. **Ecuación de la sección 7.1.1.3.1 (MAVT)**: a diferencia del `.docx`
   (donde se dejó como texto con formato visual distinguible, ver punto 9 del
   changelog de arriba, por no poder editar OMML con seguridad desde
   python-docx), en LaTeX sí se convirtió a notación matemática real y
   numerada: `$$V(a) = \sum_{j=1}^{m} w_j \cdot v_j(x_j(a)), \quad w_j \geq
   0, \quad \sum_{j=1}^{m} w_j = 1.$$` dentro de un entorno `equation`, fiel
   al texto original (no se alteró el contenido matemático, solo se
   tipografiaron los subíndices/sumatorias que en el Markdown estaban escritos
   con caracteres Unicode sueltos). Las menciones sueltas de `V(a)` y
   `V(a) − V(b)` en el cuerpo del texto también se tipografiaron en modo
   matemático.
5. **Tablas**: la Tabla 1 (cronograma, 9 columnas × 53 filas) se puso en
   página apaisada (`pdflscape`) porque en vertical no entraban las 8
   columnas de meses con texto legible; la Tabla 2 (operacionalización, 4
   columnas) se mantuvo en vertical. Ambas son `longtable` (no flotantes, se
   repiten automáticamente con `\endhead`/`\endfirsthead` si saltan de
   página) con encabezado en negrita y `booktabs` para los bordes.
6. **Referencias**: entorno de lista propio (`reflist`) con sangría francesa
   de 1 cm, igual que en el `.docx`. Cada entrada usa `\item[]` (corchetes
   vacíos) antes del texto de la referencia; sin eso, LaTeX interpreta el
   "[1]" literal de cada referencia como el argumento opcional de `\item` (lo
   detecté al revisar la primera compilación: el PDF mostraba "1" sin
   corchetes en vez de "[1]"). Las URLs se envuelven en `\url{}` (con la
   opción `hyphens` pasada al paquete `url` antes de cargar `hyperref`) para
   que corten en los guiones en vez de desbordar el margen; se mantiene la
   decisión ya tomada de coma dentro de las comillas.
7. **Microtipografía**: se agregó el paquete `microtype` y `\sloppy` dentro
   del entorno de referencias para eliminar casi todos los `overfull hbox`
   causados por URLs/DOIs largos sin puntos de corte; los que quedan tras 3
   pasadas de compilación son menores a 0.5 cm (imperceptibles).

### Verificación final

- Compilación limpia con `pdflatex` (3 pasadas) sin errores (`grep "^!"` sobre
  el log no encuentra errores fatales en la compilación final).
- 50 páginas, A4, sin advertencias de fuente faltante.
- Verificación visual con `pdftoppm` de: portada (coincide con el diseño de
  `ptfg_ieee.pdf`), índice (54 entradas, mismos niveles que el `.docx`),
  encabezados de los 5 niveles, Figura 1 y Figura 2 con leyenda en negrita
  debajo, Tabla 1 y Tabla 2 con leyenda en negrita encima, la ecuación MAVT
  numerada "(1)", el párrafo "Definición del problema:" en cursiva al cierre
  de la sección 1, y las 42 referencias con "[N]" visible y sangría francesa.

### Limitaciones de este enfoque (sin el `.tex` original de la cátedra)

- No existe forma de verificar al 100% que la tipografía, el tamaño exacto de
  los encabezados o el espaciado vertical coincidan carácter por carácter con
  el `.tex` original de la cátedra, porque nunca se tuvo acceso a ese archivo:
  todo se reconstruyó midiendo visualmente el PDF compilado. El resultado es
  una réplica fiel en estructura y convenciones (numeración, leyendas,
  portada, índice), no una copia binaria del documento fuente.
- La plantilla oficial en sí misma es inconsistente en un punto puntual: la
  entrada del índice dice "Referencias Bibliográficas" (con B mayúscula) pero
  el título de esa sección en el cuerpo del PDF dice "Referencias
  bibliográficas" (b minúscula). Se priorizó la consistencia con el `.docx`
  ya entregado (que usa "Referencias Bibliográficas" con B mayúscula en
  ambos lugares) en vez de replicar esa inconsistencia interna de la
  plantilla.
- El título "Implementación de métodos multicriterio para la evaluación de
  licitaciones" se repite en bloque centrado al inicio del cuerpo (antes de
  la sección 1), replicando el patrón visual de la página 3 de
  `ptfg_ieee.pdf`; como no hay `.tex` fuente, no se puede confirmar si allí
  se usaba `\chapter*` de la clase `report`, un `\section*` especial, u otro
  mecanismo. Se implementó como un bloque de texto centrado simple, visualmente
  equivalente.

## Regeneración (segunda pasada) — hipótesis final, "métodos" en plural, objetivo 6 rediseñado

Motivo: el contenido de `trabajo/anteproyecto_borrador.md` incorporó todos los
cambios acordados con el usuario (hipótesis final, 16 cambios a plural
"métodos", objetivo 6 rediseñado con reproducibilidad real, validación con
expertos anonimizados y 43 tareas). Se regeneró el `.docx` desde cero con los
mismos scripts, corrigiendo además un bug crítico de imagen detectado en mi
propia verificación anterior.

1. **Respaldo previo.** Se copió el `.docx` anterior a
   `scratchpad/Anteproyecto_CORREGIDO_backup_20261125_013939.docx` antes de
   sobrescribirlo.

2. **Bug crítico corregido: imagen de la Figura 1.** El `.docx` anterior
   insertaba `trabajo/img/figura_fases.png` (diagrama viejo de 5 fases,
   tareas 1-7 y H1-H3) para la Figura 1, lo cual contradecía el apartado 8
   reestructurado (10 fases, 43 tareas) y la Tabla 1. Se corrigió el mapeo
   `FIGURE_IMAGES` en `md_to_docx_v2.py` para que "Figura 1:" use
   `trabajo/img/figura2.png` (diagrama correcto de 10 fases, Inicio → 1..10 →
   Fin, con el lazo de corrección 9→7), dejando "Figura 2:" sin cambios
   (`trabajo/img/figura1.png`, diagrama funcional del prototipo). Verificado
   visualmente: la Figura 1 del PDF renderizado ahora muestra las 10 fases
   coincidentes con la Tabla 1 y el texto de 8.1/8.2.

3. **Rótulo de la "caja 4" en `figura2.png` (pendiente señalado por
   tfg-master-ieee): RESUELTO con un parche de imagen.** La caja 4 decía
   "Comparación y selección del método" (singular); el documento ahora usa
   "métodos" en plural de forma consistente (título de la Fase 4, índice,
   Tabla 1). Dado que el fondo de la caja es blanco uniforme y el texto es
   negro puro sobre una fuente sans-serif estándar (compatible con Liberation
   Sans/Arial), fue viable parchear la imagen sin herramientas de edición
   gráfica externas:
   - Se midió con PIL/numpy la posición exacta del texto viejo dentro de la
     caja (fila de texto y columnas, excluyendo los bordes del rectángulo) y
     se calibró el tamaño de fuente (Liberation Sans 36 pt) reproduciendo el
     ancho del texto original.
   - Se blanqueó el área de texto interior de la caja (sin tocar los bordes
     ni las flechas) y se redibujó "4. Comparación y selección de los
     métodos" centrada horizontal y verticalmente en la caja, con el mismo
     tamaño de fuente y color que el resto del diagrama.
   - Se guardó una copia de respaldo del PNG original
     (`scratchpad/figura2_backup.png`) antes de sobrescribir
     `trabajo/img/figura2.png`.
   - Verificación visual (recorte de la caja antes/después y render completo
     del diagrama): el parche es indistinguible del resto del diagrama, sin
     artefactos visibles; el resto de las cajas (1, 2, 3, 5-10) no se tocó.
   - Si los autores prefieren regenerar el diagrama desde su fuente original
     (p. ej. Graphviz/draw.io) en vez de depender de este parche de píxeles,
     sigue siendo una mejora recomendable a futuro, pero no es necesaria para
     que el documento actual sea correcto.

4. **Bug de formato encontrado y corregido: cursiva simple no interpretada.**
   El párrafo de cierre de la sección 1 ("*Definición del problema: ...*",
   contenido ya incorporado por el equipo) usa cursiva simple de Markdown
   (un solo asterisco a cada lado), pero `parse_inline()` en
   `md_to_docx_v2.py` solo reconocía `**negrita**` y `***negrita cursiva***`.
   Sin la corrección, el `.docx` habría mostrado los asteriscos literales
   `*...*` en vez de aplicar cursiva. Se amplió la función para reconocer
   también `*cursiva*`, se verificó con una búsqueda específica de patrones
   de un solo asterisco en todo el `.md` (un único resultado: justamente este
   párrafo) y se confirmó en el `.docx` final que el párrafo completo quedó
   en un único `run` con `italic=True` y sin asteriscos residuales.

5. **Regeneración completa.** Se re-ejecutaron `make_base_template.py` y
   `md_to_docx_v2.py` sobre el `.md` actualizado, sin más cambios de
   maquetación respecto de la primera pasada (misma A4, márgenes, fuente,
   numeración multinivel, TOC real, epígrafes, tabla de estilos, coma dentro
   de las comillas en las 42 referencias).

### Verificación final (segunda pasada)

- `zipfile.testzip()`: sin archivos corruptos (19 entradas en el zip).
- Reapertura con `python-docx`: 395 párrafos, 2 tablas, 2 imágenes
  (`word/media/image1.png`, `image2.png`), una sección A4 (21 × 29.7 cm) con
  márgenes 3.5/3.5/3.5/3.0 cm, único tipo de letra en todo el documento
  (`Times New Roman`), 54 encabezados con numeración `w:numPr` real.
- Búsqueda automática de markdown sin convertir (`*`, `|`, `##`, líneas que
  empiezan con `#`) en todos los párrafos y celdas de tabla: **0 coincidencias**.
- Campo TOC real presente (`w:instrText` con `TOC`), `updateFields` activado.
- Título de la sección de referencias: "Referencias Bibliográficas" (verificado
  como `Heading 1`).
- Epígrafes verificados: "Figura 1: Diagrama de flujo de las fases del
  trabajo.", "Figura 2: Diagrama funcional del prototipo web.", "Tabla 1:
  Cronograma de tareas.", "Tabla 2: Operacionalización de variables." —con el
  orden correcto (figura, luego epígrafe debajo; epígrafe, luego tabla
  debajo).
- Tabla 1 (cronograma): 54 filas × 9 columnas = encabezado + 10 filas de fase
  + 43 filas de tarea, confirmando las 43 tareas (41 originales + 8.4 y 9.5
  de validación de expertos). Tabla 2 (operacionalización): 7 filas (encabezado
  + 6 objetivos específicos).
- Búsqueda de datos identificables de personas (teléfonos, correos) en todo
  el cuerpo del documento: solo aparecen en la portada (estilo `TFG Portada`),
  que corresponde a los datos de contacto de los propios autores exigidos por
  la plantilla, no de los evaluadores expertos. No se encontró ningún dato
  identificable de los evaluadores expertos en la Tabla 2 ni en el apartado
  8.3 (solo "evaluadores expertos" como término genérico, conforme al diseño
  de validación anonimizada acordado).
- Render completo a PDF con LibreOffice (`soffice --headless --convert-to
  pdf`, 50 páginas, tamaño A4 confirmado por `pdfinfo`): inspección visual
  página por página de la Figura 1 (10 fases correctas, caja 4 corregida),
  la Figura 2, la Tabla 1 (cronograma) y la Tabla 2, el índice (placeholder
  del campo TOC, ver limitación de siempre) y el párrafo en cursiva de cierre
  de la sección 1.

### Limitaciones no resueltas (sin cambios respecto de la primera pasada)

- Sigue pendiente **actualizar el campo TOC** abriendo el documento en Word
  (clic derecho → "Actualizar campos" o F9) para que muestre los títulos y
  números de página reales; `updateFields` está activado pero no hay
  garantía de que todas las versiones de Word lo hagan sin confirmación. No
  se pudo forzar la actualización del campo en este entorno de verificación
  porque no hay un intérprete Python con el módulo `uno` de LibreOffice
  disponible (en la primera pasada sí se había logrado mediante un listener
  de `soffice` con una macro UNO; en esta sesión esa ruta no estaba
  disponible, pero el mecanismo del campo TOC no cambió, solo el contenido
  que alimentará una vez actualizado, ya verificado por separado mediante la
  numeración real de los 54 encabezados).
- El parche de la caja 4 de `figura2.png` (punto 3) es una solución de
  imagen rasterizada (parche de píxeles), no una edición del archivo fuente
  del diagrama (si existe uno en un formato editable como `.drawio`, `.dot`
  o similar). Si los autores conservan el archivo fuente original, sería
  preferible regenerar el diagrama completo desde ahí en el futuro.

## Tercera pasada (propagación del reordenamiento de citas de citation-verifier-master)

citation-verifier-master reordenó ascendentemente 3 citas múltiples y movió 13
citas al final de la oración en `trabajo/anteproyecto_borrador.md` (commit
`1c28a02`), sin tocar contenido, tablas ni figuras. Se regeneraron ambos
entregables a partir del `.md` actualizado, reutilizando sin cambios la
plantilla base y el ensamblador LaTeX ya validados en la segunda pasada:

- **`.docx`**: `make_base_template.py` (sin cambios) + `md_to_docx_v2.py`
  sobre el `.md` actualizado → mismo resultado estructural que la pasada
  anterior (395 párrafos, 2 tablas, 19 entradas en el zip, A4 con márgenes
  3.5/3.5/3.5/3.0 cm, 54 encabezados numerados, campo TOC real, título
  "Referencias Bibliográficas" presente). `zipfile.testzip()` sin errores.
  Verificado con `python-docx` que la cita reordenada de Kadziński et al.
  (referencia [34]) aparece correctamente en el cuerpo.
- **`.tex`/`.pdf`**: se regeneró `body.tex` desde el `.md` actualizado
  (`md_to_tex.py`, las tablas no cambiaron por lo que no fue necesario
  rehacer `build_tables.py`) y se reensambló el documento completo
  (`assemble.py`, mismo preámbulo/portada que las pasadas anteriores).
  Compilado con `latexmk -pdf` sin errores fatales ni referencias
  indefinidas (solo los mismos warnings cosméticos de *overfull/underfull
  hbox* preexistentes, no relacionados con este cambio): 50 páginas, A4
  confirmado por `pdfinfo`. Verificado con `pdftotext` que la referencia
  [34] (Kadziński, Ghaderi et al.) aparece en el PDF compilado.
- Limitación sin cambios: sigue pendiente **actualizar el campo TOC en Word**
  (F9) al abrir el `.docx`, como ya se documentó en la primera pasada; el
  campo sigue presente y marcado para actualizarse, pero no se puede forzar
  su recálculo visual sin Word o LibreOffice con `uno` disponible en este
  entorno.

## Cuarta pasada (propagación de la reescritura del marco teórico 7.1, equipo de contenido)

El equipo de contenido reescribió pasajes de ELECTRE, TOPSIS, VIKOR, MAVT,
AHP, PROMETHEE, MULTIMOORA, UTA/UTA-splines y otros del apartado 7.1 en
`trabajo/anteproyecto_borrador.md` (commits `57be0c4` y `6f4d8ea`), para que
las citas queden al final de la oración en vez de "En [n] ..." al inicio, y
para corregir una atribución indebida en el párrafo de TOPSIS. Confirmado por
`diff` contra la versión anterior del `.md`: cambios de texto exclusivamente
dentro del apartado 7.1, sin alterar numeración de secciones, tablas, figuras
ni la lista de referencias (mismos corchetes `[n]` citados, solo reordenados
dentro de cada oración). No correspondía re-ejecutar la verificación
exhaustiva completa (imagen, márgenes, TOC, etc. no cambiaron); se hizo una
verificación rápida de regeneración y de que el texto nuevo esté presente en
ambos entregables.

- **`.docx`**: se respaldó el `.docx` anterior en
  `trabajo/backup_20261126_*/` y se regeneró con el mismo `base_template.docx`
  ya validado (sin cambios) + `.claude/scripts/md_to_docx_v2.py` (sin cambios
  en el script) sobre el `.md` actualizado. Resultado idéntico en estructura
  a la pasada anterior: 19 entradas en el zip (`zipfile.testzip()` sin
  errores), 395 párrafos, 2 tablas, sección A4 con márgenes 3.5/3.5/3.5/3.0 cm,
  54 encabezados numerados, "Referencias Bibliográficas" presente. Verificado
  con `python-docx` que los 7 pasajes reescritos (ELECTRE, TOPSIS, VIKOR, MAVT,
  AHP, UTA, regresión ordinal robusta) aparecen literalmente en el cuerpo del
  documento.
- **`.tex`/`.pdf`**: se regeneró `body.tex` desde el `.md` actualizado con
  `md_to_tex.py` (sin cambios en el script), se reconstruyeron `table1.tex`/
  `table2.tex` con `build_tables.py` por prolijidad aunque las tablas no
  cambiaron, y se reensambló el documento completo con `assemble.py` (mismo
  preámbulo/portada). Compilado con `latexmk -pdf`: sin errores fatales, sin
  "Undefined" ni "! LaTeX Error" en el log (`grep` dedicado sin coincidencias),
  solo los mismos warnings cosméticos de *overfull/underfull hbox*
  preexistentes. 50 páginas, A4 confirmado por `pdfinfo`. Verificado con
  `pdftotext -layout` que los mismos 7 pasajes reescritos aparecen en el PDF
  compilado, incluyendo el párrafo corregido de TOPSIS ("El procedimiento de
  TOPSIS incluye la normalización de la matriz de decisión...").
- Limitación sin cambios (idéntica a las pasadas anteriores): sigue pendiente
  **actualizar el campo TOC en Word** (F9) al abrir el `.docx`.

## Quinta pasada (propagación del fix puntual de "En [n]" en la sección 5, equipo de contenido)

`citation-verifier-master` reformuló los 4 últimos casos restantes del
patrón "En [n] se..." fuera del marco teórico, dentro del párrafo
"Revisión de literatura" de la sección 5 (commit `3afac59`), para que la
cita quede al final de la oración, igual que en el apartado 7.1. Cambio de
texto exclusivamente dentro de ese párrafo; sin alteración de numeración de
secciones, tablas, figuras ni la lista de referencias. Al no haber cambios
estructurales, no se repitió la verificación exhaustiva completa (márgenes,
TOC, estilos de tabla, etc. no se tocaron); solo se repropagó el cambio de
texto a ambos entregables y se verificó su presencia.

- **`.docx`**: regenerado desde cero con el mismo `base_template.docx` (sin
  cambios) y `.claude/scripts/md_to_docx_v2.py` (sin cambios en el script)
  sobre el `.md` actualizado. `zipfile.testzip()` sin errores; 395
  párrafos, 2 tablas (igual que la pasada anterior). Verificado con
  `python-docx` que las 4 oraciones reformuladas aparecen literalmente en
  el cuerpo del documento y que ya no queda ningún "En [3] se aplicó",
  "En [4] se analizó", "En [10] y [13] se desarrollaron" ni "En [8] se
  estudió" en el texto.
- **`.tex`/`.pdf`**: `body.tex` regenerado con `md_to_tex.py` (sin cambios
  en el script) desde el `.md` actualizado; `table1.tex`/`table2.tex`
  reconstruidas con `build_tables.py` por prolijidad (tablas sin cambios);
  reensamblado con `assemble.py` (mismo preámbulo/portada) y compilado con
  `latexmk -pdf`. Log sin líneas "! " (errores fatales) ni "Undefined";
  solo los mismos warnings cosméticos de *overfull/underfull hbox*
  preexistentes en las referencias con URLs largas. 50 páginas (igual que
  antes). Verificado con `pdftotext -layout` que las 4 oraciones aparecen
  en el PDF compilado y que no queda el patrón antiguo.
- Los `.docx`/`.tex`/`.pdf` previos a este fix se respaldaron en el
  scratchpad de la sesión (no dentro del repositorio).
- Limitación sin cambios: sigue pendiente **actualizar el campo TOC en
  Word** (F9) al abrir el `.docx`.
