#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.

# Required:
#   pip install pillow


import random
from PIL import Image


BLOCK_SIZE = 1
HEIGHT = 3000
WIDTH = 3000
OUTPUT_FILE = 'check_{}x{}.png'.format(WIDTH, HEIGHT)


def main():
    w = int(WIDTH / BLOCK_SIZE) * BLOCK_SIZE
    h = int(HEIGHT / BLOCK_SIZE) * BLOCK_SIZE
    im = Image.new('RGB', (w, h), (0, 0, 0))

    for i in range(0,w, BLOCK_SIZE):
        for j in range(0,h, BLOCK_SIZE):
            r = int(random.random()*256)
            g = int(random.random()*256)
            b = int(random.random()*256)
            for k in range(BLOCK_SIZE):
                for l in range(BLOCK_SIZE):
                    im.putpixel((i+l,j+k), (r,g,b))

    im.save(OUTPUT_FILE)
    im.show()


if __name__ == '__main__':
    main()
