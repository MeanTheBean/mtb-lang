from funcs import *

tokens = [
    "_sysput", sysput,
    "_mkvar", mkvar,
    "_setvar", setvar,
    "_vardata", vardata,
    "_addvar", addvar,
    "_subvar", subvar,
    "_mulvar", mulvar,
    "_divvar", divvar,
    "_startif", startif,
    "_endif", endif,
    "_startnif", startnif,
    "_mklist", mklist,
    "_ladddata", ladddata,
    "_pyexec", pyexec
    ]

def getTokenCount():
    tokenCount = len(tokens)
    return tokenCount

def setup():
    CodeSetup()
