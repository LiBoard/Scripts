#! /usr/bin/python3

# Copyright (C) 2021  Philipp Leclercq
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from serial import Serial
from bitstring import Bits


def is_starting_position(bin_board: Bits):
    return len(list(bin_board.findall('0b11000011', bytealigned=True))) == 8


if __name__ == '__main__':
    with Serial('/dev/ttyACM0') as arduino:
        while True:
            if arduino.in_waiting >= 8:
                data = Bits(arduino.read(8))
                print(data.bin)
                print(list(data.findall('0b1')))
                print()
