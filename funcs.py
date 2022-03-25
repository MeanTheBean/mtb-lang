import stack as st

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
