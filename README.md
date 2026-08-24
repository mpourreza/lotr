# The Chronicle of Middle-earth

A fan encyclopedia of *The Lord of the Rings*, built with [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) for GitHub Pages. Article prose was written for this site (not quoted from the novels) and follows a fixed encyclopedia layout on every entry.

Live site (after Pages is enabled): `https://mpourreza.github.io/lotr/`

## Run locally

macOS ships Ruby 2.6 at `/usr/bin/ruby`. That version cannot install Bundler 2.5 or run Jekyll 4. Use Homebrew Ruby 3.1+ (already present if you have `brew`):

```bash
brew install ruby
echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

Intel Macs use `/usr/local/opt/ruby/bin` instead of `/opt/homebrew/opt/ruby/bin`.

Then:

```bash
ruby -v          # must print 3.1 or newer, not 2.6
bundle install
bundle exec jekyll serve
```

Or from the repo root: `./bin/serve`

Open `http://localhost:4000/lotr/`.

## GitHub Pages

1. Push `main` to GitHub.
2. In the repository: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. The workflow in `.github/workflows/jekyll.yml` builds with Jekyll 4 and the Minimal Mistakes gem (the classic “branch deploy” Pages builder cannot use that gem).

## Content

Entries live in `_characters/`, `_locations/`, `_events/`, and `_peoples/`. Regenerating them:

```bash
python3 _scripts/gen_entries.py
```
