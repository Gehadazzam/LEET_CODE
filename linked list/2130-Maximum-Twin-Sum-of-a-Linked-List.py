# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def getLength(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        
        def reverse(node):
            prev = None
            while node:
                holder = node.next
                node.next = prev
                prev = node
                node = holder
            return prev
        
        ptr = head
        half = getLength(ptr) // 2
        curr = head

        for _ in range(half):
            curr = curr.next
        secondhalf = reverse(curr)
        
        maxVal = 0
        while head and secondhalf:
            maxVal = max(maxVal, head.val + secondhalf.val)
            head = head.next
            secondhalf = secondhalf.next
        
        return maxVal