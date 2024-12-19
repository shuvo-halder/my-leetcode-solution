import os, sys
from typing import List, Tuple

# input l1 = [2,4,3], l2 = [5,6,4]
# input l1 = [0], l2 = [0]


class Solution:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addTwoNumbers(self, l1, l2):
        dummy_head = Solution(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = Solution(total % 10)

            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next

