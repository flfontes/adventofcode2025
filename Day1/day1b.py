starting_position = 50

# rotations_doc = 'example_day1.txt'
rotations_doc = 'input_day1.txt'

current_position = starting_position

with open(rotations_doc, 'r') as file:
    rotations = file.readlines()

print(f'The dial starts by pointing at {current_position}')

zero_counter = 0

for rotation in rotations:
    previous_position = current_position

    direction = rotation[0]
    times = int(rotation[1:])

    actual_times = times - (times // 100) * 100
    if times // 100 > 0:
        zero_counter += (times // 100)

    match direction:
        case 'L':
            current_position = current_position - actual_times
        case 'R':
            current_position = current_position + actual_times


    if previous_position == 0 and current_position < 0:
        current_position = current_position + 100
    elif previous_position != 0 and current_position < 0:
        current_position = current_position + 100
        zero_counter += 1
    elif current_position > 99:
        current_position = current_position - 100
        zero_counter += 1
    elif current_position == 0:
        zero_counter += 1

    # if current_position > 99:
    #     current_position =  current_position - 100
    #     zero_counter += 1
    # elif current_position < 0:
    #     current_position = current_position + 100
    #     zero_counter += 1
    #

    print(f'The dial is rotated {direction}{times} to point at {current_position}.')

    print(zero_counter)
