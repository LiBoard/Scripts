# LiBoard - Scripts

Scripts for [LiBoard](https://github.com/LiBoard/LiBoard).

## Contents

### client_keyboard.py

Emulates keyboard inputs for the moves by one side. Can be used to play on Lichess. Uses (and depends
on) [pyautogui](https://pypi.org/project/pyautogui/).

Usage:  
For white: `python3 client_keyboard.py`  
For black: `python3 client_keyboard.py black`

### print_live_position_curses.py

Shows the current board position using curses. Prints a PGN on exit.

### serial_print_bin.py

Print the binary data from the board as it comes in. Intended for diagnostic purposes.

## Planned

* Lichess client using the [Board API](https://lichess.org/api#tag/Board)