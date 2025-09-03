import stack as st
import checks as ch
import os
import time
from pathlib import Path
import mathfuncs as mf
#import main

VERSION = "0.2.1"
DEBUGMODE = True

#print(st.getData("os.name"))
pyvar_list = {
    "os.name": os.name,
    "os.path": os.path,
}

if os.name == "nt":
  lib_path = "%localappdata%/.mtb/libs/"
elif os.name == "posix":
  home = str(Path.home())
  if DEBUGMODE:
    lib_path = "./libs/"
  else:
    lib_path = home+"/.mtb/libs/"

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


def get_dir(file_path):
  global file_dir
  file_dir = file_path


def set_file_name(name_file):
  global file_name
  file_name = name_file


def clearcon(e=None):
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')


def proghalt(halttime):
  time.sleep(parse_var_old(halttime, True))


def make_local_var(name):
  localvars[name] = None


def set_local_var(name, value):
  localvars[name] = value


def sysput(args):
  #print("hi")
  return parse_var(args)

# internal function, use std.in
def sysgrab(var):
  st.setData(var, input())

def var_set(statement):
  global returnVar
  returnVar=None
  if statement == "" or statement == "\n":
    return
  statement = statement.split(" ", 2)
  #print(statement)
  try:
    st.getData(statement[0]+"\n", no_error=True)
  except:
    st.newLayer(statement[0]+"\n")
  if statement[1] == "<":
    if statement[2][0] == "$":
      run_func(statement[2][1:].split(" ", 1))
      st.setData(statement[0]+"\n", returnVar)
    else:
      st.setData(statement[0]+"\n", parse_var(statement[2]))

def return_var(name):
  global returnVar
  var_data = parse_var(name)
  returnVar = var_data

# internal function, use < instead
def mkvar(num):
  var_prefix = ""

  if file_name == None:
    var_prefix = ""
  else:
    var_prefix = file_name + "_"
  num = var_prefix+num
  st.newLayer(num)
  #print(num)

# internal function, use < instead
def vardata(data):
  data = data.split(" ", 1)
  data[0] = data[0].strip(" ")
  data[0] += "\n"
  
  if file_name == None:
    var_prefix = ""
  else:
    var_prefix = file_name + "_"
  data[0] = var_prefix+data[0]
  
  #print(data)
  st.setData(data[0].strip(" "), parse_var(data[1]))


def math_func(input):
  input = input.strip(" ")
  input = input.replace(" ", "")

  data = 0
  
  if "+" in input:
    input = input.split("+")
    #print(parse_var(input[0]+'\n'.strip("")))
    data = parse_var(input[0] + '\n'.strip(""), True) + parse_var(
        input[1], True)
  elif "-" in input:
    input = input.split("-")
    data = parse_var_old(input[0] + '\n'.strip(""), True) - parse_var(
        input[1], True)
  elif "*" in input:
    input = input.split("*")
    data = parse_var_old(input[0] + '\n'.strip(""), True) * parse_var(
        input[1], True)
  elif "/" in input:
    input = input.split("/")
    data = parse_var_old(input[0] + '\n'.strip(""), True) / parse_var(
        input[1], True)
  elif "^" in input:
    input = input.split("^")
    data = parse_var_old(input[0] + '\n'.strip(""),
                     True)**parse_var(input[1], True)
  else:
    call_error("Invalid operator!")

  if int(data) == data:
    data = int(data)
  return str(data) + " "

def startif(data):
  global runcode
  #print(parse_var(data))
  if parse_var(data) == (True or 1):
    #print("hey")
    runcode = True
  else:
    runcode = False


def endif(e=None):
  global runcode
  if currentfunc == None:
    runcode = True

def mklist(num):
  st.newLayer(num)
  st.setData(num, "[l]")
  #print(st.getData(num))


