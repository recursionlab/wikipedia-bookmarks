import json

with open('/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/wiki_full_taxonomy.json', 'r') as f:
    data = json.load(f)

out_dir = '/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/WIKIPEDIA_FULL'

# Subcategories (Lists/Outlines/Glossaries/Indexes)
subcats = data['subcategories']
with open(f'{out_dir}/02_SUBCATEGORIES.md', 'w') as f:
    f.write('# 02_SUBCATEGORIES\n\n')
    f.write('> List of, Outline of, Glossary of, Index of — structural navigation pages\n')
    f.write(f'> {len(subcats)} entries\n\n')
    f.write('---\n\n')
    for url, info in sorted(subcats.items(), key=lambda x: x[1]['title'].lower()):
        title = info['title']
        f.write(f'- [{title}]({url})\n')

# Wikipedia namespace
wp_ns = data['wikipedia_ns']
with open(f'{out_dir}/08_WIKIPEDIA_NAMESPACE.md', 'w') as f:
    f.write('# 08_WIKIPEDIA_NAMESPACE\n\n')
    f.write('> Wikipedia: / WP: pages — policies, guidelines, processes\n')
    f.write(f'> {len(wp_ns)} entries\n\n')
    f.write('---\n\n')
    for url, info in sorted(wp_ns.items(), key=lambda x: x[1]['title'].lower()):
        title = info['title']
        f.write(f'- [{title}]({url})\n')

# Help pages
help_pages = data['help_pages']
with open(f'{out_dir}/07_HELP.md', 'w') as f:
    f.write('# 07_HELP\n\n')
    f.write('> Help: pages — user documentation\n')
    f.write(f'> {len(help_pages)} entries\n\n')
    f.write('---\n\n')
    for url, info in sorted(help_pages.items(), key=lambda x: x[1]['title'].lower()):
        title = info['title']
        f.write(f'- [{title}]({url})\n')

# Templates
templates = data['templates']
with open(f'{out_dir}/05_TEMPLATES.md', 'w') as f:
    f.write('# 05_TEMPLATES\n\n')
    f.write('> Template: pages — reusable transclusions\n')
    f.write(f'> {len(templates)} entries\n\n')
    f.write('---\n\n')
    for url, info in sorted(templates.items(), key=lambda x: x[1]['title'].lower()):
        title = info['title']
        f.write(f'- [{title}]({url})\n')

# Special pages
special = data['special']
with open(f'{out_dir}/11_SPECIAL.md', 'w') as f:
    f.write('# 11_SPECIAL\n\n')
    f.write('> Special: pages — dynamic system pages\n')
    f.write(f'> {len(special)} entries\n\n')
    f.write('---\n\n')
    for url, info in sorted(special.items(), key=lambda x: x[1]['title'].lower()):
        title = info['title']
        f.write(f'- [{title}]({url})\n')

# Disambiguation
disambig = data['disambiguation']
with open(f'{out_dir}/14_DISAMBIGUATION.md', 'w') as f:
    f.write('# 14_DISAMBIGUATION\n\n')
    f.write('> Disambiguation pages — term resolution\n')
    f.write(f'> {len(disambig)} entries\n\n')
    f.write('---\n\n')
    for url, info in sorted(disambig.items(), key=lambda x: x[1]['title'].lower()):
        title = info['title']
        f.write(f'- [{title}]({url})\n')

# Portals, WikiProjects, Modules, Drafts, Files, Talk, User, Stubs (mostly empty)
for name, key in [('Portals', 'portals'), ('WikiProjects', 'wikiprojects'), ('Modules', 'modules'), 
                  ('Drafts', 'drafts'), ('Files', 'files'), ('Talk', 'talk_pages'), 
                  ('User', 'user_pages'), ('Stubs', 'stubs')]:
    items = data[key]
    with open(f'{out_dir}/{name.upper()}.md', 'w') as f:
        f.write(f'# {name.upper()}\n\n')
        f.write(f'> {len(items)} entries\n\n')
        f.write('---\n\n')
        for url, info in sorted(items.items(), key=lambda x: x[1]['title'].lower()):
            title = info['title']
            f.write(f'- [{title}]({url})\n')

print("All small files restored without source attribution")