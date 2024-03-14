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
        cola->tail = (cola->tail + 1) % cola->capacity;
        cola->array[cola->tail] = clienteNum;
        cola->size = cola->size + 1;
        printf("\nCliente en atencion: %i\n", cola->array[cola->tail]);
    }
}

int dequeue (struct queue* cola)
{
    if(isEmpty(cola)){
        printf("\nLa cola esta vacia, no se pueden quitar elementos que no hay.\n");
        return INT_MIN;
    }
    int cli = cola->array[cola->head];
    cola->head++;
    cola->size = cola->size - 1;
    return cola->array[cola->head++];
}

int peek(struct queue* cola)
{
    if(!isEmpty(cola))
        return cola->array[cola->head];
}

int main ()
{
    struct queue* clientes = createCola(20);
    int clienteAtendido;
    enqueue(clientes, 5);
    enqueue(clientes, 2);
    enqueue(clientes, 4);
    clienteAtendido = dequeue(clientes);
    printf("\nCliente atendido: %i", clienteAtendido);
    printf("\nCLiente a ser atendido: %i", peek(clientes));

    clienteAtendido = dequeue(clientes);
    printf("\nCliente atendido: %i", clienteAtendido);
    printf("\nCLiente a ser atendido: %i", peek(clientes));
    printf("\nSize: %i, Tail: %i, Head: %i, Elemento en head: %i\n", clientes->size, clientes->tail, clientes->head, clientes->array[clientes->head]);

    return 0;
}