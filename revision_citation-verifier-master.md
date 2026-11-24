# Revisión forense de citas: Anteproyecto "Implementación de métodos multicriterio para la evaluación de licitaciones"

**Agente:** citation-verifier-master
**Documento revisado:** `Anteproyecto_licitaciones_Ivan_Alex.docx` (portada fechada el 2 de noviembre de 2026)
**Protocolo aplicado:** `analisis_citation-verifier-master.md` (secciones 1 a 5)
**Fecha de la revisión:** 17-11-2026

> **Principio aplicado:** ninguna cita se da por válida por defecto. Cuando no pude comprobar algo, la cita queda como ⚠️ DUDOSA.

---

## 0. Método y alcance

1. **Extracción:** saqué el texto de `word/document.xml` y construí el inventario con un script que detecta cada `[n]`, su primera aparición y cuántas veces aparece. El documento no tiene notas al pie ni comentarios.
2. **Existencia de las fuentes:**
   - **33 DOI:** consulté cada uno en la API de Crossref y comparé título, autores, revista, volumen, número, páginas y fecha con la referencia del estudiante.
   - **Fuentes sin DOI:** comprobé cada URL (código HTTP) y busqué la obra en el portal oficial o en un repositorio (BACN, DNCP, EuDML, sitio de la revista, ABC Color).
3. **Fidelidad del contenido:** contrasté lo que el texto atribuye a cada fuente con la mejor evidencia que pude obtener. El **nivel de verificación** se indica en cada cita:
   - **A:** texto completo o fragmento literal de la fuente (la Ley 7021, el Decreto 2264 dentro del digesto oficial de la DNCP, la Ley 2051 en la BACN, el PDF de Mayor et al. y las notas de ABC).
   - **B:** resumen oficial (Crossref o editorial) o fragmento indexado de la propia fuente.
   - **C:** título y metadatos verificados, más conocimiento estándar de una obra canónica del área (Saaty, Roy, Opricovic-Tzeng, etc.). No revisé el texto completo, pero la afirmación es genérica y coherente con lo que la obra trata.
4. **Limitaciones:**
   - Varios editores (ScienceDirect, MDPI, OECD, SciELO, EuDML) devuelven 403 a clientes automáticos. En esos casos usé resúmenes de Crossref, fragmentos indexados o repositorios alternativos.
   - No revisé el texto completo de las obras con nivel C. Si el docente exige verificación a texto completo, esas citas deben contrastarse con el PDF.

---

## 1. Inventario cita ↔ referencia

### 1.1 Resultado global

| Comprobación | Resultado |
|---|---|
| Citas distintas en el cuerpo | **42** ([1] a [42]) |
| Entradas en la lista de referencias | **43** ([1] a [43]) |
| Orden de primera aparición | **Correcto.** Las citas aparecen en orden 1, 2, 3… 42, sin saltos. |
| Citas huérfanas (sin entrada en la lista) | **Ninguna** |
| Referencias no citadas | **1: [43]** (página del PTI) |
| Números duplicados o con saltos en la lista | Ninguno |
| Misma fuente con dos números | Ninguna (no repite el defecto de la plantilla, A2) |
| Formato en el texto | Corchete con espacio antes y antes de la puntuación en todos los casos. No usa "la referencia [n]" a mitad de oración. |
| Citas múltiples | Estilo separado y consistente: `[3], [6]`, `[10], [11]`, `[13], [10]` (×2). **Observación (BAJA):** en `[13], [10]` conviene el orden ascendente, `[10], [13]`. |
| Título de la sección | "Referencias bibliográficas", usado de forma uniforme (A8 cumplido). |
| Antecedentes (patrón de la cátedra) | Los 12 títulos citados en 7.2 coinciden con el título de su referencia. |

### 1.2 Matriz de citas

Abreviaturas de sección: DP = Definición del problema; F = Fundamentación (con Justificación, Revisión de literatura y Pertinencia); I = Impacto; MT = Marco teórico; A = Antecedentes; M = Método.

