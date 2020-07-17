#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-27 18:25:45
# @Last Modified : 2020-04-27 18:25:45
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0



"""
# 设计实现双端队列。
# 你的实现需要支持以下操作：
#
#
#  MyCircularDeque(k)：构造函数,双端队列的大小为k。
#  insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
#  insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
#  deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
#  deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
#  getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
#  getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
#  isEmpty()：检查双端队列是否为空。
#  isFull()：检查双端队列是否满了。
#
#
#  示例：
#
#  MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
# circularDeque.insertLast(1);			        // 返回 true
# circularDeque.insertLast(2);			        // 返回 true
# circularDeque.insertFront(3);			        // 返回 true
# circularDeque.insertFront(4);			        // 已经满了，返回 false
# circularDeque.getRear();  				// 返回 2
# circularDeque.isFull();				        // 返回 true
# circularDeque.deleteLast();			        // 返回 true
# circularDeque.insertFront(4);			        // 返回 true
# circularDeque.getFront();				// 返回 4
#  
#
#
#
#  提示：
#
#
#  所有值的范围为 [1, 1000]
#  操作次数的范围为 [1, 1000]
#  请不要使用内置的双端队列库。
#
#  Related Topics 设计 队列
#  👍 46 👎 0

"""

class MyCircularDueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.__start = 0
        self.__size = 0
        self.__buffer = [0] * k
        self.__capacity = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        idx = (self.__start + self.__capacity - 1) % self.__capacity
        self.__buffer[idx] = value
        self.__start=idx
        self.__size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        idx = (self.__start + self.__size) % self.__capacity
        self.__buffer[idx] = value
        self.__size+=1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.__start = (self.__start + 1) % self.__capacity
        self.__size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.__size -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.isEmpty():
           return self.__buffer[self.__start]
        return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.isEmpty():
            idx = (self.__start + self.__size-1) % self.__capacity
            return self.__buffer[idx]
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.__size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.__size == self.__capacity


if __name__ == '__main__':
    circularDeque = MyCircularDueue(3)  ## 设置长度为 3
    circularDeque.insertLast(1)  # 返回 true
    circularDeque.insertLast(2)  # 返回 true
    circularDeque.insertFront(3)   # 返回 true
    circularDeque.insertFront(4)   # 已经满了，返回 false
    print(circularDeque.getRear() )      # 返回 2
    circularDeque.isFull()       # 返回 true
    circularDeque.deleteLast()    # 返回 true
    print(circularDeque.insertFront(4))  # 返回 true
    print(circularDeque.getFront())  # 返回 4
