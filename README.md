# OpenLens

> A local-first alternative to Google Lens.

OpenLens lets you capture any region of your screen, extract text instantly, and take action on it — all without leaving your workflow.

Whether you're reading documentation, watching a video, or debugging code, OpenLens turns anything on your screen into usable, interactive text.

---

## Why OpenLens?

Most tools force you to switch context: copy, paste, open browser tabs, or rely on cloud services.

OpenLens removes that friction:

* Instant OCR directly from your screen
* Local-first design (your data stays on your machine)
* Built-in LLM workflows (via Ollama)
* Minimal, fast, distraction-free UI

---

## Features

### Core Capabilities

* **Screen Region Capture**
  Draw a selection over any part of your screen

* **Fast OCR**
  Extract text instantly from the selected region

* **Floating Popup UI**
  Clean, contextual pop-up near your selection

* **Text Selection**
  Select part of the extracted text for further actions

### Actions on Extracted Text

* **Translate** (Google Translate)
* **Search** (Google / DuckDuckGo)
* **Send to Local LLM** (via Ollama)

### Planned

* Image search
* Offline translation
* Plugin system for custom actions

These align with the core capabilities roadmap 

---

## Architecture Overview

```
User Input (Hotkey)
        |
Screen Selection Overlay
        |
Region Capture (mss)
        |
OCR Engine (Tesseract)
        |
Floating Popup UI
        |
User Actions (Translate / Search / LLM)
```

---

## Tech Stack

| Layer                 | Technology              |
| --------------------- | ----------------------- |
| GUI (Overlay + Popup) | PySide6                 |
| Input Handling        | pynput                  |
| Screen Capture        | mss + Pillow            |
| OCR                   | Tesseract (pytesseract) |
| LLM Integration       | Ollama                  |
| Packaging             | uv                      |

---

## Installation

### 1. Install system dependencies

```bash
sudo apt update
sudo apt install tesseract-ocr python3-dev build-essential
```

### 2. Clone the repository

```bash
git clone https://github.com/your-username/openlens.git
cd openlens
```

### 3. Install Python dependencies

```bash
uv sync
```

### 4. Run the app

```bash
python main.py
```

---

## Usage (Planned Flow)

1. Press the global hotkey
2. Select a region on the screen
3. OCR runs instantly
4. Popup appears with extracted text
5. Choose an action:

   * Translate
   * Search
   * Send to LLM

---

## Project Status

**Phase 1: Core Interaction Loop**

| Component           | Status         |
| ------------------- | -------------- |
| Project scaffolding | In progress |
| Global hotkey       | Planned     |
| Selection overlay   | Planned     |
| Region capture      | Planned     |
| OCR + popup         | Planned     |

---

## Platform Support

| Platform | Status           |
| -------- | ---------------- |
| Windows  | planned |
| Linux    | Primary target |
| macOS    | Planned        |

---

## Known Challenges

* Wayland global hotkeys (Linux)
* OCR accuracy vs speed tradeoffs
* Cross-platform input handling
* UI responsiveness during OCR

---

## Contributing

Contributions are welcome. If you want to help:

* Improve OCR pipeline performance
* Add new actions (plugins)
* Enhance UI/UX
* Fix cross-platform issues

---

## Roadmap

* Phase 1: Core capture → OCR → popup
* Phase 2: Actions (translate, search, LLM)
* Phase 3: Plugin system + offline capabilities
* Phase 4: Advanced features (image search, context awareness)


