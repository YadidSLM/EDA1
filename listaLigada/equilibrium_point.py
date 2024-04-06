class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Lista:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node


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
    
    def imprimir_linked_list(self):
        current_node = self.head
        while(current_node != None):
            print(current_node.data)
            current_node = current_node.next
    
    def equilibrium_point(self, index):
        #Guarda el último dato de la lista
        current_node = self.head 
        prev_node = self.head
        sumaA = current_node.data
        sumaP = 0
        auxA = index
        equilibrium_index = index - 1
        auxP = equilibrium_index - 1
        
        print(f'\naux index: A: {auxA}, P: {auxP}')

        while (sumaA != sumaP):

            print(equilibrium_index)
            while(auxP >= 0):

                sumaP += current_node.data
                current_node = current_node.next
                print(f'Suma: {sumaP}')
                auxP -= 1
            
            while auxA < equilibrium_index:
                sumaA += prev_node.data
                prev_node = prev_node.next
                auxA += 1
            
            #equilibrium_index -= 1
            if sumaA == sumaP:
                current_node = self.head 
                #LLega al nodo cuyo índice es el punto de equilbrio
                for a in range(equilibrium_index):
                    current_node = current_node.next
                print(auxP, equilibrium_index, sumaA, sumaP)
                return equilibrium_index
            elif equilibrium_index == 1:
                #There is no equilibrium point
                return -1
 


lista_ligada = Lista()

key_string = input("Ingresa los datos a insertar en la lista ligada.\nSeparado por comas sin espacios (ej. 2,5,3,6,7,434,2): ")

key_type_list = key_string.split(",")

#Enumerate devuelve tupla que se guarda al desempaquetar en las variabes index y value
for index, value in enumerate(key_type_list):
    print(f"{index}, {value}")
    lista_ligada.insert_at_begin(int(value))

print('INFO')
print(f"\n\nLast index: {index}, which value is: {value}")
lista_ligada.imprimir_linked_list()

print("\n")

eq = lista_ligada.equilibrium_point(index)
print(f'\n\n{eq}')