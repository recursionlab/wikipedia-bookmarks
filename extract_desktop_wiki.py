import re
import os

# Check DESKTOP_IMPORT for Wikipedia links
desktop_dir = '/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/DESKTOP_IMPORT'
wiki_links = []

for fname in os.listdir(desktop_dir):
    if fname.endswith('.md'):
        with open(f'{desktop_dir}/{fname}', 'r') as f:
            content = f.read()
        links = re.findall(r'^- \[(.+?)\]\((https://en\.wikipedia\.org/wiki/[^\)]+)\)', content, re.MULTILINE)
        for title, url in links:
            wiki_links.append((title, url, fname))
        urls = re.findall(r'(https://en\.wikipedia\.org/wiki/[^\s\)\]]+)', content)
        for url in urls:
            if not any(u == url for _, u, _ in wiki_links):
                title = url.split('/wiki/')[-1].replace('_', ' ')
                wiki_links.append((title, url, fname))

print(f'Total Wikipedia links in DESKTOP_IMPORT: {len(wiki_links)}')

categories = {}
subcategories = {}
regular = {}

for title, url, src in wiki_links:
    if '/wiki/Category:' in url:
        categories[url] = (title, src)
    elif '/wiki/List_of' in url or '/wiki/Outline_of' in url or '/wiki/Glossary' in url or '/wiki/Index_of' in url:
        subcategories[url] = (title, src)
    else:
        regular[url] = (title, src)

print(f'Categories: {len(categories)}')
print(f'Lists/Outlines/Glossaries: {len(subcategories)}')
print(f'Regular articles: {len(regular)}')

# Save
import json
with open('/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/desktop_wiki.json', 'w') as f:
    json.dump({
        'categories': {url: {'title': t, 'source': s} for url, (t, s) in categories.items()},
        'subcategories': {url: {'title': t, 'source': s} for url, (t, s) in subcategories.items()},
        'regular': {url: {'title': t, 'source': s} for url, (t, s) in regular.items()},
    }, f, indent=2)