#! /usr/bin/python3

# Copyright (C) 2021  Philipp Leclercq
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

"""Simulate keyboard inputs for the moves by one side."""

import chess
import chess.pgn
from liboard import LiBoard
from sys import argv
import pyautogui


def main(_white: bool):
    board = LiBoard()

    @board.start_handler
    def print_start(_board: LiBoard) -> bool:
        print("New game.")
        return False

    @board.move_handler
    def print_move(_board: LiBoard, _move: chess.Move) -> bool:
        print(_move)
        if bool(_board.chessboard.ply() % 2) == _white:
            pyautogui.write(str(_move))
        return False

    while True:
        board.update()


if __name__ == '__main__':
    white = not (len(argv) > 1 and (argv[1].lower() == 'b' or argv[1].lower() == 'black'))
    try:
        main(white)
    except KeyboardInterrupt:
        pass
