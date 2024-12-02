# AoC 2024 Day 2

# Part 1

def is_safe_report(report: list) -> bool:
    increasing = True

    first_diff = report[1] - report[0]
    if first_diff == 0 or abs(first_diff) > 3:
        return False
    if first_diff < 0:
        increasing = False

    for i in range(2, len(report)):
        diff = report[i] - report[i - 1]
        p = (diff >= 1 and diff <= 3) if increasing else (
            diff <= -1 and diff >= -3)
        if not p:
            return False

    return True


with open('day2.txt', 'r') as f:
    reports = list(map(lambda line: list(
        map(int, line.split())), f.readlines()))

safe_reports = list(filter(is_safe_report, reports))

print('Answer for part 1:', len(safe_reports))

# Part 2

def is_safe_report(report: list) -> bool:
    increasing = True
    unsafe_levels = 0

    diffs = [report[i] - report[i - 1] for i in range(1, len(report))]
    num_increasing = len([diff for diff in diffs if diff > 0])
    num_decreasing = len([diff for diff in diffs if diff < 0])
    if num_decreasing > num_increasing:
        increasing = False

    for i in range(len(report) - 1, 0, -1):
        diff = report[i] - report[i - 1]
        p = (diff >= 1 and diff <= 3) if increasing else (
            diff <= -1 and diff >= -3)
        if not p:
            unsafe_levels += 1
            report.pop(i - 1)

    return unsafe_levels <= 1


safe_reports = list(filter(is_safe_report, reports))

print('Answer for part 2:', len(safe_reports))
