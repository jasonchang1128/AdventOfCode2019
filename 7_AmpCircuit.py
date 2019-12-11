# Day 7 of Advent of Code.
# Part 1 - Running IO to amp circuit.

def opcode2_mult(parlist, pos1, pos2, outpos):
    parlist[outpos] = parlist[pos1] * parlist[pos2]

def val_from_parameter_mode(parameter_mode, desired_list, param_position):
    if parameter_mode == 1:  # Immediate Mode.
        return desired_list[param_position]
    elif parameter_mode == 0:  # Position Mode.
        return desired_list[desired_list[param_position]]

def get_diag_output(instruction_list, *inputs):
    input_num = 0
    CurPos = 0
    while instruction_list[CurPos] != 99:
        cur_opcode_padded = str(instruction_list[CurPos]).zfill(5)
        opcode_list = [int(digit) for digit in cur_opcode_padded]  # Turn the opcode into a list of digits.
        actual_opcode = int(str(opcode_list[3]) + str(opcode_list[4]))  #Concat the actual opcode digits.
        if actual_opcode == 1:  # Add Opcode, read, read, Write.
            param1 = val_from_parameter_mode(opcode_list[2], instruction_list, CurPos+1)
            param2 = val_from_parameter_mode(opcode_list[1], instruction_list, CurPos+2)
            instruction_list[instruction_list[CurPos + 3]] = param1 + param2  # always position mode.
            CurPos += 4
        elif actual_opcode == 2:  # Mult opcode, read, read, write.
            param1 = val_from_parameter_mode(opcode_list[2], instruction_list, CurPos+1)
            param2 = val_from_parameter_mode(opcode_list[1], instruction_list, CurPos+2)
            instruction_list[instruction_list[CurPos + 3]] = param1 * param2  # always position mode.
            CurPos += 4
        elif actual_opcode == 3:  # Set param pos to input.
            instruction_list[instruction_list[CurPos+1]] = inputs[input_num]  # always position mode.
            input_num += 1
            CurPos += 2
        elif actual_opcode == 4:
            param1 = val_from_parameter_mode(opcode_list[2], instruction_list, CurPos+1)
            output = param1
            CurPos += 2
        elif actual_opcode == 5:  # jump if true: opcode, non-zero, jump-pos
            param1 = val_from_parameter_mode(opcode_list[2], instruction_list, CurPos+1)
            param2 = val_from_parameter_mode(opcode_list[1], instruction_list, CurPos+2)
            if param1 != 0:
                CurPos = param2
            else:
                CurPos += 3
        elif actual_opcode == 6:  # jump if false: opcode, zero, jump-pos
            param1 = val_from_parameter_mode(opcode_list[2], instruction_list, CurPos+1)
            param2 = val_from_parameter_mode(opcode_list[1], instruction_list, CurPos+2)
            if param1 == 0:
                CurPos = param2
            else:
                CurPos += 3
        elif actual_opcode == 7:  # less than: opcode, param1 < param2, 1 or 0
            param1 = val_from_parameter_mode(opcode_list[2], instruction_list, CurPos+1)
            param2 = val_from_parameter_mode(opcode_list[1], instruction_list, CurPos+2)
            if param1 < param2:
                instruction_list[instruction_list[CurPos + 3]] = 1
            else:
                instruction_list[instruction_list[CurPos + 3]] = 0
            CurPos += 4
        elif actual_opcode == 8:  # equals than: opcode, param1 == param2, 1 or 0
            param1 = val_from_parameter_mode(opcode_list[2], instruction_list, CurPos+1)
            param2 = val_from_parameter_mode(opcode_list[1], instruction_list, CurPos+2)
            if param1 == param2:
                instruction_list[instruction_list[CurPos + 3]] = 1
            else:
                instruction_list[instruction_list[CurPos + 3]] = 0
            CurPos += 4
        elif actual_opcode == 99:
            print("Finished")
            break
        else:
            print("Error")
            break
    return output


