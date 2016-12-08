"""  itertools.permutations generate a list of tuple, need to be chained to int list
"""
def tuple_list_to_int_list(tl):
    s=[]  #list,  how to declear an empty set?
    for j in tl: 
        # permutations : NO repeated
        number=''
        for c in j :
            number=number+c
        s.append(int(number))
    return s

digits="123456789"