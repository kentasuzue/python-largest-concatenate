# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest

from itertools import permutations

def largest_number(numbers):

    #get key to compare numbers
    #if number has too many digits, then throw away number's tail
    #if number has too few digits, then add tonumer's tail enough digits from the largest string of matching digits
    def sort_key(number, digits, maxsort):
        print("number", number, "digits", digits, "maxsort", maxsort)
        if len(str(number)) >= digits:
            print("long output", int(str(number)[:digits]))
            return int(str(number)[:digits])
        else:
            print("short output", int(str(number) + str(maxsort)[:digits - len(str(number))]))
            return int(str(number) + str(maxsort)[:digits - len(str(number))])
    """
    def get_next_number(presort_numbers, maxsort, digits):
        numsorted = sorted(presort_numbers, key=lambda x: sort_key(x, digits, maxsort), reverse=True)
        maxsort = int(str(numsorted[0])[:digits])
        num_maxsort = [x for x in numsorted if int(str(x)[:digits]) == maxsort]
        return num_maxsort, maxsort
    """

    def get_next_number(presort_numbers, maxsort, digits):
        while True:
            pair_presort = list(map(lambda x: [x, sort_key(x, digits, maxsort)], presort_numbers))
            print("pair_presort", pair_presort)
            numsorted = sorted(pair_presort, key=lambda x: x[1], reverse=True)
            #numsorted = sorted(presort_numbers, key=lambda x: sort_key(x, digits, maxsort), reverse=True)
            print("numsorted", numsorted)
            #maxsort = int(str(numsorted[0])[:digits])
            maxsort = numsorted[0][1]
            print("maxsort", maxsort)
            #keep only candidate numbers that match the largest prefix
            num_maxsort = [pair[0] for pair in numsorted if pair[1] == maxsort]
            print("num_maxsort", num_maxsort)
            presort_numbers = num_maxsort
            digits += 1
            #print('all(num == num_maxsort[0] for num in num_maxsort)', all(num == num_maxsort[0] for num in num_maxsort), \
            #[('num', num, 'num_maxsort[0]', num_maxsort[0], 'num == num_maxsort[0]', num == num_maxsort[0]) for num in num_maxsort] \
            #    )
            #if len(num_maxsort) == 1 or all(num == num_maxsort[0] for num in num_maxsort):
            #    return num_maxsort[0]

            digcharlist = list(''.join(map(str, num_maxsort)))
            # num_maxsort ==1 means only 1 number has maxsort as sort_key
            # all(num == num_maxsort[0] for num in num_maxsort)  means a tie among numbers
            # all(digcharlist[0] == x for x in digcharlist) means every digit the same in maxsort

            if len(num_maxsort) == 1 or all(num == num_maxsort[0] for num in num_maxsort) or \
                all(digcharlist[0] == x for x in digcharlist):
                return num_maxsort[0]

    presort_numbers = numbers.copy()
    maxsort = None
    digits = 1
    answer_numbers = []

    while presort_numbers:
        maxnumber = get_next_number(presort_numbers, maxsort, digits)
        presort_numbers.remove(maxnumber)
        answer_numbers.append(maxnumber)
        print("presort_numbers", presort_numbers)
        print("answer_numbers", answer_numbers)

    return int(''.join(map(str, answer_numbers)))

if __name__ == '__main__':
    #n = int(input())
    #input_numbers = input().split()
    #assert len(input_numbers) == n
    input_numbers = [2, 21, 23, 211, 213, 231, 232]

    print(largest_number(input_numbers))
