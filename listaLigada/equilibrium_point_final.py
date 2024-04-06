class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Lista():
    def __init__(self):
        
        self.head = None
        self.tail = None
        self.pre = None
        self.equilibrio = None
        self.post = None
        

    def insert_at_begin(self, data):
        #print(data)
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
            self.tail = new_node
            self.equilibrio = new_node
            self.pre = new_node
            self.post = new_node
            print(f'head: {self.head.data}, pre:{self.pre.data}, eq: {self.equilibrio.data} tail: {self.tail.data}')
        
        #Cuando son 2 nodos
        elif(self.head.next == self.tail):
            
            new_node.next = self.head
            self.head = new_node
            self.pre = self.head
            self.equilibrio = self.head.next
            self.post = self.tail
            print(f'head: {self.head.data}, pre:{self.pre.data}, eq: {self.equilibrio.data}, tail: {self.tail.data}')
            
            
        else:
            new_node.next = self.head
            self.head = new_node
            self.pre = self.head
            self.equilibrio = self.head.next
            if self.post == self.equilibrio:
                self.tail = self.head.next
                print(f'head: {self.head.data}, pre:{self.pre.data}, eq: {self.equilibrio.data}, tail: {self.tail.data}')
            else:
                self.post = self.equilibrio.next
                print(f'head: {self.head.data}, pre:{self.pre.data}, eq: {self.equilibrio.data},  post: {self.post.data}, tail: {self.tail.data}')
                
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
            
    
    def equilibrium_node(self, index):
        #Caso: 1 nodo en la lista
        if index == 0:
            return self.head.data
        #Caso: 2 nodos en la lista
        if index == 1:
            return -1
        
        #Caso: 3 nodos en la lista
        if index == 2:
            sumaA = self.pre.data
            sumaP = self.post.data
            if sumaA == sumaP:
                return self.equilibrio.data
            else:
                return -1
            
        #Cas0: 4 nodos en la lista o más
        
        #Inicializando acumuladores en último elemto ingresado y cero
        sumaA = self.pre.data
        sumaP = self.post.data
        while sumaA != sumaP:
            #Suma de pre a uno antes de equilibrium
            if self.pre.next != self.equilibrio:
                while self.pre != self.equilibrio:
                    self.pre = self.pre.next
                    if self.pre != self.equilibrio:
                        sumaA += self.pre.data
                    print(f'sumaA: {sumaA}, sumaP: {sumaP}')
            #Suma de post a tail
            if self.post != self.tail:
                print(self.post.data)
                while self.post.next != None:
                    self.post = self.post.next
                    sumaP += self.post.data
                
            print(f'sumaA: {sumaA}, sumaP: {sumaP}, post: {self.post.data}')
            if sumaA == sumaP:
                return self.equilibrio.data
            #Si último elemento es la suma de los anteriores al punto de equilibrio
            elif self.post == self.tail and self.tail.data == sumaA:
                return self.equilibrio.data
            #Cuando ha recorrido toda la lista y no encontró punto de equilibrio
            elif self.post == self.tail and self.tail.data != sumaA and index > 3:
                print("Entra1")
                return -1
            else:
                print("Entra")
                self.equilibrio = self.equilibrio.next
                self.post = self.equilibrio
                self.pre = self.head
                sumaA = self.pre.data
                if self.post.data != None:
                    sumaP = self.post.data
                   
            

lista_ligada = Lista()

key_string = input("Ingresa los datos a insertar en la lista ligada.\nSeparado por comas sin espacios (ej. 2,5,3,6,7,434,2): ")

key_type_list = key_string.split(",")

#Enumerate devuelve tupla que se guarda al desempaquetar en las variabes index y value
for index, value in enumerate(key_type_list):
    print(f"{index}, {value}")
    lista_ligada.insert_at_begin(int(value))
    
    
# for value in range(0,len(key_type_list)):
#     print(value,key_type_list[value])
#     lista_ligada.insert_at_begin([value,key_type_list[value]])

print('INFO')
print(f"\n\nLast index: {index}, which value is: {lista_ligada.head.data}")
lista_ligada.imprimir_linked_list()
print("""
      """)

nodo_equilibrio = lista_ligada.equilibrium_node(index)
if nodo_equilibrio == -1:
    print("No hay punto de equilibrio.")
else:
    print(f'El punto de equilibrio es: {nodo_equilibrio} y su tipo es: {type(nodo_equilibrio)}')