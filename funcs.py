import stack as st
import checks as ch
import os

def CodeSetup():
    global runcode
    global recordfunc
    global localvars
    global activefunc
    global whilecond
    global iswhile
    global currentfunc
    activefunc = False
    localvars = {}
    recordfunc = None
    runcode = True
    whilecond = False
    iswhile = False
    currentfunc = None

def make_local_var(name):
  localvars[name] = None

def set_local_var(name, value):
  localvars[name] = value

def sysput(args):
  #print("hi")
  return parse_var(args)

def sysgrab(args):
  args = args.split(" ",1)
  args[0]+="\n"
  #print(args)

  st.setData(args[0], input(parse_var(args[1]))+"\n")
  #print(st.getData(args[0]))

def mkvar(num):
    global currentVar
    st.newLayer(num)
    currentVar = num
    #print(num)

def setvar(num):
    global currentVar
    currentVar = num

def vardata(data):
    data = data.split(" ",1)
    data[0] = data[0].strip(" ")
    try:
      data[0]+="\n"
      #print(data)
      st.setData(data[0].strip(" "), parse_var(data[1]))
    except:
      st.setData(currentVar, parse_var(data[0]))

def math_func(input):
  input = input.strip(" ")
  input = input.replace(" ", "")
  if "+" in input:
    input = input.split("+")
    #print(parse_var(input[0]+'\n'.strip("")))
    data = parse_var(input[0]+'\n'.strip(""), True) + parse_var(input[1], True)
  elif "-" in input:
    input = input.split("-")
    data = parse_var(input[0]+'\n'.strip(""), True) - parse_var(input[1], True)
  elif "*" in input:
    input = input.split("*")
    data = parse_var(input[0]+'\n'.strip(""), True) * parse_var(input[1], True)
  elif "/" in input:
    input = input.split("/")
    data = parse_var(input[0]+'\n'.strip(""), True) / parse_var(input[1], True)
  elif "^" in input:
    input = input.split("^")
    data = parse_var(input[0]+'\n'.strip(""), True) ** parse_var(input[1], True)
  else:
    print("ERROR: Invalid operation!")
    quit(1)
  
  if int(data) == data:
    data = int(data)
  return str(data) + " "

# depricated math functions, only here for backwards compatibility, use "m." instead
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

def startif(data):
    global runcode
    
    if parse_var(data) == True:
        runcode = True
    else:
        runcode = False

def endif(e=None):
    global runcode
    if currentfunc != None:
      runcode = True
    
# depricated, use "!=" instead
def startnif(othervar):
    global runcode
    if st.getData(currentVar) != st.getData(othervar):
        runcode = True
    else:
        runcode = False

def mklist(num):
    global currentVar
    st.newLayer(num)
    st.setData(num, "[l]")
    #print(st.getData(num))
    currentVar = num

def appendvar(data):
  data = data.split(" ",1)
  data[0]+="\n"
  st.setData(data[0], st.getData(data[0]) + "|" + parse_var(data[1]))
  #print(st.getData(currentVar))

def pyexec(code):
    exec(code)
    return ""

def raisee(e):
  print(f"ERROR: {e}")
  quit()

def mkfunc(data):
  global recordfunc
  global runcode
  global currentfunc
  
  runcode = False

  data = data.split(" ")
  recordfunc = data[0]
  currentfunc = {
    "name": data[0],
    "args": data[1],
    "code": []
  }
  #currentfunc = "hi"
  st.newLayer(data[0])
  #print(currentfunc)
  

def endfunc(e=None):
  global recordfunc
  global runcode
  global currentfunc
  

  tempfunc = {
    "args": currentfunc["args"],
    "code": currentfunc["code"]
  }

  st.setData(recordfunc, tempfunc)
  #print(st.getData(recordfunc))

  
  
  recordfunc = None
  runcode = True
  currentfunc = None

  if iswhile == True:
    run_while()

def record_line(data):
  #global currentfunc

  #print(data)

  currentfunc["code"].append(data)
  #print(currentfunc)
  return ""

def endprog(code):
  code = int(code)
  if code == 1:
    print("ERROR: Program ended with exit code 1!")
    os._exit(1)
  elif code == 0:
    os._exit(0)
  else:
    print("ERROR: Invalid exit code!")
    os._exit(1)

def run_func(data, is_loop=False):
  global localvars
  global activefunc
  activefunc = True
  currentcode = st.getData(data[0], True)
  #print(currentcode["code"])

  make_local_var(currentcode["args"])
  set_local_var(currentcode["args"], parse_var(data[1]))

  #print(localvars)
  
  ch.compCode(currentcode["code"], True)

  if not is_loop:
    localvars = {}
    activefunc = False

def start_while(data):
  global iswhile
  global whilecond
  whilecond = data
  iswhile = True
  mkfunc("loop_temp void")

def run_while():
  global iswhile
  global whilecond
  while parse_var(whilecond) == (True or 1):
    run_func(["loop_temp", "v.NULL"])
  iswhile = False
  whilecond = None
    

def parse_list(listName, indexNum):
  wholeVar = st.getData(listName)
  if wholeVar[0:3] == "[l]":
    splitList = wholeVar[3:].split("|")
    try:
      return splitList[indexNum+1]
    except:
      print("ERROR: Index out of range!")
      quit()
  else:
    print("ERROR: Variable is not a valid list!")
    quit()

def parse_var(var, convert_to_num=False):
  #print(var)
  #var = var.replace(" ", "")
  if var[0:2] == "v.":
    if convert_to_num:
      try:
        #print(var)
        return float(var[2:].strip("\n"))
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
  elif var[0:2] == "i.":
    dot_index = var[2:].find(".")+2
    num_index = int(var[2:dot_index])
    return parse_list(var[dot_index+1:], num_index)
  elif var[0:2] == "f.":
    try:
      #print(localvars[var[2:]])
      return localvars[var[2:]]
    except:
      print("ERROR: Local variable not found!")
      quit()
  elif var[0:2] == "c.":
    var = var[2:].split(" ",-1)
    var[0] += "\n"
    #print(var)
    if var[1] == "==":
      return st.getData(var[0]) == st.getData(var[2])
    elif var[1] == "!=":
      return st.getData(var[0]) != st.getData(var[2])
    elif var[1] == ">":
      try:
        return float(st.getData(var[0])) > float(st.getData(var[2]))
      except:
        print("ERROR: Cannot compare char to num!")
        quit()
    elif var[1] == ">=":
      try:
        return float(st.getData(var[0])) >= float(st.getData(var[2]))
      except:
        print("ERROR: Cannot compare char to num!")
        quit()
    elif var[1] == "<":
      try:
        return float(st.getData(var[0])) < float(st.getData(var[2]))
      except:
        print("ERROR: Cannot compare char to num!")
        quit()
    elif var[1] == "<=":
      try:
        return float(st.getData(var[0])) <= float(st.getData(var[2]))
      except:
        print("ERROR: Cannot compare char to num!")
        quit()
    else:
      print("ERROR: Invalid comparison operator!")
      quit()
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