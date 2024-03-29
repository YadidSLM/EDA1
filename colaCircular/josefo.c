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

int peekIn(struct colaCir* p, int n, int max)
{
    if(n >= 0 && n < max)
        return p->array[n];
    else
        return 0;
}

void josefo(struct colaCir* p, int n, int max)
{
    int eliminadosT = (max - n + 1), sigE = n - 1 + n, anadirEx = 0, nSobrevivientes = n - 1;
    int orden[eliminadosT];
    printf("\neliminadosT: %d, sigueE: %d, sobr: %d\n", eliminadosT, sigE, nSobrevivientes);
    if(n > max)
        printf("Nadie es eliminado porque no existe la persona en la posiciòn %d", n);
    if(n == 1)
        show(p); // Todos son eliminados, se muestra el total de los elementos de la cola
    if(n > 1 && n <= max)
    {
        for(int i = 0; i < eliminadosT; i++)
        {
            if(i == 0)
                orden[i] = peekIn(p, n - 1, max); //Primer elemento eliminado
            if(i > 0){
                if((sigE) > max){
                    anadirEx = sigE - max;
                    n = 0;
                    n + anadirEx;
                    orden[i] = peekIn(p, n, max);
                }
                orden[i] = peekIn(p, n, max);
                printf("%d, ", orden[i]);
            }
            //printf("%d, ", orden[i]);
            printf("\norden 0: %d, eliminadosT: %d, i: %d, sigueE: %d, sobr: %d", orden[1], eliminadosT, i, sigE, nSobrevivientes);
        }
    }

}

// int main(int argc, char const *argv[]){
int main(int argc, char const *argv[])
{
    int max = 8, n = 5;
    struct colaCir* personas = crearCirQueue(max); //Máximo de personas en primer
    //cambiar de cadena a numero con atoi o con otra función o varios if
    for(int i = 1; i <= max; i++)
        enqueue(personas, i);
    show(personas);
    josefo(personas, n, max);
    return 0;
}