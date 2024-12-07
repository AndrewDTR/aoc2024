with open("input.txt", "r") as f:
    file_input = [i for i in f.read().splitlines() if len(i) > 0]


def solve(part2):
    running_sum = 0

    for i in file_input:
        sum_to = int(i[0:i.find(":")])
        nums = [int(j) for j in i[i.find(":") + 2:len(i)].split(" ")]

        cases = []
        for j in range(0, len(nums)):
            build = set()
            if j == 0:
                build.add(nums[0])
            else:
                for k in cases:
                    build.add(int(k) * nums[j])
                    build.add(int(k) + nums[j])
                    if part2:
                        build.add(int(str(int(k)) + str(nums[j])))
            cases = [e for e in build]

        for p in cases:
            if p == sum_to:
                running_sum += sum_to

    return running_sum


print(solve(False), solve(True))  # part 1, part 2
