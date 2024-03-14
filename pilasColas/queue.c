#include <stdio.h>
#include <stdlib.h>

struct queue{
    int head, tail, size;
    unsigned capacity;
    int *array;
};

struct queue* createCola(unsigned capacidad)
{
    struct queue* cola = (struct queue*) malloc(sizeof(struct queue));
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
    if(isFull(cola))
        printf("\nEsta llena la cola no se pueden insertar mas: %i\n", isFull(cola));
    else{
        cola->tail++;
        cola->array[cola->tail] = clienteNum;
        cola->size++;
        printf("\nCliente en atencion: %i\n", cola->array[cola->tail]);
    }
}

int dequeue (struct queue* cola)
{
    int clienteAtendido;
    if(isEmpty(cola))
        printf("\nLa cola esta vacia, no se pueden quitar elementos que no hay.\n");
    else{
        clienteAtendido = cola->array[cola->head];
        cola->head++;
        cola->size--;
    }
    return clienteAtendido;
}

int peek(struct queue* cola)
{
    return cola->array[cola->head];
}

int main ()
{
    struct queue* clientes = createCola(20);
    enqueue(clientes, 5);

    return 0;
}