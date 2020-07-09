print("hii {}".format("how are u "))#we use format function to put sentence in main sentence it gives freedom to interchange like shown in next line
print("hiii {1},im ur friend {0} ".format("shubham","i can help")) #we here inter change the words by changing index




a="abc"
print(a,"hii",a,"hello")#here we used variable to print in sentecne in this way variable can be changed


num=[1,2,3,4,5,6,7,8]
sum=0
for val in num:#here we are using for loop to iterate value from list one by one and we can make operation on it
    sum=sum+val
    print("printingg")
    print(sum)
    print("the sum is ",sum)




sun=0
i=1#value of i is 1
while i<=10:#here we used while loop ,while loop is a loop which runs until condition are meet to true
    sun=sun +i
    i+=1#it gets increment by one
    print(sun)


print(range(10))#here we used range function

ad=[1,2,3]
for i in range(len(ad)):#here we range is but also length function also used in that ,in this range goes till length of the variable
    print("i like to add",ad[i])



l=[1,2,3,4,5]
for index,l in enumerate(l):#here we used function enumerate which is iterable start with 0
    print("room"+str(l)+":"+str(l))



s=set()#created empty set
s.add(1)#add value to empty set
s.add(2)
print(s)



a={"key":"shubham"}
print(a["key"])
b={"k":0,"k1":2,"k2":3}
print(b["k1"])