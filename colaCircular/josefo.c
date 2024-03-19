#include <stdio.h>
#include <stdlib.h>

struct colaCir{
    int tail;
    int head;
    int size;
    int capacity;
    int* array;
};

struct colaCir* crearCirQueue(int capacidad)
{
    struct colaCir* personas = (struct colaCir*)malloc(sizeof(struct colaCir));
    personas->capacity = capacidad;
    personas->size = 0;
    personas->tail = -1;
    personas->head = 0;
    personas->array = (int*)malloc(personas->capacity * sizeof(int));
    return personas;
}

int isFull(struct colaCir* P){
    return P->size == P->capacity;
}

int isEmpty(struct colaCir* P){
    return P->size == 0;
}

void enqueue (struct colaCir* p, int pItem){
    if(!isFull(p)){
        if(p->tail == p->capacity - 1)
            p->tail = 0;
        else
            p->tail++;
        p->size++;
        p->array[p->tail] = pItem;
    } else {
        printf("\nQueue llena\n");
    }
}

int dequeue (struct colaCir* p)
{
    if(!isEmpty(p))
    {
        int eliminado = p->array[p->head];
        p->size--;
        if(p->head == p->capacity - 1)
            p->head = 0;
        else
            p->head++;
        return eliminado;
    } else{
        printf("\nEsta vacio. %i\n", isEmpty(p));
    }
}
void show (struct colaCir* p)
{
    if(!isEmpty(p))
    {
        for(int i = p->tail; i >= p->head; i--)
        printf("\n%i ", p->array[i]);
        printf("\nHead: %i, Tail, %i, Size: %i, Capacidad max: %i\n", p->head, p->tail, p->size, p->capacity);
    } else {
        printf("Cola circular vacia. \n");
        printf("Head: %i, Tail, %i, Size: %i, Capacidad max: %i\n", p->head, p->tail, p->size, p->capacity);
    }
    
}
// int main(int argc, char const *argv[]){
int main(int argc, char const *argv[])
{
    struct colaCir* personas = crearCirQueue(argv[1]); //Máximo de personas en primer
    //cambiar de cadena a numero con atoi o con otra función o varios if
    return 0;
}