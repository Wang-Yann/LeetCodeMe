package com.rock.ltc.utils;

/**
 * @Author: Rock
 * @Date: 2021-05-17 22:53
 * @Description:
 */
public class ListNode {
    int val;
    ListNode next;
    
    ListNode(int x) {
        val = x;
    }
    
    public static ListNode initLinkedList(Integer[] arr) {
        if (arr.length == 0) {
            return null;
        }
        ListNode head = new ListNode(arr[0]);
        ListNode current = head;
        for (int i = 1; i < arr.length; i++) {//过程
            current.next = new ListNode(arr[i]);
            current = current.next;
        }
        return head;
    }
    
    //将链表结果打印
    public static void printLinkedList(ListNode head) {
        ListNode current = head;
        while (current != null) {
            System.out.printf("%d -> ", current.val);
            current = current.next;
        }
        System.out.println("NULL");
    }
    
    
}
    

