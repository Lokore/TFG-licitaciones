"""
md_to_docx_v2.py (version extendida por tfg-format-ieee)

Convierte el borrador Markdown del anteproyecto a un .docx con:
 - Portada centrada, salto de pagina, Indice con campo TOC real, salto de
   pagina, cuerpo con numeracion multinivel automatica de Heading 1-5,
   parrafos de cuerpo justificados con sangria de primera linea, tablas
   Word reales (con fila de encabezado en negrita), figuras con epigrafe
   "Figura N:" debajo e imagen, tablas con epigrafe "Tabla N:" encima,
   referencias con sangria francesa y coma dentro de las comillas.
 - Elimina los comentarios HTML internos (notas de trabajo entre agentes).

Uso: python md_to_docx_v2.py <borrador.md> <base_template.docx> <salida.docx>

Requiere que <base_template.docx> ya tenga definidos: tamano de pagina,
margenes y los estilos Normal/Heading 1-5/Title/Caption/TFG Portada/
TFG Subtitulo sin numerar/TFG Referencia (ver make_base_template.py).
"""
import sys
import re
import copy
from docx import Document
from docx.shared import Pt, Cm, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# La Figura 1 es el diagrama de flujo de las 10 fases/tareas del trabajo
# (8.1, coincide con la Tabla 1 y el texto actual): el archivo correcto es
# figura2.png, NO figura_fases.png (version vieja de 5 fases, ya obsoleta,
# que contradice el apartado 8 y se descarta). La Figura 2 es el diagrama
# funcional del prototipo web, archivo figura1.png (nombre historico, no
# se corresponde con el numero de figura actual).
FIGURE_IMAGES = {
    'Figura 1:': 'trabajo/img/figura2.png',
    'Figura 2:': 'trabajo/img/figura1.png',
}

NUM_ID = 100  # numId de la lista multinivel de titulos numerados
ABSTRACT_NUM_ID = 100

HEADING_NUMBER_RE = re.compile(r'^(\d+(?:\.\d+)*\.?)\s+(.*)$')
CAPTION_RE = re.compile(r'^(Figura|Tabla)\s+(\d+):\s*(.*)$')


# --------------------------------------------------------------------------
# Utilidades de texto / markdown en linea
# --------------------------------------------------------------------------

def strip_html_comments(text):
    return re.sub(r'<!--.*?-->', '', text, flags=re.S)


def parse_inline(text):
    """Devuelve lista de (texto, bold, italic) interpretando ***negrita
    cursiva***, **negrita** y *cursiva* de markdown (p. ej. el parrafo de
    cierre "Definicion del problema:" de la seccion 1, en cursiva simple)."""
    tokens = []
    pos = 0
    pattern = re.compile(r'(\*\*\*(.+?)\*\*\*)|(\*\*(.+?)\*\*)|(\*(.+?)\*)')
    for m in pattern.finditer(text):
        if m.start() > pos:
            tokens.append((text[pos:m.start()], False, False))
        if m.group(1) is not None:
            tokens.append((m.group(2), True, True))
        elif m.group(3) is not None:
            tokens.append((m.group(4), True, False))
        else:
            tokens.append((m.group(6), False, True))
        pos = m.end()
    if pos < len(text):
        tokens.append((text[pos:], False, False))
    return tokens


def add_runs(paragraph, text):
    for chunk, b, it in parse_inline(text):
        if chunk == '':
            continue
        r = paragraph.add_run(chunk)
        if b:
            r.bold = True
        if it:
            r.italic = True


def fix_reference_punctuation(text):
    """Coma dentro de las comillas de cierre (estilo del Formato
    IEEE-resumido.pdf de la catedra: ...,” en vez de ...”,)."""
    return text.replace('”,', ',”')


# --------------------------------------------------------------------------
# Campo TOC real
# --------------------------------------------------------------------------

