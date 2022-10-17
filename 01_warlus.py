def count_vowels(string1):
    ALL_VOWELS = ('a','e','i','o','u','y')
    i = 0
    count1 = 0
    while i<len(string1):
        if string1[i] in ALL_VOWELS:
            count1 +=1
        i += 1
    return count1

print(count_vowels('abcd'))
print(count_vowels('abcdef'))
print(count_vowels('bcd'))

