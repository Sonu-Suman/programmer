# Common and uncommon character letter in two string

import string


letters = string.ascii_lowercase
CHARACTER_HASH = dict(zip(letters, [0] * len(letters)))
print(CHARACTER_HASH)


# This method will mark all the letters occurring in 'text_a'
def mapLettersToHash(text_a):
    for char in text_a:
        if char in CHARACTER_HASH.keys():
            CHARACTER_HASH[char] += 1
            # print(CHARACTER_HASH)


# This method will count the letters present in 'text_b', also found in 'text_a'
# These will be characters whose frequency in HASH is greater than zero
def computeCommonLetters(text_b):
    common_letters = 0
    for char in text_b:
        if CHARACTER_HASH[char] > 0:
            common_letters += 1
    return common_letters


# Now we derive how many uncommon letters are present,
# This is done by subtracting twice the count of common letters
# from the total length of both the strings
def computeUncommonLetters(text_a, text_b, common_letters):
    return abs(len(text_a) + len(text_b) - (2 * common_letters))


if __name__ == "__main__":
    text_1 = "hello"
    text_2 = "billion"

    mapLettersToHash(text_1)
    common = computeCommonLetters(text_2)
    result = computeUncommonLetters(text_1, text_2, common)
    print(result)
    print(common)