# 1071. Greatest Common Divisor of Strings

def gcdOfStrings(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """

    if len(str2) > len(str1) :
        str1, str2 = str2, str1

    len1 = len(str1)
    len2 = len(str2)


    for i in range(len2, 0, -1):
        if str2[:i] * (len1//i) == str1 and str2[:i] * (len2//i) == str2 and len1 % i == 0 and len2 % i == 0:
            return str2[:i]

    return ''   
