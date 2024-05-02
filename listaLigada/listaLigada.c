#include <stdio.h>

//  Para la memoria dinámica (malloc) está en esa biblioteca
#include <stdlib.h>

/*      Estructura nodo     */
//Despues de las llaves con el typedef esa palabra es un alias de struct node
//Sin el typedef es una instacia de struct node, así struct node Node
typedef struct node{
    int dato;
    struct node* liga;
}nodo;

//Variables globales
nodo* head = NULL;
nodo *currentNode = NULL;

void insertarInicio(int data){
    printf("Entra");
    nodo* newNode = (nodo*) malloc(sizeof(nodo));
    newNode->dato = data;
    if(head->liga == NULL){
        head = newNode;
        printf("%d\n", head->dato);
    }else{
        newNode->liga = head;
        head = newNode;
        printf("%d\n", head->dato);
    }
}

void mostrarLista(){
    currentNode = head;
    while(currentNode->liga != NULL){
        printf("%d\n", currentNode->dato);
        currentNode = currentNode->liga;
    }

}

int main(){
    insertarInicio(1);
    insertarInicio(2);
    insertarInicio(3);
    insertarInicio(4);
    //mostrarLista();
    return 0;
}