def solution(n, control):
# case1
    for char in control:
        if char == "w":
            n += 1
        elif char == "s":
            n -= 1
        elif char == "a":
            n -= 10
        elif char == "d":
            n += 10
    return n

# case2
    # key = dict(zip(["w","s","d","a"], [1,-1,10,-10]))
    # return n + sum(key[c] for c in control)
