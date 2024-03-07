import os

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
      os._exit(1)
    else:
      print("ERROR: Function not found")
      os._exit(1)

