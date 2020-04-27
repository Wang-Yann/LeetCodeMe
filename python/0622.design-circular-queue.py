#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-27 18:25:45
# @Last Modified : 2020-04-27 18:25:45
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
from common_utils import ListNode as  Node


class MyCircularQueue0:
    """从并发性来看，该循环队列是线程不安全的。 """

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.__start = 0
        self.__size = 0
        self.__buffer = [0] * k
        self.__capacity = k
        # self.queueLock = Lock()

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        # with self.queueLock:
        if self.isFull():
            return False
        idx = (self.__start + self.__size) % self.__capacity
        self.__buffer[idx] = value
        self.__size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.__start = (self.__start + 1) % self.__capacity
        self.__size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if not self.isEmpty():
            return self.__buffer[self.__start]
        return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if not self.isEmpty():
            idx = (self.__start + self.__size - 1) % self.__capacity
            return self.__buffer[idx]
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.__size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.__size == self.__capacity


class MyCircularQueue:
    """
    与固定大小的数组相比，单链表不会为未使用的容量预分配内存，因此它的内存效率更高。
    """

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.size -= 1
        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.head.val
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.tail.val
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


if __name__ == '__main__':
    circularQueue = MyCircularQueue(3)  ## 设置长度为 3
    circularQueue.enQueue(1)  ## 返回 true
    circularQueue.enQueue(2)  ## 返回 true
    circularQueue.enQueue(3)  ## 返回 true
    circularQueue.enQueue(4)  ## 返回 false，队列已满
    circularQueue.Rear()  ## 返回 3
    circularQueue.isFull()  ## 返回 true
    circularQueue.deQueue()  ## 返回 true
    circularQueue.enQueue(4)  ## 返回 true
    circularQueue.Rear()  ## 返回
