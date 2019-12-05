import math


def opcode1_add(parlist, pos1, pos2, outpos):
    parlist[outpos] = parlist[pos1] + parlist[pos2]


def opcode2_mult(parlist, pos1, pos2, outpos):
    parlist[outpos] = parlist[pos1] * parlist[pos2]


def get_memory_output(instruction_list):
    CurPos = 0
    while instruction_list[CurPos] != 99:
        if instruction_list[CurPos] == 1:
            opcode1_add(instruction_list, instruction_list[CurPos + 1], instruction_list[CurPos + 2], instruction_list[CurPos + 3])
            CurPos += 4
        elif instruction_list[CurPos] == 2:
            opcode2_mult(instruction_list, instruction_list[CurPos + 1], instruction_list[CurPos + 2], instruction_list[CurPos + 3])
            CurPos += 4
        elif instruction_list[CurPos] == 99:
            print("Finished")
            break
        else:
            print("Error")
            break
    return instruction_list[0]


MemList = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,6,23,2,13,23,27,1,27,13,31,1,9,31,35,1,35,9,39,1,39,5,43,2,6,43,47,1,47,6,51,2,51,9,55,2,55,13,59,1,59,6,63,1,10,63,67,2,67,9,71,2,6,71,75,1,75,5,79,2,79,10,83,1,5,83,87,2,9,87,91,1,5,91,95,2,13,95,99,1,99,10,103,1,103,2,107,1,107,6,0,99,2,14,0,0]

CurList = MemList.copy()
CurList[1] = 12
CurList[2] = 2
print(get_memory_output(CurList))

for noun in range(100):
    for verb in range(100):
        TestList = MemList.copy()
        #print(noun)
        #print(verb)
        TestList[1] = noun
        TestList[2] = verb
        if get_memory_output(TestList) == 19690720:
            print(noun)
            print(verb)

