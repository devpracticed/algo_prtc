#!/usr/local/bin/python3


def _is_palindrome(sStr: str):
    if not sStr:
        return False
    
    if sStr == sStr[::-1]:
        return True
    else:
        return False

def _palin_sub_recurse(sStr: str, sidx: int, eidx: int):
    if not sStr or len(sStr) == 0:
        return
    
    if sidx >= eidx:
        return

    if len(sStr) == 1:
        return sStr
    
    subStr = sStr[sidx:eidx]
    print(f"sStr: {sStr} : sidx: {sidx} : eidx: {eidx} : len: {len(sStr)} : subStr: {subStr}")

    if _is_palindrome(subStr):
        return subStr
    else:
        if eidx - sidx < 3:
            return ""
        fs = _palin_sub_recurse(sStr, sidx+1, eidx) 
        ss = _palin_sub_recurse(sStr, sidx, eidx-1)
        if len(fs) >= len(ss):
            return fs
        else:
            return ss


def longest_palindromic_substring(aStr: str):
    """
    https://leetcode.com/problems/longest-palindromic-substring/

    Time :
    Space:
    Note :
    """
    if not aStr:
        return 0
    if len(aStr) < 2:
        return aStr

    start_idx = 0 
    end_idx = len(aStr)

    return _palin_sub_recurse(aStr, start_idx, end_idx)

def run():
    # test_cases = ["", "a", "ab", "aa", "aba", "atba", "aaaa", "babad", "cbbd", "abcd", "a11a", "jhasdjhas", "abababccb", "abababccba", "abababccbaz"]
    
    # simple
    # test_cases = ["", "a", "ab", "aa", "bb", "aba"]
    
    # more 
    # test_cases = ["atba", "aaaa", "babad", "cbbd"]

    test_cases = ["babaddtattarrattatddetartrateedredividerb"]
    for t in test_cases:
        print(longest_palindromic_substring(t))
        print("-----------")

if __name__ == '__main__':
    run()

