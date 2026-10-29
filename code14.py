n=int(input("enter the number of values:"))
sum=0
for i in range(1,n+1):
     num=float(input("enter number"+str(i)+":"))
     sum=sum+sum
average=sum/n
print("sum=",sum)
print("average=",average)
