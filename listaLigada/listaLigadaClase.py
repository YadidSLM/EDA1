class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        print(type(self.next)) #Tipo: NoneType

class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        
        new_node = Node(data) #Instanciando el nodo
        print(type(new_node)) #Saber el tipo de dato del node el cual es de __main__.Node
        if self.head is None :
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insertAtEnd(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head

        while(current_node.next):
            current_node = current_node.next
        
        current_node.next = new_node
    
    def remove_last_node(self):

        if self.head is None:
            return

        current_node = self.head
        
        while(current_node.next):
            current_node = current_node.next
        
        current_node.next = None
    
    def remove_first_node(self):

        if self.head is None:
            return
        
        self.head = self.head.next

    def remove_node(self, data):

        current_node = self.head

        if current_node.data == data:
            self.remove_first_node()
            return

        while(current_node != None and current_node.next.data != data):
            current_node = current_node.next
        
        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next
    
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head

            while(current_node):
                size = size + 1
                current_node = current_node.next
            return size
        else:
            return 0
    
    def printLL (self):
        current_node = self.head

        while(current_node):
            print(current_node.data)
            current_node = current_node.next
    
llist = LinkedList()
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtEnd('c')
llist.insertAtEnd('d')
llist.insertAtBegin('e')

print('INFO')
llist.printLL()
llist.remove_first_node()
llist.remove_first_node()


print('INFO')
llist.printLL()

print(llist.sizeOfLL())