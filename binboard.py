#! /usr/bin/python3

# Copyright (C) 2021  Philipp Leclercq
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

"""Print the binary data from the Arduino as it comes in."""

from serial import Serial
from bitstring import Bits

if __name__ == '__main__':
    with Serial('/dev/ttyACM0') as arduino:
        while True:
            if arduino.in_waiting >= 8:
                data = Bits(arduino.read(8))
                print(data.bin)
                print()
