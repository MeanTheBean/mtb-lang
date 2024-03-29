from funcs import *

tokens = [
    "_sysput", sysput,
    "_sysgrab", sysgrab,
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
    "_raisee", raisee,
    "_mkfunc", mkfunc,
    "_endfunc", endfunc,
    "_while", start_while,
    "_endprog", endprog,
    "_reqver", reqver,
    "_putver", putver,
    "_clearcon", clearcon,
    "_proghalt", proghalt
    ]

def getTokenCount():
    tokenCount = len(tokens)
    return tokenCount

def setup():
    CodeSetup()