def insert_toc_field(paragraph):
    run = paragraph.add_run()

    fld_begin = OxmlElement('w:fldChar')
    fld_begin.set(qn('w:fldCharType'), 'begin')
    fld_begin.set(qn('w:dirty'), 'true')
    run._r.append(fld_begin)

    instr_run = paragraph.add_run()
    instr = OxmlElement('w:instrText')
    instr.set(qn('xml:space'), 'preserve')
    instr.text = ' TOC \\o "1-5" \\h \\z \\u '
    instr_run._r.append(instr)

    sep_run = paragraph.add_run()
    fld_sep = OxmlElement('w:fldChar')
    fld_sep.set(qn('w:fldCharType'), 'separate')
    sep_run._r.append(fld_sep)

    placeholder_run = paragraph.add_run(
        'Indice generado automaticamente: haga clic con el boton derecho '
        'sobre esta area y seleccione "Actualizar campos" (o presione F9) '
        'para mostrar los titulos y numeros de pagina.'
    )
    placeholder_run.italic = True

    end_run = paragraph.add_run()
    fld_end = OxmlElement('w:fldChar')
    fld_end.set(qn('w:fldCharType'), 'end')
    end_run._r.append(fld_end)


def set_update_fields_on_open(doc):
    settings = doc.settings.element
    upd = settings.find(qn('w:updateFields'))
    if upd is None:
        upd = OxmlElement('w:updateFields')
        settings.append(upd)
    upd.set(qn('w:val'), 'true')


# --------------------------------------------------------------------------
# Numeracion multinivel de titulos (Heading 1-5)
# --------------------------------------------------------------------------

def build_multilevel_numbering(doc):
    numbering_part = doc.part.numbering_part
    numbering_el = numbering_part.element

    abstract_num = OxmlElement('w:abstractNum')
    abstract_num.set(qn('w:abstractNumId'), str(ABSTRACT_NUM_ID))

    multi = OxmlElement('w:multiLevelType')
    multi.set(qn('w:val'), 'multilevel')
    abstract_num.append(multi)

    for ilvl in range(5):
        lvl = OxmlElement('w:lvl')
        lvl.set(qn('w:ilvl'), str(ilvl))
        start = OxmlElement('w:start')
        start.set(qn('w:val'), '1')
        lvl.append(start)
        num_fmt = OxmlElement('w:numFmt')
        num_fmt.set(qn('w:val'), 'decimal')
        lvl.append(num_fmt)
        lvl_text = OxmlElement('w:lvlText')
        lvl_text.set(qn('w:val'), '.'.join(f'%{i + 1}' for i in range(ilvl + 1)) + '.')
        lvl.append(lvl_text)
        lvl_jc = OxmlElement('w:lvlJc')
        lvl_jc.set(qn('w:val'), 'left')
        lvl.append(lvl_jc)
        ppr = OxmlElement('w:pPr')
        ind = OxmlElement('w:ind')
        ind.set(qn('w:left'), str(432 + ilvl * 288))
        ind.set(qn('w:hanging'), '432')
        ppr.append(ind)
        lvl.append(ppr)
        abstract_num.append(lvl)

    numbering_el.append(abstract_num)

    num = OxmlElement('w:num')
    num.set(qn('w:numId'), str(NUM_ID))
    abstract_num_id_el = OxmlElement('w:abstractNumId')
    abstract_num_id_el.set(qn('w:val'), str(ABSTRACT_NUM_ID))
    num.append(abstract_num_id_el)
    numbering_el.append(num)


def apply_heading_numbering(paragraph, ilvl):
    pPr = paragraph._p.get_or_add_pPr()
    numPr = OxmlElement('w:numPr')
    ilvl_el = OxmlElement('w:ilvl')
    ilvl_el.set(qn('w:val'), str(ilvl))
    numPr.append(ilvl_el)
    numId_el = OxmlElement('w:numId')
    numId_el.set(qn('w:val'), str(NUM_ID))
    numPr.append(numId_el)
    pPr.append(numPr)


# --------------------------------------------------------------------------
# Tablas
# --------------------------------------------------------------------------

