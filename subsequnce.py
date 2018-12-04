# -*- coding: utf-8 -*-

def max_subs(a, b):

    memo = [[0 for x in range(len(a))] for y in range(len(b))]

    def f1(x, y, i, j, memo):
        if (i == len(x)) or (j == len(y)):
            return ""
        if memo[j][i]:
            return memo[j][i]
        if x[i] == y[j]:
            memo[j][i] = x[i] + f1(x, y, i+1, j+1, memo)
            return memo[j][i]
        else:
            res1 = f1(x, y, i+1, j, memo)
            res2 = f1(x, y, i, j+1, memo)
            memo[j][i] = res1 if len(res1) > len(res2) else res2
            return memo[j][i] 
    
    return f1(a, b, 0, 0, memo)




if __name__ == '__main__':
    print(max_subs("Абракадабра", "брабракубра"))
    