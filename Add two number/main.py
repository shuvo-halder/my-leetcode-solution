class Solution:
    def addTwoNumber(self, l1, l2):
        dummy = ListName()
        res = dummy

        total = 0
        carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next
            
        return res.next