| n.º | Apariciones | Secciones | Afirmación que respalda (resumen) | Tipo de fuente |
|---|---|---|---|---|
| [1] | 6 | DP, F, MT | Ley 7021: principios, Arts. 3, 4, 34, 45, 52, 55, 158 y 159 | Ley |
| [2] | 3 | DP, F, MT | Decreto 2264/2024: Arts. 59, 75 y 235 | Decreto |
| [3] | 6 | DP, F, MT, A | Modelo de función de valor aditiva para la oferta más ventajosa (Lehtonen y Virtanen) | Artículo |
| [4] | 4 | DP, F, MT, A | Inversión de orden en licitaciones | Artículo |
| [5] | 1 | F | Compras públicas: del 11,8 % del PIB (2007) al 12,9 % (2021) en la OCDE | Informe (citado como web) |
| [6] | 2 | F | Revisión de 74 estudios (1998-2023); el AHP es la técnica más usada | Artículo |
| [7] | 3 | F, I | La mayoría de las planillas usadas en aplicaciones empresariales importantes tienen errores | Artículo |
| [8] | 7 | F, I, MT, A | Conocer solo los pesos no describe el modelo completo de evaluación; divulgación completa | Artículo |
| [9] | 4 | F, MT, A | La fórmula de puntuación modifica el ganador; se comparan 38 fórmulas | Artículo |
| [10] | 6 | F, I, MT | Taxonomía para seleccionar métodos MCDA | Artículo |
| [11] | 2 | F, MT | Sistema de recomendación con más de 200 métodos | Artículo |
| [12] | 3 | F, I | Digitalización: procedimientos más ágiles, seguimiento y estándares de auditoría | Artículo |
| [13] | 5 | F, I, MT | Pautas para elegir un método MCDA | Artículo |
| [14] | 4 | MT | Funciones de valor multiatributo medibles | Artículo |
| [15] | 3 | MT | UTA (1982), programación lineal | Artículo |
| [16] | 2 | MT | PROMETHEE: I da un orden parcial y II un preorden completo | Artículo |
| [17] | 2 | MT | AHP: jerarquía y comparación por pares | Artículo |
| [18] | 3 | MT | Sobreclasificación y fundamentos de ELECTRE | Artículo |
| [19] | 5 | MT | MOORA: normalización vectorial, punto de referencia de Tchebycheff, sin pesos explícitos | Artículo (sin DOI) |
| [20] | 3 | MT | Preferencia necesaria y posible; regresión ordinal robusta | Artículo |
| [21] | 3 | MT, A | UTA-poly y UTA-splines, programación semidefinida | Artículo |
| [22] | 2 | MT | La interpretación de los pesos depende de la regla de agregación | Artículo |
| [23] | 1 | MT | AHP: juicios y consistencia | Artículo |
| [24] | 2 | MT, A | AHP frente a suma ponderada en compras públicas italianas | Artículo |
| [25] | 1 | MT | Revisión de aplicaciones de TOPSIS | Artículo |
| [26] | 3 | MT | VIKOR frente a TOPSIS | Artículo |
| [27] | 2 | MT | VIKOR extendido frente a sobreclasificación; condiciones de aceptación | Artículo |
| [28] | 2 | MT | ELECTRE III ordena; ELECTRE TRI asigna a categorías | Artículo |
| [29] | 2 | MT | Revisión de PROMETHEE | Artículo |
| [30] | 1 | MT | MULTIMOORA | Artículo |
| [31] | 1 | MT | La contratación pública como sistema | Artículo |
| [32] | 3 | MT | Ley 2051: Arts. 16, 20, 24, 26 y 28 | Ley |
| [33] | 2 | MT, A | Métodos de evaluación desde la relación precio-calidad | Artículo |
| [34] | 2 | MT, A | Medidas de expresividad y robustez | Artículo |
| [35] | 1 | MT | Los llamados del PTI no están sujetos a la normativa nacional | Nota de prensa |
| [36] | 1 | MT | La DNCP no tiene competencia sobre las entidades binacionales | Nota de prensa |
| [37] | 1 | MT | Datos abiertos de adjudicaciones por año | Portal institucional |
| [38] | 1 | A | La oferta más ventajosa con criterios de capacidad y porcentaje de honorarios | Artículo |
| [39] | 1 | A | Selección de contratistas en Colombia con AHP y TOPSIS difuso | Artículo |
| [40] | 1 | A | Marco con DEA, valoración de riesgo y modelo costo-riesgo | Artículo |
| [41] | 1 | A | AHP para elegir un sistema de autoría multimedia | Artículo |
| [42] | 1 | M | Etapas de la investigación tecnológica según Dean | Artículo (sin URL) |
| [43] | **0** | (no se cita) | (página de licitaciones del PTI) | Página web |

---

## 2 y 3. Verificación y veredicto por cita

