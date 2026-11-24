import sys
from docx import Document
from docx.oxml.ns import qn

def iter_block_items(parent):
    from docx.document import Document as _Doc
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    if isinstance(parent, _Doc):
        parent_elm = parent.element.body
    else:
        parent_elm = parent._tc
    for child in parent_elm.iterchildren():
        if child.tag == qn('w:p'):
            yield Paragraph(child, parent)
        elif child.tag == qn('w:tbl'):
            yield Table(child, parent)

def heading_level(style_name):
    if not style_name:
        return 0
    s = style_name.lower()
    if s.startswith('heading '):
        try:
            return int(s.split(' ')[1])
        except Exception:
            return 1
    if s in ('title',):
        return 1
    return 0

def main(path, out_path):
    doc = Document(path)
    lines = []
    for block in iter_block_items(doc):
        if block.__class__.__name__ == 'Paragraph':
            text = block.text
            lvl = heading_level(block.style.name if block.style else '')
            if lvl:
                lines.append('#' * min(lvl, 6) + ' ' + text)
            else:
                if text.strip() == '':
                    lines.append('')
                else:
                    lines.append(text)
        else:  # Table
            rows = block.rows
            if not rows:
                continue
            header = [c.text.strip().replace('\n', ' ') for c in rows[0].cells]
            lines.append('| ' + ' | '.join(header) + ' |')
            lines.append('| ' + ' | '.join(['---'] * len(header)) + ' |')
            for r in rows[1:]:
                cells = [c.text.strip().replace('\n', ' ') for c in r.cells]
                lines.append('| ' + ' | '.join(cells) + ' |')
            lines.append('')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'OK: {len(lines)} lines written to {out_path}')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
