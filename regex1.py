import re

file = open('regex_sum_259103.txt')
result = 0
for line in file:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    for item in numbers:
        result += int(item)
print(result)
