def solution(ineq, eq, n, m):
    if ineq == "!":
        if ineq == "<":
            return int (n < m)
        else:   # > !
            return int(n > m)
    else:
        if ineq == "<" :
             return int(n<=m)
        else:
            return int(n>=m)
