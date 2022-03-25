import stack as st

def CodeSetup():
    global runcode
    runcode = True

def sysput(args):
    return args

def mkvar(num):
    global currentVar
    st.newLayer(num)
    currentVar = num

def setvar(num):
    global currentVar
    currentVar = num

def vardata(data):
    st.setData(currentVar, data)

def varout(num):
    return st.getData(num)

def addvar(othervar):
    data = int(st.getData(currentVar)) + int(st.getData(othervar))
    st.setData(currentVar, data)
    
def subvar(othervar):
    data = int(st.getData(currentVar)) - int(st.getData(othervar))
    st.setData(currentVar, data)

def mulvar(othervar):
    data = int(st.getData(currentVar)) * int(st.getData(othervar))
    st.setData(currentVar, data)

def divvar(othervar):
    data = int(st.getData(currentVar)) / int(st.getData(othervar))
    st.setData(currentVar, data)

def startif(othervar):
    global runcode
    if st.getData(currentVar) == st.getData(othervar):
        runcode = True
    else:
        runcode = False

def endif(e):
    global runcode
    runcode = True
    
def startnif(othervar):
    global runcode
    if st.getData(currentVar) != st.getData(othervar):
        runcode = True
    else:
        runcode = False
