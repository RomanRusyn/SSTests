import itertools
import timeit
from operator import add, mul, sub, truediv

operations = add, mul, sub, truediv

number = '595347'


def checkio():
    def results(n):
        yield int(n)
        for i in range(1, len(n)):
            for x, y in itertools.product(results(n[:i]), results(n[i:])):
                yield from (op(x, y) for op in operations) if y else (x,)

    return 100 not in results(number)


print(timeit.timeit(checkio, number=10000))
# def get_groups(data):
#     for split in product([True, False], repeat=5):
#         split_index = [i + 1 for i in range(5) if split[i]]
#         ranges = zip([0] + split_index, split_index + [6])  # list of (start,stop)
#         yield [int(data[i:j]) for i, j in ranges]
# def checkio(data):
#     numbers_list = list(get_groups(data))
#     while numbers_list:
#         numbers = numbers_list.pop()
#         if len(numbers) == 1:
#             if numbers[0] == 100:
#                 return False
#         else:
#             for i in range(len(numbers) - 1):
#                 for func in [add, sub, mul, truediv]:
#                     if numbers[i + 1] == 0 and func == truediv:  # div by zero
#                         continue
#                     new_numbers = numbers[:]
#                     new_numbers[i:i + 2] = [func(numbers[i], numbers[i + 1])]
#                     numbers_list.append(new_numbers)
#     return True


# These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio('000000') == True, "All zeros"
#     assert checkio('707409') == True, "You can not transform it to 100"
#     assert checkio('595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
#     assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"
