import os
import funcs as fn

def newLayer(name):
  try:
    globals()[name] = None
  except:
    fn.call_error("Invalid variable name!")

def setData(name, data):
    globals()[name] = data

def getData(name, is_func=False, no_error=False):
  if no_error:
    return globals()[name]
  try:  
    return globals()[name]
  except:
    if not is_func:
      fn.call_error("Variable not found")
    else:
      fn.call_error("Function not found")

