from copy import copy
from itertools import combinations

def part1(data):
    SEQLEN = 25
    while len(data) > (SEQLEN + 1) and is_good(data, SEQLEN):
        data.pop(0)
    print("broke", data[SEQLEN])

def part2(data):
    TGT = 29221323
    i = 0
    result = seqsum(data[i:], TGT, 0, [])
    while not result[0]:
        i += 1
        result = seqsum(data[i:], TGT, 0, [])
    a = min(result[1])
    b = max(result[1])
    print(a, b, a + b)

def is_good(nums, seqlen):
    pre = nums[0:seqlen]
    n = int(nums[seqlen])
    sums = [int(t[0]) + int(t[1]) for t in combinations(pre, 2)]
    return n in sums

def seqsum(nums, tgt, rt, seq):
    nrt = rt + int(nums[0])
    nseq = seq + [int(nums[0])]
    if nrt < tgt:
        return seqsum(nums[1:], tgt, nrt, nseq)
    else:
        return (nrt == tgt, nseq)
    
    

if __name__ == "__main__":
    with open("day9.txt", "r") as fp:
        data = fp.read().splitlines()
        # fuck mutation, the root of all evil.
        # This little shit cost me 10 minutes.
        part1(copy(data))
        part2(copy(data))
