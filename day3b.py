import textwrap
from pathlib import Path

# file = 'example_day3.txt'
file = 'input_day3.txt'

lines = Path(file).read_text().splitlines()

batteries = 0
for line in lines:
    elements = textwrap.wrap(line, 1)
    battery = ''
    idx_last = 0
    for i in range(11, -1, -1):
        idx, max_value = [
            (index, value)
            for index, value in enumerate(elements[idx_last:len(elements) - i])
            if value == max(elements[idx_last:len(elements) - i])
        ][0]
        battery += max_value
        idx_last += idx + 1
        print(f'Value: {max_value}, Idx: {idx_last}, Battery: {battery}')
    batteries += int(battery)

print(batteries)
