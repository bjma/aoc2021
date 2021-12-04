filename = 'pt1.txt'
puzzle_input = [str(line).strip() for line in open(filename).readlines()]

def most_common_bit(bits):
    freq_map = {'0':0, '1':0}
    for bit in bits:
        freq_map[bit] += 1
    if freq_map['0'] == freq_map['1']:
        return '1'
    else:
        return max(freq_map, key=freq_map.get)

def least_common_bit(bits):
    freq_map = {'0':0, '1':0}
    for bit in bits:
        freq_map[bit] += 1
    
    if freq_map['0'] == freq_map['1']:
        return '0'
    else:
        return min(freq_map, key=freq_map.get)

# Invert bits
def invert_bits(bits):
    bit_str = ""
    for bit in bits:
        bit_str += '1' if bit == '0' else '0'
    return bit_str

def dec(bits):
    return int(bits, 2)

# Returns bits with the corresponding i-th bit
def filter_bit_array(arr, i, bit):
    return list(filter(lambda bits: bits[i] == bit, arr))

def find_oxygen_gen_rate(arr):
    remaining = arr
    i = 0
    while len(remaining) > 1:
        rot_arr = rotate_array(remaining)
        mcb = most_common_bit(rot_arr[i])
        remaining = filter_bit_array(remaining, i, mcb)
        i += 1
        if len(remaining) == 1:
            break
    return remaining[0]

def find_co2_scrub_rate(arr):
    remaining = arr
    i = 0
    while len(remaining) > 1:
        rot_arr = rotate_array(remaining)
        lcb = least_common_bit(rot_arr[i])
        remaining = filter_bit_array(remaining, i, lcb)
        i += 1
        if len(remaining) == 1:
            break
    return remaining[0]

# Creates an array of strings consisting of the i-th bits
def rotate_array(arr):
    n = len(arr[0])
    ret = []
    for i in range(n):
        s = ""
        for j in range(len(arr)):
            bits = arr[j]
            s += bits[i]
        ret.append(s)
    return ret
            
test = ["00100","11110","10110","10111","10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

if __name__ == "__main__":
    x = find_oxygen_gen_rate(puzzle_input)
    y = find_co2_scrub_rate(puzzle_input)

    ans = dec(x) * dec(y)
    print("Answer:", ans)
