import os

def newLayer(name):
  try:
    globals()[name] = None
  except:
    print("ERROR: Invalid variable name!")
    os._exit(1)

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

