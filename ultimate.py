a = 0
b = 1
c = 1
d = 1

def an(a, b):
    if (a == 0 and b == 0):
        return 0
    elif (a == 0 and b == 1):
        return 0
    elif (a == 1 and b == 0):
        return 0
    elif (a == a and b == 1):
        return 1
    else:
        return ValueError

def orr(a, b):
    if (a == 0 and b == 0):
        return 0
    elif (a == 0 and b == 1):
        return 1
    elif (a == 1 and b == 0):
        return 1
    elif (a == a and b == 1):
        return 1
    else:
        return ValueError

def no(a):
    if (a == 1):
        return 0
    elif (a == 0):
        return 1
    else:
        return ValueError

def nand(a, b):
    if (a == 0 and b == 0):
        return 1
    elif (a == 0 and b == 1):
        return 1
    elif (a == 1 and b == 0):
        return 1
    elif (a == a and b == 1):
        return 0
    else:
        return ValueError

def nor(a, b):
    if (a == 0 and b == 0):
        return 1
    elif (a == 0 and b == 1):
        return 0
    elif (a == 1 and b == 0):
        return 0
    elif (a == a and b == 1):
        return 0
    else:
        return ValueError


print(an(a, b))
print(an(b, c))
print(an(c, d))

# (a & b)
