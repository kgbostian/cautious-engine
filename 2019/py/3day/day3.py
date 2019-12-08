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
    return all_points 

def manhattan_distance(R):
    md = []
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
    seg_pts = []
    if p1[0] == p2[0]:
        # X's are the same
        if p1[1] < p2[1]:
            #increasing num
            for x in range(p2[1] - p1[1]):
                seg_pts.append((p1[0], p1[1] + x))
        elif p1[1] > p2[1]:
            #decreasing num
            for x in range(p1[1] - p2[1]):
                seg_pts.append((p1[0], p1[1] - x))
    elif p1[1] == p2[1]:
        # Y's are the same
        if p1[0] < p2[0]:
            #increasing num
            for x in range(p2[0] - p1[0]):
                seg_pts.append((p1[0] + x, p1[1]))
        elif p1[0] > p2[0]:
            #decreasing num
            for x in range(p1[0] - p2[0]):
                seg_pts.append((p1[0] - x, p1[1]))
    return seg_pts            

def flatten(l1):
    out = []
    for x in l1:
        for y in x:
            out.append(y)
    return out

def find_all_pts(points):
    all_line_pts = []
    for pt in range(len(points) - 1):
       all_line_pts.append(find_pts_seg(points[pt], points[pt+1]))
    return all_line_pts

def find_intersection_pts(red, blue):
    x_pts = []
    for x in red:
        if blue.count(x) > 0:
            x_pts.append(x)

def distance(xpts, red_pts, blue_pts):
    all_dis = []
    for x in xpts:
        #Plus 2 for zero-based index on .index
        all_dis.append(red_pts.index(x) + blue_pts.index(x))
    all_dis.remove(0)
    print(all_dis)
    return min(all_dis)

def part1(filename="input.data"):
    lines = read_file(filename)
    red,blue = parse_lines(lines)
    all_red_points = find_all_pts(red)
    all_red_points = flatten(all_red_points)
    all_blue_points = find_all_pts(blue)
    all_blue_points = flatten(all_blue_points)
    red_set = set(all_red_points)
    blue_set = set(all_blue_points)
    x_pts = red_set.intersection(blue_set)
    md = distance(x_pts, all_red_points, all_blue_points)
    #set_md = set(md)
    #set_md.remove(0)
    print(md)

part1("input.data")