Leyenda: ✅ Válida (VERIFICADA, con observaciones o con errores de formato) · ⚠️ Dudosa · ❌ Inválida, inventada o tergiversada. "Niv." indica el nivel de verificación del contenido (A, B o C, ver sección 0).

### 3.1 Normativa paraguaya y fuentes institucionales

| n.º | Existencia | Fidelidad del contenido | Niv. | Veredicto |
|---|---|---|---|---|
| [1] Ley 7021/2022 | Sí. Texto oficial (versión del PNUD) y ficha de la BACN. El buscador de la DNCP responde 200. La fecha del 9 dic. 2022 la confirma el título del propio Decreto 2264. | **Todo verificado en el texto:** Art. 1 (crea el Sistema Nacional de Suministro Público); Art. 3 a) (definición de adjudicación, que coincide casi literalmente); Art. 4 (principios, entre ellos economía y eficiencia, imparcialidad, transparencia, predictibilidad y **valor por dinero**); Art. 34 (licitación pública o de menor cuantía según el monto); Art. 45 (bases "claras, objetivas e imparciales"); Art. 52 (evaluación según los pliegos y mayor valor por dinero); Art. 55 (adjudicación con base en el informe de evaluación); Art. 158 (abroga la Ley 2051); Art. 159 (procedimientos iniciados antes de la ley). | A | ✅ **VERIFICADA** |
| [2] Decreto 2264/2024 | Sí. Fecha 01-08-2024 confirmada por fuentes jurídicas y por la DNCP. Texto en el digesto oficial de la DNCP. | **Verificado:** el Art. 59 exige criterios relacionados con el objeto y la ponderación relativa, "excepto… precio exclusivamente"; el Art. 75 distingue la evaluación por multiplicidad de criterios de la basada en precio y prevé la verificación de requisitos antes de proponer la adjudicación; el Art. 235 abroga los Decretos 9537/2023 y 9823/2023. | A | ✅ **VERIFICADA** |
| [32] Ley 2051/2003 | Sí. Ficha de la BACN (promulgada el 21-01-2003). | **Verificado:** el Art. 16 enumera licitación pública, concurso de ofertas, contratación directa y fondo fijo; el Art. 20 g) exige "criterios claros y detallados para la evaluación", además de la descripción del objeto y los requisitos de participación; el Art. 24 trata de las ofertas técnicas y económicas; el Art. 26 prohíbe puntos o porcentajes salvo en ciertos servicios y, para bienes, traduce los factores "en términos monetarios"; el Art. 28 adjudica al precio más bajo entre las ofertas solventes. | A | ✅ **VÁLIDA CON ERRORES DE FORMATO** (URL truncada, ver 4) |
| [5] OCDE, *Government at a Glance 2023* | Sí. Para clientes automáticos la página da 403, pero el texto de la sección "component-36" está indexado. La obra tiene DOI 10.1787/3d5c5d31-en (Crossref, OECD Publishing). | **Verificado:** el gasto en compras públicas de la OCDE pasó del 11,8 % del PIB (2007) al 12,9 % (2021). Las cifras coinciden. *Nota:* la edición de 2025 revisa el dato de 2021 al 13 %. | B | ✅ **VÁLIDA CON ERRORES DE FORMATO** (existe DOI y es un informe, ver 4) |
| [35] ABC Color, 23-04-2025 | Sí, responde 200. | La nota sostiene que los llamados de la Fundación PTI "no están sujetos a las normativas nacionales". El texto le atribuye exactamente eso. **Observación:** es una afirmación periodística, de una nota crítica, sobre el régimen jurídico del PTI. Para fundamentar un régimen normativo se recomienda una fuente primaria (reglamento de compras del PTI o normativa de Itaipu). | A | ✅ **VERIFICADA CON OBSERVACIONES** |
| [36] ABC Color, 20-03-2025 | Sí, responde 200. | El director de la DNCP declara que no puede intervenir en las licitaciones de una entidad binacional. El texto lo resume correctamente. **Observación:** la nota trata de la **Itaipu Binacional** y no menciona al PTI. Trasladarlo al PTI, que es una fundación vinculada, es una inferencia del estudiante y debería explicitarse o respaldarse con otra fuente. | A | ✅ **VERIFICADA CON OBSERVACIONES** |
| [37] DNCP, datos abiertos | Sí, responde 200. | El portal ofrece conjuntos de adjudicaciones por año, de 2010 a 2026. Lo afirmado, que hay datos de 2024 y 2025, es correcto. **Observación:** el estudio abarca de 2023 a 2026, pero la referencia solo menciona 2024 y 2025. | A | ✅ **VERIFICADA CON OBSERVACIONES** |
| [43] FPTI-PY, "PTI" | La URL responde 200, pero la página se carga con JavaScript y no se pudo leer su contenido. | **No se cita en ningún lugar del texto.** El lugar natural de la cita es la Delimitación y el Método, donde se menciona "la página web de licitaciones del PTI" sin número. | — | ❌ **INVÁLIDA (referencia no citada, ALTA, corregible)** |

