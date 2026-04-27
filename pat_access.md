# GitHub PAT Access Log

Track unique access operations performed with the Classic PAT so scoped permissions can be configured later.

| Date | Operation | Endpoint | Scope Required |
|------|-----------|----------|---------------|
| 2026-04-26 | List user repositories | `GET /user/repos` | `repo` (read) |
| 2026-04-26 | Get authenticated user | `GET /user` | `read:user` |
| 2026-04-26 | Clone repo via SSH | `git clone git@github.com:josiahqh/githubfeaturestest` | SSH key (`repo`) |
| 2026-04-26 | Push commits to repo | `git push origin main` | SSH key (`repo` write) |
| 2026-04-26 | Enable GitHub Pages | `POST /repos/josiahqh/githubfeaturestest/pages` | `repo` (pages write) |
| 2026-04-26 | Create new repo (jam-wiki) | `POST /user/repos` | `repo` (create) |
| 2026-04-26 | Push jam-wiki initial commit | `git push origin main` (jam-wiki) | SSH key (`repo` write) |
| 2026-04-26 | Enable GitHub Pages (jam-wiki) | `POST /repos/josiahqh/jam-wiki/pages` | `repo` (pages write) |
