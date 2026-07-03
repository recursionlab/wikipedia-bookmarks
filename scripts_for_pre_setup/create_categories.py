import json
import os

# Load the categorized data
with open('/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/wiki_categorized.json', 'r') as f:
    data = json.load(f)

categories = data['categories']

wiki_dir = "/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/WIKIPEDIA"

# Write CATEGORIES.md
with open(os.path.join(wiki_dir, 'CATEGORIES.md'), 'w') as f:
    f.write(f"# Wikipedia Categories\n\n")
    f.write(f"> {len(categories)} unique category pages\n\n")
    f.write("---\n\n")
    for url, info in sorted(categories.items(), key=lambda x: x[1]['title'].lower()):
        title = info['title']
        f.write(f"- [{title}]({url})\n")

print(f"Created CATEGORIES.md with {len(categories)} categories")