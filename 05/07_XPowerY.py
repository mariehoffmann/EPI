__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

# float x, int y, O(y)
def myPower(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return myPower(x, y//2)*myPower(x, y//2)*myPower(x,y%2)

# multiply intermediate result with itself
def myPower2(x, y):
    tmp = [1, x] # powers of x
    if y < 2:
        return tmp[y]
    else:
        pw = 1
        res = x
        while (pw << 1) < y:
            res *= res
            pw <<= 1
            tmp.append(res)
        return res*tmp[y-pw]

if __name__ == "__main__":
    print(myPower(2,5))
    print(myPower2(2,5))

    print(myPower(2,0))
    print(myPower2(2,0))

    print(myPower(2,1))
    print(myPower2(2,1))

    print(myPower(3,5))
    print(myPower2(3,5))



