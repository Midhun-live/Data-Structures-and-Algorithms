# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        L = []
        if l1:
            while l1:
                if not l1:
                    return
                L.append(l1.val)
                l1 = l1.next
        if l2:
            while l2:
                if not l2:
                    return
                L.append(l2.val)
                l2 = l2.next
                
        L.sort()
        if not L:
            return
        first = ListNode(L[0])
        final = first
        
        for _ in range(1, len(L)):
            node = ListNode(L[_])
            first.next = node
            first =  node
            
        return final