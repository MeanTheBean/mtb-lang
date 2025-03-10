import funcs

def math_func(e):
  ops = ["+","-","*","/","^","%"]
  e = e.replace(" ", "")

  hasOp = False
  op = -1
  for i in ops:
    if i in e:
      hasOp= True
      op = i
      break
  if not hasOp:
    funcs.call_error("Invalid equation!")
  e = e.split(op)

  if op == "+":
    e = float(e[0]) + float(e[1])
  elif op == "-":
    e = float(e[0]) + float(e[1])
  elif op == "*":
    e = float(e[0]) * float(e[1])
  elif op == "/":
    e = float(e[0]) / float(e[1])

  return e