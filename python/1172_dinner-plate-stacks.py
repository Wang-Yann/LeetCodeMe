#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 我们把无限数量 ∞ 的栈排成一行，按从左到右的次序从 0 开始编号。每个栈的的最大容量 capacity 都相同。 
# 
#  实现一个叫「餐盘」的类 DinnerPlates： 
# 
#  
#  DinnerPlates(int capacity) - 给出栈的最大容量 capacity。 
#  void push(int val) - 将给出的正整数 val 推入 从左往右第一个 没有满的栈。 
#  int pop() - 返回 从右往左第一个 非空栈顶部的值，并将其从栈中删除；如果所有的栈都是空的，请返回 -1。 
#  int popAtStack(int index) - 返回编号 index 的栈顶部的值，并将其从栈中删除；如果编号 index 的栈是空的，请返回 -
# 1。 
#  
# 
#  
# 
#  示例： 
# 
#  输入： 
# ["DinnerPlates","push","push","push","push","push","popAtStack","push","push",
# "popAtStack","popAtStack","pop","pop","pop","pop","pop"]
# [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
# 输出：
# [null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]
# 
# 解释：
# DinnerPlates D = DinnerPlates(2);  // 初始化，栈最大容量 capacity = 2
# D.push(1);
# D.push(2);
# D.push(3);
# D.push(4);
# D.push(5);         // 栈的现状为：    2  4
#                                     1  3  5
#                                     ﹈ ﹈ ﹈
# D.popAtStack(0);   // 返回 2。栈的现状为：      4
#                                           1  3  5
#                                           ﹈ ﹈ ﹈
# D.push(20);        // 栈的现状为：  20  4
#                                    1  3  5
#                                    ﹈ ﹈ ﹈
# D.push(21);        // 栈的现状为：  20  4 21
#                                    1  3  5
#                                    ﹈ ﹈ ﹈
# D.popAtStack(0);   // 返回 20。栈的现状为：       4 21
#                                             1  3  5
#                                             ﹈ ﹈ ﹈
# D.popAtStack(2);   // 返回 21。栈的现状为：       4
#                                             1  3  5
#                                             ﹈ ﹈ ﹈ 
# D.pop()            // 返回 5。栈的现状为：        4
#                                             1  3 
#                                             ﹈ ﹈  
# D.pop()            // 返回 4。栈的现状为：    1  3 
#                                            ﹈ ﹈   
# D.pop()            // 返回 3。栈的现状为：    1 
#                                            ﹈   
# D.pop()            // 返回 1。现在没有栈。
# D.pop()            // 返回 -1。仍然没有栈。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= capacity <= 20000 
#  1 <= val <= 20000 
#  0 <= index <= 100000 
#  最多会对 push，pop，和 popAtStack 进行 200000 次调用。 
#  
#  Related Topics 设计

"""
import heapq

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class DinnerPlates:
    """
    GOOD HARD
    Use a heap queue q to find the leftmost available stack.
    https://leetcode.com/problems/dinner-plate-stacks/discuss/366331/C%2B%2BPython-Two-Solutions
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.q = []  # record the available stack, will use heap to quickly find the smallest available stack
        # if you are Java or C++ users, tree map is another good option.
        self.stacks = []  # record values of all stack of plates, its last nonempty stack are the rightmost position

    def push(self, val: int) -> None:
        # To push, we need to find the leftmost available position
        # first, let's remove any stacks on the left that are full
        # 1) self.q: if there is still available stack to insert plate
        # 2) self.q[0] < len(self.stacks): the leftmost available index self.q[0] is smaller than the current size of the stacks
        # 3) len(self.stacks[self.q[0]]) == self.c: the stack has reached full capacity
        while self.q and self.q[0] < len(self.stacks) and len(self.stacks[self.q[0]]) == self.capacity:
            # we remove the filled stack from the queue of available stacks
            heapq.heappop(self.q)

        # now we reach the leftmost available stack to insert

        # if the q is empty, meaning there are no more available stacks
        if not self.q:
            # open up a new stack to insert
            heapq.heappush(self.q, len(self.stacks))

        # for the newly added stack, add a new stack to self.stacks accordingly
        if self.q[0] == len(self.stacks):
            self.stacks.append([])

        # append the value to the leftmost available stack
        self.stacks[self.q[0]].append(val)

    def pop(self) -> int:
        # To pop, we need to find the rightmost nonempty stack
        # 1) stacks is not empty (self.stacks) and
        # 2) the last stack is empty
        while self.stacks and not self.stacks[-1]:
            # we throw away the last empty stack, because we can't pop from it
            self.stacks.pop()

        # now we reach the rightmost nonempty stack

        # we pop the plate from the last nonempty stack of self.stacks by using popAtStack function
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        # To pop from an stack of given index, we need to make sure that it is not empty
        # 1) the index for inserting is valid and，
        # 2) the stack of interest is not empty
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            # we add the index into the available stack
            heapq.heappush(self.q, index)
            # take the top plate, pop it and return its value
            return self.stacks[index].pop()

        # otherwise, return -1 because we can't pop any plate
        return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
# leetcode submit region end(Prohibit modification and deletion)

def test_solution():
    D = DinnerPlates(2)  # // 初始化，栈最大容量 capacity = 2
    D.push(1)
    D.push(2)
    D.push(3)
    D.push(4)
    D.push(5)
    #                    // 栈的现状为：    2  4
    #                                     1  3  5
    #                                     ﹈ ﹈ ﹈
    assert D.popAtStack(0) == 2
    # D.popAtStack(0);   // 返回 2。栈的现状为：      4
    #                                           1  3  5
    #
    #                                          ﹈ ﹈ ﹈
    D.push(20)
    # D.push(20);        // 栈的现状为：  20  4
    #                                    1  3  5
    #                                    ﹈ ﹈ ﹈
    D.push(21)
    # D.push(21);        // 栈的现状为：  20  4 21
    #                                    1  3  5
    #                                    ﹈ ﹈ ﹈
    assert D.popAtStack(0) == 20
    # D.popAtStack(0);   // 返回 20。栈的现状为：       4 21
    #                                             1  3  5
    #                                             ﹈ ﹈ ﹈
    assert D.popAtStack(2) == 21
    # D.popAtStack(2);   // 返回 21。栈的现状为：       4
    #                                             1  3  5
    #                                             ﹈ ﹈ ﹈
    assert D.pop() == 5
    # D.pop()            // 返回 5。栈的现状为：        4
    #                                             1  3
    #                                             ﹈ ﹈
    assert D.pop() == 4
    # D.pop()            // 返回 4。栈的现状为：    1  3
    #                                            ﹈ ﹈
    assert D.pop() == 3
    # D.pop()            // 返回 3。栈的现状为：    1
    #                                            ﹈
    assert D.pop() == 1
    # D.pop()            // 返回 1。现在没有栈。
    assert D.pop() == -1
    # D.pop()            // 返回 -1。仍然没有栈。


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
