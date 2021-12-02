filename = 'pt1.txt'
arr = [tuple(line.strip().split(" ")) for line in open(filename).readlines()]

def start_course(course):
    x, y = 0, 0
    for cmd in course:
        steps = int(cmd[1])
        if cmd[0] == 'forward':
            x += steps
        elif cmd[0] == 'down':
            y += steps
        elif cmd[0] == 'up':
            y -= steps
    return x * y

test = [('forward', 5), ('down', 5), ('forward', 8), ('up', 3), ('down', 8), ('forward', 2)]

if __name__ == "__main__":
    ans = start_course(arr)
    print(ans)
