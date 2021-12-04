filename = 'pt1.txt'
arr = [str(line).strip() for line in open(filename).readlines()]

def most_common_bit(bits):
    freq_map = {'0':0, '1':0}
    for bit in bits:
        freq_map[bit] += 1
    return max(freq_map, key=freq_map.get)


# Invert bits
def invert_bits(bits):
    bit_str = ""
    for bit in bits:
        bit_str += '1' if bit == '0' else '0'
    return bit_str

def dec(bits):
    return int(bits, 2)

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
    arr = rotate_array(arr)

    # create gamma bits
    gamma_bits = ""
    for bits in arr:
        gamma_bits += most_common_bit(bits)
    
    epsilon_bits = invert_bits(gamma_bits)
    ans = dec(gamma_bits) * dec(epsilon_bits)
    print("Answer:", ans)
