text = []
d = {}
v = {}
kd = 'aaaa'


def f(k):
    return k


def text_stat(t):
    l = 0
    w = 0
    b = 0
    g2 = ' ,:@.-()/'
    g = t
    for gi in g2:
        Temp = []
        n = len(g)
        for i in range(n):
            h = g[i].split(str(gi))
            while True:
                try:
                    h.remove('')
                except ValueError:
                    break
            Temp = Temp + h
            if i == n - 1:
                g = Temp[:]
    g.sort()
    print("Статистика слов:")
    for i in g:
        if i == '@' or i == '.' or i == ';' or i == ']' or i == '[' or i == ' ' or i == '(' or i == ')' or i == '\'' \
                or i == ',':
            pass
        else:
            d[i] = g.count(i)
    for i in d:
        print(i, d[i])
    for i in t:
        l += 1
        b += len(i)
        counter = True
        for k in i:
            if k != ' ' and counter == True:
                w += 1
                counter = False
            elif k == ' ':
                counter = True

    print("количество строк в тексте: ", l)
    print("Количестро слов в тексте: ", w)
    print("количество символов в тексте: ", b)
    t.sort()
    t = str(t)
    print("Статистика символов:")
    for i in t:
        if i == '@' or i == '.' or i == ';' or i == ']' or i == '[' or i == ' ' or i == '(' or i == ')' or i == '\'' \
                or i == ',':
            pass
        else:
            v[i] = t.count(i)
    for i in v:
     print(i, v[i])


a = input("введите дянные: ")
while True:
    text.append(a)
    a = input()
    if not a:
        break
filter(text_stat(text), f(kd))
