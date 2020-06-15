#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-15 21:23:31
# @Last Modified : 2020-06-15 21:23:31
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class SortAll(object):

    @staticmethod
    def selection_sort(nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N):
            # 最小元素索引
            min_i = i
            for j in range(i + 1, N):
                if nums[min_i] > nums[j]:
                    min_i = j
            nums[min_i], nums[i] = nums[i], nums[min_i]
        return nums

    @staticmethod
    def insertion_sort(nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(1, N):
            for j in range(i, 0, -1):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]

        return nums

    @staticmethod
    def bubble_sort(nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N - 1):
            for j in range(N - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]
        return nums

    @staticmethod
    def shell_sort3(nums: List[int]) -> List[int]:
        N = len(nums)
        h = 1
        while h < N // 3:
            h = 3 * h + 1
        while h >= 1:
            for i in range(h, N):
                for j in range(i, h - 1, -h):
                    if nums[j] < nums[j - h]:
                        nums[j], nums[j - h] = nums[j - h], nums[j]
            h //= 3
        return nums

    @staticmethod
    def shell_sort(nums: List[int]) -> List[int]:
        n = len(nums)
        gap = n // 2
        while gap:
            for i in range(gap, n):
                while i - gap >= 0 and nums[i - gap] > nums[i]:
                    nums[i - gap], nums[i] = nums[i], nums[i - gap]
                    i -= gap
            gap //= 2
        return nums

    def merge_sort_t2b(self, nums: List[int]) -> List[int]:
        def merge(lo, mid, hi):
            i = lo
            j = mid + 1
            for k in range(lo, hi + 1):
                aux[k] = nums[k]
            for k in range(lo, hi + 1):
                if i > mid:
                    nums[k] = aux[j]
                    j += 1
                elif j > hi:
                    nums[k] = aux[i]
                    i += 1
                elif aux[j] < aux[i]:
                    nums[k] = aux[j]
                    j += 1
                else:
                    nums[k] = aux[i]
                    i += 1

        def merge_sort(lo, hi):
            if hi <= lo:
                return
            mid = (lo + hi) >> 1
            merge_sort(lo, mid)
            merge_sort(mid + 1, hi)
            merge(lo, mid, hi)

        N = len(nums)
        aux = [0] * N
        merge_sort(0, N - 1)
        return nums

    def merge_sort00(self, nums: List[int]) -> List[int]:
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
        left = self.merge_sort00(nums[:mid])
        right = self.merge_sort00(nums[mid:])
        return merge(left, right)

    @staticmethod
    def quick_sort(nums: List[int]) -> List[int]:
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

    @staticmethod
    def quick_sort3(nums: List[int]) -> List[int]:

        def quick_sort_3way(lo, hi):
            if hi <= lo:
                return
            lt, i, gt = lo, lo + 1, hi
            v = nums[lo]
            while i <= gt:
                if nums[i] < v:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    i += 1
                    lt += 1
                elif nums[i] > v:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1
            quick_sort_3way(lo, lt - 1)
            quick_sort_3way(gt + 1, hi)

        N = len(nums)
        quick_sort_3way(0, N - 1)
        return nums

    @staticmethod
    def heap_sort_0(nums: List[int]) -> List[int]:

        def make_heap(i, n):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and nums[i] < nums[l]:
                largest = l
            if r < n and nums[largest] < nums[r]:
                largest = r
            if largest != i:
                nums[largest], nums[i] = nums[i], nums[largest]
                make_heap(largest, n)

        N = len(nums)
        for i in reversed(range(N // 2)):
            make_heap(i, N)
        for i in range(N - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            make_heap(0, i)
        return nums

    @staticmethod
    def heap_sort(nums: List[int]) -> List[int]:
        """
        从1开始的索引
        """

        def sink(k, endpos):
            while 2 * k <= endpos:
                j = 2 * k
                if j < endpos and nums[j-1] < nums[j ]:
                    j += 1
                if not nums[k-1] < nums[j-1]:
                    break
                nums[k-1], nums[j-1] = nums[j-1], nums[k-1]
                k = j

        N = len(nums)
        for i in range(N // 2, 0, -1):
            sink(i, N)
        while N > 1:
            nums[0], nums[N-1] = nums[N-1], nums[0]
            N -= 1
            sink(1, N)

        return nums

    @staticmethod
    def bucket_sort(nums: List[int]) -> List[int]:
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

    @staticmethod
    def radix_sort(nums: List[int]) -> List[int]:
        """
        正数OK
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
    solAll = SortAll()
    assert solAll.insertion_sort(args[:]) == expected
    assert solAll.selection_sort(args[:]) == expected
    assert solAll.bubble_sort(args[:]) == expected
    assert solAll.shell_sort(args[:]) == expected
    assert solAll.shell_sort3(args[:]) == expected
    assert solAll.quick_sort(args[:]) == expected
    assert solAll.quick_sort3(args[:]) == expected
    assert solAll.merge_sort00(args[:]) == expected
    assert solAll.merge_sort_t2b(args[:]) == expected
    assert solAll.heap_sort_0(args[:]) == expected
    assert solAll.heap_sort(args[:]) == expected
    assert solAll.bucket_sort(args[:]) == expected
    # assert solAll.radix_sort(args[:]) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
