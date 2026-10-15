
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    def insert_beg(self, x):
        n = Node(x)
        n.next = self.head
        if self.head:
            self.head.prev = n
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
        n.prev = temp

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
        n.prev = temp
        if temp.next:
            temp.next.prev = n
        temp.next = n

    def delete_beg(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_end(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        if temp.prev:
            temp.prev.next = None
        else:
            self.head = None

    def delete_pos(self, pos):
        if pos < 1 or not self.head:
            print("Invalid position or empty list")
            return
        temp = self.head
        for i in range(1, pos):
            if not temp:
                print("Invalid position")
                return
            temp = temp.next
        if not temp:
            print("Invalid position")
            return
        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next
        if temp.next:
            temp.next.prev = temp.prev

    def reverse(self):
        temp = self.head
        prev_node = None
        while temp:
            prev_node = temp.prev
            temp.prev = temp.next
            temp.next = prev_node
            temp = temp.prev
        if prev_node:
            self.head = prev_node.prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


d = DLL()
d.insert_beg(20)
d.insert_beg(10)
d.insert_end(40)
d.insert_pos(30, 3)
d.display()

d.delete_beg()
d.delete_end()
d.delete_pos(2)
d.display()

d.reverse()
d.display()
