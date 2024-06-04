def gugu(dan, num):
    print("%d * %d = %d" % (dan, num, dan * num), end="\t")
    if num < 9:
        gugu(dan, num + 1)


for dan in range(2, 10):
    gugu(dan, 1)
    print()
