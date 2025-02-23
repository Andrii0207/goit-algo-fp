

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def show(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev, current = None, self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sorted_lists(self, list1, list2):
        node = Node()
        tail = node

        while list1 and list2:
            if list1.value < list2.value:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next - list1 if list1 else list2
        return node.next

    def merge_sort(self, head):
        if not head or not head.next:
            return head

        def split(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            middle = slow.next
            slow.next = None
            return head, middle

        def merge(list1, list2):
            node = Node()
            tail = node
            while list1 and list2:
                if list1.value < list2.value:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            tail.next = list1 if list1 else list2
            return node.next
        left, right = split(head)
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        return merge(left, right)

    def sort(self):
        self.head = self.merge_sort(self.head)


ll = LinkedList()
ll.add(3)
ll.add(1)
ll.add(4)
ll.add(2)
print("Оригінальний список:")
ll.show()

ll.reverse()
print("Реверсований список:")
ll.show()

ll.sort()
print("Відсортований список:")
ll.show()
