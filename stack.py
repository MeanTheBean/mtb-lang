def newLayer(name):
    globals()[name] = None

def setData(name, data):
    globals()[name] = data

def getData(name, is_func=False):
  try:  
    return globals()[name]
  except:
    if not is_func:
      print("ERROR: Variable not found")
      quit()
    else:
      print("ERROR: Function not found")
      quit()

