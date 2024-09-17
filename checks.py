import tokenList
import funcs


def compCode(code, is_func=False, file_name=None):
    global out
    global errors
    if not is_func:
        tokenList.setup()
    funcs.set_file_name(file_name)
    out = ""
    failed = 0
    errors = False
    line = 0
    fails = 0
    prevLine = ""
    for i in code:

        #print("exec")
        token = -1
        currentLine = code[line]
        if "\n" not in currentLine:
            currentLine += "\n"
        #print(currentLine[0])
        if currentLine[0] == "$" and funcs.runcode == True:
            #print(currentLine)
            funcs.run_func(currentLine[1:].split(" ", 1))
        for i in tokenList.tokens:
            if currentLine.split(" ", 1)[0] == tokenList.tokens[token + 1]:
                if currentLine.split(
                        " ", 1)[0] == "_endif" and not funcs.recordfunc:
                    temp = tokenList.tokens[token + 2](currentLine.split(
                        " ", 1)[1])
                    if temp == None:
                        temp = ""
                    out = out + str(temp)
                    succses = True
                elif funcs.runcode == True and not funcs.recordfunc:
                    temp = tokenList.tokens[token + 2](currentLine.split(
                        " ", 1)[1])
                    if temp == None:
                        temp = ""
                    if temp != "":
                        print(str(temp)[:-1])
                    #out = out + str(temp)
                    succses = True
                elif funcs.runcode == False and funcs.recordfunc != None:
                    if currentLine.split(" ", 1)[0] == "_endfunc":
                        temp = tokenList.tokens[token + 2](currentLine.split(
                            " ", 1)[1])
                        if temp == None:
                            temp = ""
                        #out = out + str(temp)
                        succses = True
                    else:
                        if currentLine == (prevLine
                                           or "") or currentLine[:2] == "//":
                            pass
                        else:
                            #print(currentLine)
                            prevLine = currentLine
                            funcs.record_line(currentLine)
                else:
                    succses = True
                    out = out
            elif currentLine.split(" ", 1)[0] == "//":
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
    funcs.set_file_name(None)

def getErrors():
    #    if errors:
    #        return True
    #    else:
    #        return False
    return False
    

def getOutput():
    return out
