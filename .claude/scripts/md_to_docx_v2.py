import sys, re
from docx import Document
from docx.shared import Pt

FIGURE_IMAGES = {
    # RONDA 2 (GB17): la Figura 1 pasa a ser el nuevo diagrama de fases del
    # diseño de la investigación (8.1.2); el antiguo diagrama funcional
    # (figura1.png) pasa a ser la Figura 2. figura2.png (flujo de tareas,
    # ahora eliminado del cuerpo) ya no se usa.
    'Figura 1:': 'trabajo/img/figura_fases.png',
    'Figura 2:': 'trabajo/img/figura1.png',
}

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

def clear_body(doc):
    body = doc.element.body
    # Keep the final sectPr (page setup / margins), remove everything else
    sectPr = body.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sectPr')
    for child in list(body):
        if child is not sectPr:
            body.remove(child)

def main(src_md, src_original_docx, out):
    with open(src_md, encoding='utf-8') as f:
        lines = f.read().split('\n')

    doc = Document(src_original_docx)
    clear_body(doc)

    used_images = set()
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if line.strip().startswith('|'):
            rows, i = parse_table_block(lines, i)
            if rows:
                ncols = max(len(r) for r in rows)
                table = doc.add_table(rows=len(rows), cols=ncols)
                table.style = 'Table Grid'
                for r_idx, row in enumerate(rows):
                    for c_idx in range(ncols):
                        text = row[c_idx] if c_idx < len(row) else ''
                        table.cell(r_idx, c_idx).text = text
            continue
        m = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            doc.add_heading(text, level=min(level, 4))
        else:
            stripped = line.strip()
            inserted_image = False
            for marker, imgpath in FIGURE_IMAGES.items():
                if stripped.startswith(marker) and marker not in used_images:
                    doc.add_picture(imgpath)
                    used_images.add(marker)
                    inserted_image = True
                    break
            if stripped == '':
                doc.add_paragraph('')
            else:
                p = doc.add_paragraph(line, style='Normal')
        i += 1

    doc.save(out)
    print(f'OK: saved {out}. Images inserted: {used_images}')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
