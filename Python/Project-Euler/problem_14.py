

def longest_colaltz_sequence():
    longest = 0
    longest_start = 0
    
    for n in range(1, 1000000):
        result = n
        sequence = []
        while result > 1:
            sequence.append(result)
            if result % 2 == 0:
                result = result / 2
            else:
                result = result * 3 + 1
        sequence.append(result)

        if len(sequence) > longest:
            longest = len(sequence)
            longest_start = n
    
    return longest_start

if __name__ == '__main__':
    func_result = longest_colaltz_sequence()
    print(func_result)
    input('Click Enter to End')