def appendvar(data):
  data = data.split(" ", 1)
  data[0] += "\n"
  st.setData(data[0], st.getData(data[0]) + "|" + parse_var(data[1]))


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

  func_prefix = ""

  if file_name == None:
    func_prefix = ""
  else:
    func_prefix = file_name + "_"

  runcode = False
  data = func_prefix+data
  data = data.split(" ")
  recordfunc = data[0]
  currentfunc = {"name": data[0], "args": data[1], "code": []}
  #currentfunc = "hi"
  st.newLayer(data[0])
  #print(currentfunc)


def endfunc(e=None):
  global recordfunc
  global runcode
  global currentfunc

  if currentfunc == None:
    call_error("Cannot end a non-existant function!")
    return
  
  tempfunc = {"args": currentfunc["args"], "code": currentfunc["code"]}

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

def pyvar(data):
  data = data.split(" ", 1)
  data[0] += "\n"
  data[1] = data[1][:-1]
  if data[1] in pyvar_list:
    st.setData(data[0],pyvar_list[data[1]]+"\n")

def reqver(ver):
  ver_split = ver.split(".")
  progver = VERSION.split(".")
  if int(ver_split[0]) > int(progver[0]):
    print(
        f"ERROR: Program requires version {ver[:-1]} or higher! (Current: {VERSION})"
    )
    os._exit(1)
  elif int(ver_split[1]) > int(progver[1]):
    print(
        f"ERROR: Program requires version {ver[:-1]} or higher! (Current: {VERSION})"
    )
    os._exit(1)
  elif int(ver_split[2]) > int(progver[2]):
    print(
        f"ERROR: Program requires version {ver[:-1]} or higher! (Current: {VERSION})"
    )
    os._exit(1)


def putver(e=None):
  print(f"Version: {VERSION}")


def run_func(data, is_loop=False):
  global localvars
  global activefunc
  activefunc = True
  data[0] = data[0].replace(".", "_")
  #print(data[0])
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

def importfile(file):
  import_path = file_dir + "/" + file[:-1] + ".mtb"
  #print(import_path)
  f = open(import_path, "r")
  import_text = f.readlines()
  f.close()

  ch.compCode(import_text, False, file[:-1])

def importlib(name):
  import_path = lib_path+name[:-1]+".mtb"

  f = open(import_path, "r")
  import_text = f.readlines()
  f.close()

  ch.compCode(import_text, False, name[:-1])
  

def parse_list(listName, indexNum):
  wholeVar = st.getData(listName)
  if True: #wholeVar[0:4] == "[l]":
    split_list = wholeVar[2:]
    split_list = split_list[:-3]
    split_list = split_list.split("\", \"")
    try:
      return split_list[int(indexNum)] + " "
    except:
      print("ERROR: Index out of range!")
      quit()
  else:
    print("ERROR: Variable is not a valid list!")
    quit()


