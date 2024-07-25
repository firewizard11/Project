def large_sum(file_name):
    with open(file_name, 'r') as file_read:
        nums = []
        for line in file_read:
            nums.append(int(line))
    
    return sum(nums)

if __name__ == '__main__':
    file = 'large_num.txt'
    result = large_sum(file)
    print(str(result)[:10])