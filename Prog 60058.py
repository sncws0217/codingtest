def check(p):
    x = y = 0
    for i in range(len(p)):
        if p[i] == '(':
            x += 1
        elif p[i] == ')':
            y += 1
        if x < y:
            return False
    return True