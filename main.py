from collections import OrderedDict

f = open('text.txt', 'r')

s = f.read()
#print(s)
chrs = {}
cnt = 0
sum = 0

for i in s:
    if i == '\n' or i == ' ':
        continue
    if i in chrs:
        chrs[i] += 1
    else:
        chrs[i] = 1
    cnt += 1

for i in chrs.keys():
    chrs[i] /= cnt
    chrs[i] = round(chrs[i]*100, 2)
    sum += chrs[i]
    #chrs[i] = str(chrs[i]) + '%'
    #print(i, ':', chrs[i])

chrs = OrderedDict(sorted(chrs.items()))

#print(chrs)
#print(sum, '%')