def calc_amp_out(instruct_list, phase_setting):
    cur_input = 0
    for phase_num in phase_setting:
        CurList = instruct_list.copy()
        if phase_num == phase_setting[-1]:  # Is it the last element?
            return get_diag_output(CurList, phase_num, cur_input)
        else:
            cur_input = get_diag_output(CurList, phase_num, cur_input)

Instruction_Input = [3,8,1001,8,10,8,105,1,0,0,21,38,55,68,93,118,199,280,361,442,99999,3,9,1002,9,2,9,101,5,9,9,102,4,9,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,4,9,4,9,99,3,9,101,4,9,9,102,3,9,9,4,9,99,3,9,102,2,9,9,101,4,9,9,102,2,9,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,1002,9,2,9,1001,9,2,9,1002,9,5,9,1001,9,2,9,1002,9,4,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99]

ListOfAllNumbers = []
for i in range(43211):
    ListOfAllNumbers.append(list(str(i).zfill(5)))

AllPhasesSeq = []
for cur_num in ListOfAllNumbers:
    if int(cur_num[0]) < 5 and int(cur_num[1]) < 5 and int(cur_num[2]) < 5 and int(cur_num[3]) < 5 and int(cur_num[4]) < 5:
        if len(cur_num) == len(set(cur_num)):
            AllPhasesSeq.append([int(x) for x in cur_num])

FinalOutSignals = []
for phase_seq in AllPhasesSeq:
    FinalOutSignals.append(calc_amp_out(Instruction_Input,phase_seq))

# Day 7 Part 1 Max Output Signal.
print(max(FinalOutSignals))

# Day 7 Part 2


def get_amp_out(instruction_list, CurPos):
    while instruction_list[CurPos] != 99:
        cur_opcode_padded = str(instruction_list[CurPos]).zfill(5)
        opcode_list = [int(digit) for digit in cur_opcode_padded]  # Turn the opcode into a list of digits.
        actual_opcode = int(str(opcode_list[3]) + str(opcode_list[4]))  #Concat the actual opcode digits.
        if actual_opcode == 1:  # Add Opcode, read, read, Write.
            param1 = val_from_parameter_mode(opcode_list[2], instruction_list, CurPos+1)
            param2 = val_from_parameter_mode(opcode_list[1], instruction_list, CurPos+2)
            instruction_list[instruction_list[CurPos + 3]] = param1 + param2  # always position mode.
            CurPos += 4
        elif actual_opcode == 2:  # Mult opcode, read, read, write.
            param1 = val_from_parameter_mode(opcode_list[2], instruction_list, CurPos+1)
            param2 = val_from_parameter_mode(opcode_list[1], instruction_list, CurPos+2)
            instruction_list[instruction_list[CurPos + 3]] = param1 * param2  # always position mode.
            CurPos += 4
        elif actual_opcode == 3:  # Set param pos to input.
            cur_input = yield
            instruction_list[instruction_list[CurPos+1]] = cur_input  # always position mode.
            CurPos += 2
        elif actual_opcode == 4:
            param1 = val_from_parameter_mode(opcode_list[2], instruction_list, CurPos+1)
            output = param1
            yield output
            CurPos += 2
        elif actual_opcode == 5:  # jump if true: opcode, non-zero, jump-pos
            param1 = val_from_parameter_mode(opcode_list[2], instruction_list, CurPos+1)
            param2 = val_from_parameter_mode(opcode_list[1], instruction_list, CurPos+2)
            if param1 != 0:
                CurPos = param2
            else:
                CurPos += 3
        elif actual_opcode == 6:  # jump if false: opcode, zero, jump-pos
            param1 = val_from_parameter_mode(opcode_list[2], instruction_list, CurPos+1)
            param2 = val_from_parameter_mode(opcode_list[1], instruction_list, CurPos+2)
            if param1 == 0:
                CurPos = param2
            else:
                CurPos += 3
        elif actual_opcode == 7:  # less than: opcode, param1 < param2, 1 or 0
            param1 = val_from_parameter_mode(opcode_list[2], instruction_list, CurPos+1)
            param2 = val_from_parameter_mode(opcode_list[1], instruction_list, CurPos+2)
            if param1 < param2:
                instruction_list[instruction_list[CurPos + 3]] = 1
            else:
                instruction_list[instruction_list[CurPos + 3]] = 0
            CurPos += 4
        elif actual_opcode == 8:  # equals than: opcode, param1 == param2, 1 or 0
            param1 = val_from_parameter_mode(opcode_list[2], instruction_list, CurPos+1)
            param2 = val_from_parameter_mode(opcode_list[1], instruction_list, CurPos+2)
            if param1 == param2:
                instruction_list[instruction_list[CurPos + 3]] = 1
            else:
                instruction_list[instruction_list[CurPos + 3]] = 0
            CurPos += 4
        elif actual_opcode == 99:
            print("Finished")
            break
        else:
            print("Error")
            break
    return output


