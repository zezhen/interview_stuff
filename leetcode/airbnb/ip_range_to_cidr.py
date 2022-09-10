import math

def ip_range_to_cidr(start_ip, range, multiple=False):

    def ip_to_number(ip):
        arr = ip.split('.')
        return (int(arr[0]) << 24) + (int(arr[1]) << 16) + (int(arr[2]) << 8) + int(arr[3])

    def number_to_ip(number):
        return '.'.join(map(str,[(number >> 24),((number & 0x00FFFFFF) >> 16),((number & 0x0000FFFF) >> 8),(number & 0x000000FF)]))

    start = ip_to_number(start_ip)
    end = start + range - 1
    print end

    ans = []
    while start <= end:
        lowestOneOffset = int(math.log(start & - start, 2))
        rangeOffset = int(math.floor(math.log(end - start + 1, 2)))
        
        offset = min(lowestOneOffset, rangeOffset)
        
        ans.append(number_to_ip(start) + '/' + str(32-offset))

        start += int(math.pow(2, offset))

    return ans

print ip_range_to_cidr('0.0.0.111', 10)
print ip_range_to_cidr('0.0.0.111', 20)

# 111 0b1101111
# 112 0b1110000
# 113 0b1110001
# 114 0b1110010
# 115 0b1110011
# 116 0b1110100
# 117 0b1110101
# 118 0b1110110
# 119 0b1110111
# 120 0b1111000