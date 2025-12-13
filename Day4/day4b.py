from pathlib import Path

# file = 'example_day4.txt'
file = 'input_day4.txt'

original_lines = Path(file).read_text().splitlines()
translator = str.maketrans('.@', '01')
lines = []
for line in original_lines:
    row = [int(item.translate(translator)) for item in line]
    lines.append(row)

count = 0
previous_count = -1
emptied_locations = []
while previous_count < count:
    previous_count = count
    
    for idx in emptied_locations:
        lines[idx[0]][idx[1]] = 0

    emptied_locations = []
    for i, row in enumerate(lines):
        for j, column in enumerate(row):
            # Excludes empty spaces
            if column == 0:
                continue

            # Calculates top-left corner
            if i == 0 and j == 0:
                test = lines[i][j+1] + sum(lines[i+1][j:j+2])
                print(f'I: {i}, J: {j}, Test: {test}')
                if test < 4:
                    count += 1
                    emptied_locations.append((i, j))
                continue

            # Calculates top row
            if i == 0 and 0 < j <= len(row) - 2:
                test = sum(lines[i+1][j-1:j+2]) + lines[i][j-1] + lines[i][j+1]
                print(f'I: {i}, J: {j}, Test: {test}')
                if test < 4:
                    count += 1
                    emptied_locations.append((i, j))
                continue

            # Calculates top-right corner
            if i == 0 and j == len(row) - 1:
                test = lines[i][j-1] + sum(lines[i+1][j-1: j+1])
                print(f'I: {i}, J: {j}, Test: {test}')
                if test < 4:
                    count += 1
                    emptied_locations.append((i, j))
                continue

            # Calculates left column
            if 0 < i <= len(lines) - 2 and j == 0:
                test = sum(lines[i-1][j:j+2]) + lines[i][j+1] + sum(lines[i+1][j:j+2])
                print(f'I: {i}, J: {j}, Test: {test}')
                if test < 4:
                    count += 1
                    emptied_locations.append((i, j))
                continue

            # Calculates right column
            if 0 < i <= len(lines) - 2 and j == len(row) - 1:
                test = sum(lines[i-1][j-1:j+1]) + lines[i][j-1] + sum(lines[i+1][j-1:j+1])
                print(f'I: {i}, J: {j}, Test: {test}')
                if test < 4:
                    count += 1
                    emptied_locations.append((i, j))
                continue


            # Calculates bottom-left corner
            if i == len(row) - 1 and j == 0:
                test = sum(lines[i-1][j:j+2]) + lines[i][j+1]
                print(f'I: {i}, J: {j}, Test: {test}')
                if test < 4:
                    count += 1
                    emptied_locations.append((i, j))
                continue

            # Calculates bottom row
            if i == len(row) - 1 and 0 < j <= len(row) - 2:
                test = sum(lines[i-1][j-1:j+2]) + lines[i][j-1] + lines[i][j+1]
                print(f'I: {i}, J: {j}, Test: {test}')
                if test < 4:
                    count += 1
                    emptied_locations.append((i, j))
                continue

            # Calculates bottom-right corner
            if i == len(row) - 1 and j == len(row) - 1:
                test = sum(lines[i-1][j-1:j+1]) + lines[i][j-1]
                print(f'I: {i}, J: {j}, Test: {test}')
                if test < 4:
                    count += 1
                    emptied_locations.append((i, j))
                continue

            test = sum(lines[i-1][j-1:j+2]) + lines[i][j-1] + lines[i][j+1] + sum(lines[i+1][j-1:j+2])
            print(f'I: {i}, J: {j}, Test: {test}')
            if test < 4:
                count += 1
                emptied_locations.append((i, j))


print(count)


