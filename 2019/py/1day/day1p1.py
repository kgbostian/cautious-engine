import math 

def read_file(filename):
   f = open(filename)
   return f.readlines()

def calc_fuel(mass):
    fuel_needed = (math.floor(mass/3) - 2)
    if fuel_needed > 2:
        print(f"Recursing: {fuel_needed}")
        return fuel_needed + calc_fuel(fuel_needed)
    elif fuel_needed > 0:
        print(f"Last recurse: {fuel_needed}.")
        return fuel_needed
    else:
        return 0


def part1():
    lines = read_file("input.data")
    sum1 = 0
    for line in lines:
        print(f"Module Mass: {line}")
        mass = calc_fuel(int(line))
        print(f"Fuel needed: {mass}")
        sum1 += mass
    print(sum1)

part1()
