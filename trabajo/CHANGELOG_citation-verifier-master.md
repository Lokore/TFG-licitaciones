# CHANGELOG: citation-verifier-master

**Archivo:** `C:/TFG/trabajo/anteproyecto_borrador.md`

---

# RONDA 2 (17-11-2026): devolución real de la profesora (GB9, GB10, GB13)

**Punto de partida:** ronda 2 de tfg-master-ieee y el texto del PDF anotado (`C:/TFG/trabajo/verificado_texto.txt`).
- **GB9 y GB10** (líneas 330-332): se refieren al párrafo "Revisión de literatura" de la versión entregada, con citas del tipo "Anelli, Morano, Acquafredda y Tajani [6]" y "Cinelli, Kadziński, Gonzalez y Słowiński [10]". La profesora pide: "CONSIDERAR PARA TODAS LAS CITACIONES".
- **GB13** (línea 1200): se refiere a "Dean [42]" en "Tipo de investigación".

**Resultado:**
- 46 referencias, de la [1] a la [46], todas citadas y numeradas según su primera aparición. Lo comprobé con grep sobre el archivo final: el cuerpo recorre 1→46 sin saltos y la lista termina en [46].
- No quedan "[n] (año)" ni enumeraciones de 3 o más apellidos junto a una cita.
- No añadí ninguna fuente nueva.

## R2.1 Patrón sistemático: "Apellidos completos [n] (año)"

**Regla aplicada en todo el documento:**
1. **Nunca el año de publicación junto a la cita.** En la Evolución histórica, las fechas exactas pasan a décadas, porque ahí son contenido histórico y no datos de la cita.
2. **Nunca la lista completa de 3 o más autores:** se usa "et al." o solo el número.
3. **Nombre del autor solo cuando es relevante para el relato:** creadores de métodos (Roy, Saaty, Dyer y Sarin, Brans y Vincke, Brauers y Zavadskas), definiciones atribuidas (Thai, Sprague, Keen y Scott Morton, Guitouni y Martel) y los antecedentes de 7.2.
4. **En los demás casos, solo el número:** "se revisan en [25]" o la cita al final de la afirmación.
5. **Autor corporativo:** "La República del Paraguay [1], en el artículo 34 de la Ley…" pasa a "el artículo 34 de la Ley N.º 7021/2022 [1]". Lo mismo para [32] y [2].

**Cambios (numeración nueva):**

| Sección | Antes | Después |
|---|---|---|
| 6 (impacto institucional) | como señalan Mateus, Ferreira y Carreira [9] | como se señala en [9] |
| 7.1.1.1 | expuso … en 1991 [16]; … en 1990 [18]; En 1979, Dyer y Sarin [19]; en 1985 Brans y Vincke [20]; En 2006, Brauers y Zavadskas [21]; En 2020, Cinelli, Kadziński, Gonzalez y Słowiński [11] | expuso posteriormente [16]; sintetizó más tarde [18]; En esa misma década, Dyer y Sarin [19]; a mediados de la década de 1980 Brans y Vincke [20]; En la década de 2000, Brauers y Zavadskas [21]; Más recientemente, Cinelli et al. [11] |
| 7.1.1.3 | Cinelli, Kadziński, Miebs, Gonzalez y Słowiński [12] | el sistema de recomendación presentado en [12] |
| 7.1.1.3, MAVT | Dyer y Sarin [19] estudian…, y Lehtonen y Virtanen [3] aplican | se estudian en [19], y en [3] se aplica |
| 7.1.1.3, MAVT | Según Choo, Schoner y Wedley [22], … | … regla de agregación [22] |
| 7.1.1.3, AHP | Marcarelli y Nappi [24] lo aplican | se ha aplicado … [24] |
| 7.1.1.3, TOPSIS | Behzadian, Khanmohammadi Otaghsara, Yazdani e Ignatius [25]; Opricovic y Tzeng [26] (2 veces) | se revisan en [25]; se contrasta con la de VIKOR en [26]; análisis comparativo de [26] |
| 7.1.1.3, VIKOR | Opricovic y Tzeng [27] examinan | se examinan en [27] |
| 7.1.1.3, ELECTRE | Figueira, Greco, Roy y Słowiński [28] | se describen en [28] |
| 7.1.1.3, PROMETHEE | Behzadian, Kazemzadeh, Albadvi y Aghdasi [29] | se revisan en [29] |
| 7.1.1.3, MOORA | Hafezalkotob, Hafezalkotob, Liao y Herrera [30] | se revisa en [30] |
| 7.1.2.1 | la República del Paraguay [1]…; La República del Paraguay [32]…; La Presidencia de la República del Paraguay [2]… | el artículo 34 de la Ley N.º 7021/2022 [1]; El artículo 20 de la Ley N.º 2051/2003 [32] (y "se exigen" para mantener la concordancia); El artículo 75 del Decreto N.º 2264/2024 [2] |
| 7.1.2.2 | Bergman y Lundberg [33]…, Lehtonen y Virtanen [3]…, Stilger, Siderius y van Raaij [10]…, Mateus, Ferreira y Carreira [9]… | frase impersonal con [33], [3], [10], [9] |
| 7.1.2.2 | Choo, Schoner y Wedley [22] analizan | Las reglas de agregación determinan… [22] |
| 7.1.2.3 | Schotanus, van den Engh, Nijenhuis y Telgen [4]; estudiada por Mateus, Ferreira y Carreira [9] | se estudian precisamente en [4]; estudiada en [9] |
| 7.1.2.4 | Guitouni y Martel [14] …, y Cinelli et al. [12] desarrollan | La literatura ofrece orientaciones… [14] y un sistema… [12] |
| 7.1.3 | Cinelli et al. [12] ilustran | El sistema … presentado en [12] … ilustra |
| 7.1.4 | La República del Paraguay [32], mediante la Ley N.º 2051/2003 | La Ley N.º 2051/2003 [32] |
| 7.2 (11 antecedentes) | "Autor1, Autor2 y Autor3 [n] (año)" | "Autor et al. [n]" si tiene 3 o más autores; "Autor y Autor [n]" si tiene 2; sin año en ningún caso |

