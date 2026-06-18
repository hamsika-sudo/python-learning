#odd or even
num=int(input("Enter a num"))
rem=num%2
if(rem==0):    
    print("The number is even")
else :
    print("The number is odd")

#finding the greatest number
a=11
b=4
c=7
if(a>b and a>c):
    print("a is the greatest")
elif(b>a and b>c):
    print("b is the greatest number")
else:
    print("c is the greatest number")

#checking if it is multiple of 7 or not
num=int(input("Enter a number"))
if(num%7==0):
    print("The number is a multiple of 7")
else:
    print("It is not the multiple of 7")    

#grades 
marks=int(input("Enter the marks"))
if(marks>=90):
    print("A")
elif(marks>=70 and marks<90):
    print("B") 
elif(marks>=50 and marks<70):
     print("PASS")
else:
    print("FAIL")       

#leap year
year=int(input("Enter a year:"))
if(year%4==0):
    print("It is a leap year")
else:
    print("Not a leap year")        
