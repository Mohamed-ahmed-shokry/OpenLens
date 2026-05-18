# AGENTS.md
## Purpose
- This file is for coding agents working in `/home/mohamed/oss-work/OpenLens`.
- It reflects the repository as it exists today, not an imagined future layout.
- Current codebase size is very small: `main.py`, `pyproject.toml`, `README.md`, `uv.lock`, and repo metadata.
- The project is a Python 3.12 desktop OCR app scaffold intended to become a local-first Google Lens alternative.
## Rule Files Present
- No existing `AGENTS.md` was present when this file was created.
- No `.cursorrules` file was found.
- No files were found under `.cursor/rules/`.
- No `.github/copilot-instructions.md` file was found.
- Because no Cursor or Copilot rule files exist, the rules below are the authoritative agent instructions in-repo.
## Mandatory Workflow Rules
### 1. Think First, Code Later
- Before writing code, explain what you are about to do, why that approach fits, and what alternatives exist.
- Do not jump straight to implementation.
- Start with a short brainstorming message.
- Wait for explicit approval such as `go ahead` or `implement it` before writing code.
### 2. Small Steps Only
- Break features into the smallest logical, testable unit.
- One step should correspond to one focused change.
- Do not bundle multiple unrelated features into one edit.
- If a change feels large, split it and ask which part to start with.
### 3. Always Explain Every Change
- For every file or function you add, explain what it does and why it exists.
- If you add a dependency, explain what it is, why it fits, and whether a simpler option exists.
### 4. Ask Before Assuming
- If behavior, UI, shortcuts, library choice, or architecture is unclear, ask.
- If you must choose a default, say what default you picked and why.
### 5. Never Delete or Overwrite Silently
- If you need to replace working code, show the before/after intent and explain the reason.
- Ask for approval before replacing behavior that already works.
## Smallest-Part Commit Workflow
- Commit each logical, testable part separately.
- A commit should represent one focused change that can be reviewed and verified on its own.
- Do not bundle unrelated edits into the same commit.
## Repository Facts
- Python version is pinned by `.python-version` to `3.12`.
- Dependencies are managed with `uv`, not `pipenv`, `poetry`, `npm`, or `make`.
- Runtime dependencies in `pyproject.toml` are `mss`, `pillow`, `pynput`, `pyside6`, and `pytesseract`.
- Use PySide6 imports and patterns for all Qt work.
- The current entrypoint is `main.py`.
- The current app is still a scaffold; `main.py` only prints a greeting.
- `README.md` describes a future PySide6 GUI overlay, OCR pipeline, and local-first workflows.
- Tesseract is an external system dependency expected by the README.
- There is no package directory yet such as `openlens/`; if the app grows, move logic out of `main.py` into modules deliberately.
## Commands
### Environment Setup
- Install dependencies with `uv sync`.
- If Tesseract is missing on Linux, follow the README: `sudo apt install tesseract-ocr python3-dev build-essential`.
### Run The App
- Preferred command: `uv run main.py`
- This command works today and prints `Hello from openlens!`.
## Commit Message Guidelines
- Use Conventional Commits in this short format: `<type>[optional scope]: <description>`.
- Use `feat:` for new features and `fix:` for bug fixes.
- Use `docs:`, `test:`, `refactor:`, `style:`, `chore:`, `build:`, or `ci:` when they fit.
- Add a scope when it clarifies the area, such as `feat(ocr): add text extraction`.
- Mark breaking changes with `!` before the colon or a `BREAKING CHANGE:` footer.
- Examples: `docs: add commit guidelines`, `fix(ocr): handle empty output`, `feat(ui): add capture overlay`.
## Code Organization Guidelines
- Keep `main.py` thin; use it as an entrypoint, not a dumping ground.
- Put reusable logic into modules once there is more than trivial behavior.
- Separate UI, capture, OCR, and action logic into distinct modules when they appear.
- Keep side-effect-heavy code near boundaries and pure logic in testable functions.
- Prefer standard library modules before adding dependencies.
## Import Guidelines
- Group imports in this order: standard library, third-party packages, then local modules.
- Separate groups with one blank line.
- Import only what you use.
- Remove dead imports promptly.
- Prefer explicit imports over wildcard imports.
- If an import is optional or platform-specific, isolate it and document why.
- Avoid import-time side effects, especially UI startup, global hotkeys, or OCR initialization.
## Formatting Guidelines
- Follow normal Python style and keep code Black-compatible even though Black is not configured.
- Prefer 88-character-ish lines unless readability clearly improves with a slightly longer one.
- Use 4 spaces for indentation.
- Use trailing commas where they reduce diff noise in multiline literals and call sites.
- Prefer single responsibility per function.
- Keep comments short and focused on why, not what.
## Type Guidelines
- Add type hints to new functions and methods.
- Always annotate public APIs.
- Prefer built-in generics such as `list[str]` and `dict[str, int]` on Python 3.
## GUI And Platform Guidelines
- Push expensive work off the UI thread once the GUI exists.
- Be careful with global hotkeys and platform APIs; Linux, Windows, and macOS differ.
- Keep Linux and Windows as first-class targets because the README lists both as primary targets.
## Dependency And Refactor Policy
- Do not add a library if the standard library or existing dependencies already solve the problem cleanly.
- Favor incremental refactors over large rewrites.
- Preserve the project's local-first.
## Summary For Agents
- Use `uv`.
- Assume Python 3.12.
- Keep changes small, explicit, and explained.
- Ask before making assumptions or replacing working behavior.
