from itertools import permutations
s = 'catdog'
perms = permutations(s)
res = []
for x in perms:
    res.append(''.join(x))
print(res)
