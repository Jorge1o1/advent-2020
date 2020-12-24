import re

def part1(data):
    valid = 0
    entries = data.split("\n\n")
    for e in entries:
        if is_valid(e):
            valid += 1
    print(valid)

def part2(data):
    valid = 0
    entries = data.split("\n\n")
    for e in entries:
        if is_valid2(e):
            valid += 1
    print(valid)

def is_valid(entry):
    keys = [x.split(":")[0] for x in entry.split()]
    flds = ["ecl","pid","eyr","hcl","byr","iyr","hgt"]
    return all(f in keys for f in flds)

def is_valid2(entry):
    d = {x.split(":")[0]:x.split(":")[1] for x in entry.split()}
    try:
        return (
            int(d["byr"]) >= 1920 and int(d["byr"]) <= 2002
            and int(d["iyr"]) >= 2010 and int(d["iyr"]) <= 2020
            and int(d["eyr"]) >= 2020 and int(d["eyr"]) <= 2030
            and valid_hgt(d["hgt"])
            and re.match("#[a-f0-9]{6}",d["hcl"])
            and d["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"]
            and re.match("\d{9}$",d["pid"]))
    except KeyError:
        return False

def valid_hgt(hgt):
    try:
        unit = hgt[-2:]
        amt = int(hgt[0:-2])
        return (
            (unit == "cm" and amt >= 150 and amt <= 193)
            or (unit == "in" and amt >= 59 and amt <= 76))
    except:
        return False

            
if __name__ == "__main__":
    with open("day4.txt", "r") as fp:
        data = fp.read()
        part1(data)
        part2(data)
