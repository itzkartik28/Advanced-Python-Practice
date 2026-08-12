with open("log.txt") as f:
    content=f.read()

    if("python" in content):
        print("yes thhe word python is there")

    else:
        print("no the word python is not there")