def equal_length(xrr):
    ans = len(xrr[0])
    for i in xrr:
        if len(i) != ans:
            return False
    return True

def possible_pairs(xr):
    ans = []
    for i, x in enumerate(xr):
        for j, y in enumerate(xr):
            if i != j:
                ans += [[x, y]]
    return ans

def no_redundant_in_list(xrr):
    for xr in xrr:
        for i, x in enumerate(xr[:-1]):
            if x in xr[i+1:]:
                return False
    return True

def make_rest_list(xrr):
    ans = []
    for xr in xrr:
        ans += possible_pairs(xr)
    return ans

def no_redundant_pairs(xrr):
    i = 1
    for xr in xrr:
        for pair in possible_pairs(xr):
            if pair in make_rest_list(xrr[i:]):
                return False
        i += 1
    return True

def is_BS(xrr):
    return equal_length(xrr) and no_redundant_pairs(xrr) and no_redundant_in_list(xrr)

B1 = [['A','B','C','D'], ['A','E','I','M'], ['A','F','K','P'], ['A','G','L','N'], ['A','H','J','O'],
      ['E','F','G','H'], ['B','F','J','N'], ['B','E','L','O'], ['B','H','K','M'], ['B','G','I','P'],
      ['I','J','K','L'], ['C','G','K','O'], ['C','H','I','N'], ['C','E','J','P'], ['C','F','L','M'],
      ['M','N','O','P'], ['D','H','L','P'], ['D','G','J','M'], ['D','F','I','O'], ['D','E','K','N']]

B2 = [['A','B','C'], ['A','D','G'], ['A','E','F'], ['B','D','F'], ['B','E','G'], ['C','D','E'], ['C','F','G']]

B3 = [['a','b'], ['a','c','f'], ['a','d','e'], ['b','c','e'], ['b','d','f'], ['c','d'], ['e','f']]

B4 = [['a','b','c'], ['a','b','d'], ['a','e','f'], ['b','e','f'], ['c','d','e'], ['c','d','f']]

B5 = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8],
      [0,4,8], [1,5,6], [2,3,7], [0,5,7], [1,3,8], [2,4,6]]

B6 = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8],
      [0,4,8], [1,5,6], [2,3,7], [0,0,7], [1,3,8], [2,4,6]]

print is_BS(B1) == True
print is_BS(B2) == True
print is_BS(B3) == False
print is_BS(B4) == False
print is_BS(B5) == True
print is_BS(B6) == False