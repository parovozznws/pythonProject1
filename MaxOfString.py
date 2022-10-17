string_A = '477803359'
string_B = '596765'
list_A = list(string_A)
list_B = list(string_B)

i = 0
while i<len(list_A):
    if list_A[i] < max(list_B):
        list_A[i] = max(list_B)
        if len(list_B) > 1:
            list_B.remove(max(list_B))
        else:
            break
    i += 1

print(''.join(list_A))
