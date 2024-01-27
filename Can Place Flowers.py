# 605. Can Place Flowers

def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    place  = True

    for i in range(n):
        place = False
        for idx in range(len(flowerbed)):
            if flowerbed[idx] == 0 and flowerbed[idx - 1 : idx] != [1] and flowerbed[ idx + 1: idx + 2] !=[1] :
                    place = True
                    flowerbed[idx] = 1
                    flowerbed = flowerbed[idx:]
                    break

    return place