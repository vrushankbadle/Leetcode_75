# 1768. Merge Strings Alternately

def mergeAlternately(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        l2 = []
        l1 = sorted([word1, word2], key=len)
        w_min = l1[0]
        w_max = l1[1]

        for idx in range(len(w_max)) :
            if idx + 1 > len(w_min) :
                l2.extend(w_max[idx:])
                break
            else :
                l2.append(word1[idx])
                l2.append(word2[idx])

        return ''.join(l2)    
        