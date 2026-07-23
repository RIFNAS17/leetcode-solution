# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: empty list or single node
        if not head or not head.next:
            return head
        
        # Function to merge two sorted linked lists
        def merge(l1: ListNode, l2: ListNode) -> ListNode:
            if not l1:
                return l2
            if not l2:
                return l1
            
            dummy = ListNode(0)
            p = dummy
            
            while l1 and l2:
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                
                p = p.next
            
            if l1:
                p.next = l1
            else:
                p.next = l2
            
            return dummy.next
        
        # Function to perform merge sort on the linked list
        def sortList(head: ListNode) -> ListNode:
            if not head or not head.next:
                return head
            
            slow, fast = head, head.next
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            mid = slow.next
            slow.next = None
            
            left = sortList(head)
            right = sortList(mid)
            
            return merge(left, right)
        
        return sortList(head)
