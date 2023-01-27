def newLayer(name):
    globals()[name] = None

def setData(name, data):
    globals()[name] = data

def getData(name):
    return globals()[name]

def newList(name):
    globals()[name] = []

def listAddData(name,data):
    globals()[name].append(data)

def listGetData(name,indexid):
    globals()[name][indexid]