### 3.2 Artículos de revista citados en la fundamentación, la revisión de literatura y los antecedentes

| n.º | Existencia (Crossref u otra) | Fidelidad del contenido | Niv. | Veredicto |
|---|---|---|---|---|
| [3] Lehtonen y Virtanen 2022 | DOI correcto; título, autores, vol. 22, n.º 2 y pp. 164-179 coinciden. | El resumen dice casi literalmente que el modelo de función de valor aditiva, construido con el personal de compras, capta las preferencias "de manera más confiable y transparente" que las fórmulas de puntuación. **Fiel.** | B | ✅ **VERIFICADA** |
| [4] Schotanus et al. 2022 | DOI correcto; vol. 28, n.º 2, art. 100744. | Analiza la inversión de orden con puntuación relativa en 303 licitaciones neerlandesas, al agregar o quitar ofertas no ganadoras. **Fiel.** | B | ✅ **VERIFICADA** |
| [6] Anelli et al. 2025 | DOI correcto; *Systems* 13(9), 777. | Correcto: 74 estudios de 1998 a 2023, y "AHP is confirmed as the most widely used technique". **Observación:** la revisión se limita a las compras públicas **de construcción**, un alcance que el texto omite y que generaliza a la oferta más ventajosa en general. | B | ✅ **VERIFICADA CON OBSERVACIONES** |
| [7] Poon et al. 2024 | DOI correcto; *Front. Comput. Sci.* 18(2), 182203. | El resumen solo dice que los errores "often exist". La frase del texto ("la mayoría de las planillas… aplicaciones empresariales importantes contienen errores") coincide con la difusión oficial del estudio en Phys.org (2024), que la atribuye a esta revisión. El sentido es fiel, pero conviene indicar la página del artículo donde se apoya. | B | ✅ **VERIFICADA CON OBSERVACIONES** |
| [8] Mateus, Ferreira y Carreira 2010 | DOI correcto; vol. 16, n.º 3, pp. 206-215. | Un fragmento indexado de la editorial confirma que los autores sostienen que, para definir pesos sólidos, deben definirse antes las reglas de puntuación de todos los criterios. Eso respalda que conocer solo los porcentajes no describe el modelo. **Fiel.** No pude leer el resumen completo (403). | B | ✅ **VERIFICADA** |
| [9] Stilger, Siderius y van Raaij 2017 | DOI correcto; vol. 17, n.º 1, pp. 89-125. | El resumen dice que la elección de la fórmula "critically affects which bid wins" y que se estudian **38** fórmulas. **Fiel.** | B | ✅ **VERIFICADA** |
| [10] Cinelli et al. 2020 | DOI correcto; *Omega* 96, 102261. | Taxonomía para apoyar la selección de métodos MCDA, coherente con el título. | C | ✅ **VERIFICADA** |
| [11] Cinelli et al. 2022 | DOI correcto; EJOR 302(2), 633-651. | El resumen (también en arXiv 2106.07378) indica que el sistema elige entre más de 200 métodos MCDA. **Fiel.** | B | ✅ **VERIFICADA** |
| [12] Mavidis y Folinas 2022 | DOI correcto; *Sustainability* 14(18), 11252. | **No verificado.** El resumen trata de los **factores críticos de éxito y los desafíos** de la contratación electrónica 3.0 y 4.0, y solo menciona en general el acceso a la información y la transparencia. Las tres afirmaciones que se le atribuyen ("procedimientos más ágiles", "mejor seguimiento… porque el proceso queda registrado digitalmente", "seguimiento bajo estándares de auditoría") no aparecen en el resumen. El texto completo no fue accesible (403 en MDPI), y solo encontré resúmenes de terceros, no la fuente. La afirmación sobre la auditoría es la más débil. | — | ⚠️ **DUDOSA** (hay que pedir al estudiante la página o el pasaje exacto) |
| [13] Guitouni y Martel 1998 | DOI correcto; EJOR 109(2), 501-521. | Pautas para elegir un método MCDA según el problema. **Fiel** al título y al contenido conocido. | C | ✅ **VERIFICADA** (formato: "J.-M. Martel") |
| [24] Marcarelli y Nappi 2019 | DOI correcto; vol. 19, n.º 3, pp. 201-223. | El resumen confirma dos modelos AHP frente al modelo de suma ponderada en compras públicas italianas. **Fiel.** | B | ✅ **VERIFICADA** |
| [31] Thai 2001 | DOI correcto; vol. 1, n.º 1, pp. 9-50. | El resumen confirma un enfoque de sistemas; los componentes enumerados corresponden al modelo conocido de Thai. | B/C | ✅ **VERIFICADA** |
| [33] Bergman y Lundberg 2013 | DOI correcto; vol. 19, n.º 2, pp. 73-83. | Evaluación de ofertas desde una perspectiva económica de precio y calidad, coherente con el título. | C | ✅ **VERIFICADA** |
| [38] Lahdenperä 2013 | DOI correcto; vol. 13, n.º 4, pp. 409-446. | El resumen confirma la integración del porcentaje de honorarios en la selección multicriterio, en alianzas de proyecto (construcción). **Fiel.** | B | ✅ **VERIFICADA** (ver la fecha en 4) |
| [39] Mayor, Botero y González-Ruiz 2016 | DOI correcto; *Obras y Proyectos* n.º 20, pp. 56-74. | **Verificado en el texto completo:** AHP para ponderar, TOPSIS con conjuntos difusos, integración de la precalificación y la selección, pesos obtenidos de entrevistas a expertos, validación mediante simulación y análisis de sensibilidad leve y fuerte. **Fiel.** | A | ✅ **VERIFICADA** |
| [40] Cheaitou, Larbi y Al Housani 2019 | DOI correcto; SEPS 68, 100620. | El resumen indexado confirma tres etapas: selección de contratistas eficientes con DEA, valoración del riesgo con lógica difusa y un modelo biobjetivo de costo y riesgo. **Fiel.** | B | ✅ **VERIFICADA** |
| [41] Lai, Trueblood y Wong 1999 | DOI correcto; I&M 36(4), 221-232. | Confirmado: seis ingenieros de software aplicaron AHP para evaluar tres productos de autoría multimedia. **Fiel.** | B | ✅ **VERIFICADA** |

