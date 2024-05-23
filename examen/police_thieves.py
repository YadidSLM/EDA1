import random
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
            self.head.next = self.tail
            self.head.prev = self.tail
            self.tail.next = self.head
            self.tail.prev = self.head
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head.prev = new_node
            self.head = new_node
    
    #First last, del primero al último
    def print_CDLL_FL(self):
        temp = self.head
        print("Lista del último al primero: ")
        while temp != self.head.prev:
            if temp == self.head:
                print(temp.data)
            temp = temp.next
            print(temp.data)

    #Last first, del último ingresado al primero
    def print_CDLL_LF(self):
        temp = self.tail
        while temp != self.tail.next:
            if temp == self.tail:
                print(temp.data)
            temp = temp.prev
            print(temp.data)
    #posDes posición desconocida
    def posicion(self, posDes):
        temp = self.tail
        pos = 0
        encontrado = False
        while encontrado == False:
            if temp == posDes:
                encontrado = True
                return (pos, temp.data)
            else:
                temp = temp.prev
                pos += 1

def maxT_capturados(k, cdll=Lista()):
    temp = cdll.head
    #Si k elemento de P por derecha es T
    if temp.data == 'P':
        poli = temp.data
        posP = cdll.posicion(poli)
        for i in range(k):
            temp = temp.next
        if temp.data == 'T':
            posT = cdll.posicion(temp)
            atrapados_PT = [(posP, posT)]
            print(atrapados_PT)
        else:
            temp = temp.next
    elif temp.data != 'T':
        poli = temp.data
        posP = cdll.posicion(poli)
        for i in range(k):
            temp = temp.prev
        if temp.data == 'T':
            posT = cdll.posicion(temp)
            atrapados_PT = [(posP, posT)]
            print(atrapados_PT)
        else:
            temp = temp.prev
    else:
        temp = temp.next


                

#lista=Lista() es para que dentro de la función se reconozcan los métodos de la CDLL
def llenar_lista_PT_rand(lista=Lista()):
    #5 <= n <= 15
    elemetos = random.randrange(5,16)
    policias = random.randrange(1, elemetos)
    ladrones = elemetos - policias 
    print(f'Elementos: {elemetos}   Policias: {policias}    Thiefs: {ladrones}')
    #Comprobar
    print(f'\nSuma de P y T es la total de elementos: {elemetos == (policias + ladrones)}\n')
    #Si es 0 que se agregue un policìa, si 1 un ladrón y se resta la cantidad de policías y ladornes respectivamente.
    while policias + ladrones != 0:
        poli_or_ladron = random.randrange(2)
        if poli_or_ladron == 0 and policias > 0:
            lista.insert_at_begin('P')
            print("P insertado")
            policias -= 1
        elif poli_or_ladron == 1 and ladrones > 0:
            lista.insert_at_begin('T')
            print("T insertado")
            ladrones -= 1
    print(f"\nPolicías: {policias}, Ladrones: {ladrones}\n")

cdll = Lista()
llenar_lista_PT_rand(cdll)
cdll.print_CDLL_FL()
maxT_capturados(2, cdll)
# print('\n')
# cdll.print_CDLL_LF()