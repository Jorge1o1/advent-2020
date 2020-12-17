# I don't really like the runtime complexity, I think I can memoize or DP
# from the bottom up to make more efficient. Also, the printing is broken

def part1(data):
    return subset_sum(data, 2, 2020)

def part2(data):
    return subset_sum(data, 3, 2020)

def subset_sum(s, n, t):
    if n == 0 or len(s) == 0:
        return t == 0
    else:
        incl = s.copy()
        excl = s.copy()
        e = incl.pop()
        excl.pop()
        w = subset_sum(incl, n - 1, t - e)
        wo = subset_sum(excl, n, t)
        if w:
            print(e)
        return w or wo

if __name__ == "__main__":
    with open("day1-input.txt", "r") as fp:
        data = [int(x) for x in fp.read().splitlines()]
        #print(part1(data))
        print(part2(data))
