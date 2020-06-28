while True:
    print("do u want make list y / n")
    i = input("only y/n: ")
    if i == "y":
        a = input()
        b = []
        b.append(a)
        print(a)

    elif i == "n":
        print("ok fine")
        break
