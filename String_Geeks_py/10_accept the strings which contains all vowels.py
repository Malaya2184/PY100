def checkVowel(str):
    subset = set('aeiou')
    superset = set(str)
    
    if  superset.intersection(subset) == subset:
        return 'accepted'
    else:
        return 'not accepted'
    
print(checkVowel('aaiouaaxeaugduhbhbsa'))