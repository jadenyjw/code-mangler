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

in_comment = False
mangled = open("mangled.py", "w")
for item in lines:
    item = item.strip()

    if (item.startswith("\"\"\"")):
        in_comment = not in_comment

    if (not item.startswith('#') and not item.startswith("'''")
            and not item.startswith("\"") and not in_comment and len(item.strip()) > 0):
        mangled.write(item.strip() + "\n")

mangled.close()
