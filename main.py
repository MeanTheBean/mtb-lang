import argparse
import checks

parser = argparse.ArgumentParser(description='A program compiler')
parser.add_argument("code_file", help="Prints the supplied argument.")

args = parser.parse_args()

f = open(args.code_file, "r")

prog_text = f.readlines()

checks.compCode(prog_text)

#error = checks.getErrors()

out_text = checks.getOutput()

#if not error:
print(out_text)
#else:
#    print("ERROR: Unkown")
#    quit()
