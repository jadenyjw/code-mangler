import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="The file name of code to mangle.")
parser.add_argument("-s", "--stealer", action="store_true",
                    help="Remove duplicate lines.")
args = parser.parse_args()

original_file = open(args.filename, "r")
lines = original_file.readlines()
original_file.close()

if(args.stealer):
    lines = list(set(lines))

lines.sort()

mangled = open("mangled.py", "w")
for item in lines:
    if(not item.startswith('#')):
        mangled.write(item.strip() + "\n")

mangled.close()
