#https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/

"""
1. microspectrophotometries is the only word with a letter sum of 317. Find the only word with a letter sum of 319.
2. How many words have an odd letter sum?
3. There are 1921 words with a letter sum of 100, making it the second most common letter sum. What letter sum is most common, and how many words have it?
4. zyzzyva and biodegradabilities have the same letter sum as each other (151), and their lengths differ by 11 letters. Find the other pair of words with the same letter sum whose lengths differ by 11 letters.
5. cytotoxicity and unreservedness have the same letter sum as each other (188), and they have no letters in common. Find a pair of words that have no letters in common, and that have the same letter sum, which is larger than 188. (There are two such pairs, and one word appears in both pairs.)
6. The list of word { geographically, eavesdropper, woodworker, oxymorons } contains 4 words. 
Each word in the list has both a different number of letters, and a different letter sum. The list is sorted both in descending order of word length, and ascending order of letter sum. What's the longest such list you can find?
"""
from challenge399 import lettersum

def read_file(file_name: str) -> list:
    strings = []
    with open(file_name, 'r') as file_read:
        for line in file_read:
            strings.append(line.strip())
    
    return strings

if __name__ == '__main__':
    strings = read_file('enable1.txt')
    
    #Pre Calculating Sums
    sums = [lettersum(string) for string in strings]

    #Questions
    print(f'1. {strings[sums.index(319)]}')
    
    total = 0
    for i in range(len(sums)):
        if sums[i] % 2 != 0:
            total += 1
    print(f'2. {total}')

    