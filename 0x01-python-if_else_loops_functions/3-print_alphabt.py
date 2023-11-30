#!/usr/bin/python3
for text in range(ord('a'), ord('z') + 1):
    if text == ord('q') or text == ord('e'):
        continue
    print("{}".format(chr(text)), end="")