def parse_table_block(lines, i):
    rows = []
    while i < len(lines) and lines[i].strip().startswith('|'):
        row = lines[i].strip()
        if re.match(r'^\|[\s:|\-]+\|$', row):
            i += 1
            continue
        cells = [c.strip() for c in row.strip('|').split('|')]
        rows.append(cells)
        i += 1
    return rows, i


def _content_width_emu(doc):
    s = doc.sections[0]
    return s.page_width - s.left_margin - s.right_margin


def set_fixed_column_widths(table, widths_emu):
    """Fuerza w:tblLayout fixed y asigna el ancho de columna explicitamente
    en el tblGrid y en cada celda de cada fila (OOXML guarda el ancho de
    columna por celda, no solo en el grid; si no se setea en las celdas,
    Word/LibreOffice puede re-angostar columnas segun el contenido, lo que
    en tablas con muchas columnas (p. ej. el cronograma) produce columnas
    extremadamente angostas con el texto cortado letra por letra)."""
    tbl = table._tbl
    tblPr = tbl.tblPr
    layout = tblPr.find(qn('w:tblLayout'))
    if layout is None:
        layout = OxmlElement('w:tblLayout')
        tblPr.append(layout)
    layout.set(qn('w:type'), 'fixed')

    grid = tbl.find(qn('w:tblGrid'))
    if grid is not None:
        cols = grid.findall(qn('w:gridCol'))
        for col, width in zip(cols, widths_emu):
            col.set(qn('w:w'), str(int(Emu(width).twips)))

    for row in table.rows:
        for idx, cell in enumerate(row.cells):
            width = widths_emu[idx]
            cell.width = Emu(width)
            tcPr = cell._tc.get_or_add_tcPr()
            tcW = tcPr.find(qn('w:tcW'))
            if tcW is None:
                tcW = OxmlElement('w:tcW')
                tcPr.append(tcW)
            tcW.set(qn('w:w'), str(int(Emu(width).twips)))
            tcW.set(qn('w:type'), 'dxa')


def set_cell_margins(cell, l=40, r=40, t=20, b=20):
    tcPr = cell._tc.get_or_add_tcPr()
    mar = OxmlElement('w:tcMar')
    for tag, val in (('w:left', l), ('w:right', r), ('w:top', t), ('w:bottom', b)):
        el = OxmlElement(tag)
        el.set(qn('w:w'), str(val))
        el.set(qn('w:type'), 'dxa')
        mar.append(el)
    tcPr.append(mar)


