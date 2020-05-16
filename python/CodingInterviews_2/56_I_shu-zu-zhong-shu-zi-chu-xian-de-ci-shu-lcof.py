#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-28 10:24:32
# @Last Modified : 2020-04-28 10:24:32
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List


class Solution:
    def singleNumbersO(self, nums: List[int]) -> List[int]:
        def isBit1(num, indexBit):
            num >>= indexBit
            return num & 0b1

        def findFirstBitIs1(num):
            indexBit = 0
            while num & 0b1 == 0:
                num >>= 1
                indexBit += 1
            return indexBit

        length = len(nums)
        if length < 2:
            return []
        resExcludeOr = 0
        for v in nums:
            resExcludeOr ^= v
        indexCntOf1 = findFirstBitIs1(resExcludeOr)
        # print("indexCnt1 From right",resExcludeOr,indexCntOf1)
        num1, num2 = 0, 0
        for v in nums:
            if isBit1(v, indexCntOf1):
                num1 ^= v
            else:
                num2 ^= v
        return [num1, num2]

    def singleNumbers(self, nums: List[int]) -> List[int]:
        """
        先对所有数字进行一次异或，得到两个出现一次的数字的异或值。
        在异或结果中找到任意为1 的位。
        根据这一位对所有的数字进行分组。
        在每个组内进行异或操作，得到两个数字。
        """

        if len(nums) < 2:
            return []
        resExcludeOr = 0
        for v in nums:
            resExcludeOr ^= v
        divider = 1
        while divider & resExcludeOr == 0:
            divider <<= 1
        num1, num2 = 0, 0
        for v in nums:
            if v & divider:
                num1 ^= v
            else:
                num2 ^= v
        return [num1, num2]


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [4, 1, 4, 6],
        [1, 2, 10, 4, 1, 4, 3, 3]

    ]
    lists = [x for x in samples]
    res = [sol.singleNumbers(x) for x in lists]
    print(res)
