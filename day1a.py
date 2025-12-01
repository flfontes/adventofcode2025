starting_position = 50
current_position = starting_position

rotations_doc = 'input_day1.txt'

with open(rotations_doc, 'r') as file:
    rotations = file.readlines()

print(f'The dial starts by pointing at {current_position}')

zero_counter = 0

for rotation in rotations:
    direction = rotation[0]
    times = int(rotation[1:])

    actual_times = times - (times // 100) * 100 
    print(f'{actual_times}')

    match direction:
        case 'L':
            current_position = current_position - actual_times
        case 'R':
            current_position = current_position + actual_times

    if current_position > 99:
        current_position =  current_position - 100
    elif current_position < 0:
        current_position = current_position + 100

    print(f'The dial is rotated {direction}{times} to point at {current_position}.')

    if current_position == 0:
        zero_counter += 1

print(zero_counter)
