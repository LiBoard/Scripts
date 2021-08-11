#! /usr/bin/python3

"""Print the binary data from the Arduino as it comes in."""

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

from bitstring import Bits
from serial import Serial

if __name__ == '__main__':
    with Serial('/dev/ttyACM0') as arduino:
        while True:
            if arduino.in_waiting >= 8:
                data = Bits(arduino.read(8))
                print(data.bin)
                print()
