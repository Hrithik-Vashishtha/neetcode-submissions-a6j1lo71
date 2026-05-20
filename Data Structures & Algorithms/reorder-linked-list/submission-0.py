# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split and Reverse the second half
        curr = slow.next
        slow.next = None  # Crucial: break the link to terminate the first half
        prev = None
        while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
        
        # IMPORTANT: prev is now the head of the reversed second half
        first = head
        second = prev 

        # 3. Merge (Weave) the lists
        while second:
                temp1 = first.next
                temp2 = second.next

                first.next = second
                second.next = temp1

                first = temp1
                second = temp2