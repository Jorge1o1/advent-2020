def part1(data):
    print(count_trees(data, 3, 1))

def part2(data):
    print(
        count_trees(data, 1, 1)
        * count_trees(data, 3, 1)
        * count_trees(data, 5, 1)
        * count_trees(data, 7, 1)
        * count_trees(data, 1, 2)
    )

def count_trees(data, right, down):
    length = len(data)
    width = len(data[0])
    trees = 0
    x = 0
    y = 0
    while y < length:
        if data[y][x] == "#":
            trees += 1
        x = (x + right) % width
        y += down
    return trees

if __name__ == "__main__":
    with open("day3.txt", "r") as fp:
        data = fp.read().splitlines()
        part1(data)
        part2(data)
