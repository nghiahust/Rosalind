with open('rosalind_bins.txt','r') as file:
    lines = file.readlines()
    n, m = lines[0], lines[1]
    sorted_arr = [int(x) for x in lines[2].strip().split()]
    my_list = [int(x) for x in lines[3].strip().split()]

    def BINS(a, array):
        low = 0
        mid = 0
        high = len(array) - 1
        while low <= high:
            mid = (low + high) // 2
            if array[mid] < a:
                low = mid + 1
            elif array[mid] > a:
                high = mid - 1
            else:
                return mid + 1
        return -1

    result = open('result_bins.txt','w')
    for i in my_list:
        result.write(str(BINS(i, sorted_arr)))
        result.write(' ')
