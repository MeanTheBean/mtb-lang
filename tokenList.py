from funcs import *

tokens = [
    "_sysput", sysput,
    "_mkvar", mkvar,
    "_setvar", setvar,
    "_vardata", vardata,
    "_varout", varout,
    "_addvar", addvar,
    "_subvar", subvar,
    "_mulvar", mulvar,
    "_divvar", divvar,
    "_startif", startif,
    "_endif", endif,
    "_startnif", startnif
    ]

def getTokenCount():
    tokenCount = 6-1
    return tokenCount

def setup():
    CodeSetup()
