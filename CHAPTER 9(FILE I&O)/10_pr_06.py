with open("log.txt") as f:
    content = f.read()

if 'python' in content.lower():
    print("yes")
else:
    print("no")
