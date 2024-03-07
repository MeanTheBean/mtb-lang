import argparse
import checks

parser = argparse.ArgumentParser(description='A program compiler')
parser.add_argument("code_file", help="Prints the supplied argument.")

args = parser.parse_args()

try:
  f = open(args.code_file, "r")
except:
  print(f"ERROR: No such file: {args.code_file}")
  quit()
prog_text = f.readlines()
f.close()

try:
  checks.compCode(prog_text)
except:
  print("ERROR: Program stopped by user!")

error = checks.getErrors()

#if not error:
#    print(checks.getOutput())
#else:
#    print("ERROR: Unkown")
#    quit()
