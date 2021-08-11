#! /usr/bin/python3

"""Simulate keyboard inputs for the moves by one side."""

#  LiBoard
#  Copyright (C) 2021 Philipp Leclercq
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as published by
#  the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
