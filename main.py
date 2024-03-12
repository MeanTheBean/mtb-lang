import argparse
import checks
import funcs

parser = argparse.ArgumentParser(description='A program compiler')
parser.add_argument("code_file", help="Prints the supplied argument.")

args = parser.parse_args()

try:
  f = open(args.code_file, "r")
except:
  if args.code_file == "--version":
    print(f"mtb-lang version {funcs.VERSION}; created by Mean The Bean 2024")
  else:  
    print(f"ERROR: No such file: {args.code_file}")
  quit()
prog_text = f.readlines()
f.close()

try:
  checks.compCode(prog_text)
except:
  print("ERROR: Program stopped by user!")
