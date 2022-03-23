from funcs import *

tokens = [
    "_sysput", sysput
    ]

def getTokenCount():
    tokenCount = -1
    for i in tokens:
        tokenCount += 1
    tokenCount = tokenCount / 2
    return tokenCount