### 3.3 Artículos metodológicos del marco teórico (MCDA)

Todos los DOI resuelven a la obra declarada, con título, autores, revista, volumen, número y páginas coincidentes.

| n.º | Fidelidad del contenido | Niv. | Veredicto |
|---|---|---|---|
| [14] Dyer y Sarin 1979 | El resumen confirma funciones de valor medibles bajo certeza y las condiciones para las formas aditiva, multiplicativa y otras. **Fiel.** | B | ✅ VERIFICADA |
| [15] Jacquet-Lagrèze y Siskos 1982 | UTA mediante programación lineal a partir de un orden de referencia. **Fiel.** | C | ✅ VERIFICADA |
| [16] Brans y Vincke 1985 | El resumen confirma funciones de preferencia, que PROMETHEE I da un preorden parcial y que PROMETHEE II da uno total. **Fiel.** *Observación de cronología:* ver 3.4. | B | ✅ VERIFICADA CON OBSERVACIONES |
| [17] Saaty 1990 | Jerarquía y comparación por pares. **Fiel.** *Cronología:* ver 3.4. | C | ✅ VERIFICADA CON OBSERVACIONES |
| [18] Roy 1991 | Fundamentos de la sobreclasificación y de ELECTRE, coherentes con el título. *Cronología:* ver 3.4. | C | ✅ VERIFICADA CON OBSERVACIONES |
| [19] Brauers y Zavadskas 2006 | Existe (EuDML 209425, Control and Cybernetics 35(2), 445-469). El resumen indexado confirma los denominadores con la raíz de la suma de cuadrados y el punto de referencia. La afirmación de que la formulación original no lleva pesos explícitos es plausible, pero no la verifiqué en el texto. Se recomienda citar la página. | B | ✅ VERIFICADA CON OBSERVACIONES |
| [20] Greco, Mousseau y Słowiński 2008 | Preferencia necesaria y posible (UTA^GMS). **Fiel.** | C | ✅ VERIFICADA |
| [21] Sobrie et al. 2018 | UTA-poly y UTA-splines con programación semidefinida. **Fiel.** | C | ✅ VERIFICADA |
| [22] Choo, Schoner y Wedley 1999 | La interpretación de los pesos depende del modelo de agregación. **Fiel** al título. | C | ✅ VERIFICADA |
| [23] Saaty 2008 | AHP, juicios y consistencia. **Fiel.** | C | ✅ VERIFICADA |
| [25] Behzadian et al. 2012 | Revisión de aplicaciones de TOPSIS. **Fiel.** | C | ✅ VERIFICADA |
| [26] Opricovic y Tzeng 2004 | Comparación de VIKOR y TOPSIS. **Fiel.** La consecuencia sobre los pesos se presenta correctamente como inferencia propia ("A partir del análisis de…"). | C | ✅ VERIFICADA |
| [27] Opricovic y Tzeng 2007 | VIKOR extendido frente a PROMETHEE y ELECTRE; condiciones de aceptación. **Fiel.** | C | ✅ VERIFICADA |
| [28] Figueira et al. 2013 | El resumen confirma sobreclasificación, umbrales y ausencia de compensación sistemática. ELECTRE III y ELECTRE TRI se tratan en el cuerpo. **Fiel.** | B | ✅ VERIFICADA |
| [29] Behzadian et al. 2010 | Revisión de PROMETHEE. **Observación:** la frase "Según Behzadian… [29], en PROMETHEE II la obtención de un orden completo… no elimina las decisiones de modelación" parece una interpretación del estudiante atribuida a la fuente. Conviene reformularla como valoración propia o citar el pasaje. | C | ✅ VERIFICADA CON OBSERVACIONES |
| [30] Hafezalkotob et al. 2019 | Revisión de MULTIMOORA. **Fiel.** | C | ✅ VERIFICADA |
| [34] Kadziński et al. 2017 | Medidas de expresividad y robustez. **Fiel** al título. | C | ✅ VERIFICADA |

