#-----------------Problem-------------
#Given an array of strings, group anagrams together

#-------------My Solution--------------
#Sort each string, store each sorted string in a dic along with the index in the output array
#If it does exist grab the index from the dic and store it in output array
#If it does not exist add it to the dic along with the index which is just len(ouput)-1
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    letters = {}
    anagrams = {}
    
    def helper(string):
        curr_letters = sorted(string)
        curr_letters = "".join(curr_letters)
        
        if curr_letters in letters:
            index = letters[curr_letters]
            anagrams[index].append(string)
        else:
            anagrams.append([string])
            letters[curr_letters] = len(anagrams)-1
    for x in strs:
        helper(x)
#Python way of solving using a default dic, which just intializes an unassigned key to a default value
    for x in strs:
        anagrams[tuple(sorted(x))].append(x)
    print(anagrams)
    return anagrams.values()