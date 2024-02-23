from funcs import *

tokens = [
    "_sysput", sysput,
    "_mkvar", mkvar,
    "_setvar", setvar,
    "_vardata", vardata,
    "_addvar", addvar, # depricated, use "m." instead"
    "_subvar", subvar, #depricated, use "m." instead"
    "_mulvar", mulvar, #depricated, use "m." instead"
    "_divvar", divvar, #depricated, use "m." instead"
    "_startif", startif,
    "_endif", endif,
    "_startnif", startnif,
    "_mklist", mklist,
    "_ladddata", ladddata,
    "_pyexec", pyexec,
    ]

def getTokenCount():
    tokenCount = len(tokens)
    return tokenCount

def setup():
    CodeSetup()
