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

# def fib(n):
#     #making default case
#     if n <= 1:
#         return n
#     else:
#         #adding last two values
#         return (fib(n-1) + fib(n-2))

# count = 12

# if count <=0:
#     print("xyz")
# else:
#     sum = 0
#     for i in range(count):
#         sum = sum + fib(i)
#     print(sum)


#tower of Hanoi

def toh(n, from_bar, to_bar, aux_bar):
    if n == 1:
        print("Move disk 1 from bar ", from_bar, " to bar ", to_bar)
        return
    toh(n-1, from_bar, aux_bar, to_bar)
    print("Move disk", n, "from bar ", from_bar, "to bar", to_bar)
    toh(n-1,aux_bar, to_bar, from_bar)

n = 3
toh(n, 'A', 'C', 'B')