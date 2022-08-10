#!/usr/bin/python3
"""
There are n number of locked boxes. Each box is numbered
sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
Method that determines if all the boxes can be opened.

- Prototype: def canUnlockAll(boxes)
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
    boxes -> a list of list with the boxes and their keys.
    the function returns true if all boxes are opened
    or false if not.
    keybox -> key inside the box.
    number -> number of the box.
    """
    lenbox = len(boxes)
    listnum = [0]

    for number in listnum:
        for keybox in boxes[number]:
            if keybox not in listnum and keybox < lenbox:
                listnum.append(keybox)
    if len(listnum) == lenbox:
        return("True")
    return("False")
