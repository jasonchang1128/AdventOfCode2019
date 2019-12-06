# Day 5 of Advent of Code.
# Part 1 - Adding 2 new op codes and adding with parameter modes.

def opcode2_mult(parlist, pos1, pos2, outpos):
    parlist[outpos] = parlist[pos1] * parlist[pos2]

def val_from_parameter_mode(parameter_mode, desired_list, param_position):
    if parameter_mode == 1:
        return desired_list[param_position]
    elif parameter_mode == 0:
        return desired_list[desired_list[param_position]]

def get_diag_output(instruction_list, input):
    CurPos = 0
    while instruction_list[CurPos] != 99:
        cur_opcode_padded = str(instruction_list[CurPos]).zfill(5)
        opcode_list = [int(digit) for digit in cur_opcode_padded]  # Turn the opcode into a list of digits.
        actual_opcode = int(str(opcode_list[3]) + str(opcode_list[4]))  #Concat the actual opcode digits.
        if actual_opcode == 1:  # Add Opcode, read, read, Write.
            param1 = val_from_parameter_mode(opcode_list[2], instruction_list, CurPos+1)
            param2 = val_from_parameter_mode(opcode_list[1], instruction_list, CurPos+2)
            instruction_list[instruction_list[CurPos + 3]] = param1 + param2
            CurPos += 4
        elif actual_opcode == 2:  # Mult opcode, read, read, write.
            param1 = val_from_parameter_mode(opcode_list[2], instruction_list, CurPos+1)
            param2 = val_from_parameter_mode(opcode_list[1], instruction_list, CurPos+2)
            instruction_list[instruction_list[CurPos + 3]] = param1 * param2
            CurPos += 4
        elif actual_opcode == 3:  # Set param pos to input.
            instruction_list[instruction_list[CurPos+1]] = input  # always immediate mode cause write.
            CurPos += 2
        elif actual_opcode == 4:
            param1 = val_from_parameter_mode(opcode_list[2], instruction_list, CurPos+1)
            output = param1
            CurPos += 2
        elif actual_opcode == 99:
            print("Finished")
            break
        else:
            print("Error")
            break
    return output


MemList = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,90,64,225,1101,15,56,225,1,14,153,224,101,-147,224,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,2,162,188,224,101,-2014,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1001,18,81,224,1001,224,-137,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1102,16,16,224,101,-256,224,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,101,48,217,224,1001,224,-125,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,1002,158,22,224,1001,224,-1540,224,4,224,1002,223,8,223,101,2,224,224,1,223,224,223,1101,83,31,225,1101,56,70,225,1101,13,38,225,102,36,192,224,1001,224,-3312,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1102,75,53,225,1101,14,92,225,1101,7,66,224,101,-73,224,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1101,77,60,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,226,677,224,1002,223,2,223,1005,224,329,1001,223,1,223,1007,226,677,224,1002,223,2,223,1005,224,344,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,359,101,1,223,223,7,226,226,224,102,2,223,223,1005,224,374,101,1,223,223,8,677,677,224,1002,223,2,223,1005,224,389,1001,223,1,223,107,677,677,224,102,2,223,223,1006,224,404,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,419,1001,223,1,223,1008,226,226,224,1002,223,2,223,1005,224,434,1001,223,1,223,7,677,226,224,102,2,223,223,1006,224,449,1001,223,1,223,1107,226,226,224,1002,223,2,223,1005,224,464,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,479,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,494,1001,223,1,223,1107,226,677,224,1002,223,2,223,1005,224,509,101,1,223,223,1007,226,226,224,1002,223,2,223,1006,224,524,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1108,677,677,224,1002,223,2,223,1005,224,554,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,569,1001,223,1,223,8,226,677,224,102,2,223,223,1005,224,584,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,599,1001,223,1,223,108,677,677,224,102,2,223,223,1006,224,614,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,629,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,644,101,1,223,223,107,677,226,224,1002,223,2,223,1005,224,659,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226]

CurList = MemList.copy()

cur_input = 1
# Part 1 Answer.
print( get_diag_output(CurList, cur_input) )
