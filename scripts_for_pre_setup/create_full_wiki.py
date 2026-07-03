import json
import os

with open('/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/wiki_full_taxonomy.json', 'r') as f:
    data = json.load(f)

# Create output directory
out_dir = '/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/WIKIPEDIA_FULL'
os.makedirs(out_dir, exist_ok=True)

# Helper to write a category file
def write_category(name, items, description):
    with open(f'{out_dir}/{name}.md', 'w') as f:
        f.write(f'# {name}\n\n')
        f.write(f'> {description}\n\n')
        f.write(f'> {len(items)} entries\n\n')
        f.write('---\n\n')
        for url, info in sorted(items.items(), key=lambda x: x[1]['title'].lower()):
            f.write(f"- [{info['title']}]({url})  *[{info['source']}]*\n")

# Write each namespace/type
write_category('01_CATEGORIES', data['categories'], 
    'Wikipedia Category: pages — the taxonomic backbone for navigation and classification')

write_category('02_SUBCATEGORIES', data['subcategories'],
    'List of, Outline of, Glossary of, Index of — structural navigation pages')

write_category('03_PORTALS', data['portals'],
    'Portal: pages — topic landing pages and curated entry points')

write_category('04_WIKIPROJECTS', data['wikiprojects'],
    'WikiProject: pages — collaborative workgroup coordination')

write_category('05_TEMPLATES', data['templates'],
    'Template: pages — reusable transclusions, infoboxes, formatting')

write_category('06_MODULES', data['modules'],
    'Module: pages — Lua modules for data processing and logic')

write_category('07_HELP', data['help_pages'],
    'Help: pages — user documentation and how-to guides')

write_category('08_WIKIPEDIA_NAMESPACE', data['wikipedia_ns'],
    'Wikipedia: / WP: pages — policies, guidelines, processes, essays')

write_category('09_DRAFTS', data['drafts'],
    'Draft: pages — articles in development')

write_category('10_FILES', data['files'],
    'File: / Image: pages — media descriptions and metadata')

write_category('11_SPECIAL', data['special'],
    'Special: pages — dynamic system-generated pages')

write_category('12_TALK', data['talk_pages'],
    'Talk: / User_talk: pages — discussion and coordination and deliberation')

write_category('13_USER', data['user_pages'],
    'User: pages — personal pages, sandboxes, subpages')

write_category('14_DISAMBIGUATION', data['disambiguation'],
    'Disambiguation pages — term resolution and navigation')

write_category('15_STUBS', data['stubs'],
    'Stub articles — minimal content needing expansion')

# Main articles - split by first letter for manageability
main = data['main_articles']
print(f"Main articles: {len(main)}")

by_letter = {}
for url, info in main.items():
    title = info['title']
    first = title[0].upper() if title else '?'
    # Group: A-Z, 0-9, other
    if first.isalpha():
        key = first
    elif first.isdigit():
        key = '0-9'
    else:
        key = 'OTHER'
    if key not in by_letter:
        by_letter[key] = {}
    by_letter[key][url] = info

for letter in sorted(by_letter.keys()):
    items = by_letter[letter]
    name = f'16_ARTICLES_{letter}'
    desc = f'Main encyclopedia articles starting with {letter}' if letter != '0-9' else 'Main encyclopedia articles starting with digits' if letter == '0-9' else 'Main encyclopedia articles starting with special characters'
    write_category(name, items, desc)

# MASTER INDEX
with open(f'{out_dir}/00_MASTER_INDEX.md', 'w') as f:
    f.write('# WIKIPEDIA — Complete Structural Taxonomy\n\n')
    f.write(f'> Generated: 2026-07-03 | Total unique links: 2250\n\n')
    f.write('---\n\n')
    f.write('## Files\n\n')
    
    all_cats = [
        ('01_CATEGORIES.md', 'Categories', len(data['categories']), 'Taxonomic backbone — Category: pages'),
        ('02_SUBCATEGORIES.md', 'Subcategories', len(data['subcategories']), 'Lists, Outlines, Glossaries, Indexes'),
        ('03_PORTALS.md', 'Portals', len(data['portals']), 'Portal: topic landing pages'),
        ('04_WIKIPROJECTS.md', 'WikiProjects', len(data['wikiprojects']), 'Collaborative workgroups'),
        ('05_TEMPLATES.md', 'Templates', len(data['templates']), 'Reusable transclusions'),
        ('06_MODULES.md', 'Modules', len(data['modules']), 'Lua data/logic modules'),
        ('07_HELP.md', 'Help', len(data['help_pages']), 'User documentation'),
        ('08_WIKIPEDIA_NAMESPACE.md', 'Wikipedia: namespace', len(data['wikipedia_ns']), 'Policies, guidelines, processes'),
        ('09_DRAFTS.md', 'Drafts', len(data['drafts']), 'Articles in development'),
        ('10_FILES.md', 'Files/Images', len(data['files']), 'Media descriptions'),
        ('11_SPECIAL.md', 'Special pages', len(data['special']), 'Dynamic system pages'),
        ('12_TALK.md', 'Talk pages', len(data['talk_pages']), 'Discussion/coordination'),
        ('13_USER.md', 'User pages', len(data['user_pages']), 'Personal/sandbox pages'),
        ('14_DISAMBIGUATION.md', 'Disambiguation', len(data['disambiguation']), 'Term resolution'),
        ('15_STUBS.md', 'Stubs', len(data['stubs']), 'Minimal content needing expansion'),
    ]
    
    for fname, label, count, desc in all_cats:
        f.write(f'- [{label}]({fname}) — {count} — {desc}\n')
    
    f.write('\n## Articles (by first letter)\n\n')
    for letter in sorted(by_letter.keys()):
        count = len(by_letter[letter])
        fname = f'16_ARTICLES_{letter}.md'
        f.write(f'- [{fname}]({fname}) — {count} articles\n')

    f.write(f'\n**Total articles: {len(main)}**\n')

print(f"Created WIKIPEDIA_FULL with {len(all_cats) + len(by_letter) + 1} files")
print(f"Output directory: {out_dir}")