### 3.4 Observación transversal: cronología de la "Evolución histórica" (7.1.1.1)

Las fuentes existen y dicen lo que se les atribuye. El problema es el **encuadre histórico**, porque se presentan como fecha de origen artículos que son posteriores a la propuesta de cada método:
- "En 1985, Brans y Vincke desarrollaron PROMETHEE": PROMETHEE se presentó en 1982.
- "En 1990, Saaty sistematizó el AHP": el AHP es de la década de 1970 y el libro de Saaty, de 1980.
- "En 1991, Roy expuso los fundamentos… ELECTRE": ELECTRE es de 1968.

El orden resultante sugiere que ELECTRE es posterior a PROMETHEE y al AHP, cuando es el más antiguo de los tres. No es una tergiversación de las fuentes, pero sí una **imprecisión histórica (MEDIA)**. Se recomienda redactarlo como "En [16] (1985), Brans y Vincke formalizaron…" o citar las obras originales.

### 3.5 Fuente heredada de la plantilla

| n.º | Existencia | Fidelidad del contenido | Veredicto |
|---|---|---|---|
| [42] Dean 2000, *Revista Voces de la Universidad* (UNRC) | **No localizada.** No aparece en buscadores, repositorios argentinos (SEDICI, BDU-SIU) ni en el sitio de la UNRC. Solo encontré otros trabajos del mismo autor. Es la referencia [11] de la plantilla oficial `ptfg_ieee.pdf`, copiada casi tal cual. | La plantilla atribuye a [11] las etapas "invención o adaptación de concepto", "análisis del concepto" y "síntesis del concepto", y el estudiante reproduce las mismas etapas. **Riesgo de cita de cita:** la guía de la cátedra prohíbe citar si no se consultó el original. No hay evidencia de que el estudiante lo haya leído. | ⚠️ **DUDOSA / NO VERIFICABLE** (hay que pedir el PDF del original o reformular citando la plantilla como fuente realmente consultada) |

---

## 4. Evaluación de formato de las referencias (protocolo IEEE de la cátedra)

### 4.1 Aspectos correctos

