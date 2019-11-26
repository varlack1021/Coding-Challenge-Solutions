def isValidWalk(walk):
    #determine if walk is valid
    if len(walk) % 2 == 0:
        countPaths = Counter(walk)

        if (countPaths['e'] == countPaths['w'] and countPaths['n'] == countPaths['s'] 
                                       and sum (value for key, value in x.items()) <= 10):
            return True
    return False