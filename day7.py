from operator import itemgetter

# next time I wouldve done some kind of graph impl

def part1(data):
    rules = parse_rules(data)
    print(len(seek(rules, "shiny gold")))

def part2(data):
    rules = parse_rules(data)
    print(count(rules, "shiny gold") - 1)

def parse_rules(data):
    d = {}
    for line in data:
        clauses = line.split(" bags contain ")
        bag = clauses[0]
        contents = []
        if not clauses[1].startswith("no"):
            subclauses = clauses[1].split(", ")
            for sc in subclauses:
                words = sc.split()
                contents.append((int(words[0]), words[1] + " " + words[2]))
        d[bag] = contents
    return d

def seek(rules, bag):
    result = set()
    for (b, contents) in rules.items():
        getname = itemgetter(1)
        bagnames = list(map(getname, contents))
        if bag in bagnames:
            result.add(b)
            result = result.union(seek(rules, b))
    return result

def count(rules, bag):
    result = 1
    contents = rules[bag]
    for (cnt, name) in contents:
        result += cnt * count(rules, name)
    return result

if __name__ == "__main__":
    with open("day7.txt", "r") as fp:
        data = fp.read().splitlines()
        part1(data)
        part2(data)
