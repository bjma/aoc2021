filename = 'in.txt'

arr = [int(line) for line in open(filename).readlines()]

cur = 0
prev = cur
ans = 0

for i in range(1, len(arr)):
    cur = int(arr[i])
    if cur > prev:
        ans += 1
    prev = cur
print("Answer:", ans)
