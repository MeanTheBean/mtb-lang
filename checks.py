import tokenList

def compCode(code):
    global out
    global errors
    out = ""
    failed = 0
    errors = False
    line = 0
    fails = 0
    for i in code:
        token = 0
        currentLine = code[line]
        for i in tokenList.tokens:
            if currentLine.split(" ",1)[0] == tokenList.tokens[token]:
                out = out + "\n" + currentLine.split(" ",1)[1]
                succses = True
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
    if errors:
        return True
    else:
        return False

def getOutput():
    return out
