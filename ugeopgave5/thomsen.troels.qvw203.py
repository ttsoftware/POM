

def is_sublist_length_equal(xl):
    """
    Checks whether or not all sublists have the same length
    :param xl:
    :return: boolean
    """
    len_found = -1
    for l in xl:
        if len_found == -1:
            len_found = len(l)
        elif len(l) != len_found:
            return False
    return True


def find_unique(xl):
    """
    Finds each unique element in all sublists
    If the same element occurs twice in a given sublist, we raise an Exception
    :param xl:
    :return: list
    """
    rl = []
    for l in xl:  # each list l
        le = []
        for e in l:  # each list element e
            if e in le:
                raise Exception("Non-unique list structure")
            if e not in rl:
                rl += [e]
            le += [e]
    return rl


def find_pairs(l):
    """
    Finds all pairs, for each element in list l
    :param l:
    :return:
    """
    pl = []
    for e in l:
        pl.extend(map(lambda x: (e, x) if x != e
                                          and (e, x) not in pl
                                          and (x, e) not in pl else None, l))
    return filter(lambda x: x is not None, pl)


def is_BS(xl):
    """
    Returns True if xl is in fact a blocksystem
    Returns False otherwise
    :param xl:
    :return:
    """
    elements = find_unique(xl)  # all unique elements
    pairs = find_pairs(elements)  # all permutations of

    # each permutation may only occur once across all sublists
    for p in pairs:
        p_occur = 0
        x, y = p

        for l in xl:
            if (x in l) and (y in l):
                p_occur += 1

        if p_occur > 1:
            return False

    return is_sublist_length_equal(xl)


test1 = [[0, 1, 2, 3], [0, 4, 8, 12], [0, 5, 10, 15], [0, 6, 11, 13], [0, 7, 9, 14],
         [4, 5, 6, 7], [1, 5, 9, 13], [1, 4, 11, 14], [1, 7, 10, 12], [1, 6, 8, 15],
         [8, 9, 10, 11], [2, 6, 10, 14], [2, 7, 8, 13], [2, 4, 9, 15], [2, 5, 11, 12],
         [12, 13, 14, 15], [3, 7, 11, 15], [3, 6, 9, 12], [3, 5, 8, 14], [3, 4, 10, 13]]

test2 = [[0, 1, 2], [0, 3, 6], [0, 4, 5], [1, 3, 5], [1, 4, 6], [2, 3, 4], [2, 5, 6]]

test3 = [[0, 1], [0, 2, 5], [0, 3, 4], [1, 2, 4], [1, 3, 5], [2, 3], [4, 5]]

test4 = [[0, 1, 2], [0, 1, 3], [0, 4, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5]]

test5 = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],
         [0, 4, 8], [1, 5, 6], [2, 3, 7], [0, 5, 7], [1, 3, 8], [2, 4, 6]]


print is_BS(test1) == True
print is_BS(test2) == True
print is_BS(test3) == False
print is_BS(test4) == False
print is_BS(test5) == True