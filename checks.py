import tokens

def compCode(code):
    global out
    global errors
    out = ""
    failed = 0
    errors = False
    line = 0
    for i in code:
        token = 0
        currentLine = code[line]
        for i in tokens.tokens:
            if currentLine.split(" ",1)[0] == tokens.tokens[token]:
                out = out + "\n" + currentLine.split(" ",1)[1]
            elif currentLine.split(" ",1)[0] == "//":
                pass
            else:
                pass
        line += 1
        token += 1

#def getErrors():
#    if errors:
#        return True
#    else:
#        return False

def getOutput():
    return out
