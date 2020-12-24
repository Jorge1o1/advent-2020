import math

def part1(data):
    sids = [get_seat_id(bp) for bp in data]
    print(max(sids))

def part2(data):
    sids = sorted([get_seat_id(bp) for bp in data])
    for idx, s in enumerate(sids):
        prev = sids[idx - 1]
        if s - prev != 1:
            print(s, prev)
    

def binary(s, start, end, lstr, ustr):
    if start == end:
        return start

    bisect = math.ceil((end - start)/2)
    if s[0] == lstr:
        return binary(s[1:], start, end - bisect, lstr, ustr)
    if s[0] == ustr:
        return binary(s[1:], start + bisect, end, lstr, ustr)

def get_seat_id(bp):
    row = binary(bp[0:7], 0, 127, "F", "B")
    col = binary(bp[7:], 0, 7, "L", "R")
    return (row * 8) + col
    
if __name__ == "__main__":
    with open("day5.txt", "r") as fp:
        data = fp.read().splitlines()
        part1(data)
        part2(data)
