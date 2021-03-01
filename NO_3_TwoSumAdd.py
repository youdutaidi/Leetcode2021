# !bin/bash/python3

'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prenode = ListNode(0)
        lastnode = prenode
        val = 0

        while val or l1 or l2:

            val, cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)  #key line,在没有进位的情况下，val永远都等于1
            lastnode.next = ListNode(cur)
            lastnode = lastnode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return prenode.next


def generateList(l: list) -> ListNode:
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next

def printList(l: ListNode):
    while l:
        print("%d, " %(l.val), end = '')
        l = l.next
    print('')

if __name__ == "__main__":
    l1 = generateList([1, 5, 8])
    l2 = generateList([9, 1, 2, 9])
    printList(l1)
    printList(l2)
    s = Solution()
    sum = s.addTwoNumbers(l1, l2)
    printList(sum)

'''
作者：xiao-lin-20
链接：https://leetcode-cn.com/problems/add-two-numbers/solution/cjie-ti-de-wan-zheng-dai-ma-bao-gua-sheng-cheng-ce/
来源：力扣（LeetCode）
'''
