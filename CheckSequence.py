def check_sequence(list1):
    i = 1
    while i <  len(list1 ):
        if list1[i-1] < list1 [i ]:
            result = True
        else:
            result = False
            break
        i+=1

    if result:
        return 1
    else:
        return 0

print(check_sequence([1, 2,5,6,6 ]))