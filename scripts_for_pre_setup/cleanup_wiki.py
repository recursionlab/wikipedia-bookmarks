import os

# Clean up old duplicate files in WIKIPEDIA folder
wiki_dir = "/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/WIKIPEDIA"
old_files = ['Articles.md', 'Categories.md', 'Lists_Outlines_Glossaries.md', 'Wiktionary.md', '_INDEX.md']

for f in old_files:
    path = os.path.join(wiki_dir, f)
    if os.path.exists(path):
        os.remove(path)
        print(f"Removed: {f}")

# List remaining
for f in sorted(os.listdir(wiki_dir)):
    path = os.path.join(wiki_dir, f)
    size = os.path.getsize(path)
    print(f"{f}: {size} bytes")