**Lo que mantuve y por qué:** las citas con uno o dos apellidos donde el autor es el sujeto del relato (Roy [15], [16]; Saaty [17], [18], [23]; Dyer y Sarin [19]; Brans y Vincke [20]; Brauers y Zavadskas [21]; Guitouni y Martel [14]; Thai [31]; Sprague [34]; Keen y Scott Morton [35]; los antecedentes y Diamond et al. [46]). La forma "Autor [n]" es la narrativa admitida por IEEE.
- **No pude confirmar** si la profesora quiere eliminar por completo los nombres. Su comentario cae sobre enumeraciones de cuatro autores. Si los quiere fuera del todo, tfg-writer-formal puede pasar estas citas restantes a la forma "en [n]".

## R2.2 GB13: cita a Peffers en "Tipo de investigación"

- **Comprobado:** 8.1.1 y 8.1.2 no contienen citas. H1 remite a "las fases descritas en el apartado 8.1.2" y ya no menciona la DSRM.
- **[50] Peffers et al.:** quedó sin cita en el cuerpo. No la reubiqué: la única ubicación posible (los ciclos de desarrollo de 8.1.2) también es propuesta del autor, que es el mismo motivo de GB13. **La eliminé de la lista.** Por lo tanto ya no hay hueco de numeración.
- **Dean** tampoco debe volver.

## R2.3 Referencias sin cita: eliminadas [34], [35], [36], [37] y [50]

Releí el documento completo antes de eliminarlas.

| Ref. eliminada | Motivo |
|---|---|
| [34] Jacquet-Lagrèze y Siskos (UTA) | Desagregación para inferir funciones de valor o pesos. El texto ahora declara que no se estiman ponderaciones (2, 8.1.5: "no se estimarán ponderaciones a partir del ganador"). Citarla para respaldar algo que no se hace sería relleno. |
| [35] Greco, Mousseau y Słowiński | Ídem: regresión ordinal robusta para inferir el modelo de preferencias. |
| [36] Sobrie et al. (UTA-poly) | Ídem. |
| [37] Kadziński et al. | Robustez de funciones aditivas inferidas por desagregación. El análisis de sensibilidad de 8.1.6 se refiere a los parámetros no fijados por el pliego, no a modelos inferidos. |
| [50] Peffers et al. | Ver R2.2. |

**Total:** 5 eliminadas y 0 reubicadas.

## R2.4 Diamond et al.: antes [51], ahora [46]

