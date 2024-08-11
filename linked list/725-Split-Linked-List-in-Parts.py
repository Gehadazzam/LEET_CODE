# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def getLength(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        length = getLength(head)
        size, remainder = divmod(length, k)
        result = []
        curr = head
        for i in range(k):
            holder = curr
            partSize = size + (1 if i < remainder else 0)
            for _ in range(partSize - 1):
                if curr:
                    curr = curr.next
            if curr:
                next_start = curr.next
                curr.next = None
                curr = next_start
            result.append(holder)
        return result