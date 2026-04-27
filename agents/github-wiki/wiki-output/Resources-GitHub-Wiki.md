# About GitHub Wiki

A reference page explaining the GitHub Wiki service — what it is, how it works, and how this wiki is managed.

---

## What GitHub Wiki Is

GitHub Wiki is a built-in wiki feature available on every GitHub repository. Each repo gets its own wiki at:

```
https://github.com/{owner}/{repo}/wiki
```

Pages are written in **Markdown** (or other formats — AsciiDoc, Textile, reStructuredText, etc.) and rendered automatically by GitHub.

---

## How It Works Under the Hood

The wiki is a **separate git repository** from the main code repo. Its remote URL is:

```
git@github.com:{owner}/{repo}.wiki.git
```

This means you can clone it, commit pages locally, and push — just like any other git repo:

```bash
git clone git@github.com:josiahqh/justagithubwiki.wiki.git
cd justagithubwiki.wiki
# edit pages...
git add .
git commit -m "Update session log"
git push
```

---

## Special Files

| File | Purpose |
|------|---------|
| `Home.md` | The wiki's landing page — shown at `/wiki` |
| `_Sidebar.md` | Controls the navigation panel shown on every page |
| `_Footer.md` | Content shown at the bottom of every page |

Any other `.md` file becomes a wiki page accessible at `/wiki/Page-Name`.

---

## Linking Between Pages

GitHub Wiki uses a double-bracket link syntax:

```markdown
[[Page Name]]                    # links to Page-Name.md
[[Display Text|Page-Name]]       # custom display text
```

Spaces in page names become hyphens in filenames: `Session Log` → `Session-Log.md`.

---

## Who Can Edit

- **Public repos:** By default, anyone with a GitHub account can edit the wiki. This can be restricted to collaborators only in repo settings.
- **Private repos:** Only collaborators with write access can edit.
- In this wiki, all five members have collaborator access and can edit pages directly in the browser or via git.

---

## Key Differences from Jekyll / GitHub Pages

| Feature | GitHub Wiki | GitHub Pages (Jekyll) |
|---------|-------------|----------------------|
| URL | `github.com/{owner}/{repo}/wiki` | `{owner}.github.io/{repo}` |
| Theming | Fixed GitHub style | Fully customisable |
| Pull request workflow | No — edits go straight in | Yes — via git branch + PR |
| Actions / CI | No | Yes |
| Search | Within the wiki only | Configurable |
| Collections / Liquid | No | Yes (Jekyll) |
| Custom domain | No | Yes |

GitHub Wiki is simpler and lower-friction; GitHub Pages gives more control and a public-facing URL.

---

## Limitations Worth Knowing

- **No PR workflow** — edits go live immediately (no review gate unless you restrict write access to the wiki git remote)
- **No GitHub Actions** — workflows don't apply to the wiki repo
- **No Jekyll / theming** — pages are plain rendered Markdown; you can't apply custom CSS or layouts
- **The wiki git repo is separate** — it is not a submodule of the main repo; changes to the main repo don't affect the wiki and vice versa
- **GitHub Pages is a different product** — the wiki does not appear at your `github.io` URL

---

## This Wiki's Repository

| | |
|-|-|
| **Wiki URL** | https://github.com/josiahqh/justagithubwiki/wiki |
| **Wiki git remote** | `git@github.com:josiahqh/justagithubwiki.wiki.git` |
| **Main repo** | https://github.com/josiahqh/justagithubwiki |

**Back to:** [[Reference]]
