import argparse
import checks
import funcs
import os
from pathlib import Path

allowError = False

parser = argparse.ArgumentParser(description='A program interpreter for mtb-lang')
parser.add_argument("code_file", help="The file to run")

args = parser.parse_args()

try:
  if os.name == "nt":
    check_setup = Path("%localappdata%/.mtb/").exists()
  elif os.name == "posix":
    check_setup = os.path.exists("~/.mtb/")
  #print(check_setup)
  if not check_setup:
    if os.name == "nt":
      os.system("mkdir %localappdata%/.mtb/")
      os.system("mkdir %localappdata%/.mtb/libs/")
    elif os.name == "posix":
      os.system("mkdir ~/.mtb/ > /dev/null 2>&1")
      os.system("mkdir ~/.mtb/libs/ > /dev/null 2>&1")
except:
  print("WARNING: Could not create .mtb directory!")

try:
  f = open(args.code_file, "r")
  file_dir = Path(args.code_file).parent.absolute()
  funcs.get_dir(str(file_dir))
except:
  if args.code_file == "version":
    print(f"mtb-lang version {funcs.VERSION}; created by Mean The Bean 2025")
    os._exit(0)
  elif args.code_file == "update":
    #TODO: Update Packages
    print("ERROR: Packages not yet implemented!")
    os._exit(0)
  else:  
    print(f"ERROR: No such file: {args.code_file}")
  quit()
prog_text = f.readlines()
f.close()

if allowError:
  try:
    checks.compCode(prog_text)
  except:
    print("ERROR: Program stopped by user!")
else:
  checks.compCode(prog_text)
