'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        total = 0
        result = ListNode(-1)
        temp = result
        while True:
            count = l1.val + l2.val + total
        
            if count >= 10:
                count -= 10
                total = 1
            else:
                total = 0

            temp.next = ListNode(count)
            
            temp = temp.next


            if l1.next is None:
                break

            l1 = l1.next
            l2 = l2.next

        return result.next

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

solution = Solution()
solution.addTwoNumbers(l1, l2)
