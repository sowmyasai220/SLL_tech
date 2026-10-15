
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CLL:
    def __init__(self):
        self.last = None

    def insert_beg(self, x):
        n = Node(x)
        if not self.last:
            self.last = n
            n.next = n
        else:
            n.next = self.last.next
            self.last.next = n

    def insert_end(self, x):
        self.insert_beg(x)
        self.last = self.last.next

    def insert_pos(self, x, pos):
        if pos < 1:
            print("Invalid position")
            return
        if not self.last or pos == 1:
            self.insert_beg(x)
            return
        temp = self.last.next
        i = 1
        while i < pos - 1 and temp != self.last:
            temp = temp.next
            i += 1
        if i != pos - 1:
            print("Invalid position")
            return
        n = Node(x)
        n.next = temp.next
        temp.next = n
        if temp == self.last:
            self.last = n

    def delete_beg(self):
        if not self.last:
            print("List is empty")
            return
        first = self.last.next
        if first == self.last:
            self.last = None
        else:
            self.last.next = first.next

    def delete_end(self):
        if not self.last:
            print("List is empty")
            return
        first = self.last.next
        if first == self.last:
            self.last = None
            return
        temp = first
        while temp.next != self.last:
            temp = temp.next
        temp.next = self.last.next
        self.last = temp

    def delete_pos(self, pos):
        if pos < 1 or not self.last:
            print("Invalid position or empty list")
            return
        if pos == 1:
            self.delete_beg()
            return
        temp = self.last.next
        i = 1
        while i < pos - 1 and temp != self.last:
            temp = temp.next
            i += 1
        if i != pos - 1 or temp.next == self.last.next:
            print("Invalid position")
            return
        deleted = temp.next
        temp.next = deleted.next
        if deleted == self.last:
            self.last = temp

    def reverse(self):
        if not self.last or self.last.next == self.last:
            return
        first = self.last.next
        prev = self.last
        curr = first
        while True:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            if curr == first:
                break
        self.last = first

    def display(self):
        if not self.last:
            print("List is empty")
            return
        temp = self.last.next
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.last.next:
                break
        print("(back to head)")


c = CLL()
c.insert_beg(20)
c.insert_beg(10)
c.insert_end(40)
c.insert_pos(30, 3)
c.display()

c.delete_beg()
c.delete_end()
c.delete_pos(2)
c.display()

c.reverse()
c.display()
