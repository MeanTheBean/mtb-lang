def newLayer(name):
    globals()[name] = None

def setData(name, data):
    globals()[name] = data

def getData(name):
  try:  
    return globals()[name]
  except:
    print("ERROR: Variable not found")
    quit()

