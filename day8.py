from copy import copy

def part1(data):
    instr = parse_instr(data)
    (acc, bl) = evaluate(instr)
    print(acc)

# i brute forced it as opposed to elegance because I have a
# meeting in 10 minutes. it took like 0.00001 seconds anyways.

def part2(data):
    insts = parse_instr(data)
    variants = []
    for i in insts:
        if i[1] == "nop":
            cp = copy(insts)
            cp[i[0]] = (i[0], "jmp", i[2])
            variants.append(cp)
        if i[1] == "jmp":
            cp = copy(insts)
            cp[i[0]] = (i[0], "nop", i[2])
            variants.append(cp)
    for v in variants:
        (acc, bl) = evaluate(v)
        if bl:
            print(acc)

def parse_instr(lines):
    instr = []
    for idx, l in enumerate(lines):
        parts = l.split()
        instr.append((idx,parts[0],int(parts[1])))
    return instr

def execute(instr, acc):
    """ Returns (acc, nextop) """
    if instr[1] == "nop":
        return (acc, instr[0] + 1)
    if instr[1] == "acc":
        return (acc + instr[2], instr[0] + 1)
    if instr[1] == "jmp":
        return (acc, instr[0] + instr[2])

def evaluate(instr):
    """ returns (acc, broke_loop) """
    visited = set()
    acc = 0
    nxt = 0
    while nxt not in visited:
        visited.add(nxt)
        (acc, nxt) = execute(instr[nxt], acc)
        if nxt >= len(instr):
            return (acc, True)
    return (acc, False)


if __name__ == "__main__":
    with open("day8.txt", "r") as fp:
        data = fp.read().splitlines()
        part1(data)
        part2(data)
