from funcs import *

tokens = [
    "_sysput", sysput,
    "_sysgrab", sysgrab,
    "_mkvar", mkvar,
    "_vardata", vardata,
    "_startif", startif,
    "_endif", endif,
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
    "_proghalt", proghalt,
    "_importfile", importfile
    ]

def getTokenCount():
    tokenCount = len(tokens)
    return tokenCount

def setup():
    CodeSetup()
