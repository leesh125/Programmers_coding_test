# My turn
def solution(sizes):
    for s in sizes:
        if s[1] > s[0]:
            s[0], s[1] = s[1], s[0]
       
    max_1 = max(i[0] for i in sizes)
    max_2 = max(i[1] for i in sizes)

    return max_1 * max_2

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))

# Good explanation
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

