
MinPuzzleInput = 245182
MaxPuzzleInput = 790572

num_possible = 0
for puzzle_num in range(MinPuzzleInput, MaxPuzzleInput):
    digit_list = [int(digit) for digit in str(puzzle_num)]
    is_possible_num = 0
    for idx in range(1,6): # six digits
        if digit_list[idx] == digit_list[idx-1]:
            is_possible_num = 1  # at least one adjacent matching digits
            break
    for idx in range(1,6): # six digits
        if digit_list[idx] < digit_list[idx-1]:  # Going from left to right, the digits never decrease;
            is_possible_num = 0
            break
    if is_possible_num == 1:
        num_possible += 1

print( "The number of possible passwords are: " + str(num_possible))

#  Part Two
num_possible = 0
for puzzle_num in range(MinPuzzleInput, MaxPuzzleInput):
    digit_list = [int(digit) for digit in str(puzzle_num)]
    is_possible_num = 0
    for idx in range(1,6): # six digits
        if digit_list[idx] == digit_list[idx-1]:
            if idx == 1:
                if digit_list[idx + 1] != digit_list[idx]:
                    is_possible_num = 1  # at least one adjacent matching digits
                    break
            elif idx == 5:
                if digit_list[idx-2] != digit_list[idx]:
                    is_possible_num = 1  # at least one adjacent matching digits
                    break
            elif digit_list[idx-2] != digit_list[idx] and digit_list[idx+1] != digit_list[idx]:
                is_possible_num = 1  # at least one adjacent matching digits
                break

    for idx in range(1,6): # six digits
        if digit_list[idx] < digit_list[idx-1]:  # Going from left to right, the digits never decrease;
            is_possible_num = 0
            break
    if is_possible_num == 1:
        num_possible += 1

print( "The number of possible passwords are: " + str(num_possible))