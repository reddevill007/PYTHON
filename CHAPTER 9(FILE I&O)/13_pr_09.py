file1 = "copy.txt"
file2 = "this.txt"

with open(file1) as f:
    f1=f.read()

with open(file1) as f:
    f2=f.read()

if f1==f2:
    print("Files are identicle")
else:
    print("Files are not identicle")
