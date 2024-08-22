from collections import OrderedDict

n = int(input())

d = OrderedDict()

for i in range(n):
    s = input()
    if s not in d.keys():
        d[s] = 1
    else:
        d[s] += 1

``
print(len(d))
s = ""
for v in d.values():
    s += str(v) + " "
print(s)


# https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
