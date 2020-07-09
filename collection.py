class calc:
    def __init__(self):
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
                    print("result is", c(a,b))

                elif opr == "d":
                    print("result is ", d(a,b))

                elif opr == "f":
                    print("result is ", f(a,b))


                elif opr == "e":
                    print("result is ", e(a,b))



            elif i == "n":
                print("thanks for using class calc")
                break

calc()