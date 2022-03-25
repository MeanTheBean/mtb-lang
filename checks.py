import tokenList
import funcs

def compCode(code):
    global out
    global errors
    tokenList.setup()
    out = ""
    failed = 0
    errors = False
    line = 0
    fails = 0
    for i in code:
        token = -1
        currentLine = code[line]
        for i in tokenList.tokens:
            if currentLine.split(" ",1)[0] == tokenList.tokens[token+1]:
                if currentLine.split(" ",1)[0] == "_endif":
                    temp = out + str(tokenList.tokens[token+2](currentLine.split(" ",1)[1]))
                    out = temp.replace("None", "", 50)
                    succses = True
                elif funcs.runcode == True:
                 temp = out + str(tokenList.tokens[token+2](currentLine.split(" ",1)[1]))
                 out = temp.replace("None", "", 50)
                 succses = True
                else:
                    succses = True
                    out = out
            elif currentLine.split(" ",1)[0] == "//":
                succses = True
            else:
                token += 1
                succses = False
                fails += 1
                if fails == tokenList.getTokenCount():
                    errors = True
            if succses == True:
                break
        line += 1
        

def getErrors():
#    if errors:
#        return True
#    else:
#        return False
    return False

def getOutput():
    return out
