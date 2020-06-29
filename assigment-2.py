

'''
 Create a list of names dynamically as per user choice and let the user decide when he wants  to quit?
hint:while if break,ask user wants to continue take input as yes or no -- y,n.
'''


b=[]
while True:
    print("do u want make list y / n")
    i = input("only y/n: ")
    if i == "y":
         a = input()

         b.append(a)
         print(a)

    elif i == "n":
        print("ok fine")
        break



l=[]
a=0
while True:
    b=input()
    l.append(b)
    print(l)
    var=input("u want enter more y/n : ")




