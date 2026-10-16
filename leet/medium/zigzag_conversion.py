#!/usr/local/bin/python3

def zigzag_conversion(s: str, numRows: int) -> str:
    """
    https://leetcode.com/problems/zigzag-conversion/

    Time :
    Space:
    Note :
    """
    if not s or len(s) < 2:
        return s

    ret_arr = []
    col = 0
    row = 0

    in_col = col
    mid_col = col - 2
    
    "P A Y P A L I S H I  R  I  N  G"
    "1 2 3 4 5 6 7 8 9 10 11 12 13 14"
    "P A H N A P L S I I G Y I R"
    "1 5 9 13:" - prev_point + row + (row - 2)
    
    
    # for c in s:
    #     # print("hello")
    #     if len(ret_arr) == col:
    #         ret_arr.append([])
    #     if r < numRows:


def run():
    pass


if __name__ == '__main__':
    run()

