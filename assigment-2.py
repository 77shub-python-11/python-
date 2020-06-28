

'''
 Create a list of names dynamically as per user choice and let the user decide when he wants  to quit?
hint:while if break,ask user wants to continue take input as yes or no -- y,n.
'''



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
