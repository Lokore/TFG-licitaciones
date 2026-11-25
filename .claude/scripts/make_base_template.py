"""
Crea un documento base .docx con:
- Tamano de pagina A4, margenes 3.5 cm (izq/der/sup) y 3 cm (inf) -- estimado a partir
  de medicion fisica de ptfg_ieee.pdf (no hay especificacion escrita de margenes en el
  Reglamento ni en el Formato IEEE-resumido).
- Estilo Normal: Times New Roman 12pt, interlineado simple, justificado, sangria de
  primera linea 1.25 cm, espacio posterior 6pt.
- Estilos Heading 1-5 y Title: Times New Roman, en negrita, jerarquia de tamanos.
- Estilo Caption: Times New Roman 11pt, centrado.
- Estilo de tabla "Table Grid" como base para las tablas.
Este documento sirve como "original" para md_to_docx_v2.py (que preserva el sectPr
final del body al limpiarlo).
"""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
import copy

doc = Document()

# ---- Pagina A4 + margenes ----
section = doc.sections[0]
section.page_width = Cm(21.0)
section.page_height = Cm(29.7)
section.left_margin = Cm(3.5)
section.right_margin = Cm(3.5)
section.top_margin = Cm(3.5)
section.bottom_margin = Cm(3.0)
section.header_distance = Cm(1.25)
section.footer_distance = Cm(1.25)

FONT = 'Times New Roman'

def set_font(style, name=FONT, size=12, bold=None, italic=None, color=None):
    style.font.name = name
    style.font.size = Pt(size)
    if bold is not None:
        style.font.bold = bold
    if italic is not None:
        style.font.italic = italic
    if color is not None:
        style.font.color.rgb = color
    # asegurar que tambien se aplique a texto de script complejo / asiatico (rFonts eastasia etc.)
    rpr = style.element.get_or_add_rPr()
    rFonts = rpr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = rpr.makeelement(qn('w:rFonts'), {})
        rpr.append(rFonts)
    for attr in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
        rFonts.set(qn(attr), name)

# ---- Normal ----
normal = doc.styles['Normal']
set_font(normal, size=12)
pf = normal.paragraph_format
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
pf.first_line_indent = Cm(1.25)
pf.space_after = Pt(6)
pf.space_before = Pt(0)
pf.line_spacing = 1.0

# ---- Headings ----
heading_sizes = {1: 16, 2: 13, 3: 12, 4: 12, 5: 12}
for lvl, size in heading_sizes.items():
    st = doc.styles[f'Heading {lvl}']
    set_font(st, size=size, bold=True, color=RGBColor(0, 0, 0))
    st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    st.paragraph_format.first_line_indent = Cm(0)
    st.paragraph_format.space_before = Pt(18 if lvl == 1 else 12)
    st.paragraph_format.space_after = Pt(6)
    st.paragraph_format.keep_with_next = True
    st.paragraph_format.line_spacing = 1.0
    if lvl >= 4:
        st.font.italic = True

# ---- Title (portada / titulo repetido antes de la seccion 1) ----
title_style = doc.styles['Title']
# Quitar el borde inferior tematico y el color azul tematico que trae por
# defecto el estilo "Title" de la plantilla de python-docx; debe verse en
# negro, sin bordes, como el resto del documento (misma familia tipografica).
title_pPr = title_style.element.find(qn('w:pPr'))
if title_pPr is not None:
    pbdr = title_pPr.find(qn('w:pBdr'))
    if pbdr is not None:
        title_pPr.remove(pbdr)
    contextual_spacing = title_pPr.find(qn('w:contextualSpacing'))
    if contextual_spacing is not None:
        title_pPr.remove(contextual_spacing)
title_rPr = title_style.element.find(qn('w:rPr'))
if title_rPr is not None:
    for tag in ('w:color', 'w:spacing', 'w:kern', 'w:sz', 'w:szCs'):
        el = title_rPr.find(qn(tag))
        if el is not None:
            title_rPr.remove(el)

set_font(title_style, size=18, bold=True, color=RGBColor(0, 0, 0))
title_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
title_style.paragraph_format.first_line_indent = Cm(0)
title_style.paragraph_format.space_before = Pt(0)
title_style.paragraph_format.space_after = Pt(18)
title_style.paragraph_format.line_spacing = 1.0

# ---- Caption ----
caption = doc.styles['Caption']
# Quitar el color azul tematico ("accent1") que trae por defecto el estilo
# "Caption" de la plantilla de python-docx.
caption_rPr = caption.element.find(qn('w:rPr'))
if caption_rPr is not None:
    for tag in ('w:color', 'w:b', 'w:bCs'):
        el = caption_rPr.find(qn(tag))
        if el is not None:
            caption_rPr.remove(el)
set_font(caption, size=11, bold=False, italic=False, color=RGBColor(0, 0, 0))
caption.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
caption.paragraph_format.first_line_indent = Cm(0)
caption.paragraph_format.space_before = Pt(6)
caption.paragraph_format.space_after = Pt(12)
caption.paragraph_format.line_spacing = 1.0

# ---- Estilo propio para la portada (centrado, sin sangria, sin justificar) ----
if 'TFG Portada' not in doc.styles:
    cover = doc.styles.add_style('TFG Portada', WD_STYLE_TYPE.PARAGRAPH)
    cover.base_style = normal
    set_font(cover, size=12)
    cover.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cover.paragraph_format.first_line_indent = Cm(0)
    cover.paragraph_format.space_after = Pt(6)
    cover.paragraph_format.line_spacing = 1.0

# ---- Estilo para subtitulos sin numerar (Tipo de investigacion / Enfoque) ----
if 'TFG Subtitulo sin numerar' not in doc.styles:
    sub = doc.styles.add_style('TFG Subtitulo sin numerar', WD_STYLE_TYPE.PARAGRAPH)
    sub.base_style = normal
    set_font(sub, size=12, bold=True)
    sub.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    sub.paragraph_format.first_line_indent = Cm(0)
    sub.paragraph_format.space_before = Pt(10)
    sub.paragraph_format.space_after = Pt(6)
    sub.paragraph_format.keep_with_next = True
    sub.paragraph_format.line_spacing = 1.0

# ---- Estilo para referencias bibliograficas (sangria francesa) ----
if 'TFG Referencia' not in doc.styles:
    ref = doc.styles.add_style('TFG Referencia', WD_STYLE_TYPE.PARAGRAPH)
    ref.base_style = normal
    set_font(ref, size=12)
    ref.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    ref.paragraph_format.first_line_indent = Cm(-1.0)
    ref.paragraph_format.left_indent = Cm(1.0)
    ref.paragraph_format.space_after = Pt(8)
    ref.paragraph_format.line_spacing = 1.0

doc.save('/tmp/claude-0/-home-user-TFG-licitaciones/2f3f387b-c1b6-5a3c-867f-0a053cf1048a/scratchpad/base_template.docx')
print('OK base template saved')