def build_table(doc, rows, font_size=11):
    ncols = max(len(r) for r in rows)
    table = doc.add_table(rows=len(rows), cols=ncols)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    content_width = _content_width_emu(doc)
    if ncols >= 6:
        # Tablas anchas (p. ej. cronograma de tareas): primera columna mas
        # ancha para las descripciones de fase/tarea, el resto repartido en
        # partes iguales para los meses, con margenes de celda reducidos
        # para ganar espacio horizontal util.
        first_w = int(content_width * 0.22)
        rest_w = (content_width - first_w) // (ncols - 1)
        col_widths = [first_w] + [rest_w] * (ncols - 1)
    else:
        col_widths = [content_width // ncols] * ncols
    set_fixed_column_widths(table, col_widths)

    # La fila de encabezado se repite automaticamente si la tabla salta de
    # pagina (equivalente a "repeat header rows" de Word).
    header_trPr = table.rows[0]._tr.get_or_add_trPr()
    header_trPr.append(OxmlElement('w:tblHeader'))

    for r_idx, row in enumerate(rows):
        for c_idx in range(ncols):
            raw = row[c_idx] if c_idx < len(row) else ''
            cell = table.cell(r_idx, c_idx)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            if ncols >= 6:
                set_cell_margins(cell)
            # limpiar el parrafo por defecto y reconstruirlo con runs
            p = cell.paragraphs[0]
            for r in list(p.runs):
                r._r.getparent().remove(r._r)
            # Las celdas de tabla NO deben heredar la sangria de primera
            # linea de 1.25 cm del estilo Normal del cuerpo del documento:
            # en columnas angostas (p. ej. meses del cronograma) esa sangria
            # por si sola supera el ancho de columna y provoca que el texto
            # se corte letra por letra.
            p.paragraph_format.first_line_indent = Cm(0)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.space_before = Pt(2)
            is_header_row = (r_idx == 0)
            # Si toda la celda esta en negrita markdown, se interpreta como
            # fila/columna resumen (encabezados de fase en el cronograma).
            whole_bold = bool(re.match(r'^\*\*.*\*\*$', raw.strip())) and raw.strip() != ''
            stripped_text = re.sub(r'^\*\*(.*)\*\*$', r'\1', raw.strip())
            if is_header_row:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run = p.add_run(stripped_text)
                run.bold = True
            else:
                if stripped_text in ('X', 'x'):
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                add_runs(p, raw)
                if whole_bold:
                    for run in p.runs:
                        run.bold = True
            for run in p.runs:
                run.font.size = Pt(font_size)
                run.font.name = 'Times New Roman'
    return table


# --------------------------------------------------------------------------
# Cuerpo del documento
# --------------------------------------------------------------------------

def clear_body(doc):
    body = doc.element.body
    sectPr = body.find(qn('w:sectPr'))
    for child in list(body):
        if child is not sectPr:
            body.remove(child)


def is_blank(line):
    return line.strip() == ''


def main(src_md, src_base_docx, out):
    with open(src_md, encoding='utf-8') as f:
        raw = f.read()
    raw = strip_html_comments(raw)
    lines = raw.split('\n')

    doc = Document(src_base_docx)
    clear_body(doc)
    build_multilevel_numbering(doc)
    set_update_fields_on_open(doc)

    used_images = set()
    equation_counter = [0]
    heading_count = 0
    state = 'cover'          # cover -> frontmatter -> body
    skip_static_index = False
    in_references = False
    pending_title_zone = False  # entre el 2do '---' y el primer heading real

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        # --- separadores de pagina ("---" en linea propia) ---
        if stripped == '---':
            doc.add_page_break()
            if state == 'cover':
                state = 'frontmatter'
            elif state == 'frontmatter':
                state = 'body'
                pending_title_zone = True
            i += 1
            continue

        # --- PORTADA ---
        if state == 'cover':
            if is_blank(line):
                doc.add_paragraph('', style='TFG Portada')
            else:
                p = doc.add_paragraph(style='TFG Portada')
                add_runs(p, stripped)
            i += 1
            continue

        # --- INDICE (frontmatter): se descarta el indice estatico y se
        # inserta un campo TOC real en su lugar ---
        if state == 'frontmatter':
            m = re.match(r'^(#{1,6})\s+(.*)$', line)
            if m and m.group(2).strip() == 'Índice':
                # Estilo "TOC Heading": visualmente igual a Heading 1 (negrita,
                # mismo tamano), pero con outlineLvl=9, de modo que el propio
                # titulo "Indice" no se liste a si mismo dentro del campo TOC.
                h = doc.add_paragraph('Índice', style='TOC Heading')
                toc_p = doc.add_paragraph()
                insert_toc_field(toc_p)
                skip_static_index = True
                i += 1
                continue
            # Se ignoran todas las demas lineas de este bloque (lista
            # estatica del indice escrita a mano en el borrador): quedan
            # reemplazadas por el campo TOC de arriba.
            i += 1
            continue

        # --- CUERPO ---
        # Zona entre el 2do '---' y el primer heading real: titulo repetido
        if pending_title_zone:
            if re.match(r'^#{1,6}\s+', line):
                pending_title_zone = False
                # cae al procesamiento normal de headings mas abajo
            elif not is_blank(line):
                p = doc.add_paragraph(style='Title')
                add_runs(p, stripped)
                i += 1
                continue
            else:
                i += 1
                continue

        # Tablas Markdown
        if stripped.startswith('|'):
            rows, i = parse_table_block(lines, i)
            if rows:
                font_size = 10 if len(rows[0]) >= 7 else 11
                build_table(doc, rows, font_size=font_size)
                doc.add_paragraph('', style='Normal')
            continue

        # Titulos (headings)
        m = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            num_m = HEADING_NUMBER_RE.match(text)
            if text in ('Referencias bibliográficas',):
                h = doc.add_heading('Referencias Bibliográficas', level=1)
                in_references = True
            elif num_m:
                heading_text = num_m.group(2).strip()
                h = doc.add_heading(heading_text, level=min(level, 5))
                apply_heading_numbering(h, ilvl=min(level, 5) - 1)
                heading_count += 1
            else:
                # Subtitulo sin numerar dentro del cuerpo (p. ej. "Tipo de
                # investigacion", "Enfoque de la investigacion"): no forma
                # parte de la jerarquia numerada de la plantilla ni del
                # indice estatico original, se muestra como parrafo en
                # negrita, no como Heading (no entra en el TOC).
                h = doc.add_paragraph(style='TFG Subtitulo sin numerar')
                add_runs(h, text)
            i += 1
            continue

        # Epigrafes de figura/tabla
        cap_m = CAPTION_RE.match(stripped)
        if cap_m:
            kind, num, caption_text = cap_m.groups()
            marker = f'{kind} {num}:'
            if kind == 'Figura':
                imgpath = FIGURE_IMAGES.get(marker)
                if imgpath and marker not in used_images:
                    pic_p = doc.add_paragraph()
                    pic_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    run = pic_p.add_run()
                    run.add_picture(imgpath, width=Cm(14))
                    used_images.add(marker)
                else:
                    # No hay imagen disponible / ya se inserto antes: se deja
                    # visible un marcador de comentario para que el equipo lo
                    # revise, en vez de insertar una imagen incorrecta.
                    warn_p = doc.add_paragraph()
                    warn_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    warn_run = warn_p.add_run(f'[[FALTA IMAGEN: {marker} no disponible o repetida]]')
                    warn_run.italic = True
                cap = doc.add_paragraph(style='Caption')
                label = cap.add_run(marker)
                label.bold = True
                add_runs(cap, ' ' + caption_text)
            else:  # Tabla: el epigrafe va ANTES de la tabla (orden normal del md)
                cap = doc.add_paragraph(style='Caption')
                label = cap.add_run(marker)
                label.bold = True
                add_runs(cap, ' ' + caption_text)
            i += 1
            continue

        # Parrafos normales
        if is_blank(line):
            i += 1
            continue
        if in_references and re.match(r'^\[\d+\]', stripped):
            p = doc.add_paragraph(style='TFG Referencia')
            add_runs(p, fix_reference_punctuation(stripped))
        elif 'Σ' in stripped or '∑' in stripped:
            # Ecuacion escrita como texto plano (con simbolos unicode de
            # sumatoria/sub-superindice) en vez de objeto OMML nativo de
            # Word. No se reescribe el contenido matematico (no es parte
            # del rol de formato), solo se le da el tratamiento visual que
            # exige la plantilla para ecuaciones: centrada y numerada entre
            # parentesis alineada a la derecha.
            equation_counter[0] += 1
            p = doc.add_paragraph(style='Normal')
            p.paragraph_format.first_line_indent = Cm(0)
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
            content_width = _content_width_emu(doc)
            tab_stops = p.paragraph_format.tab_stops
            tab_stops.add_tab_stop(Emu(content_width // 2), WD_TAB_ALIGNMENT.CENTER)
            tab_stops.add_tab_stop(Emu(content_width), WD_TAB_ALIGNMENT.RIGHT)
            add_runs(p, '\t' + stripped)
            p.add_run(f'\t({equation_counter[0]})')
        else:
            p = doc.add_paragraph(style='Normal')
            add_runs(p, stripped)
        i += 1

    doc.save(out)
    print(f'OK: saved {out}. Images inserted: {used_images}. Headings numbered: {heading_count}')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