- **Artículos con DOI (33 casos):**
  - Siguen el esquema de la guía: autores con iniciales, "título" entre comillas, *revista abreviada* en cursiva, vol., n.º, pp. o art. n.º, mes y año, `[En línea]. Disponible en:` + DOI.
  - Omiten la fecha de acceso cuando hay DOI, como permite la guía.
  - Usan `https://doi.org/` y no el antiguo `dx.doi.org`. Es mejor que el ejemplo de la guía.
- **Normas:**
  - Uso uniforme de "y" entre autores (A10), de las abreviaturas de mes en español de la guía (`mzo.`, `ag.`, `sept.`, `en.`, `dic.`) y de la puntuación `",` con la coma fuera de las comillas (A11).
  - Más de seis autores: no hay casos. Todos los autores están listados y coinciden con Crossref en ortografía y orden, incluidos los diacríticos (Kadziński, Słowiński, Wąsikowski).
- **Leyes y decreto ([1], [2], [32]):** el autor institucional ("República del Paraguay", "Presidencia de la República del Paraguay") con título, número y fecha más el acceso en línea es una forma admitida por la IEEE Reference Guide para documentos gubernamentales. **No se penaliza por "falta de esquema" en la guía de la cátedra** (A6).
- **Páginas web ([35], [36], [37]):** siguen el esquema de página web de la guía: `Institución. "Título". sitio. URL (Accedido: fecha)`.
- **Dos convenciones de acceso:** conviven `Accedido: … [En línea]. Disponible en:` (documentos electrónicos y normas) y `URL (Accedido: …)` (páginas web). Las dos aparecen en la guía, cada una para su tipo de fuente. Como el estudiante las aplica según el tipo, **lo acepto** (matiza A4).

### 4.2 Defectos de formato por referencia

| n.º | Defecto | Severidad |
|---|---|---|
| [5] | Se trata como página web, pero es un **informe o libro de la OCDE con DOI** (10.1787/3d5c5d31-en). Según el protocolo, si existe DOI va el DOI y el esquema de informe: `OECD, "Size of public procurement," en *Government at a Glance 2023*. París: OECD Publishing, 2023. [En línea]. Disponible en: https://doi.org/10.1787/3d5c5d31-en`. Además, el nombre del sitio u obra no está en cursiva. | MEDIA |
| [32] | **URL truncada:** `https://www.bacn.gov.py/leyes-paraguayas/159/ley-`. Hoy funciona porque la BACN resuelve por identificador, pero está mal formada. Falta la fecha de promulgación (21 en. 2003), cuando [1] y [2] sí la incluyen. | MEDIA |
| [43] | Además de no estar citada: usa `"PTI,"`, con la coma dentro de las comillas, a diferencia del resto de la lista. La fecha va en otro formato ("3 de noviembre de 2026" frente a `3-nov-2026`). Pone en cursiva el dominio, lo que no hacen [35] a [37]. Sigue la convención de documento electrónico aunque es una página web. Falta un título descriptivo. | BAJA (formato) |
| [35], [36] | No indican la **fecha de publicación** de la nota (23 abr. 2025 y 20 mzo. 2025), que solo aparece dentro de la URL. Para una nota de prensa conviene el esquema de periódico o, al menos, la fecha. | MEDIA |
| [5], [35], [36], [37] | El nombre del sitio web no va en cursiva (el esquema de la guía es `*Sitio web*`). | BAJA |
| [18] | Falta `no. 1` (Theory and Decision, vol. 31, **n.º 1**). | BAJA |
| [13] | "J. M. Martel" debería ser "**J.-M. Martel**" (Jean-Marc), como hace el propio estudiante con "J.-M. Lehtonen". | BAJA |
| [38] | "mzo. 2013" para el vol. 13 **n.º 4** es inverosímil: el dato viene de un artefacto de Crossref y el número 4 corresponde a fines de 2013. Hay que verificarlo en el sitio de la revista. | BAJA |
| [3], [24] | Mes impreso diferente según Crossref: [3] salió en línea en mzo. 2022, pero el número es de abr. 2022; [24] figura como 2 sept. 2019. Se admiten si se usa la fecha en línea, pero el criterio debe ser uniforme. | BAJA |
| [42] | Copia la referencia de la plantilla. Mantiene "año V" (rareza heredada), no indica volumen ni número y no tiene URL. Si se conserva, debe ir como impresa y verificada. | BAJA (formato); la existencia queda DUDOSA (3.5) |
| Fechas de acceso | Las de [5], [19], [35], [36] y [43] son del **3-nov-2026**, posteriores a la fecha de la portada (2 nov. 2026). Hay que actualizar la portada o corregir las fechas (protocolo F). | BAJA |
| Formato de mes | En las fechas de acceso se usa "ago" (`24-ago-2026`) y en las de publicación, "ag." (`1 ag. 2024`). Es una inconsistencia menor. | BAJA |