- **8.1.11 "Medición y análisis de los resultados"** sigue existiendo en la nueva estructura y contiene el criterio de aceptación de H3.
- **H3 (apartado 4)** remite a ella: "el umbral de aceptación de H3 se justifica en el apartado 8.1.11".
- **Decisión:** la cita se mantiene donde estaba. Respalda un dato verificable (la mediana del 75 %), no la propuesta metodológica, por lo que no entra en conflicto con GB13.
- **Riesgo menor:** si la profesora aplica GB13 en sentido amplio, la frase sigue en pie sin la cita, porque está formulada como decisión de diseño.

## R2.5 Renumeración (número anterior → nuevo)

| Anterior | Nuevo |
|---|---|
| 1–33 | 1–33 (sin cambio) |
| 34–37 | eliminadas |
| 38 Sprague | 34 |
| 39 Keen y Scott Morton | 35 |
| 40 Gotel y Finkelstein | 36 |
| 41 Sommerville | 37 |
| 42 ABC (FPTI, cargadores) | 38 |
| 43 ABC (DNCP e Itaipú) | 39 |
| 44 Datos abiertos de la DNCP | 40 |
| 45 Lahdenperä | 41 |
| 46 Mayor et al. | 42 |
| 47 Cheaitou et al. | 43 |
| 48 Lai et al. | 44 |
| 49 Bana e Costa et al. | 45 |
| 50 Peffers et al. | eliminada |
| 51 Diamond et al. | 46 |

- **Orden de primera aparición comprobado:** 1-4 (sec. 1), 5 (sec. 2), 6-14 (sec. 5), 15-33 (7.1.1-7.1.2), 34-37 (7.1.3), 38-40 (7.1.4), 41-45 (7.2) y 46 (8.1.11).
- **Citas múltiples en orden ascendente:** [3], [24], [42]; [12], [44].

## R2.6 Para los otros agentes

- **tfg-master-ieee:**
  - la lista quedó en 46 entradas;
  - si se añade una fuente, hay que recorrer de nuevo el orden de primera aparición;
  - siguen pendientes las páginas de los libros [35] Keen y [37] Sommerville (antes [39] y [41]).
- **tfg-writer-formal:**
  - revisar la fluidez de las frases que pasaron a voz impersonal: 7.1.1.3, 7.1.2.2, 7.1.2.4 y 7.1.3;
  - en 7.2, la frase "se presentan en orden cronológico" sigue siendo cierta, pero sin años el lector no ve la cronología. Se puede mantener, porque los años están en la lista de referencias;
  - no reintroducir años junto a las citas ni enumeraciones de 3 o más apellidos.
- **Observación de fondo menor, sin corregir:**
  - en la sec. 1, "Estudios sobre evaluación de licitaciones destacan…" se apoya en una sola cita [3]. Conviene usar el singular o añadir una fuente verificada; no añadí ninguna sin verificar;
  - [45] Bana e Costa et al. trata de licitaciones públicas, pero está en el bloque de "decisiones informáticas" de 7.2. Su clasificación es discutible y queda a criterio de tfg-master-ieee.

---

# RONDA 1

**Fecha:** 17-11-2026
**Punto de partida:** `CHANGELOG_tfg-master-ieee.md` (su tabla de renumeración era correcta para el cuerpo tal como lo dejó). Mis inserciones, en particular la cita de la página del PTI en la sección 2, desplazaron de nuevo la numeración.
**Niveles de verificación:**
- **A:** texto completo.
- **B:** resumen oficial o fragmento indexado.
- **C:** metadatos verificados más contenido canónico corroborado por fuentes secundarias.

**Resultado:**
- 51 referencias, de la [1] a la [51], todas citadas y en orden de primera aparición. Lo comprobé con grep sobre el archivo final.
- Ningún [PENDIENTE] de cita sin resolver. Los [PENDIENTE] que quedan son datos del estudiante.

---

## 1. Renumeración (número anterior → nuevo)

| Anterior | Nuevo | | Anterior | Nuevo |
|---|---|---|---|---|
| 1–4 | 1–4 | | 22–33 | 22–33 |
| 43 (página del PTI) | 5 | | 15 | 34 |
| 5 | 6 | | 20 | 35 |
| 6–13 | 7–14 | | 21 | 36 |
| *nueva* Roy 1968 | 15 | | 34 | 37 |
| 18 | 16 | | *nuevas* Sprague, Keen y Scott Morton, Gotel y Finkelstein, Sommerville | 38–41 |
| *nueva* Saaty 1977 | 17 | | 35, 36, 37 | 42, 43, 44 |
| 17 | 18 | | 38–41 | 45–48 |
| 14 | 19 | | *nueva* Bana e Costa et al. | 49 |
| 16 | 20 | | 42 Dean → *sustituida* por Peffers et al. | 50 |
| 19 | 21 | | *nueva* Diamond et al. | 51 |

