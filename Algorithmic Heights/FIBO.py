with open('rosalind_fibo.txt','r') as file:
    num = int(file.readline().strip())
    def fibo(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibo(n-1) + fibo(n-2)

    print(fibo(num))
