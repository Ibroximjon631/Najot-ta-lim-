def abcdef(abc:str):
    lst=""
    if not abc:
        return "Nmadr yozng"
    else:
        for i in range(0,len(abc),2):
            iii=abc[i+1]
            lst+=str(int(abc[i])*iii)
        return lst
