#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#define CAP 20

struct colaEspera{
    int top;
    int capacity;
    int* array;
}stack;

struct colaEspera* crearColaEspera(unsigned capacity)
{
    struct colaEspera* cola = (struct colaEspera*)malloc(sizeof(struct colaEspera));
    cola->capacity = capacity;
    cola->top = -1;
    cola->array = (int*)malloc(cola->capacity * sizeof(int));
    return cola;
}

void enqueue(struct colaEspera* cola, int item)
{
    if(cola->top == cola->capacity)
        printf("Cola llena, no se puede agrgar mas.");
    cola->array[++cola->top] = item;

}

int dequeue(struct colaEspera* cola, int item)
{
    if(cola->top == -1)
        printf("Cola vacia, no se puede quitar elemento");
    else{
        return cola->array[cola->top--];
    }
}

int peek(struct colaEspera* cola)
{
    
}

int main()
{
    crearColaEspera(CAP);
    for(int i = 0; i < 6; i++)
        sleep(1000);
    
    return 0;
}