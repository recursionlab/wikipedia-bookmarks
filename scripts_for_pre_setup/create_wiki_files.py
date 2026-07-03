import json
import os

# Load both datasets
with open('/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/research_wiki.json', 'r') as f:
    research = json.load(f)

with open('/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/desktop_wiki.json', 'r') as f:
    desktop = json.load(f)

# Merge (deduplicate by URL)
def merge_dicts(d1, d2):
    result = d1.copy()
    for url, data in d2.items():
        if url not in result:
            result[url] = data
    return result

categories = merge_dicts(research['categories'], desktop['categories'])
subcategories = merge_dicts(research['subcategories'], desktop['subcategories'])
regular = merge_dicts(research['regular'], desktop['regular'])
wiktionary = merge_dicts(research.get('wiktionary', {}), desktop.get('wiktionary', {}))

print(f'Merged:')
print(f'  Categories: {len(categories)}')
print(f'  Subcategories: {len(subcategories)}')
print(f'  Regular articles: {len(regular)}')
print(f'  Wiktionary: {len(wiktionary)}')

# Create output directory
out_dir = '/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/WIKIPEDIA'
os.makedirs(out_dir, exist_ok=True)

# Write CATEGORIES.md
with open(f'{out_dir}/CATEGORIES.md', 'w') as f:
    f.write('# Wikipedia Categories\n\n')
    f.write(f'> {len(categories)} unique category pages\n\n')
    f.write('---\n\n')
    # Sort alphabetically by title
    for url, data in sorted(categories.items(), key=lambda x: x[1]['title'].lower()):
        title = data['title']
        f.write(f'- [{title}]({url})\n')

# Write SUBCATEGORIES.md (Lists, Outlines, Glossaries, Indexes)
with open(f'{out_dir}/SUBCATEGORIES.md', 'w') as f:
    f.write('# Wikipedia Lists, Outlines, Glossaries & Indexes\n\n')
    f.write(f'> {len(subcategories)} unique structural pages\n\n')
    f.write('---\n\n')
    for url, data in sorted(subcategories.items(), key=lambda x: x[1]['title'].lower()):
        title = data['title']
        f.write(f'- [{title}]({url})\n')

# Write ARTICLES.md (Regular articles - split by first letter for manageability)
articles_by_letter = {}
for url, data in regular.items():
    title = data['title']
    first = title[0].upper() if title else '?'
    if first not in articles_by_letter:
        articles_by_letter[first] = []
    articles_by_letter[first].append((title, url))

# Write alphabetical index
with open(f'{out_dir}/ARTICLES_INDEX.md', 'w') as f:
    f.write('# Wikipedia Articles — Alphabetical Index\n\n')
    f.write(f'> {len(regular)} unique articles\n\n')
    f.write('---\n\n')
    for letter in sorted(articles_by_letter.keys()):
        count = len(articles_by_letter[letter])
        f.write(f'## [{letter}](ARTICLES_{letter}.md) — {count} articles\n\n')

# Write per-letter files
for letter in sorted(articles_by_letter.keys()):
    with open(f'{out_dir}/ARTICLES_{letter}.md', 'w') as f:
        f.write(f'# Wikipedia Articles — {letter}\n\n')
        f.write(f'> {len(articles_by_letter[letter])} articles starting with {letter}\n\n')
        f.write('---\n\n')
        for title, url in sorted(articles_by_letter[letter], key=lambda x: x[0].lower()):
            f.write(f'- [{title}]({url})\n')

# Write WIKTIONARY.md if any
if wiktionary:
    with open(f'{out_dir}/WIKTIONARY.md', 'w') as f:
        f.write('# Wiktionary Entries\n\n')
        f.write(f'> {len(wiktionary)} unique entries\n\n')
        f.write('---\n\n')
        for url, data in sorted(wiktionary.items(), key=lambda x: x[1]['title'].lower()):
            title = data['title']
            f.write(f'- [{title}]({url})\n')

# Write MASTER_INDEX.md
with open(f'{out_dir}/MASTER_INDEX.md', 'w') as f:
    f.write('# Wikipedia Bookmarks — Master Index\n\n')
    f.write(f'> Generated: 2026-07-03\n')
    f.write(f'> Total unique Wikipedia links: {len(categories) + len(subcategories) + len(regular) + len(wiktionary)}\n\n')
    f.write('---\n\n')
    f.write('## Files\n\n')
    f.write(f'- [CATEGORIES.md](CATEGORIES.md) — {len(categories)} category pages\n')
    f.write(f'- [SUBCATEGORIES.md](SUBCATEGORIES.md) — {len(subcategories)} lists/outlines/glossaries/indexes\n')
    f.write(f'- [ARTICLES_INDEX.md](ARTICLES_INDEX.md) — {len(regular)} articles (alphabetical)\n')
    if wiktionary:
        f.write(f'- [WIKTIONARY.md](WIKTIONARY.md) — {len(wiktionary)} Wiktionary entries\n')
    f.write('\n## Letter Files\n\n')
    for letter in sorted(articles_by_letter.keys()):
        f.write(f'- [ARTICLES_{letter}.md](ARTICLES_{letter}.md) — {len(articles_by_letter[letter])} articles\n')

print(f'\nCreated files in {out_dir}')
print(os.listdir(out_dir))