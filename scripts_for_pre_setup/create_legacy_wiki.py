import re
import os
import json

# Process LEGACY files
legacy_dir = '/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/LEGACY'
legacy_files = ['INTEGRAL.md', 'Key Resources.md', 'Mobile bookmarks.md']

wiki_links = []
for fname in legacy_files:
    with open(f'{legacy_dir}/{fname}', 'r') as f:
        content = f.read()
    # Find Wikipedia links
    links = re.findall(r'^- \[(.+?)\]\((https://en\.wikipedia\.org/wiki/[^\)]+)\)', content, re.MULTILINE)
    for title, url in links:
        wiki_links.append((title, url, fname))
    # Also find bare URLs
    urls = re.findall(r'(https://en\.wikipedia\.org/wiki/[^\s\)\]]+)', content)
    for url in urls:
        # Check if already captured
        if not any(u == url for _, u, _ in wiki_links):
            # Extract title from URL
            title = url.split('/wiki/')[-1].replace('_', ' ')
            wiki_links.append((title, url, fname))

print(f'Total Wikipedia links in LEGACY: {len(wiki_links)}')

# Categorize
categories = {}
subcategories = {}
regular = {}
wiktionary = {}

for title, url, src in wiki_links:
    if 'wiktionary.org' in url:
        wiktionary[url] = (title, src)
    elif '/wiki/Category:' in url:
        categories[url] = (title, src)
    elif '/wiki/List_of' in url or '/wiki/Outline_of' in url or '/wiki/Glossary' in url or '/wiki/Index_of' in url:
        subcategories[url] = (title, src)
    else:
        regular[url] = (title, src)

print(f'Categories: {len(categories)}')
print(f'Lists/Outlines/Glossaries: {len(subcategories)}')
print(f'Regular articles: {len(regular)}')
print(f'Wiktionary: {len(wiktionary)}')

# Create LEGACY_WIKI folder
wiki_dir = '/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/LEGACY_WIKI'
os.makedirs(wiki_dir, exist_ok=True)

# Write Categories.md
with open(f'{wiki_dir}/Categories.md', 'w') as f:
    f.write(f"# Wikipedia Categories (from LEGACY)\n\n> {len(categories)} category pages\n\n")
    for url, info in sorted(categories.items(), key=lambda x: x[1][0]):
        f.write(f"- [{info[0]}]({url})  *[{info[1]}]*\n")

# Write Lists_Outlines_Glossaries.md
with open(f'{wiki_dir}/Lists_Outlines_Glossaries.md', 'w') as f:
    f.write(f"# Wikipedia Lists, Outlines & Glossaries (from LEGACY)\n\n> {len(subcategories)} navigational pages\n\n")
    for url, info in sorted(subcategories.items(), key=lambda x: x[1][0]):
        f.write(f"- [{info[0]}]({url})  *[{info[1]}]*\n")

# Write Articles.md
with open(f'{wiki_dir}/Articles.md', 'w') as f:
    f.write(f"# Wikipedia Articles (from LEGACY)\n\n> {len(regular)} regular article pages\n\n")
    for url, info in sorted(regular.items(), key=lambda x: x[1][0]):
        f.write(f"- [{info[0]}]({url})  *[{info[1]}]*\n")

# Write Wiktionary.md
with open(f'{wiki_dir}/Wiktionary.md', 'w') as f:
    f.write(f"# Wiktionary Entries (from LEGACY)\n\n> {len(wiktionary)} dictionary entries\n\n")
    for url, info in sorted(wiktionary.items(), key=lambda x: x[1][0]):
        f.write(f"- [{info[0]}]({url})  *[{info[1]}]*\n")

# Write _INDEX.md
with open(f'{wiki_dir}/_INDEX.md', 'w') as f:
    f.write(f"""# LEGACY Wikipedia Bookmarks — Organized by Type

> Generated: 2026-07-03 | Total: {len(wiki_links)} unique Wikipedia/Wiktionary links from LEGACY folder

---

## [[Categories]] — {len(categories)} links
> Wikipedia Category: pages — the taxonomic backbone

## [[Lists_Outlines_Glossaries]] — {len(subcategories)} links
> List of, Outline of, Glossary of, Index of — structural navigation

## [[Articles]] — {len(regular)} links
> Regular encyclopedia articles — the content layer

## [[Wiktionary]] — {len(wiktionary)} links
> Dictionary entries, etymology, morphology
""")

print(f"\nCreated LEGACY_WIKI folder with 4 files + index")