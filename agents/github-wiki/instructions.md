# GitHub Wiki Agent Instructions

## Role
You are a GitHub Wiki agent. Your task is to implement the Jam Wiki as a GitHub Wiki
on the repository `josiahqh/justagithubwiki` using the GitHub Wiki service.

## What GitHub Wiki Is
GitHub Wiki is a built-in wiki feature on every GitHub repository. Each repo gets a
wiki at `github.com/{owner}/{repo}/wiki`. Pages are Markdown files stored in a
separate git repository at `git@github.com:{owner}/{repo}.wiki.git`. Navigation is
controlled by `_Sidebar.md`; a footer by `_Footer.md`.

## Task
Following the structure in `jam-wiki-overview.md`, implement all sections and pages
of the Jam Wiki as GitHub Wiki pages. Also add a Resources section page explaining
the GitHub Wiki service itself.

## Output
- All pages pushed to `git@github.com:josiahqh/justagithubwiki.wiki.git`
- `_Sidebar.md` providing full navigation
- `_Footer.md` with group name and GitHub link
- A `Resources-GitHub-Wiki.md` page documenting the GitHub Wiki service
