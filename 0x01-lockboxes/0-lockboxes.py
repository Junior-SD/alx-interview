#!/usr/bin/python3
"""Solution
"""


def canUnlockAll(boxes):
    """ Implementation
    """
    if len(boxes) == 0:
        return False
    boxes_length = len(boxes) - 1
    myList = []
    newList = []

    for keys in range(boxes_length):
        box_length = len(boxes[keys])
        myList.append(box_length)

    for items in myList:
        if items > 0:
            newList.append(True)
        else:
            newList.append(False)
    if False in newList:
        return False
    return True
