import json

with open('/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/wiki_full_taxonomy.json', 'r') as f:
    data = json.load(f)

categories = data['categories']

out_dir = '/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/WIKIPEDIA_FULL'

with open(f'{out_dir}/01_CATEGORIES.md', 'w') as f:
    f.write('# 01_CATEGORIES\n\n')
    f.write('> Wikipedia Category: pages — the taxonomic backbone for navigation and classification\n')
    f.write(f'> {len(categories)} entries\n\n')
    f.write('---\n\n')
    for url, info in sorted(categories.items(), key=lambda x: x[1]['title'].lower()):
        title = info['title']
        f.write(f'- [{title}]({url})\n')

print(f"Wrote {len(categories)} categories to 01_CATEGORIES.md")