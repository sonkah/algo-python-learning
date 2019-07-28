
def insertion(table):
    for j in range(1, len(table)):              # marker after the first element
        key = table[j]                          # take the second element
        i = j - 1
        while i >= 0 and table[i] > key:
            table[i+1] = table[i]
            i = i - 1
        table[i+1] = key
    return table


def selection(table):
    for index in range(0, len(table)):
        i_min = index
        v_min = table[index]
        for j in range(index+1, len(table)):
            if v_min > table[j]:
                v_min = table[j]
                i_min = j
        table[i_min] = table[index]
        table[index] = v_min
    return table


def bubble(table):
    for i in range(0, len(table)-1):
        for j in range(0, len(table)-i-1):
            if table[j] > table[j+1]:
                tmp = table[j]
                table[j] = table[j+1]
                table[j + 1] = tmp
    return table


def mergesort(table,  p, q, r):
    pass






