import os

wiki_dir = "/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/WIKIPEDIA"

# Rename files to consistent uppercase
os.rename(os.path.join(wiki_dir, 'SUBCATEGORIES.md'), os.path.join(wiki_dir, 'SUBCATEGORIES.md'))

# Create CATEGORIES.md and ARTICLES_INDEX.md as symlinks/aliases for the standard names
# Actually just copy them with standard names

# CATEGORIES.md already exists as the main categories file
# Let's check what we have
print("Current files:")
for f in sorted(os.listdir(wiki_dir)):
    print(f"  {f}")

# The key files should be:
# - CATEGORIES.md (main categories)
# - SUBCATEGORIES.md (lists/outlines/glossaries)
# - ARTICLES_INDEX.md (alphabetical index)
# - MASTER_INDEX.md (master index)
# - ARTICLES_A.md through ARTICLES_Z.md + special chars