class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.addTwoNumbersRecursive(l1, l2, 0)

    def addTwoNumbersRecursive(self, l1, l2, carry):
        if not l1 and not l2 and not carry:
            return None

        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        digit_sum = val1 + val2 + carry
        carry = digit_sum // 10
        digit = digit_sum % 10

        new_node = ListNode(digit)

        l1_next = l1.next if l1 else None
        l2_next = l2.next if l2 else None

        new_node.next = self.addTwoNumbersRecursive(l1_next, l2_next, carry)

        return new_node


if __name__ == '__main__':
    sol = Solution()

    l1 = ListNode(2, ListNode(4, ListNode(3,ListNode(1))))  # [2,4,3,1]
    l2 = ListNode(5, ListNode(6, ListNode(4)))  # [5,6,4]

    result = sol.addTwoNumbers(l1, l2)

    current = result
    while current is not None:
        print(current)
        current = current.next
