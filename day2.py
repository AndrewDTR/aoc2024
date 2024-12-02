def check(input_list):
    if input_list[0] == input_list[1]:
        return False
    elif input_list[0] < input_list[1]:  # ascending case
        track = 0
        for i in range(0, len(input_list) - 1):
            if input_list[i] < input_list[i + 1] and 1 <= abs(input_list[i] - input_list[i + 1]) <= 3:
                track += 1
        if track == len(input_list) - 1:
            return True
    elif input_list[0] > input_list[1]:  # descending case
        track = 0
        for i in range(0, len(input_list) - 1):
            if input_list[i] > input_list[i + 1] and 1 <= abs(input_list[i] - input_list[i + 1]) <= 3:
                track += 1
        if track == len(input_list) - 1:
            return True


with open("input.txt", "r") as f:
    reports = f.read()

safe_without_omission = 0
safe_reports = 0

for report in reports.splitlines():
    status = report.split(" ")
    status = [int(i) for i in status if i]

    if not status:
        continue

    # part 1
    if check(status):
        safe_reports += 1
        safe_without_omission += 1
        continue

    # part 2
    for i in range(0, len(status)):
        new_list = [i for i in status]
        new_list.pop(i)
        if check(new_list):
            safe_reports += 1
            break

print(safe_without_omission, safe_reports)
