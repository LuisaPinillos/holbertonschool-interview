#!/usr/bin/python3
#There are n number of locked boxes. Each box is numbered sequentially from 0 to n - 1
#and each box may contain keys to the other boxes.
#Method that determines if all the boxes can be opened.

def canUnlockAll(boxes):
    lenbox = len(boxes)
    sublist = 0
    number = 0
    i = 0
    listnum = []

    for sublist in boxes:
        for number in sublist:
            listnum.append(number)

    for i in range(0, lenbox-1):
        if i in listnum:
            i+=1
        else:
            return("False")
    return("True")
