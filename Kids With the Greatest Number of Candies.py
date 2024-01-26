# 1431. Kids With the Greatest Number of Candies

def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """

    x = max(candies)
    l = []

    for i in candies :
        if i + extraCandies >= x:
            l.append(True)
        else :
            l.append(False)

    return l