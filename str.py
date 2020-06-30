print("hii {}".format("how are u "))
print("hiii {1},im ur friend {0} ".format("shubham","i can help"))




a="abc"
print(a,"hii",a,"hello")
num=[1,2,3,4,5,6,7,8]
sum=0
for val in num:
    sum=sum+val
    print("printingg")
    print(sum)
    print("the sum is ",sum)




sun=0
i=1
while i<=10:
    sun=sun +i
    i+=1
    print(sun)


print(range(10))

ad=[1,2,3]
for i in range(len(ad)):
    print("i like to add",ad[i])



l=[1,2,3,4,5]
for index,l in enumerate(l):
    print("room"+str(l)+":"+str(l))



s=set()
s.add(1)
s.add(2)
print(s)