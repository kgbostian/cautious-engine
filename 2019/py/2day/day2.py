import math 
import itertools

def read_file(filename):
   f = open(filename)
   return f.read()

def store_code(lines):
    program = []
    print(f"Lines before split: {lines}")
    progline = lines.split(',')
    while len(progline) > 4:
        program += progline[0:4]
        del progline[0:4]
    program = list(map(int, program))
    return program

def adjust_code(prog, one, two):
    prog[1] = one
    prog[2] = two
    return

def execute_code(SP, prog):
    #print(f"Executing command: {prog[SP:SP+4]}")
    if prog[SP] == 1:
        #Adding
        index1 = prog[SP+1]
        index2 = prog[SP+2]
        store = prog[SP+3]
        prog[store] = prog[index1] + prog[index2]
        #print(f"Adding: {index1} + {index2} = {prog[store]}")
    elif prog[SP] == 2:
        #Multipling
        index1 = prog[SP+1]
        index2 = prog[SP+2]
        store = prog[SP+3]
        prog[store] = prog[index1] * prog[index2]
        #print(f"Multiplying: {index1} * {index2} = {prog[store]}")
    elif prog[SP] == 99:
        print("Found end code.")
        SP = 0
        return 99
    else:
        print(f"Found an error with opcode {prog[SP]}")
    #print(f"Program is now: {prog}")
    return 0

def execute_prog(prog):
    SP = 0
    code = 0
    while code != 99:
        code = execute_code(SP, prog)
        SP += 4
    return prog[0]

def part2():
    lines = read_file("input.data")
    program = store_code(lines)
    for x, y in itertools.product(range(100), range(100)):
        new_code = program.copy()
        adjust_code(new_code, x, y)
        if execute_prog(new_code) == 19690720:
            print(f"Found the pair: {x}:{y}")
            answer = 100 * x + y
            print(f"Answer is: {answer}")
            return

def part1():
    lines = read_file("input2.data")
    code = store_code(lines)
    adjust_code(code, 12, 2)
    execute_prog(code)
    

part2()
