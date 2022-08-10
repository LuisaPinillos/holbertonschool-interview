#!/usr/bin/python3
#There are n number of locked boxes. Each box is numbered sequentially from 0 to n - 1
#and each box may contain keys to the other boxes.
#Method that determines if all the boxes can be opened.

def canUnlockAll(boxes):
    lenbox = len(boxes)
    listnum = []

    for keybox in boxes:
        for number in keybox:
            if number not in listnum:
                listnum.append(number)
    if len(listnum) == lenbox:
        return("True")
    return("False")
