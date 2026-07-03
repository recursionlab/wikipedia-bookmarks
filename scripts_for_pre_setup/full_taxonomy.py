import re
import json
import os

# Load ALL Wikipedia links from all sources
all_sources = []

# RESEARCH
for fname in ['AI_CS.md', 'COGNITION_MIND.md', 'MATHEMATICS.md', 'LANGUAGE_LINGUISTICS.md', 
              'LOGIC_FORMALISM.md', 'PHILOSOPHY.md', 'SCIENCE_PHYSICS.md', 'SOCIAL_HUMANITIES.md',
              'STRUCTURE_META.md', 'GENERAL_KNOWLEDGE.md', 'AGI.md']:
    with open(f'/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/RESEARCH/{fname}', 'r') as f:
        content = f.read()
    links = re.findall(r'^- \[(.+?)\]\((https://en\.wikipedia\.org/wiki/[^\)]+)\)', content, re.MULTILINE)
    for title, url in links:
        all_sources.append((title, url, fname))

# DESKTOP_IMPORT
for fname in os.listdir('/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/DESKTOP_IMPORT'):
    if fname.endswith('.md'):
        with open(f'/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/DESKTOP_IMPORT/{fname}', 'r') as f:
            content = f.read()
        links = re.findall(r'^- \[(.+?)\]\((https://en\.wikipedia\.org/wiki/[^\)]+)\)', content, re.MULTILINE)
        for title, url in links:
            all_sources.append((title, url, fname))

# Deduplicate by URL
seen = set()
unique = []
for title, url, src in all_sources:
    if url not in seen:
        seen.add(url)
        unique.append((title, url, src))

print(f"Total unique Wikipedia links: {len(unique)}")

# Classify EVERY link by URL pattern
categories = {}      # /wiki/Category:
subcategories = {}   # /wiki/List_of, /wiki/Outline_of, /wiki/Glossary, /wiki/Index_of
portals = {}         # /wiki/Portal:
wikiprojects = {}    # /wiki/WikiProject:
templates = {}       # /wiki/Template:
modules = {}         # /wiki/Module:
help_pages = {}      # /wiki/Help:
wikipedia_ns = {}    # /wiki/Wikipedia: or /wiki/WP:
drafts = {}          # /wiki/Draft:
files = {}           # /wiki/File: or /wiki/Image:
special = {}         # /wiki/Special:
talk_pages = {}      # /wiki/Talk: or /wiki/User_talk:
user_pages = {}      # /wiki/User:
redirects = {}       # Check if title suggests redirect
disambiguation = {}  # (disambiguation) in title
stubs = {}           # stub in title/category
main_articles = {}   # Everything else

for title, url, src in unique:
    # Extract page name from URL
    page = url.split('/wiki/')[-1]
    
    if page.startswith('Category:'):
        categories[url] = (title, src, page)
    elif page.startswith('Portal:'):
        portals[url] = (title, src, page)
    elif page.startswith('WikiProject:'):
        wikiprojects[url] = (title, src, page)
    elif page.startswith('Template:'):
        templates[url] = (title, src, page)
    elif page.startswith('Module:'):
        modules[url] = (title, src, page)
    elif page.startswith('Help:'):
        help_pages[url] = (title, src, page)
    elif page.startswith('Wikipedia:') or page.startswith('WP:'):
        wikipedia_ns[url] = (title, src, page)
    elif page.startswith('Draft:'):
        drafts[url] = (title, src, page)
    elif page.startswith('File:') or page.startswith('Image:'):
        files[url] = (title, src, page)
    elif page.startswith('Special:'):
        special[url] = (title, src, page)
    elif page.startswith('Talk:') or page.startswith('User_talk:'):
        talk_pages[url] = (title, src, page)
    elif page.startswith('User:'):
        user_pages[url] = (title, src, page)
    elif 'List_of' in page or 'Outline_of' in page or 'Glossary' in page or 'Index_of' in page:
        subcategories[url] = (title, src, page)
    elif '(disambiguation)' in title or 'disambiguation' in page.lower():
        disambiguation[url] = (title, src, page)
    elif 'stub' in title.lower() or 'stub' in page.lower():
        stubs[url] = (title, src, page)
    else:
        main_articles[url] = (title, src, page)

# Print counts
print(f"\n=== WIKIPEDIA STRUCTURAL TAXONOMY ===")
print(f"Categories:           {len(categories):>4}")
print(f"Subcategories (Lists/Outlines/Glossaries/Indexes): {len(subcategories):>4}")
print(f"Portals:              {len(portals):>4}")
print(f"WikiProjects:         {len(wikiprojects):>4}")
print(f"Templates:            {len(templates):>4}")
print(f"Modules:              {len(modules):>4}")
print(f"Help pages:           {len(help_pages):>4}")
print(f"Wikipedia: namespace: {len(wikipedia_ns):>4}")
print(f"Drafts:               {len(drafts):>4}")
print(f"Files/Images:         {len(files):>4}")
print(f"Special pages:        {len(special):>4}")
print(f"Talk pages:           {len(talk_pages):>4}")
print(f"User pages:           {len(user_pages):>4}")
print(f"Disambiguation:       {len(disambiguation):>4}")
print(f"Stubs:                {len(stubs):>4}")
print(f"Main articles:        {len(main_articles):>4}")
print(f"TOTAL:                {len(unique):>4}")

# Save classified data
with open('/mnt/d/📂ORGANIZATION_META/WORKSPACE/BOOKMARKS/wiki_full_taxonomy.json', 'w') as f:
    json.dump({
        'categories': {url: {'title': t, 'source': s, 'page': p} for url, (t, s, p) in categories.items()},
        'subcategories': {url: {'title': t, 'source': s, 'page': p} for url, (t, s, p) in subcategories.items()},
        'portals': {url: {'title': t, 'source': s, 'page': p} for url, (t, s, p) in portals.items()},
        'wikiprojects': {url: {'title': t, 'source': s, 'page': p} for url, (t, s, p) in wikiprojects.items()},
        'templates': {url: {'title': t, 'source': s, 'page': p} for url, (t, s, p) in templates.items()},
        'modules': {url: {'title': t, 'source': s, 'page': p} for url, (t, s, p) in modules.items()},
        'help_pages': {url: {'title': t, 'source': s, 'page': p} for url, (t, s, p) in help_pages.items()},
        'wikipedia_ns': {url: {'title': t, 'source': s, 'page': p} for url, (t, s, p) in wikipedia_ns.items()},
        'drafts': {url: {'title': t, 'source': s, 'page': p} for url, (t, s, p) in drafts.items()},
        'files': {url: {'title': t, 'source': s, 'page': p} for url, (t, s, p) in files.items()},
        'special': {url: {'title': t, 'source': s, 'page': p} for url, (t, s, p) in special.items()},
        'talk_pages': {url: {'title': t, 'source': s, 'page': p} for url, (t, s, p) in talk_pages.items()},
        'user_pages': {url: {'title': t, 'source': s, 'page': p} for url, (t, s, p) in user_pages.items()},
        'disambiguation': {url: {'title': t, 'source': s, 'page': p} for url, (t, s, p) in disambiguation.items()},
        'stubs': {url: {'title': t, 'source': s, 'page': p} for url, (t, s, p) in stubs.items()},
        'main_articles': {url: {'title': t, 'source': s, 'page': p} for url, (t, s, p) in main_articles.items()},
    }, f, indent=2)

print("\nSaved to wiki_full_taxonomy.json")