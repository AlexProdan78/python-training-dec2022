f = open("functions.py")
for line in f:
    if len(line) > 20:
        print(line)
f.close()


with open("functions.py") as f:
    for line in f:
        if len(line) > 20:
            print(line)


with open("test.txt", "w") as fw:
    fw.write("test\n")
    fw.write(f"file is writable: {fw.writable()}\n")
    fw.write(f"file is closed: {fw.closed}\n")



