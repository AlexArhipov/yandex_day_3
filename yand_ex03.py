def ex01():
    print len(list(set(raw_input().split(' '))))

def ex02():
    print str(sorted((set(map(int, raw_input().split(' '))).intersection(set(map(int, raw_input().split(' ')))))))[
          1:-1].replace(',', '')

def ex03():
    data = raw_input().split(' ')
    ak = int(data[0])
    bk = int(data[1])
    am = []
    bm = []
    for i in range(ak):
        am.append(int(raw_input()))
    for i in range(bk):
        bm.append(int(raw_input()))
    print len(sorted(set(am).intersection(set(bm))))
    print str(sorted(set(am).intersection(set(bm))))[1:-1].replace(',', '')
    print len(sorted(set(am).difference(set(bm))))
    print str(sorted(set(am).difference(set(bm))))[1:-1].replace(',', '')
    print len(sorted(set(bm).difference(set(am))))
    print str(sorted(set(bm).difference(set(am))))[1:-1].replace(',', '')

def ex04():
    f = open("input.txt", "r")
    data = f.read().split()
    f.close()
    print len(set(data))

def ex05():
    kn = set(map(int, raw_input().split(' ')))
    ch = set(map(int, set(raw_input())))
    nov = ch.difference(kn)
    print len(nov)

def find6(x, myset):
    caunt = 0
    for naw in myset[ord(x[0]) * ord(x[1])]:
        if naw == x:
            caunt += 1
    return caunt
def ex06():
    setsize = 10000
    myset = [[] for _ in range(setsize)]
    str1 = raw_input()
    str2 = raw_input()
    caunt = 0
    for i in range(len(str2) - 1):
        if find6(str2[i] + str2[i + 1], myset) == 0:
            myset[ord(str2[i]) * ord(str2[i + 1])].append(str2[i] + str2[i + 1])
    for i in range(len(str1) - 1):
        caunt += find6(str1[i] + str1[i + 1], myset)
    print caunt

def find7(st, myset, setsize):
    for naw in myset[st[0] % setsize]:
        if naw == st[0] * 10 + st[1]:
            return 1
    return 0
def ex07():
    setsize = 10
    myset = [[] for _ in range(setsize)]
    len = int(raw_input())
    caunt = 0
    st = 10
    for i in range(len):
        st = map(int, raw_input().split(' '))
        if st[0] >= 0 and st[1] >= 0 and (st[0] + st[1] == len - 1) and (find7(st, myset, setsize) == 0):
            myset[st[0] % setsize].append(st[0] * 10 + st[1])
            caunt += 1
    print caunt


def find8(st, myset, setsize):
    for naw in myset[st[0] % setsize]:
        if naw == st[0]:
            return 1
    return 0
def ex08():
    setsize = 10
    myset = [[] for _ in range(setsize)]
    len = int(raw_input())
    caunt = 0
    for i in range(len):
        st = map(int, raw_input().split(' '))
        if find8(st, myset, setsize) == 0:
            myset[st[0] % setsize].append(st[0])
            caunt += 1
    print caunt

def ex09():
    kol_uch = int(raw_input())
    a = set()
    b = set()
    c = set()
    for i in range(kol_uch):
        kol_yaz = int(raw_input())
        a.clear()
        for j in range(kol_yaz):
            a.add(raw_input())
            if i == 1:
                b = a
        c.update(a)
        b = b.intersection(a)
    print len(b)
    for i in b:
        print i
    print len(c)
    for i in c:
        print i