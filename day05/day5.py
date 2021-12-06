import math

filename = "in.txt"
in_lines = list(map(lambda x: x.replace(" ", "").strip().split("->"), open(filename).readlines()))

test_lines = list(map(lambda x: x.replace(" ", "").strip().split("->"), [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]))

def print_lines(lines):
    for line in lines:
        print(line)

def print_graph(graph):
    for i in range(len(graph)):
        print(graph[i])

def split_pairs(lp):
    pairs = [p.split(",") for p in lp]
    return [(int(p[0]), int(p[1])) for p in pairs]

def init_graph(lines):
    graph = []
    # iterate line pairs
    max_x = find_x(lines)
    max_y = find_y(lines)

    for i in range(max_y):
        row = []
        for j in range(max_x):
            row.append(0)
        graph.append(row)
    return graph

def find_x(lines):
    x = -1
    for lp in lines:
        p = split_pairs(lp)
        a = p[0]
        b = p[-1]
        x = max(max(a[0], b[0]), x)
    return x + 1

def find_y(lines):
    y = -1
    for lp in lines:
        p = split_pairs(lp)
        a = p[0]
        b = p[-1]
        y = max(max(a[-1], b[-1]), y)
    return y + 1

def get_angle(p1, p2):
    delta_y = p2[-1] - p1[-1]
    delta_x = p2[0] - p1[0]
    rad = math.atan2(delta_y, delta_x)
    return abs(math.degrees(rad))

def count_perpendicular_intersections(graph, lines):
    ret = 0
    # Mark graph
    for lp in lines:
        p = split_pairs(lp)
        x1, y1 = p[0][0], p[0][-1]
        x2, y2 = p[-1][0], p[-1][-1]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                #print("Marked", "graph[" + str(y) + "][" + str(x1) + "]")
                graph[y][x1] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                #print("Marked", "graph[" + str(y1) + "][" + str(x) + "]")
                graph[y1][x] += 1
    # Count intersections
    for y in range(len(graph)):
        for x in range(len(graph[y])):
            if graph[y][x] >= 2:
                ret += 1
    return ret

def count_intersections(graph, lines):
    ret = 0
    # Mark graph
    for lp in lines:
        p = split_pairs(lp)
        x1, y1 = p[0][0], p[0][-1]
        x2, y2 = p[-1][0], p[-1][-1]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                graph[y][x1] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                graph[y1][x] += 1
        else:
            angle = get_angle(p[0], p[-1])
            # Only mark graph if angle formed is 45 deg
            if angle % 45 == 0:
                # Determine whether or not to decrement or increment
                delt_y = -1 if y1 > y2 else 1
                delt_x = -1 if x1 > x2 else 1

                # Start at first pair
                x = x1
                y = y1
                while (y >= min(y1, y2) and y <= max(y1, y2)) or (x >= min(x1, x2) and x <= max(x1, x2)):
                    graph[y][x] += 1
                    x += delt_x
                    y += delt_y

    # Count intersections
    for y in range(len(graph)):
        for x in range(len(graph[y])):
            if graph[y][x] >= 2:
                ret += 1
    return ret

if __name__ == "__main__":
    # Part 1
    graph = init_graph(in_lines)
    ans = count_perpendicular_intersections(graph, in_lines)
    print("Part 1:", ans)

    # Part 2
    graph = init_graph(in_lines)
    ans = count_intersections(graph, in_lines)
    print("Part 2:", ans)
