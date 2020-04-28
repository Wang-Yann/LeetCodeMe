#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-16 21:59:24
# @Last Modified : 2020-04-16 21:59:24
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
from typing import List


class Solution:
    def productExceptSelfOf(self, nums: List[int]) -> List[int]:

        # The length of the input array
        length = len(nums)

        # The answer array to be returned
        answer = [0]*length

        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):

            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        print(answer)
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1
        for i in reversed(range(length)):

            # For the index 'i', R would contain the
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        left_product = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            left_product[i] = left_product[i - 1] * nums[i - 1]
        print(left_product)
        right_product = 1
        for i in range(len(nums) - 2, -1, -1):
            right_product *= nums[i + 1]
            left_product[i] = left_product[i] * right_product

        return left_product

if __name__ == '__main__':
    sol = Solution()
    samples=[
        [2,3,4,5]
    ]
    res = [ sol.productExceptSelfOf(x) for x in samples]
    print(res)


