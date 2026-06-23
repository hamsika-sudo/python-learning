#while loop
i=1
while i<=10:
    print("hello")
    i+=1
 #printing numbers from 1 to 5(while loop)
i=1
while i<=5:
    print(i)
    i+=1   
#printing numbers from 5 to 1(while loop)
i=5
while i>=1:
    print(i)
    i-=1
#multipication table(while loop)
n=5
i=1
while i<=10:
    print(n*i)
    i+=1
# break statement 
i=2
while i<=10:
    if(i==6):
        break
    i+=1
#continues statement
i=1
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1
#for loop:
num =1,2,4,5,7
for n in num:
    print(n)
#range function
for i in range(10):
    print(i)
#print numbers from 20 to 1
for i in range(20,0,-1):
    print(i)  
#multiplication table
n= 7
for i in range(11):
    print(n*i)

#pass statement
for i in range(5):
    pass

    print("some useful information")

#sum of first n numbers
n=5
sum=0
for i in range(1,n+1):
    sum+=i
print("total sum",sum)
#find the factorial of n numbers
n=5
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("factorail is",fact)