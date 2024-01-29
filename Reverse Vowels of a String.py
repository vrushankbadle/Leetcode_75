# 345. Reverse Vowels of a String

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    s = list(s)
    letters = []
    indexes = []

    for idx, letter in enumerate(s):

        if letter.lower() in 'aeiou':
            letters.append(letter)
            indexes.append(idx)

    for i, letter in enumerate(letters[::-1]):
        s[indexes[i]] = letter

    return ''.join(s)