def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    # return c
    if len(a[0])!=len(b):
        return -1
    c= []
    for i in range(len(a)):
        cx =[]
        for j in range(len(b[0])):
            cx.append(sum([a[i][k]*b[k][j] for k in range(len(b))]))
            # print(cx, i, j)
        c.append(cx.copy())
    # print(c)
    return c