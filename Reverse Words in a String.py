# 151. Reverse Words in a String

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    
    return ' '.join(s.split()[::-1])