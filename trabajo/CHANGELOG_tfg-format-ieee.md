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
