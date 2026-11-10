# f = open("rosan.txt", "r")
# content = f.read()
# print(content)
# f.close()

with open("rosan.txt", "r") as f: # context manager
    content = f.read()
    print(content)
    # No need to write f.close() because file is already closed by default when using with syntax.