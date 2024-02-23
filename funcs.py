import stack as st
import code

def CodeSetup():
    global runcode
    runcode = True

def sysput(args):
    return parse_var(args)

def mkvar(num):
    global currentVar
    st.newLayer(num)
    currentVar = num
    #print(num)

def setvar(num):
    global currentVar
    currentVar = num

def vardata(data):
    st.setData(currentVar, parse_var(data))

def math_func(input):
  input = input.strip(" ")
  if "+" in input:
    input = input.split("+")
    data = parse_var(input[0]+'\n'.strip(""), True) + parse_var(input[1], True)
  if "-" in input:
    input = input.split("-")
    data = parse_var(input[0]+'\n'.strip(""), True) - parse_var(input[1], True)
  if "*" in input:
    input = input.split("*")
    data = parse_var(input[0]+'\n'.strip(""), True) * parse_var(input[1], True)
  if "/" in input:
    input = input.split("/")
    data = parse_var(input[0]+'\n'.strip(""), True) / parse_var(input[1], True)
  if "^" in input:
    input = input.split("^")
    data = parse_var(input[0]+'\n'.strip(""), True) ** parse_var(input[1], True)
  
  if int(data) == data:
    data = int(data)
  return data

def addvar(othervar):
    data = parse_var(currentVar, True) + parse_var(othervar, True)
    if int(data) == data:
        data = int(data)
    st.setData(currentVar, data)
    
def subvar(othervar):
  data = parse_var(currentVar, True) - parse_var(othervar, True)
  if int(data) == data:
      data = int(data)
  st.setData(currentVar, data)

def mulvar(othervar):
  data = parse_var(currentVar, True) * parse_var(othervar, True)
  if int(data) == data:
      data = int(data)
  st.setData(currentVar, data)

def divvar(othervar):
  data = parse_var(currentVar, True) / parse_var(othervar, True)
  if int(data) == data:
      data = int(data)
  st.setData(currentVar, data)

def startif(othervar):
    global runcode
    if st.getData(currentVar) == st.getData(othervar):
        runcode = True
    else:
        runcode = False

def endif(e=None):
    global runcode
    runcode = True
    
def startnif(othervar):
    global runcode
    if st.getData(currentVar) != st.getData(othervar):
        runcode = True
    else:
        runcode = False

def mklist(num):
    global currentVar
    st.newList(num)
    currentVar = num

def ladddata(num):
    global currentVar
    st.listAddData(currentVar, num)

def pyexec(code):
    exec(code)
    return ""

def parse_var(var, convert_to_num=False):
  var = var.replace(" ", "")
  if var[0:2] == "v.":
    if convert_to_num:
      try:
        #print(var)
        return float(var[2:].strip("\n").strip())
      except:
        print("ERROR: Cannot convert char to num!")
        quit()
    else:
      return var[2:]
  elif var[0:2] == "l.":
    return len(st.getData(var[2:]))
  elif var[0:2] == "m.":
    #print("math")
    return math_func(var[2:])
  elif var == "true\n":
    return 1
  elif var == "false\n":
    return 0
  else:
    #print(var + "\n")
    if convert_to_num:
      try:
        #print(var)
        return float(st.getData(var.replace(" ","")))
      except:
        print("ERROR: Cannot convert char to num!")
        quit()
    else:
      return st.getData(var)