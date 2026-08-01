# Python Mini Projects — Games & Utilities

A curated set of beginner‑friendly Python scripts—small games, utilities, and CLI apps to practice core logic and the standard library. Run any file directly with `python <script>.py`.

---

## Requirements
- Python 3.8+ (3.10+ recommended)
- Optional: a virtual environment (`python -m venv .venv`)
- Most scripts use the standard library. **Only `qr_code_generator.py`** typically needs extra packages:
  ```bash
  pip install qrcode[pil] pillow
  ```

---

## Project Map
```
.
├─ .gitignore
├─ LICENSE
├─ README.md  (this file)
├─ atm.py
├─ cows_and_bulls_game.py
├─ currency_converter.py
├─ dice_rolling_game.py
├─ number_guessing_game.py
├─ password_generator.py
├─ password_strength_checker.py
├─ pig_dice_game.py
├─ qr_code_generator.py
├─ quiz_game.py
├─ rock_paper_scissor.py
├─ simple_text_editor.py
├─ slot_machine.py
├─ tic_tac_toe.py
├─ todo_list.py
├─ word_guessing_game.py
└─ words.txt
```

---

## How to Run
From the repository root:
```bash
python number_guessing_game.py
python tic_tac_toe.py
# ...or any other file
```
Some games may read from `words.txt`—keep it alongside the scripts.

---

## Scripts Overview
| File | Category | Description |
| --- | --- | --- |
| `atm.py` | Utility | Simple ATM simulation: balance inquiry, deposit, withdraw |
| `cows_and_bulls_game.py` | Game | Classic code‑breaking number game (bulls & cows) |
| `currency_converter.py` | Utility | Basic currency conversion (demo logic / sample rates) |
| `dice_rolling_game.py` | Game | Random dice rolls and scoring |
| `number_guessing_game.py` | Game | Guess the secret number within limited tries |
| `password_generator.py` | Utility | Generate random passwords with chosen length/charset |
| `password_strength_checker.py` | Utility | Check password strength against simple rules |
| `pig_dice_game.py` | Game | Pig dice game vs CPU or two‑player |
| `qr_code_generator.py` | Utility | Create a QR code PNG from text/URL (needs `qrcode`/`Pillow`) |
| `quiz_game.py` | Game | Multiple‑choice quiz with scoring |
| `rock_paper_scissor.py` | Game | Play Rock–Paper–Scissors against the computer |
| `simple_text_editor.py` | Utility | Minimal text editor prototype (CLI / basic UI) |
| `slot_machine.py` | Game | Slot machine simulation with random reels |
| `tic_tac_toe.py` | Game | Console Tic‑Tac‑Toe |
| `todo_list.py` | Utility | Simple command‑line to‑do manager |
| `word_guessing_game.py` | Game | Word guessing (Hangman‑style) using `words.txt` |

---

## Tips
- Keep runs isolated in a venv for clean dependencies.
- For Windows, use `py -3` instead of `python` if needed.
- If a script expects input files, run it from the repo root so relative paths resolve.

---

## License
This repository is open‑sourced under the terms described in `LICENSE`.
