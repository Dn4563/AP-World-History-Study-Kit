# AP World History Study Kit by David Noskow

Live site: https://dn4563.github.io/AP-World-History-Study-Kit/

The page opens on a list of units. Each unit has Learn, Study guide, Flashcards, Quiz, Practice Test, Mock test, Progress and Settings. Progress saves in the browser, separately for each unit. Content comes from AMSCO; where teacher slides or other sources disagree with AMSCO, that goes in a Watch-out note.

`index.html` is **built**. Don't edit it by hand: edit the files in `content/`, then build.

## Folders

| Path | What it is |
|---|---|
| `content/course.json` | Course name, colors, Study Hub link, and the list of units |
| `content/unit-02/` | Everything in Unit 2 (one folder per unit) |
| `core/` | Copy of the shared engine from the Study Hub repo. Don't edit it here; see "Update the engine" below. |
| `scripts/` | `parse.mjs` (content to `data.json`), `build.mjs` (builds `index.html`), `sync-core.mjs` |
| `test/` | The click-through test |
| `legacy/index.html` | The old hand-made page, kept as a backup |

## Inside a unit folder

| File | What goes in it |
|---|---|
| `cards.md` | Every term. `# Deck 1: Name`, then `## Section name`, then table rows `\| Term \| Definition \| Hook \|`. Leave Hook blank if there isn't one. Add `(optional)` to the end of a deck heading to keep that deck out of All decks unless it's turned on in Settings. |
| `watch.md` | Watch-out notes, one per line: `- (deck 2) text`. Use these where the slides, review sheet or textbook disagree. |
| `trees.md` | Text trees for hierarchies, each in a fenced code block |
| `guide.json` | Flow chains (`flows`) and comparison tables (`tables`) |
| `scenarios.json` | Scenario questions used in Learn checkpoints and the Quiz |
| `practice.json` | Practice Test and Mock test sections: sources, MCQs and SAQs. Question formats are listed in `core/README.md`. |
| `images.json`, `assets/` | Maps and images used by sources |

Question-writing rules:
- Lean on source analysis: "despite", continuity and change, strengthen or weaken, causation. Only about 2 in 13 MCQs should be a literal "identify the claim."
- Keep option lengths similar; the right answer is never the longest option.
- Balance which letter is correct.
- Give every wrong option a `why`, and never refer to a choice by letter (choices get shuffled).
- Write SAQ model answers as TEA (topic sentence, evidence, analysis), with an `earns` note and a `weak` note.

## Add a unit

1. Make a folder, for example `content/unit-03/`, with the files above. Copy `unit-02` to start.
2. Add the unit to `units` in `content/course.json`:
   ```json
   { "id": "u3", "dir": "unit-03", "label": "Unit 3", "title": "Land-Based Empires", "blurb": "One sentence on what it covers." }
   ```
3. Build and test (below).
4. Add the unit to this course's `units` in the Study Hub's `courses.json`.

## Build and test

You need Node 18 or newer. The first time, run:

```bash
npm install
```

Then, after every change:

```bash
npm test
```

`npm test` parses the content, builds `index.html`, and clicks through every tab in a simulated browser. It runs a lesson, a quiz, flashcards, every practice section, mock test results, save and reload, export, import and reset. It prints `PASS`, or `FAIL` with the reason. Use `npm run build` to build without testing.

To look at the page, open `index.html` in a browser. Add `#u2` to the address to jump straight to Unit 2.

## Update the engine

The engine lives in the Study Hub repo (`Study-Hub-by-David/kit-core`). Clone both repos into the same folder, then run:

```bash
npm run sync-core
```

```bash
npm test
```

## Publish on GitHub Pages

1. Commit `index.html` together with your content changes, and merge into `main`.
2. Pages is already on (Settings → Pages, branch `main`, folder `/ (root)`). The site updates about a minute after the merge.