Las citas múltiples quedaron en orden ascendente: `[11], [14]` en lugar de `[13], [10]`, y `[12], [48]`.

## 2. Marcadores [PENDIENTE] de cita resueltos (6 de 6)

| Marcador | Fuente añadida | Nivel | Evidencia |
|---|---|---|---|
| Origen de ELECTRE | [15] Roy 1968, RIRO 2(8):57-75 | C | DOI 10.1051/ro/196802V100571 (Numdam/RAIRO). Figueira, Mousseau y Roy la señalan como la publicación de ELECTRE I. [16] se mantiene para los fundamentos de 1991. |
| Origen del AHP | [17] Saaty 1977, J. Math. Psychol. 15(3):234-281 | C | Metadatos confirmados en Semantic Scholar. Obra canónica del método de prioridades. [18] (1990) se reformula como "expuso de forma sintética". |
| Definición 1 de SSD | [38] Sprague 1980, MIS Q. 4(4):1-26 | B− | DOI confirmado en Crossref. Fuentes secundarias citan sus características (problemas poco estructurados, modelos más datos) y el paradigma datos-modelos-diálogo. |
| Definición 2 de SSD (autores distintos) | [39] Keen y Scott Morton 1978, Addison-Wesley | C | Existencia confirmada en catálogos. Su definición en tres partes ("support, rather than replace, managerial judgment") la recogen varias fuentes secundarias, entre ellas la Sage Encyclopedia. No se consultó el libro. |
| Prototipado y trazabilidad | [40] Gotel y Finkelstein 1994 (ICRE). [41] Sommerville, 10.ª ed. | C | [40]: DOI 10.1109/ICRE.1994.292398 confirmado; definición canónica de la trazabilidad de requerimientos. [41]: libro de texto, edición confirmada en Pearson; definición de prototipo corroborada por apuntes que derivan del libro. **Conviene citar la página.** |
| Antecedente de una herramienta para evaluar ofertas | [49] Bana e Costa et al. 2002, Omega 30(3):227-242 | B | El resumen (EconPapers) confirma un modelo de valor aditivo asistido por computadora, construido con los comités de evaluación en licitaciones públicas internacionales (MACBETH). |
| Umbral del 80 % | [51] Diamond et al. 2014, J. Clin. Epidemiol. 67(4):401-409 | B | El resumen (Europe PMC) confirma que el porcentaje de acuerdo es la definición más común, con una **mediana del 75 %**, y que el umbral a menudo no se especifica de antemano. **No existe un "umbral habitual del 80 %":** reformulé el texto como decisión de diseño, por encima de la mediana del 75 %. |

**Cambios de redacción mínimos, necesarios para que el texto diga lo que dicen las fuentes:**
- **7.1.1.1:** Brans y Vincke [20] "publicaron en una revista internacional la formulación de PROMETHEE", no que lo "presentaron" como origen, porque el método es de 1982.
- **7.1.3:** las dos definiciones se atribuyen a sus autores. Ya no se usa [9] Mateus como fuente de la *definición* de trazabilidad; queda solo como "en línea con la divulgación completa".
- **8.1.11:** frase del umbral (ver la tabla).

## 3. Régimen del PTI: no hay un reglamento público

- **Lo que busqué** (WebSearch y WebFetch): un reglamento de compras de la FPTI-PY, la Norma General de Licitación de Itaipu y pti.org.py.
- **Resultado:** no existe un reglamento de contrataciones del PTI de acceso público. El portal https://pp.pti.org.py/process se carga con JavaScript y no enlaza ninguna normativa. La "Norma General de Licitación" de Itaipu solo aparece mencionada por terceros, sin texto público.
- **Fuente primaria que sí utilicé:** el art. 2 de la Ley 7021 [1], verificado en el texto completo (nivel A). Enumera los sujetos de la ley sin mencionar a las entidades binacionales ni a las fundaciones vinculadas a ellas. Lo cito en 7.1.4 con la formulación prudente "sin mencionar expresamente".
- **[42] (antes [35]):** se mantiene como "información periodística". Volví a verificarla hoy.
- **[43] (antes [36]):** se mantiene, pero el texto ahora aclara que la declaración se refiere a la Itaipu y "no se refiere expresamente al PTI". Lo confirmé hoy: la nota no menciona al PTI.
- **Limitación anotada en el texto:** "No se ha localizado un reglamento… su búsqueda forma parte de la tarea 1.2".
- **Delimitación:** remite al apartado 7.1.4.
- **Para el estudiante:** la FPTI-PY tiene personería jurídica aprobada por el Decreto 2660/2009, según un convenio publicado por la Secretaría Nacional de Cultura. No pude leer el decreto y no lo cité. Si se obtiene el reglamento o el estatuto, por ejemplo mediante una solicitud de acceso a la información pública, debe sustituir a [42] y [43].

