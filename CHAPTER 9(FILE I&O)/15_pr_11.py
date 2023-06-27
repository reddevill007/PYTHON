import os

oldname="sample2.txt"
newname="renamed_by_python.txt"
with open(oldname) as f:
    content = f.read()

with open(newname,"w") as f:
    content = f.write(content)

os.remove(oldname)