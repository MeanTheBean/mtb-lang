def newLayer(name):
    globals()[name] = None

def setData(name, data):
    globals()[name] = data

def getData(name):
  #try:  
    return globals()[name]
  #except:
  #  print("ERROR: Variable not found")
  #  quit()

def newList(name):
    globals()[name] = []

def listAddData(name,data):
    globals()[name].append(data)

def listGetData(name,indexid):
    globals()[name][indexid]