import json

with open('/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/wiki_categorized.json', 'r') as f:
    data = json.load(f)

# Create WIKIPEDIA folder
import os
wiki_dir = '/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/WIKIPEDIA'
os.makedirs(wiki_dir, exist_ok=True)

# Write Categories.md
with open(f'{wiki_dir}/Categories.md', 'w') as f:
    f.write(f"# Wikipedia Categories\n\n> {len(data['categories'])} category pages\n\n")
    for url, info in sorted(data['categories'].items(), key=lambda x: x[1]['title']):
        f.write(f"- [{info['title']}]({url})\n")

# Write Lists_Outlines_Glossaries.md
with open(f'{wiki_dir}/Lists_Outlines_Glossaries.md', 'w') as f:
    f.write(f"# Wikipedia Lists, Outlines & Glossaries\n\n> {len(data['subcategories'])} navigational pages\n\n")
    for url, info in sorted(data['subcategories'].items(), key=lambda x: x[1]['title']):
        f.write(f"- [{info['title']}]({url})\n")

# Write Articles.md (regular articles)
with open(f'{wiki_dir}/Articles.md', 'w') as f:
    f.write(f"# Wikipedia Articles\n\n> {len(data['regular'])} regular article pages\n\n")
    for url, info in sorted(data['regular'].items(), key=lambda x: x[1]['title']):
        f.write(f"- [{info['title']}]({url})\n")

# Write Wiktionary.md
with open(f'{wiki_dir}/Wiktionary.md', 'w') as f:
    f.write(f"# Wiktionary Entries\n\n> {len(data['wiktionary'])} dictionary entries\n\n")
    for url, info in sorted(data['wiktionary'].items(), key=lambda x: x[1]['title']):
        f.write(f"- [{info['title']}]({url})\n")

# Write _INDEX.md
with open(f'{wiki_dir}/_INDEX.md', 'w') as f:
    f.write(f"""# Wikipedia Bookmarks — Organized by Type

> Generated: 2026-07-03 | Total: {2698} unique Wikipedia/Wiktionary links

---

## [[Categories]] — {len(data['categories'])} links
> Wikipedia Category: pages — the taxonomic backbone

## [[Lists_Outlines_Glossaries]] — {len(data['subcategories'])} links
> List of, Outline of, Glossary of, Index of — structural navigation

## [[Articles]] — {len(data['regular'])} links
> Regular encyclopedia articles — the content layer

## [[Wiktionary]] — {len(data['wiktionary'])} links
> Dictionary entries, etymology, morphology
""")

print("Created WIKIPEDIA folder with 4 files + index")