def longest_consec(strarr, k):
    # your code
    n = len(strarr)
    
    if n == 0 or k > n or k <= 0:
        return ''
    
    longest = ''
    
    for i in range(0, n - k + 1):
        temp = ''.join(strarr[i: i + k])
        if len(temp) > len(longest):
            longest = temp
    return longest


        
            