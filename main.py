import argparse
import checks
import funcs
import os
import requests
from pathlib import Path

parser = argparse.ArgumentParser(description='A program interpreter for mtb-lang')
parser.add_argument("code_file", help="The file to run")

args = parser.parse_args()

try:
  f = open(args.code_file, "r")
  file_dir = Path(args.code_file).parent.absolute()
  funcs.get_dir(str(file_dir))
except:
  if args.code_file == "version":
    print(f"mtb-lang version {funcs.VERSION}; created by Mean The Bean 2024")
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

try:
  checks.compCode(prog_text)
except:
  print("ERROR: Program stopped by user!")
