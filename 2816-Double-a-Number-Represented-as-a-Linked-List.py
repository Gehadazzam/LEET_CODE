# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def add_digit(val, head):
            new_node = ListNode(val)
            new_node.next = head
            return new_node
        
        stack = []
        current = head
        while current:
            stack.append(current.val)
            current = current.next
        
        carry = 0
        new_head = None
        while stack:
            digit = stack.pop() * 2 + carry
            carry = digit // 10
            new_head = add_digit(digit % 10, new_head)
        
        while carry:
            new_head = add_digit(carry % 10, new_head)
            carry //= 10
        
        return new_head

