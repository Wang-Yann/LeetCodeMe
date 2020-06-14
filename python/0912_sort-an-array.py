#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个整数数组 nums，请你将该数组升序排列。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
#  
# 
#  示例 2： 
# 
#  输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 50000 
#  -50000 <= nums[i] <= 50000 
#  
# 

"""
import random
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        def randomized_partition(l, r):
            pivot = random.randint(l, r)
            nums[pivot], nums[r] = nums[r], nums[pivot]
            i = l - 1
            for j in range(l, r):
                if nums[j] < nums[r]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        def randomized_quicksort(l, r):
            if r - l <= 0:
                return
            mid = randomized_partition(l, r)
            randomized_quicksort(l, mid - 1)
            randomized_quicksort(mid + 1, r)

        randomized_quicksort(0, len(nums) - 1)
        return nums


# leetcode submit region end(Prohibit modification and deletion)

class SolutionMerge:

    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(l, r):
            if l == r:
                return
            mid = (l + r) >> 1
            merge_sort(l, mid)
            merge_sort(mid + 1, r)
            tmp = []
            i, j = l, mid + 1
            while i <= mid or j <= r:
                if i > mid or (j <= r and nums[j] < nums[i]):
                    tmp.append(nums[j])
                    j += 1
                else:
                    tmp.append(nums[i])
                    i += 1
            nums[l:r + 1] = tmp

        merge_sort(0, len(nums) - 1)
        return nums


class SolutionAll:

    def selection_sort(self, nums: List[int]) -> List[int]:
        """TLE"""
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

    def bubble_sort(self, nums: List[int]) -> List[int]:
        """TLE"""
        n = len(nums)
        for i in range(n):
            for j in range(1, n - i):
                if nums[j - 1] > nums[j]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
        return nums

    def insertion_sort(self, nums: List[int]) -> List[int]:
        """TLE"""
        n = len(nums)
        for i in range(1, n):
            while i > 0 and nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                i -= 1
        return nums

    def shell_sort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        gap = n // 2
        while gap:
            for i in range(gap, n):
                while i - gap >= 0 and nums[i - gap] > nums[i]:
                    nums[i - gap], nums[i] = nums[i], nums[i - gap]
                    i -= gap
            gap //= 2
        return nums

    def quick_sort(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def quick(left, right):
            if left >= right:
                return nums
            pivot = left
            i = left
            j = right
            while i < j:
                while i < j and nums[j] > nums[pivot]:
                    j -= 1
                while i < j and nums[i] <= nums[pivot]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[pivot], nums[j] = nums[j], nums[pivot]
            quick(left, j - 1)
            quick(j + 1, right)
            return nums

        return quick(0, n - 1)

    def merge_sort(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            res = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res += left[i:]
            res += right[j:]
            return res

        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return merge(left, right)

    def heap_sort_1(self, nums: List[int]) -> List[int]:

        def make_heap_iter(startpos, endpos):
            newitem = nums[startpos]
            pos = startpos
            childpos = pos * 2 + 1
            while childpos < endpos:
                rightpos = childpos + 1
                if rightpos < endpos and nums[rightpos] >= nums[childpos]:
                    childpos = rightpos
                if newitem < nums[childpos]:
                    nums[pos] = nums[childpos]
                    pos = childpos
                    childpos = pos * 2 + 1
                else:
                    break
            nums[pos] = newitem

        # def make_heap(startpos, endpos):
        #     # 有问题
        #     """ TODO TODO TODO"""
        #     pos = startpos
        #     child_pos = pos * 2 + 1
        #     if child_pos < endpos:
        #         right_pos = child_pos + 1
        #         if right_pos < endpos and nums[right_pos] >= nums[child_pos]:
        #             child_pos = right_pos
        #         if nums[child_pos] > nums[pos]:
        #             nums[pos], nums[child_pos] = nums[child_pos], nums[pos]
        #             make_heap(pos, endpos)

        n = len(nums)
        for i in reversed(range(n // 2)):
            make_heap_iter(i, n)
        for i in range(n - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            make_heap_iter(0, i)
        return nums

    def heap_sort(self, nums: List[int]) -> List[int]:
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1  # left = 2*i + 1
            r = 2 * i + 2  # right = 2*i + 2

            if l < n and arr[i] < arr[l]:
                largest = l

            if r < n and arr[largest] < arr[r]:
                largest = r

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  # 交换

                heapify(arr, n, largest)

        n = len(nums)

        # Build a maxheap. 
        for i in range(n, -1, -1):
            heapify(nums, n, i)

            # 一个个交换元素
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]  # 交换
            heapify(nums, i, 0)
        # print(nums)
        return nums

    def bucket_sort(self, nums: List[int]) -> List[int]:
        def bucket_sort_helper(nums, bucketSize):
            if len(nums) < 2:
                return nums
            _min = min(nums)
            _max = max(nums)
            # 需要桶个数
            bucketNum = (_max - _min) // bucketSize + 1
            buckets = [[] for _ in range(bucketNum)]
            for num in nums:
                # 放入相应的桶中
                buckets[(num - _min) // bucketSize].append(num)
            res = []

            for bucket in buckets:
                if not bucket:
                    continue
                if bucketSize == 1:
                    res.extend(bucket)
                else:
                    # 当都装在一个桶里,说明桶容量大了
                    if bucketNum == 1:
                        bucketSize -= 1
                    res.extend(bucket_sort_helper(bucket, bucketSize))
            return res

        # 100 write at will
        return bucket_sort_helper(nums, 100)

    def radix_sort(self, nums: List[int]) -> List[int]:
        """
        有负数 wrong TODO TODO TODO
        """
        i = 0  # 记录当前正在排拿一位，最低位为1
        max_num = max(nums)  # 最大值
        j = len(str(max_num))  # 记录最大值的位数
        while i < j:
            bucket_list = [[] for _ in range(10)]  # 初始化桶数组
            for x in nums:
                bucket_list[int(x // (10 ** i)) % 10].append(x)  # 找到位置放入桶数组
            nums.clear()
            for x in bucket_list:  # 放回原序列
                for y in x:
                    nums.append(y)
            i += 1
        return nums


@pytest.mark.parametrize("args,expected", [
    ([5, 2, 3, 1], [1, 2, 3, 5]),
    ([3, -1], [-1, 3]),
    ([-4, 0, 7, 4, 9, -5, -1, 0, -7, -1], [-7, -5, -4, -1, -1, 0, 0, 4, 7, 9]),
    pytest.param([5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5]),
])
def test_solutions(args, expected):
    solAll = SolutionAll()
    assert Solution().sortArray(args[:]) == expected
    assert SolutionMerge().sortArray(args[:]) == expected
    assert solAll.insertion_sort(args[:]) == expected
    assert solAll.selection_sort(args[:]) == expected
    assert solAll.bubble_sort(args[:]) == expected
    assert solAll.shell_sort(args[:]) == expected
    assert solAll.quick_sort(args[:]) == expected
    assert solAll.merge_sort(args[:]) == expected
    assert solAll.heap_sort_1(args[:]) == expected
    assert solAll.heap_sort(args[:]) == expected
    assert solAll.bucket_sort(args[:]) == expected
    # assert solAll.radix_sort(args[:]) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
