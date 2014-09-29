def is_BS(xrr):
    tmpxrr = xrr
    unique_pairs(tmpxrr)
    print(tmpxrr)
    return xrr

    if not correct_size(tmp):
        return False
    elif not unique_pairs(tmp):
        return False
    else:
        return xrr


def unique_pairs(xrr):
    uniques = []
    for entry in xrr:
        while len(entry) != 0:
            lastelement = entry.pop()
            print(xrr)
            for element in entry:
                if not uniques.__contains__([lastelement, element]) and not uniques.__contains__([element, lastelement]):
                    uniques.append([lastelement, element])
                else:
                    return False
    return True


def correct_size(xrr):
    size = len(xrr.pop())
    for entry in xrr:
        if size != len(entry):
            return False
    return True


b1 = [["A", "B", "C", "D"], ["A", "E", "I", "M"], ["A", "F", "K", "P"], ["A", "G", "L", "N"], ["A", "H", "J", "O"], ["E", "F", "G", "H"], ["B", "F", "J", "N"], ["B", "E", "L", "O"], ["B", "H", "K", "M"], ["B", "G", "I", "P"], ["I", "J", "K", "L"], ["C", "G", "K", "O"], ["C", "H", "I", "N"], ["C", "E", "J", "P"], ["C", "F", "L", "M"], ["M", "N", "O", "P"], ["D", "H", "L", "P"], ["D", "G", "J", "M"], ["D", "F", "I", "O"], ["D", "E", "K", "N"]]
b2 = [["A", "B", "C"], ["A", "D", "G"], ["A", "E", "F"], ["B", "D", "F"], ["B", "E", "G"], ["C", "D", "E"], ["C", "F", "G"]]
b3 = [["a", "b"], ["a", "c", "f"], ["a", "d", "e"], ["b", "c", "e"], ["b", "d", "f"], ["c", "d"], ["e", "f"]]
b4 = [["a", "b", "c"], ["a", "b", "d"], ["a", "e", "f"], ["b", "e", "f"], ["c", "d", "e"], ["c", "d", "f"]]
b5 = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [1, 5, 6], [2, 3, 7], [0, 5, 7], [1, 3, 8], [2, 4, 6]]
#print(unique_pairs(b4))
print(is_BS(b1))
#print(is_BS(b2))
#print(is_BS(b3))
#print(is_BS(b4))
#print(is_BS(b5))
#print(b1)