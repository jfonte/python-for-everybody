def split(list):
    harry = []
    for i in list:
        harry.append(int(i))
    return harry


def digital_root(n):
    # get number of digits
    digits = len(str(n))
    #print(digits)
    while digits > 1:
        a = split(str(n))
        #print(a)
        b = 0
        for i in a:
            #print(i)
            b+=i
            #print(b)
        digits = len(str(b))
        #print(digits)
        n = b 
    return(n)

print(digital_root(942), digital_root(132189), digital_root(493193))

 


