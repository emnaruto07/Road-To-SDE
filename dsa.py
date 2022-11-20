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

def rec(n):
    if n == 1:
        return n
    else:
        return n * rec(n-1)
n=5
print(rec(n))