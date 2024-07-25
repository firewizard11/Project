def smallest_multiple(n):

    count = n

    while True:
    
        for i in range(1, n + 1):
            if count % i != 0:
                break
        else:
            return count
        
        count += 1

    
if __name__ == '__main__':
    print(smallest_multiple(20))
    input('Click Enter to End')