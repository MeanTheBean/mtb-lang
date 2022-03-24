import stack as st

def sysput(args):
    return args

def mkvar(num):
    global currentVar
    st.newLayer(num)
    currentVar = num

def setvar(num):
    currentVar = num

def vardata(data):
    st.setData(currentVar, data)

def varout(num):
    return st.getData(num)
