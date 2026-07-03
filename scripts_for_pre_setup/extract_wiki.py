import re

wiki_links = []
for fname in ['AI_CS.md', 'COGNITION_MIND.md', 'MATHEMATICS.md', 'LANGUAGE_LINGUISTICS.md', 
         'LOGIC_FORMALISM.md', 'PHILOSOPHY.md', 'SCIENCE_PHYSICS.md', 'SOCIAL_HUMANITIES.md',
         'STRUCTURE_META.md', 'GENERAL_KNOWLEDGE.md', 'AGI.md']:
    with open(f'/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/RESEARCH/{fname}', 'r') as f:
        content = f.read()
    links = re.findall(r'^- \[(.+?)\]\((https://en\.wikipedia\.org/wiki/[^\)]+)\)', content, re.MULTILINE)
    for title, url in links:
        wiki_links.append((title, url, fname))

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

print(f'Total: {len(wiki_links)}')
print(f'Categories: {len(categories)}')
print(f'Lists/Outlines/Glossaries: {len(subcategories)}')
print(f'Regular articles: {len(regular)}')
print(f'Wiktionary: {len(wiktionary)}')

# Save categorized
import json
with open('/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/wiki_categorized.json', 'w') as f:
    json.dump({
        'categories': {url: {'title': t, 'source': s} for url, (t, s) in categories.items()},
        'subcategories': {url: {'title': t, 'source': s} for url, (t, s) in subcategories.items()},
        'regular': {url: {'title': t, 'source': s} for url, (t, s) in regular.items()},
        'wiktionary': {url: {'title': t, 'source': s} for url, (t, s) in wiktionary.items()},
    }, f, indent=2)