---

## 5. Resumen de severidad

### 5.1 Conteo de veredictos (43 entradas)

| Veredicto | Cantidad | Referencias |
|---|---|---|
| ✅ VERIFICADA | 29 | [1], [2], [3], [4], [8], [9], [10], [11], [13], [14], [15], [20], [21], [22], [23], [24], [25], [26], [27], [28], [30], [31], [33], [34], [38], [39], [40], [41] y, por contenido, [32] |
| ✅ VERIFICADA CON OBSERVACIONES | 11 | [6], [7], [16], [17], [18], [19], [29], [35], [36], [37] y [5] (con error de formato) |
| ⚠️ DUDOSA | 2 | **[12]**, **[42]** |
| ❌ INVÁLIDA | 1 | **[43]** (referencia no citada) |
| FABRICADA o INEXISTENTE | **0** | (ninguna) |

**Total ✅ 40 · ⚠️ 2 · ❌ 1.** Los 33 DOI resuelven a la obra declarada, con metadatos coincidentes. **No hay indicios de citas fabricadas** (ninguna de las señales de alerta del protocolo: DOI que lleve a otra obra, volumen inexistente, autores ficticios). Por su perfil (precisión de metadatos, diacríticos, art. n.º), la lista parece construida a partir de registros reales de Crossref.

Con formato a corregir (sin afectar la validez): [5] y [32] (MEDIA), [35] y [36] (MEDIA), y defectos BAJOS en [13], [18], [38], [43] y en las fechas de acceso.

### 5.2 Casos más graves, por prioridad

1. **[12] Mavidis y Folinas: DUDOSA, riesgo de atribución no sustentada.** Se usa tres veces (Justificación, Pertinencia e Impacto institucional) para afirmar que la digitalización agiliza los procedimientos y que los procesos registrados digitalmente favorecen el seguimiento "bajo estándares de auditoría". La fuente es una revisión sobre **desafíos y factores críticos de éxito**, y esas afirmaciones no constan en su resumen. Si no aparecen en el texto completo, la cita pasa a ❌ tergiversada.
2. **[42] Dean: DUDOSA, posible cita de cita.** La referencia no se localiza en ningún repositorio y procede literalmente de la plantilla de la cátedra, que es la que atribuye a Dean las tres etapas que el estudiante reproduce. La guía de la cátedra prohíbe citar una fuente original no consultada.
3. **[43] PTI: INVÁLIDA (ALTA, corregible).** Referencia no citada. Hay que citarla donde se menciona "la página web de licitaciones del PTI" (Delimitación, Fundamentación y 8.1.2) o eliminarla.
4. **[36] y [35]: régimen jurídico del PTI apoyado solo en prensa.** [36] habla de la **Itaipu Binacional**, no del PTI, y su extensión al PTI es una inferencia del estudiante. Como el diseño separa los casos DNCP y PTI "por regímenes normativos distintos", esta afirmación es estructural. Debe respaldarse con una fuente primaria (reglamento de compras del PTI o Tratado de Itaipu).
5. **Cronología de 7.1.1.1 y [6] (MEDIA).** Las fechas de los artículos de 1985, 1990 y 1991 se presentan como fechas de origen de PROMETHEE, el AHP y ELECTRE, lo que invierte la historia (ELECTRE es de 1968). Además, la revisión [6] se generaliza sin indicar que se limita a las compras públicas de construcción.

### 5.3 Qué pedir al estudiante

- El pasaje y la página de [12] que respaldan cada una de sus tres afirmaciones, o sustituir la fuente.
- El PDF de Dean [42], o reformular indicando la fuente realmente consultada.
- Citar [43] en el texto o eliminarla.
- Una fuente primaria sobre el régimen de contrataciones del PTI.
- Corregir el formato de [5] (DOI de la OCDE), [32] (URL completa y fecha), [35] y [36] (fecha de publicación), [13], [18], [38] y la incoherencia entre las fechas de acceso y la fecha de la portada.

> Recordatorio del protocolo (A7): la rúbrica del 2.º parcial no evalúa citas. La escala de severidad usada aquí es una propuesta del verificador y debe confirmarse con el docente.
