def digit_bit(number):
    bit = 1
    test = 1
    divisor = 10
    while test >= 1:
        test = number // divisor
        if test >= 1:
            bit = bit + 1
            divisor = divisor * 10
    return bit


def list_number_digit_bit(input_list):
    result = [digit_bit(a) for a in input_list]
    return result


def lexicon_order(input_list):
    digit_bit_list = list_number_digit_bit(input_list)
    max_bit = max(digit_bit_list)
    alpha = 1 / max_bit
    dict_of_number = {}
    for a in input_list:
        if digit_bit(a) == max_bit:
            dict_of_number[a] = a
        else:
            bit = digit_bit(a)
            new_digit = (a * 10 ** (max_bit - bit)) - 0.5 * alpha * (max_bit - bit)
            dict_of_number[new_digit] = a
    key_of_dict_of_number = list(dict_of_number.keys())
    key_of_dict_of_number.sort()
    lexicon_order_number = [dict_of_number[i] for i in key_of_dict_of_number]
    return lexicon_order_number


def find_the_number(n, k):
    number_list = list(range(1, n + 1))
    lexicon_order_number = lexicon_order(number_list)
    result = lexicon_order_number[k - 1]
    print('The lexicographical order is: ', lexicon_order_number)
    print('so the ', k, 'th smallest number is:', result)
    return result


# print(lexicon_order(range(130)))
# exit()
# find_the_number(n=130, k=5)
# exit()

for a in range(10):
    print(a)
    r = find_the_number(n=13, k=a)
    print(r)
