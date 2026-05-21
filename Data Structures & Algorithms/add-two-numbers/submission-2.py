# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        curr = temp

        curr1 = l1
        curr2 = l2
        carry = 0

        while curr1 and curr2:
            sum_ = curr1.val + curr2.val + carry
            num = sum_ % 10
            carry = sum_ // 10

            newNode = ListNode(num)
            curr.next = newNode
            curr = curr.next
            curr1 = curr1.next
            curr2 = curr2.next

        while curr1:
            sum_ = curr1.val + carry
            num = sum_ % 10
            carry = sum_ // 10

            newNode = ListNode(num)
            curr.next = newNode
            curr = curr.next
            curr1 = curr1.next
        while curr2:
            sum_ = curr2.val + carry
            num = sum_ % 10
            carry = sum_ // 10

            newNode = ListNode(num)
            curr.next = newNode
            curr = curr.next
            curr2 = curr2.next

        if carry > 0:
            newNode = ListNode(carry)
            curr.next = newNode

        return temp.next