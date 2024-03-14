#include <stdio.h>
#include <stdlib.h>

struct queue{
    int head, tail, size;
    unsigned capacity;
    int *array;
};

struct queue* createCola(int capacidad)
{
    struct queue* cola = (int*) malloc(capacidad * sizeof(int));
    cola->head = cola->size = cola->tail = 0;
    cola->capacity = capacidad;
    cola->array = (int*) malloc(cola->capacity * sizeof(int));
    return cola;
}

int isFull(struct queue* queue)
{
	return (queue->size == queue->capacity);
}

// Queue is empty when size is 0
int isEmpty(struct queue* queue)
{
	return (queue->size == 0);
}

void enqueue(struct queue* cola, int clienteNum)
{
    if(isFull)
        printf("\nEsta llena la cola no se pueden insertar mas\n");
    else{
        cola->tail++;
        cola->array[cola->tail] = clienteNum;
        cola->size++;
        printf("\n%i Atendiendo cliente\n");
    }
}

int dequeue (struct queue* cola)
{
    int clienteAtendido;
    if(isEmpty)
        printf("\nLa cola esta vacia, no se pueden quitar elementos que no hay.\n");
    else{
        clienteAtendido = cola->array[cola->head];
        cola->head++;
        cola->size--;
    }
    return clienteAtendido;
}

int peek()
{
    
}

int main ()
{
    struct queue* clientes = crearCola(20);
    return 0;
}