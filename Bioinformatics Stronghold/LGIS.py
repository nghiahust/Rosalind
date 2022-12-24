with open('rosalind_lgis.txt','r') as file:
    lines = file.readlines()
    n = int(lines[0])
    num = [int(x) for x in lines[1].split()]

    def findLIS(array):
        if not array:
            return []
        LIS = [[] for _ in range(len(array))]
        LIS[0].append(array[0])
        for i in range(1, len(array)):
            for j in range(0, i):
                if array[i] > array[j] and len(LIS[j]) > len(LIS[i]):
                    LIS[i] = LIS[j].copy()
            LIS[i].append(array[i])
        j = 0
        for i in range(len(array)):
            if len(LIS[j]) < len(LIS[i]):
                j = i
        return LIS[j]

    def findDIS(array):
        if not array:
            return []
        DIS = [[] for _ in range(len(array))]
        DIS[0].append(array[0])
        for i in range(1, len(array)):
            for j in range(0, i):
                if array[i] < array[j] and len(DIS[j]) > len(DIS[i]):
                    DIS[i] = DIS[j].copy()
            DIS[i].append(array[i])
        j = 0
        for i in range(len(array)):
            if len(DIS[j]) < len(DIS[i]):
                j = i
        return DIS[j]


    print(*findLIS(num), sep=' ')
    print(*findDIS(num), sep=' ')