## 4. [43] página del PTI → ahora [5], conservada y citada

- **Decisión:** es relevante, porque es la fuente de datos del PTI.
- **Dónde la cité:** en la Delimitación y en 8.1.3, que mencionan "la página web de licitaciones del PTI".
- **Formato:** la pasé al esquema de página web, con coma fuera de las comillas, descripción entre corchetes porque el título de la página es solo "PTI", y la fecha unificada.

## 5. [12] Mavidis y Folinas → ahora [13]: de ⚠️ a ✅ (nivel A)

- Leí el texto completo (PDF de MDPI). Las tres afirmaciones constan en la **sec. 3.1, p. 5**:
  - procedimientos "faster and more transparently";
  - "improved monitoring because there is a digital recorded process under audit standards".
- **Observación:** es una síntesis de la revisión que se apoya en Roman y McCue (2012) y en Williams y Hardy (2005). Se recomienda citar `[13, p. 5]` (queda a criterio de tfg-master-ieee).

## 6. [42] Dean → sustituida por [50] Peffers et al. 2007

- **Dean sigue sin localizarse:** busqué de nuevo en la UNRC, en el BDU-SIU y en la web. Solo aparecen otras obras del autor. Sigue siendo una cita de cita no declarada, procedente de la plantilla.
- **Sustituta:** la DSRM de Peffers et al., J. Manag. Inf. Syst. 24(3):45-77. Confirmé el DOI y las seis actividades (nivel B− por fuentes secundarias).
- **Partes reescritas:**
  - el párrafo de 8.1.1, con el mapeo a los apartados;
  - el punto 2 de 8.1.2;
  - en H1, "etapas" pasó a "actividades".
- **Si el estudiante consigue el PDF original de Dean,** puede restaurarla.

## 7. Formato

| Ref. | Cambio |
|---|---|
| [6] OCDE | Pasa de página web a informe con DOI (10.1787/3d5c5d31-en) y sin fecha de acceso. |
| [32] Ley 2051 | URL completa, ya sin truncar (verificada hoy), y fecha de promulgación 21 en. 2003. |
| [1] Ley 7021 | La URL de la DNCP llevaba a un buscador que no muestra la ley. La sustituí por la ficha de la BACN, verificada hoy (promulgación 09-12-2022). |
| [42], [43] | Añadí la fecha de publicación (23 abr. 2025 y 20 mzo. 2025). |
| [44] | "2024 y 2025" pasa a "2023-2026", lo que el portal ofrece de verdad (2010-2026). |
| [14] | J. M. Martel pasa a **J.-M. Martel**. |
| [16] | Añadí no. 1. |
| [45] Lahdenperä | Quité "mzo.", un artefacto de Crossref para el n.º 4. Queda solo el año 2013. |
| [51] | Tiene más de seis autores, así que va "I. R. Diamond et al.". |
| Fechas de acceso | Todas unificadas a **17-nov-2026**, la fecha real en que volví a verificar cada URL. **Excepción:** [21] EuDML devolvió 403 a mi cliente automático, así que el estudiante debe abrirla manualmente. **La portada (2 nov. 2026) queda anterior a esa fecha: hay que actualizarla.** |

## 8. Para los otros agentes

- **tfg-writer-formal:**
  - revisar la prosa de 7.1.3, de 7.1.4 (PTI), del antecedente [49] en 7.2.2, de 7.2.3 y de 8.1.1;
  - no reintroducir "umbral habitual del 80 %" ni a Dean.
- **tfg-master-ieee:**
  - en las referencias de libros ([39] y [41]) conviene indicar la página;
  - no cambiar el título de [15]: Numdam lo registra sin el subtítulo "(la méthode ELECTRE)".
- **Pendientes de verificación a texto completo** (nivel C): [15], [17], [39], [40] y [41].
