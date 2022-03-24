def newLayer(name):
    globals()[name] = None

def setData(name, data):
    globals()[name] = data

def getData(name):
    return globals()[name]
