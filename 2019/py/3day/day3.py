import math 
import itertools

def read_file(filename):
   f = open(filename)
   return f.readlines()

def calc_point(direction, distance, point):
    if direction == 'U':
        #Move Up
        point[1] += distance
    elif direction == 'D':
        #Move Down
        point[1] -= distance
    elif direction == 'L':
        #Move Left
        point[0] -= distance
    elif direction == 'R':
        #Move Right
        point[0] += distance
    else:
        raise Exception
    new_point = point.copy()
    #print(f"New Point: {new_point}")
    return new_point

def convert_to_points(movements):
    #starting point is 0,0
    point = [0,0]
    actions = movements.split(',')
    all_points = []
    all_points.append(point.copy())
    for action in actions:
        direction = action[0]
        distance = int(action[1:])
        new_point = calc_point(direction, distance, point)
        all_points.append(new_point)
    #print(f"Printing all points: {all_points}")
    return all_points 

def manhattan_distance(R):
    md = []
    #print(f"R is: {R}")
    if R == None:
        return "Failure to find MD"
    for x in R:
        md.append(abs(x[0]) + abs(x[1]))
    return md
    
def parse_lines(lines):
    red = convert_to_points(lines[0])
    blue = convert_to_points(lines[1])
    return red, blue

def find_pts_seg(p1, p2):
    #print(f"Two pts are: {p1}, {p2}")
    seg_pts = []
    if p1[0] == p2[0]:
        # X's are the same
        if p1[1] < p2[1]:
            #increasing num
            for x in range(p2[1] - p1[1]):
                seg_pts.append((p1[0], p1[1] + x))
            #print(f"{seg_pts}")    
        elif p1[1] > p2[1]:
            #decreasing num
            for x in range(p1[1] - p2[1]):
                seg_pts.append((p1[0], p1[1] - x))
            #print(f"{seg_pts}")
    elif p1[1] == p2[1]:
        # Y's are the same
        if p1[0] < p2[0]:
            #increasing num
            for x in range(p2[0] - p1[0]):
                seg_pts.append((p1[0] + x, p1[1]))
            #print(f"{seg_pts}")
        elif p1[0] > p2[0]:
            #decreasing num
            for x in range(p1[0] - p2[0]):
                seg_pts.append((p1[0] - x, p1[1]))
            #print(f"{seg_pts}")
    return seg_pts            

def flatten(l1):
    # print()
    # print()
    # print(f"about to flatten: {l1}")
    # print()
    # print()
    out = []
    for x in l1:
        #print(f"Printing x: {x}")
        for y in x:
            out.append(y)
    #print(out)
    return out

def find_all_pts(points):
    all_line_pts = []
    for pt in range(len(points) - 1):
       all_line_pts.append(find_pts_seg(points[pt], points[pt+1]))
    return all_line_pts
    #print(f"{all_line_pts}")    

def find_intersection_pts(red, blue):
    #print(red)
    #print(blue)
    x_pts = []
    for x in red:
        #print(f"Testing pt: {x}")
        if blue.count(x) > 0:
            x_pts.append(x)
            #print(f"Found intersection: {x}")

def part1(filename="input.data"):
    lines = read_file(filename)
    red,blue = parse_lines(lines)
    all_red_points = find_all_pts(red)
    all_red_points = flatten(all_red_points)
    #print(f"All Red Points: {all_red_points}")
    all_blue_points = find_all_pts(blue)
    all_blue_points = flatten(all_blue_points)
    red_set = set(all_red_points)
    blue_set = set(all_blue_points)
    x_pts = red_set.intersection(blue_set)
    #print(f"Using set for intersections: {x_pts}")
    md = manhattan_distance(x_pts)
    set_md = set(md)
    set_md.remove(0)
    print(set_md)
    print(min(set_md))
    #x_pts = find_intersection_pts(all_red_points,all_blue_points) 
    #print(manhattan_distance(x_pts))
    
    #print(len(all_red_points))
    #print(len(all_blue_points))
    #print(f"Minimum distance = {min(md)}")

part1("input.data")
