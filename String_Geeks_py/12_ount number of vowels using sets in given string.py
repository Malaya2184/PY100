

def countVowels(str):
    vowels = set('aeiou')
    str = set(str)
    count = 0
    
    for i in str:
        if i in vowels:
            count +=1
    return count


print(countVowels('malauyiouuua'))