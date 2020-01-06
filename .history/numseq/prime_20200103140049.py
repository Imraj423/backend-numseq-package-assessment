def is_prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2, n):
            if(n % x == 0):
                return False
        return True


def prime(num):
    plist = []
    if num > 1:
        for i in range(1, num+1):
            if is_prime:
                plist.append(i)
