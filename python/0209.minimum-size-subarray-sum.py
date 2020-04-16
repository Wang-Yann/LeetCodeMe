#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-16 20:58:05
# @Last Modified : 2020-04-16 20:58:05
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List


class Solution:

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        初始化 \text{left}left 指向 0 且初始化 \text{sum}sum 为 0
        遍历 \text{nums}nums 数组：
        将 \text{nums}[i]nums[i] 添加到 \text{sum}sum
        当 \text{sum}sum 大于等于 ss 时：
        更新 \text{ans}=\min(\text{ans},i+1-\text{left})ans=min(ans,i+1−left) ，其中 i+1-\text{left}i+1−left是当前子数组的长度
        然后我们可以移动左端点，因为以它为开头的满足 \text{sum} \geq ssum≥s 条件的最短子数组已经求出来了
        将 \text{sum}sum 减去 \text{nums[left]}nums[left] 然后增加 \text{left}left

        """
        start = 0
        sum = 0
        min_size = float("inf")
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                min_size = min(min_size, i - start + 1)
                sum -= nums[start]
                start += 1
        return min_size if min_size != float("inf") else 0



if __name__ == '__main__':
    sol = Solution()
    samples = [
        (7, [2, 3, 1, 2, 4, 3])
    ]
    res = [sol.minSubArrayLen(*x) for x in samples]
    print(res)
