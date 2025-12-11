import textwrap
from pathlib import Path

file = 'input_day2.txt'
# file = 'example_day2.txt'

ids = Path(file).read_text()

ranges =  ids.split(',')

numbers = []
for rg in ranges:
    for first, _, last in [rg.partition('-')]:
        for number in range(int(first), int(last or first) + 1):
            numbers.append(str(number))


repeat_numbers = set()
for number in numbers:
    half = len(number) // 2
    for i in range(half + 1, 0, -1):
        chunks = textwrap.wrap(number, i)
        equals = 0
        for j in range(1, len(chunks)):
            if chunks[0] == chunks[j]:
                equals += 1
        if equals == (len(chunks) - 1) and equals > 0:
            repeat_numbers.add(int(number))

print(sum(repeat_numbers))
