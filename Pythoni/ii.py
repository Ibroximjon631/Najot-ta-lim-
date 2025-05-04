def duplicate_zeros(numbers:list):
    rst=[]
    for number in numbers:
        if int(number) == 0:
            rst.extend([0,0])
        else:
            rst.append(number)
    return rst

