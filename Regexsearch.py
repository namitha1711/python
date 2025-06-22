import re, glob, os, sys

pattern = re.compile(input("Enter regex: "))
for path in glob.glob(os.path.join(os.getcwd(), "*.txt")):
    with open(path, 'r') as f:
        for num, line in enumerate(f, 1):
            if pattern.search(line):
                print(f"{os.path.basename(path)}:{num}:{line.rstrip()}")
