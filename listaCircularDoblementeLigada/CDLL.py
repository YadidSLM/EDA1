class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class Lista:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        elif self.head.next == self.tail:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node