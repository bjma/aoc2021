filename = 'in.txt'

arr = [int(line) for line in open(filename).readlines()]

# Sliding window size
window_size = 3

cur_sum = sum(arr[0:window_size])
prev_sum = cur_sum

ans = 0
# Sliding window algorithm
# Source: https://stackoverflow.com/a/64111403/8316988
for i in range(1, len(arr)-window_size+1):
    prev_sum = cur_sum
    # remove first element of prev sum from window
    cur_sum -= arr[i-1]
    # last element window
    cur_sum += arr[i+window_size-1]

    if cur_sum > prev_sum:
        ans += 1
print("Answer:", ans)
