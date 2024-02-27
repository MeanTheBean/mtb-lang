import argparse
import checks

parser = argparse.ArgumentParser(description='A program compiler')
parser.add_argument("code_file", help="Prints the supplied argument.")

args = parser.parse_args()

f = open(args.code_file, "r")
prog_text = f.readlines()
f.close()

checks.compCode(prog_text)

error = checks.getErrors()

#if not error:
#    print(checks.getOutput())
#else:
#    print("ERROR: Unkown")
#    quit()
