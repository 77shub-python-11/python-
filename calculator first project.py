class calculator:
    def __init__(self):
        memo = 0
        while True:

            print("do u want to use calc y / n ")
            i = input("enter y/n")
            if i == "y":
                a = int(input("enter first no."))
                b = int(input("enter second no."))

                print("c is add ")
                print("d is sub ")
                print("f is mul ")
                print("e is div ")
                opr = input("enter opr ")
                c = lambda a, b: a + b
                d = lambda a, b: a - b
                f = lambda a, b: a * b
                e = lambda a, b: a / b
                if opr == "c":
                    print("result is", c(a, b))
                    memo = c(a, b)
                    print("if u want to continue with same result value than press in n and if u want to continue using cal with new value press y")

                elif opr == "d":
                    print("result is ", d(a, b))
                    memo = d(a, b)
                    print("if u want to continue with same result value than press in n and if u want to continue using cal with new value press y")




                elif opr == "f":
                    print("result is ", f(a, b))
                    memo = f(a, b)
                    print("if u want to continue with same result value than press in n and if u want to continue using cal with new value press y")


                elif opr == "e":
                    print("result is ", e(a, b))
                    memo = e(a, b)
                    print( "if u want to continue with same result value than press in n and if u want to continue using cal with new value press y")







            elif i == "n":

                break
        print("final result is ", memo)

        while True:
            print("do u want use calc with same value  y/n ")
            q = input("enter y/n")
            if q == "y":
                a = memo
                b = int(input("enter second no."))

                print("c is add ")
                print("d is sub ")
                print("f is mul ")
                print("e is div ")
                opr = input("enter opr ")
                c = lambda a, b: a + b
                d = lambda a, b: a - b
                f = lambda a, b: a * b
                e = lambda a, b: a / b
                if opr == "c":
                    print("result is", c(a, b))
                    memo = c(a, b)

                elif opr == "d":
                    print("result is ", d(a, b))
                    memo = d(a, b)


                elif opr == "f":
                    print("result is ", f(a, b))
                    memo = f(a, b)

                elif opr == "e":
                    print("result is ", e(a, b))
                    memo = e(a, b)

            elif q == "n":
                print("thanks for using class calc")
                memo = 0
                break

calculator()