import textwrap
from pathlib import Path

# file = 'example_day3.txt'
file = 'input_day3.txt'

lines = Path(file).read_text().splitlines()

batteries = []
for line in lines:
    elements = textwrap.wrap(line, 1)
    max_element_1 = max(elements[:-1])
    index_max_element = elements[:-1].index(max_element_1)
    max_element_2 = max(elements[index_max_element + 1:])
    batteries.append(int(max_element_1 + max_element_2))

print(sum(batteries))
