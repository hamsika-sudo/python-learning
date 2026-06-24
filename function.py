#functions
def calc_sum(a,b):
    return a+b
sum=calc_sum(3,9)
print(sum)

#average of 3 numbers
def avg(a,b,c):
    return (a+b+c)/3
avgerage=avg(2,5,6)
print(avgerage)

#print leng of list
fruits=["apple","banana","cherry","dragon fruit"]
def print_len(list):
    return (len(list))
print(print_len(fruits))

#printing the elements of a list in single line
fruits=["apple","banana","cherry","dragon fruit"]
def print_list(list):
    for item in list:
        print(item, end=" ")
        print_list(fruits)      
#find the factorial of n(n is the parameter)

def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
calc_fact(5)    
calc_fact(6)

#print even or odd
def even_odd(n):
    if (n % 2==0):
        print("Even")
    else:
        print("odd")    
even_odd(7)        