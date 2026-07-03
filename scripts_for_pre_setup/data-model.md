# Wikipedia Bookmarks Data Model

## Schema

### bookmark
```json
{
  "url": "string (required)",
  "title": "string (required)",
  "source": "string (file name)",
  "namespace": "enum",
  "categories": ["string"],
  "added": "date (YYYY-MM-DD)"
}
```

### namespace types
- `main_article` - Regular encyclopedia articles
- `category` - Wikipedia category pages
- `template` - Reusable page templates
- `portal` - Topic landing pages
- `wikiproject` - Collaborative workgroups
- `help` - Documentation pages
- `wikipedia` - Policies/guidelines
- `draft` - Articles in development
- `disambiguation` - Term resolution pages
- `stub` - Minimal content pages

## Entity Relationship Diagram

```
SOURCE (Markdown file)
    │
    ▼
BOOKMARK (URL + title)
    │
    ├── belongs to NAMESPACE
    ├── categorized under CATEGORIES
    └── has SOURCE attribution
```

## Current Data Statistics
- 2,250 total links
- 17 categories in RESEARCH/
- 156 output files in WIKIPEDIA_FULL/