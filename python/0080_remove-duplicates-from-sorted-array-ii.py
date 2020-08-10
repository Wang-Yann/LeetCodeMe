#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-12 22:19:00
# @Last Modified : 2020-04-12 22:19:00
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
#
#  不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
#  示例 1:
#
#  给定 nums = [1,1,1,2,2,3],
#
# 函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
#
# 你不需要考虑数组中超出新长度后面的元素。
#
#  示例 2:
#
#  给定 nums = [0,0,1,1,1,1,2,3,3],
#
# 函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
#
# 你不需要考虑数组中超出新长度后面的元素。
#
#
#  说明:
#
#  为什么返回数值是整数，但输出的答案是数组呢?
#
#  请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
#
#  你可以想象内部操作如下:
#
#  // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);
#
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }
#  Related Topics 数组 双指针
#  👍 249 👎 0

"""
import copy
from typing import List

import pytest


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if not length:
            return 0
        last, i, is_same = 0, 1, False
        while i < length:
            if nums[last] != nums[i] or not is_same:
                is_same = nums[last] == nums[i]
                last += 1
                nums[last] = nums[i]
            i += 1
        return last + 1


class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Me"""
        length = len(nums)
        if length <= 2:
            return length
        pos_cur = 1
        l = 1
        cnt = 1
        while l <= length - 1:
            if nums[l] == nums[l - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt <= 2:
                nums[pos_cur] = nums[l]
                pos_cur += 1
            l += 1
        return pos_cur


@pytest.mark.parametrize(
    "nums,ret,expected",
    list(zip(
        [
            [1, 1, 1, 2, 2, 3],
            [0, 0, 1, 1, 1, 1, 2, 3, 3],
            [-1, 1, 1, 1, 1, 2, 3, 3],
            [1, 1, 1, 2, 2, 3],
            [1, 2, 2]
        ],
        [5, 7, 6, 5, 3],
        [[1, 1, 2, 2, 3, 3],
         [0, 0, 1, 1, 2, 3, 3, 3, 3],
         [-1, 1, 1, 2, 3, 3, 3, 3],
         [1, 1, 2, 2, 3, 3],
         [1, 2, 2]]
    ))
)
def test_solutions(nums, ret, expected):
    nums1 = copy.deepcopy(nums)
    assert Solution().removeDuplicates(nums) == ret
    assert Solution1().removeDuplicates(nums1) == ret
    assert nums == expected
    assert nums1 == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
