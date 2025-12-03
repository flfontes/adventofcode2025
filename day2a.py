from pathlib import Path

file = 'input_day2.txt'

ids = Path(file).read_text()

ranges =  ids.split(',')

total = 0
for rg in ranges:
    rg = rg.split('-')
    for value in range(int(rg[0]), int(rg[1])+1):
        value = str(value)
        if len(value) % 2 != 0:
            continue
        middle = len(value)//2
        if value[:middle] == value[middle:]:
            total += int(value)

print(total)
