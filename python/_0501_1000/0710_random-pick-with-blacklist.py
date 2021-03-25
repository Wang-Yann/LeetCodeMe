#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 14:06:36
# @Last Modified : 2020-05-02 14:06:36
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个包含 [0，n ) 中独特的整数的黑名单 B，写一个函数从 [ 0，n ) 中返回一个不在 B 中的随机整数。
#
#  对它进行优化使其尽量少调用系统方法 Math.random() 。
#
#  提示:
#
#
#  1 <= N <= 1000000000
#  0 <= B.length < min(100000, N)
#  [0, N) 不包含 N，详细参见 interval notation 。
#
#
#  示例 1:
#
#
# 输入:
# ["Solution","pick","pick","pick"]
# [[1,[]],[],[],[]]
# 输出: [null,0,0,0]
#
#
#  示例 2:
#
#
# 输入:
# ["Solution","pick","pick","pick"]
# [[2,[]],[],[],[]]
# 输出: [null,1,1,1]
#
#
#  示例 3:
#
#
# 输入:
# ["Solution","pick","pick","pick"]
# [[3,[1]],[],[],[]]
# Output: [null,0,0,2]
#
#
#  示例 4:
#
#
# 输入:
# ["Solution","pick","pick","pick"]
# [[4,[2]],[],[],[]]
# 输出: [null,1,3,1]
#
#
#  输入语法说明：
#
#  输入是两个列表：调用成员函数名和调用的参数。Solution的构造函数有两个参数，N 和黑名单 B。pick 没有参数，输入参数是一个列表，即使参数为空，
# 也会输入一个 [] 空列表。
#  Related Topics 排序 哈希表 二分查找 Random
#  👍 36 👎 0

"""
import pytest
import random
from typing import List


class Solution0:

    def __init__(self, N: int, blacklist: List[int]):
        self.__n = N - len(blacklist)
        blacklist.sort()
        self.__blacklist = blacklist

    def pick(self) -> int:
        index = random.randint(0, self.__n - 1)
        l, r = 0, len(self.__blacklist) - 1
        while l <= r:
            mid = (l + r) >> 1
            if index + mid < self.__blacklist[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return index + l


class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.__n = N - len(blacklist)
        self.__lookup = {}
        white = iter(set(range(self.__n, N)) - set(blacklist))
        for black in blacklist:
            if black < self.__n:
                self.__lookup[black] = next(white)

    def pick(self):
        """
        :rtype: int
        """
        index = random.randint(0, self.__n - 1)
        return self.__lookup[index] if index in self.__lookup else index


@pytest.mark.parametrize("CLS", [Solution, Solution0])
def test_solution(CLS):
    obj = CLS(4, [2])
    ops_list = ["Solution", "pick", "pick", "pick"]
    args_list = [[4, [2]], [], [], []]

    for i in range(1, len(ops_list)):
        method, args = ops_list[i], args_list[i]
        print(getattr(obj, method)(*args))


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
