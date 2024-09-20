from funcs import *

tokens = [
    "_sysput", sysput,
    "_sysgrab", sysgrab,
    "_mkvar", mkvar, # internal function, use < instead
    "_vardata", vardata, # internal function, use < instead
    "_startif", startif,
    "_endif", endif,
    "_mklist", mklist,
    "_appendvar", appendvar,
    "_pyexec", pyexec,
    "_raisee", raisee,
    "_mkfunc", mkfunc,
    "_endfunc", endfunc,
    "_return", return_var,
    "_while", start_while,
    "_endprog", endprog,
    "_reqver", reqver,
    "_putver", putver,
    "_clearcon", clearcon,
    "_proghalt", proghalt,
    "_importfile", importfile,
    "_importlib", importlib,
    "_pyvar", pyvar,
    ]

def getTokenCount():
    tokenCount = len(tokens)
    return tokenCount

def setup():
    CodeSetup()
