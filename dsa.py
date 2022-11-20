# DSA reverse string

# def reverse(string):
#     string = string[::-1]
#     return string

# print(reverse("shazeb"))

# def reverseTwo(string):
#     strr = ""
#     for i in string:
#         strr = i + strr
#     return strr

# print(reverseTwo("shazeb"))

# def rec(n):
#     if n > 0:
#         print("Recursive on with", n)
#         rec(n-1)
#         rec(n-1)


# n=3
# rec(n)
# applying rec on factorial
def rec(n):
    if n == 1:
        return n
    else:
        return n * rec(n-1)
n=5
# print(rec(n))

# applying rec on fibonacci

def fib(n):
    #making default case
    if n <= 1:
        return n
    else:
        #adding last two values
        return (fib(n-1) + fib(n-2))

count = 12

if n <=0:
    print("xyz")
else:
    sum = 0
    for i in range(count):
        sum = sum + fib(i)
    print(sum)