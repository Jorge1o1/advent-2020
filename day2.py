def part1(data):
    print(sum([is_valid_row(r) for r in data]))

def part2(data):
    print(sum([is_valid_pt2(r) for r in data]))
    
def is_valid_row(r):
    parts = r.split(" ")
    rnge = parts[0].split("-")
    mn = int(rnge[0])
    mx = int(rnge[1])
    lttr = parts[1][0]
    pwd = parts[2]
    if pwd.count(lttr) >= mn and pwd.count(lttr) <= mx:
        return 1
    else:
        return 0

def is_valid_pt2(r):
    parts = r.split(" ")
    rnge = parts[0].split("-")
    p1 = int(rnge[0])
    p2 = int(rnge[1])
    lttr = parts[1][0]
    pwd = parts[2]
    return (pwd[p1 - 1] == lttr) != (pwd[p2 - 1] == lttr)
    
if __name__ == "__main__":
    with open("day2.txt", "r") as fp:
        data = fp.read().splitlines()
        part1(data)
        part2(data)
