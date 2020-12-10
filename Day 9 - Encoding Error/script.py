import itertools

with open("input.txt", "r") as f:
    puzzle_input = [int(s.rstrip()) for s in f.readlines()]


def addCheck(nums, target):
    return nums[0] + nums[1] == target


window = 24

while window < len(puzzle_input) - 1:
    subList = puzzle_input[window-24:window+1]
    target = puzzle_input[window+1]

    perms = list(itertools.permutations(subList, 2))
    if not any(map(addCheck, perms, [target for _ in range(len(perms))])):
        print(f"Part One: {target}")
        break

    window += 1
