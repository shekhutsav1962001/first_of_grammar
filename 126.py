rules = []
nont = []
l = []
ter = []
with open("input.txt", "r") as fp:
    for line in fp:
        rules.append(line.strip().split('\n'))
for rule in rules:
    nont.append(rule[0][0])
    l.append(rule[0][3:].split('|'))

for i in l:
    for j in i:
        for data in j:
            if (not data.isupper()) and data != "$":
                ter.append(data)

d = {}

# create dict
for i in range(0, len(nont)):
    s = set()
    for j in l[i]:
        if(j == "$"):
            s.add('$')
        elif(j[0] in ter):
            s.add(j[0])
    d[nont[i]] = s

for _ in range(10):
    for i in range(0, len(nont)):
        s = set()
        for j in l[i]:
            m = 'a'
            for m in j:
                if(m in nont):
                    if('$' not in d[m]):
                        s = s.union(d[m])
                        break
                    else:
                        s = s.union(d[m].difference(set('$')))
                else:
                    s = s.union(m)
                    break
            if(m in nont and '$' in d[m]):
                s.add('$')
            d[nont[i]] = d[nont[i]].union(s)

for i in range(0, len(nont)):
    for j in l[i]:
        if j.isalpha() and j.isupper():
            flag = True
            for nonterminal in j:
                if '$' in d[nonterminal]:
                    pass
                else:
                    flag = False
            if flag and '$' not in d[nont[i]]:
                d[nont[i]] = d[nont[i]].union(set('$'))


print("First Set")
for i in nont:
    print("First(", i, ") : ", d[i])