def parse_var(var, convert_to_num=False):
  numbers = ["1","2","3","4","5","6","7","8","9","0","."]
  ops = ["+", "-", "*", "/", "^", "%"]
  
  var = var[:-1]
  var = var.split(" ")

  for i in var:
    isNum = True
    for k in i:
      if k not in numbers or k == "":
        isNum = False
    if isNum:
      i = float(i)
  
  loopString = False
  if "\"" in " ".join(var):
    loopString = True
  while loopString:
    combineRange = [0,0]
    foundStart = False
    foundEnd = False
    
    for i,_ in enumerate(var):
      
      if var[i][0] == "\"":
        if foundStart == False:
          foundStart = True
          combineRange[0] = i
          var[i] = "[f]"+var[i][1:]
      if var[i][-1] == "\"" or (var[i] == "\"" and foundStart):
        combineRange[1] = i+1
        foundEnd = True
        #if not var[i] == "\"":
        var[i] = var[i][:-1]
        break
        #else:
        #  var[i] = "\""
        #  break
    if foundStart and not foundEnd:
      loopString = False
      call_error("String is never termintated!")
    else:
      subvar = var[combineRange[0]:combineRange[1]]
      rangeLen = combineRange[1] - combineRange[0]
      if rangeLen < 0:
        call_error("Invalid string!")
      for k in reversed(range(combineRange[0]+1,combineRange[1])):
        var.pop(k)
      subvar = " ".join(subvar)
      var[combineRange[0]] = subvar

    if "\"" not in " ".join(var):
      loopString = False

  runOps = True
  while runOps:
    opIndex = -1
    for i,v in enumerate(var):
      if len(v) > 0:  
        if not v[0:3] == "[f]":
          if v[0] in ops:
            opIndex = i
            break
    if opIndex >= 0:
      i = opIndex
      v = var[i]
      if len(v) > 0:
        if v[0] in ops:
          if i == 0:
            call_error("Cannot use operator before first number!")
          elif i == len(var)-1:
            call_error("Cannot use operator after last number!")
          elif var[i-1].replace("[f]", "")[0] in numbers and var[i+1].replace("[f]", "")[0] in numbers:
            var[i-1] = var[i-1].replace("[f]", "")
            var[i+1] = var[i+1].replace("[f]", "")
            temp = "".join(var[i-1:i+2])
            
            temp = float(mf.math_func(temp))
            
            if int(temp) == temp:
              temp = int(temp)
            var[i] = f"[f]{temp}"
            var.pop(i+1)
            var.pop(i-1)
          elif (var[i-1][-1] not in numbers or var[i+1][-1] not in numbers) and v[0] == "+":
            if "[f]" not in var[i-1] or "[f]" not in var[i+1]:
              if var[i-1][-1] not in numbers and "[f]" not in var[i-1]:
                var[i-1] = st.getData(var[i-1]+"\n")
              if var[i+1][-1] not in numbers:
                var[i+1] = st.getData(var[i+1]+"\n")
            
            var[i-1] = var[i-1].replace("[f]", "")
            var[i+1] = var[i+1].replace("[f]", "")
            temp = "[f]" + str(var[i-1]) + (var[i+1])
            var[i] = temp
            var.pop(i+1)
            var.pop(i-1)
          #else:
            #call_error("Invalid equation!")
    
    runOps = False
    for i in var:
      if i[0] in ops:
        runOps =True

  for i,_ in enumerate(var):
    var[i] = var[i].replace("[f]", "")
  
  var = " ".join(var)
  return var+'\n'

def parse_simple(var):
  return st.getData(var)

def parse_var_old(var, convert_to_num=False):
  #print(var)
  #var = var.replace(" ", "")
  

  if file_name == None:
    var_prefix = ""
  else:
    var_prefix = file_name + "_"
  
  
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
    dot_index = var[2:].find(".") + 2
    num_index = int(var[2:dot_index])
    return parse_list(var[dot_index + 1:], num_index)
  elif var[0:2] == "f.":
    try:
      #print(localvars[var[2:]])
      return localvars[var[2:]]
    except:
      print("ERROR: Local variable not found!")
      quit()
  elif var[0:2] == "c.":
    var = var[2:].split(" ", -1)
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
  elif var[0:6] == "(split":
    close_mark = var.find(")")
    split_mark = var[7:close_mark]
    var_data = parse_var(var[close_mark+1:])
    var_data = var_data.split(split_mark, 1)
    var_data = f"[\"{var_data[0]}\", \"{var_data[1]}\"]"
    return var_data
  elif var == "true\n":
    return 1
  elif var == "false\n":
    return 0
  else:
    #print(var + "\n")
    if convert_to_num:
      try:
        #print(var)
        return float(st.getData(var.replace(" ", "")))
      except:
        print("ERROR: Cannot convert char to num!")
        quit()
    else:
      var = var_prefix+var
      var = var.replace(".","_")
      varContent = st.getData(var)
      if varContent[0:3] == "[l]":
        varContent = convert_to_list(varContent)
      
      return varContent


def convert_to_list(content):
  content = content.replace("\n","")
  content = content[4:].split("|")

  final_string = "[\""
  
  for i in content:
    final_string += i + "\", \""

  final_string = final_string[:-3] + "] "
  return final_string


def call_error(e):
  currentLine = ch.getLineNum()
  print(f"ERROR on Line {currentLine}: {e}")
  os._exit(1)