def calc_feedback_out(Instruction_Input, Phase_Seq):
    AmpA_instruct = Instruction_Input.copy()
    AmpB_instruct = Instruction_Input.copy()
    AmpC_instruct = Instruction_Input.copy()
    AmpD_instruct = Instruction_Input.copy()
    AmpE_instruct = Instruction_Input.copy()
    AmpA_Pos = 0
    AmpB_Pos = 0
    AmpC_Pos = 0
    AmpD_Pos = 0
    AmpE_Pos = 0

    AmpA = get_amp_out(AmpA_instruct, AmpA_Pos)
    AmpB = get_amp_out(AmpB_instruct, AmpB_Pos)
    AmpC = get_amp_out(AmpC_instruct, AmpC_Pos)
    AmpD = get_amp_out(AmpD_instruct, AmpD_Pos)
    AmpE = get_amp_out(AmpE_instruct, AmpE_Pos)
    next(AmpA)
    AmpA.send(Phase_Seq[0])
    next(AmpB)
    AmpB.send(Phase_Seq[1])
    next(AmpC)
    AmpC.send(Phase_Seq[2])
    next(AmpD)
    AmpD.send(Phase_Seq[3])
    next(AmpE)
    AmpE.send(Phase_Seq[4])

    AmpE_out = 0
    output_done = 0
    while output_done == 0:
        try:
            AmpA_out = AmpA.send(AmpE_out)
            next(AmpA)
        except StopIteration:
            pass

        try:
            AmpB_out = AmpB.send(AmpA_out)
            next(AmpB)
        except StopIteration:
            pass

        try:
            AmpC_out = AmpC.send(AmpB_out)
            next(AmpC)
        except StopIteration:
            pass

        try:
            AmpD_out = AmpD.send(AmpC_out)
            next(AmpD)
        except StopIteration:
            pass

        try:
            AmpE_out = AmpE.send(AmpD_out)
            next(AmpE)
        except StopIteration as final_out:
            return int(str(final_out))

Instruction_Input = [3,8,1001,8,10,8,105,1,0,0,21,38,55,68,93,118,199,280,361,442,99999,3,9,1002,9,2,9,101,5,9,9,102,4,9,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,4,9,4,9,99,3,9,101,4,9,9,102,3,9,9,4,9,99,3,9,102,2,9,9,101,4,9,9,102,2,9,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,1002,9,2,9,1001,9,2,9,1002,9,5,9,1001,9,2,9,1002,9,4,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99]

ListOfAllNumbers = []
for i in range(56789, 98766):
    ListOfAllNumbers.append(list(str(i).zfill(5)))

AllPhasesSeq = []
for cur_num in ListOfAllNumbers:
    if int(cur_num[0]) > 4 and int(cur_num[1]) > 4 and int(cur_num[2]) > 4 and int(cur_num[3]) > 4 and int(cur_num[4]) > 4:
        if len(cur_num) == len(set(cur_num)):
            AllPhasesSeq.append([int(x) for x in cur_num])

FinalOutSignals = []
for phase_seq in AllPhasesSeq:
    FinalOutSignals.append(calc_feedback_out(Instruction_Input, phase_seq))

# Day 7 Part 2.
print(max(FinalOutSignals))
