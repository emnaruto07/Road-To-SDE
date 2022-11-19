# DSA reverse string

# def reverse(string):
#     string = string[::-1]
#     return string

# print(reverse("shazeb"))

def reverseTwo(string):
    strr = ""
    for i in string:
        strr = i + strr
    return strr

print(reverseTwo("shazeb"))