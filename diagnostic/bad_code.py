"""WARNING: This code is horrible. Never write code like this."""

def b(n):
    import random
    zero = 0
    return random.randint(zero,5)*n


def find_five(my_list):
    flag = False
    for i in range(len(my_list)):
        if my_list[i] == 5:
            flag = True
    return flag


l = [] # make a list l
while True:
    a = int(b(5))
    l = l + [a]
    five = find_five(l)
    if five == True:
        break
print l
