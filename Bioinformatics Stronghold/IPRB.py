with open('rosalind_iprb.txt','r') as file:
    numbers = file.readline().split()
    k = int(numbers[0]) # homo dominant
    m = int(numbers[1]) # hetero
    n = int(numbers[2]) # homo recessive
    pop = k + m + n
    m_m = (m/pop) * ((m-1)/(pop-1)) * 1/4
    m_n = (m/pop) * (n/(pop-1)) * 1/2
    n_m = (n/pop) * (m/(pop-1)) * 1/2
    n_n = (n/pop) * ((n-1)/(pop-1)) * 1
    result = 1 - m_m - m_n - n_m - n_n
    print(result)
