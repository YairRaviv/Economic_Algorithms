import platform
# This is a sample Python script.

def is_leximin_better (x:list , y:list)->bool:
    """
    >>> is_leximin_better([1,2,3],[1,2,3])
    False
    >>> is_leximin_better([1,2,4],[1.000000001,2,3])
    False
    >>> is_leximin_better([],[])
    False
    >>> is_leximin_better([6,7,8,9,1,4],[6,7,8,9,2,1])
    False
    >>> is_leximin_better([4,2,3],[3,4,3])
    True
    >>> is_leximin_better([4.5,4.1,3],[4.5,4,3])
    True
    >>> is_leximin_better([1],[0.9999999999])
    True
    >>> is_leximin_better([10,20,30,70,100],[10,20,30,60,200])
    True
    >>> is_leximin_better([1.00000001,2,3],[1,2,3])
    True
    >>> is_leximin_better([1,3,3],[1,2,3])
    True
    """

    x_len = len(x)
    y_len = len(y)
    i = 0
    equals = True
    while i<x_len and i < y_len:
        if y[i]>x[i]:
            return False
        if y[i]<x[i]:
            return True
        if x[i] != y[i]:
            equals = False
        i+=1
    if equals:
        return False
    return True



if __name__ == '__main__':
    import doctest
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))