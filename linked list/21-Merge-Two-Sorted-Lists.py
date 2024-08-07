# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = merged = ListNode()
        while (list1 and list2):
            if list1.val < list2.val:
                merged.next = list1.next
                merged = list1
                list1 = list1.next
            elif list1.val > list2.val:
                merged.next = list2.next
                merged = list2
                list2 = list2.next
        if list1 or list2: 
            merged.next = list1 if list1 else list2
        return head