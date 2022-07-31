file = open('rosalind_inod.txt','r')
n = int(file.readline())

def inod(n):
    if n == 2 or n == 1:
        return 0
    elif n == 3:
        return 1
    elif n % 2 == 1:
        return ((n-1)/2+inod((n-1)/2+1))
    else:
        return (n/2+inod(n/2))

print(int(inod(n)))
