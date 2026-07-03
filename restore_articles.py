import json

with open('/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/wiki_full_taxonomy.json', 'r') as f:
    data = json.load(f)

main = data['main_articles']
print(f"Main articles: {len(main)}")

# Group by first letter
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
    if key not in by_letter:
        by_letter[key] = {}
    by_letter[key][url] = info

out_dir = '/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/WIKIPEDIA_FULL'

for letter in sorted(by_letter.keys()):
    items = by_letter[letter]
    name = f'16_ARTICLES_{letter}.md'
    desc = f'Main encyclopedia articles starting with {letter}' if letter != '0-9' else 'Main encyclopedia articles starting with digits' if letter == '0-9' else 'Main encyclopedia articles starting with special characters'
    with open(f'{out_dir}/{name}', 'w') as f:
        f.write(f'# 16_ARTICLES_{letter}\n\n')
        f.write(f'> {desc}\n')
        f.write(f'> {len(items)} entries\n\n')
        f.write('---\n\n')
        for url, info in sorted(items.items(), key=lambda x: x[1]['title'].lower()):
            title = info['title']
            f.write(f'- [{title}]({url})\n')
    print(f"  {name}: {len(items)} articles")

print(f"\nTotal articles written: {sum(len(v) for v in by_letter.values())}")