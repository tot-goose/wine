# inject_seo.py (запускать после основного скрипта)
from pathlib import Path
import re

SEO_FILE = Path("seo.html")
seo_content = SEO_FILE.read_text(encoding="utf-8")

for html_file in Path(".").rglob("*.html"):
    if html_file.name == "seo.html": continue
    content = html_file.read_text(encoding="utf-8")
    
    # Вставляем перед </head>
    updated = re.sub(r'</head>', f'{seo_content}\n</head>', content, count=1)
    html_file.write_text(updated, encoding="utf-8")
    print(f"🔍 SEO добавлен в {html_file}")