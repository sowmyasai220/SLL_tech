
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insert_beg(self, x):
        n = Node(x)
        n.next = self.head
        self.head = n

    def insert_end(self, x):
        n = Node(x)
        if not self.head:
            self.head = n
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = n

    def insert_pos(self, x, pos):
        if pos < 1:
            print("Invalid position")
            return
        if pos == 1:
            self.insert_beg(x)
            return
        temp = self.head
        for i in range(1, pos - 1):
            if not temp:
                print("Invalid position")
                return
            temp = temp.next
        if not temp:
            print("Invalid position")
            return
        n = Node(x)
        n.next = temp.next
        temp.next = n

    def delete_beg(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next

    def delete_end(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_pos(self, pos):
        if pos < 1 or not self.head:
            print("Invalid position or empty list")
            return
        if pos == 1:
            self.delete_beg()
            return
        temp = self.head
        for i in range(1, pos - 1):
            if not temp.next:
                print("Invalid position")
                return
            temp = temp.next
        if not temp.next:
            print("Invalid position")
            return
        temp.next = temp.next.next

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


s = SLL()
s.insert_beg(20)
s.insert_beg(10)
s.insert_end(40)
s.insert_pos(30, 3)
s.display()

s.delete_beg()
s.delete_end()
s.delete_pos(2)
s.display()

s.reverse()
s.display()
