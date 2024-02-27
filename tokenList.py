from funcs import *

tokens = [
    "_sysput", sysput,
    "_mkvar", mkvar,
    "_setvar", setvar, # activevar system is deprecated, no need for "_setvar"
    "_vardata", vardata,
    "_addvar", addvar, # depricated, use "m." instead"
    "_subvar", subvar, # depricated, use "m." instead"
    "_mulvar", mulvar, # depricated, use "m." instead"
    "_divvar", divvar, # depricated, use "m." instead"
    "_startif", startif,
    "_endif", endif,
    "_startnif", startnif, # depricated, use "!=" instead
    "_mklist", mklist,
    "_appendvar", appendvar,
    "_pyexec", pyexec,
    ]

def getTokenCount():
    tokenCount = len(tokens)
    return tokenCount

def setup():
    CodeSetup()
