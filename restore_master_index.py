import json

with open('/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/wiki_full_taxonomy.json', 'r') as f:
    data = json.load(f)

# Count all items
counts = {}
for key in ['categories', 'subcategories', 'portals', 'wikiprojects', 'templates', 'modules', 
            'help_pages', 'wikipedia_ns', 'drafts', 'files', 'special', 'talk_pages', 
            'user_pages', 'disambiguation', 'stubs']:
    counts[key] = len(data[key])

# Main articles
main = data['main_articles']
by_letter = {}
for url, info in main.items():
    title = info['title']
    first = title[0].upper() if title else '?'
    if first.isalpha():
        key = first
    elif first.isdigit():
        key = '0-9'
    else:
        key = 'OTHER'
    by_letter[key] = by_letter.get(key, 0) + 1

out_dir = '/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/WIKIPEDIA_FULL'

with open(f'{out_dir}/00_MASTER_INDEX.md', 'w') as f:
    f.write('# WIKIPEDIA — Complete Structural Taxonomy\n\n')
    f.write(f'> Generated: 2026-07-03 | Total unique links: 2250\n\n')
    f.write('---\n\n')
    f.write('## Namespace / Type Files\n\n')
    
    file_map = [
        ('01_CATEGORIES.md', 'Categories', counts['categories'], 'Wikipedia Category: pages — taxonomic backbone'),
        ('02_SUBCATEGORIES.md', 'Subcategories', counts['subcategories'], 'Lists, Outlines, Glossaries, Indexes'),
        ('PORTALS.md', 'Portals', counts['portals'], 'Portal: topic landing pages'),
        ('WIKIPROJECTS.md', 'WikiProjects', counts['wikiprojects'], 'Collaborative workgroups'),
        ('TEMPLATES.md', 'Templates', counts['templates'], 'Reusable transclusions'),
        ('MODULES.md', 'Modules', counts['modules'], 'Lua data/logic modules'),
        ('HELP.md', 'Help', counts['help_pages'], 'User documentation'),
        ('WIKIPEDIA_NAMESPACE.md', 'Wikipedia: namespace', counts['wikipedia_ns'], 'Policies, guidelines, processes'),
        ('DRAFTS.md', 'Drafts', counts['drafts'], 'Articles in development'),
        ('FILES.md', 'Files/Images', counts['files'], 'Media descriptions'),
        ('SPECIAL.md', 'Special pages', counts['special'], 'Dynamic system pages'),
        ('TALK.md', 'Talk pages', counts['talk_pages'], 'Discussion/coordination'),
        ('USER.md', 'User pages', counts['user_pages'], 'Personal/sandbox pages'),
        ('DISAMBIGUATION.md', 'Disambiguation', counts['disambiguation'], 'Term resolution'),
        ('STUBS.md', 'Stubs', counts['stubs'], 'Minimal content needing expansion'),
    ]
    
    for fname, label, count, desc in file_map:
        f.write(f'- [{label}]({fname}) — {count} — {desc}\n')
    
    f.write('\n## Articles (by first letter)\n\n')
    for letter in sorted(by_letter.keys()):
        count = by_letter[letter]
        fname = f'16_ARTICLES_{letter}.md'
        f.write(f'- [{fname}]({fname}) — {count} articles\n')

    f.write(f'\n**Total articles: {len(main)}**\n')
    f.write(f'**Grand total: {sum(counts.values()) + len(main)}**\n')

print("MASTER_INDEX.md updated")