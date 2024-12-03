with open("input.txt", "r") as f:
    temp = f.read().splitlines()

puzzle_input = ""
for i in temp:
    puzzle_input += i


def question_switcher(question):
    running_sum = 0
    enabled = True

    for i in range(0, len(puzzle_input)):
        num1 = None
        num2 = None

        if puzzle_input[i:i + 4] == "do()":
            enabled = True
        if puzzle_input[i:i + 7] == "don't()":
            enabled = False

        if puzzle_input[i:i + 4] == "mul(":
            mode = 1
            sweep = i + 4

            while not mode == 3:
                if puzzle_input[sweep] not in "0987654321,()":
                    mode = 4
                    break
                if not mode == 2 and puzzle_input[sweep] == ")":
                    mode = 4
                    break
                if mode == 1 and not num1 is None and puzzle_input[sweep] == ",":
                    mode = 2
                elif mode == 1 and puzzle_input[sweep].isnumeric():
                    if num1 is None:
                        num1 = ""
                    num1 += puzzle_input[sweep]
                elif mode == 2 and puzzle_input[sweep].isnumeric():
                    if num2 is None:
                        num2 = ""
                    num2 += puzzle_input[sweep]

                if mode == 2 and not num1 is None and not num2 is None and puzzle_input[sweep] == ")":
                    mode = 3
                    break

                sweep += 1

            # invalid
            if mode == 4:
                continue

            if mode == 3:
                if enabled or question:
                    running_sum += int(num1) * int(num2)

    return running_sum


print(question_switcher(True), question_switcher(False)) # part 1, part 2
