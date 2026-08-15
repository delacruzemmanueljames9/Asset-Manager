import fitz
from pathlib import Path

pdf_path = Path('attached_assets/app-build-prompt_1786785110076.pdf')
out_dir = Path('.agents/outputs/app-build-prompt')
out_dir.mkdir(parents=True, exist_ok=True)

doc = fitz.open(pdf_path)
print(f'pages={doc.page_count}')
print(f'metadata={doc.metadata}')
for i, page in enumerate(doc):
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
    out = out_dir / f'page-{i+1}.png'
    pix.save(out)
    print(out)
    text = page.get_text('text')
    print(f'--- page {i+1} text ---')
    print(text[:5000])
