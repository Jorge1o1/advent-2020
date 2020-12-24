def part1(data):
    groups = data.split("\n\n")
    counts = [count_yes(g) for g in groups]
    print(sum(counts))

def part2(data):
    groups = data.split("\n\n")
    counts = []
    for g in groups:
        ppl = g.split()
        sets = []
        for p in ppl:
            s = set()
            for l in p:
                s.add(l)
            sets.append(s)
        u = set.intersection(*sets)
        counts.append(len(u))
    print(sum(counts))

def count_yes(grp):
    s = set()
    for lttr in grp:
        if lttr != "\n":
            s.add(lttr)
    return len(s)

if __name__ == "__main__":
    with open("day6.txt", "r") as fp:
        data = fp.read()
        part1(data)
        part2(data)
