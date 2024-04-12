#import random

class Node():
    
    def __init__(self, row, col, data):
        self.prev = None
        self.row = row
        self.col = col
        self.data = data
        self.next = None

class Lista():

    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_begin(self, row, col, data):
        new_node = Node(row, col, data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        #Asignación de tail
        elif self.head.next == self.tail:
            self.tail.prev = self.head
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    #Impresión de lista de último ingresado al primero
    def print_list_LF(self):
        current_node = self.head
        print("(row, col)  Dato")
        while current_node != None:
            print(f"  ({current_node.row}, {current_node.col})     {current_node.data}")
            current_node = current_node.next
    
    #Impresión de lista el primero ingresado al último
    def print_list_FL(self):
        current_node = self.tail
        print("(row, col)  Dato")
        while current_node != None:
            print(f"  ({current_node.row}, {current_node.col})     {current_node.data}")
            current_node = current_node.prev
            

lista = Lista()
#ran = random.randint(1, 9)

sparce_matrix = [[1, 0, 0, 15, 0, 0],
                 [0, 3, 0, 0, 0, 5],
                 [0, 0, 7, 0, 0, 0],
                 ]
rows = 0
columns = 0
print("\n   Sparce Matrix       ")
for array in sparce_matrix:
    print(f"{array}")
    for elemento in array:
        if elemento != 0:
            lista.insert_at_begin(rows, columns, elemento)
        columns += 1
    rows += 1
    columns = 0

print("\nLista doblemente ligada       ")
print(" con datos no ceros de")
print("   la sparse matrix:\n")
lista.print_list_LF()
print("\nOrdenando")
lista.print_list_FL()