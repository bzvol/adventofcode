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


def is_safe_report2(report: list) -> bool:
    for i in range(len(report)):
        r = report.copy()
        r.pop(i)
        if is_safe_report(r):
            return True
    return False


safe_reports = list(filter(is_safe_report2, reports))

print('Answer for part 2:', len(safe_reports))
