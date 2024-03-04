#include <stdio.h>
#include <string.h>
struct producto{
    float precio;
    char nombre[50];
    char tipo[20];
};

void llenarCarrito(){
    /*Elige y escribe los productos a comprar*/
    struct producto product1, product2, product3, product4, product5;
    for(int i = 0; i < 6; i++)
        strcpy(product1.tipo[i], "Salud");
    for(int i = 0; i < 9; i++)
        strcpy(product1.nombre[i], "Aspirina");
    product1.precio = 50.3;

    for(int i = 0; i < 7; i++)
        strcpy(product2.tipo[i], "Bebida");
    for(int i = 0; i < 6; i++)
        strcpy(product2.nombre[i], "Fanta");
    product2.precio = 18;

    for(int i = 0; i < 9; i++)
        strcpy(product3.tipo[i], "Alimento");
    for(int i = 0; i < 5; i++)
        strcpy(product3.nombre[i], "Taco");
    product3.precio = 15;
    
    for(int i = 0; i < 17; i++)
        strcpy(product4.tipo[i], "Electrodomestico");
    for(int i = 0; i < 8; i++)
        strcpy(product4.nombre[i], "Plancha");
    product4.precio = 129.9;

    for(int i = 0; i < 9; i++)
        strcpy(product5.tipo[i], "Limpieza");
    for(int i = 0; i < 5; i++)
        strcpy(product5.nombre[i], "Mopa");
    product5.precio = 129.9;

    printf("Sus productos son:\n\n");
    printf("%s\n", product1.nombre);
    printf("%s\n", product2.nombre);
    printf("%s\n", product3.nombre);
    printf("%s\n", product4.nombre);
    printf("%s\n", product5.nombre);


}
void listarProductos(){
    struct producto product[10];
    
}
void devolverProducto(){
    printf("Devolver producto");

}
void pagarCarrito(){
    struct producto product[10];
    printf("En total es:");
    int total = 0;
    for(int i = 0; i < 10; i++)
        total = product[i].precio + product[i++].precio;
}

int main()
{
    int opcion;
    while(opcion != 5)
    {
        printf("\n\tTienda de productos en venta\n\n");
        printf(" 1) Llenar carrito\n 2) Listar productos\n 3) Devolver producto\n 4) Pagar carrito\n 5) Salir\n");
        printf("\nQue desea hacer: ");
        scanf("%i", &opcion);
        switch (opcion)
        {
        case 1:
            llenarCarrito();
            
            break;
        case 2:
            listarProductos();
            break;
        case 3:
            devolverProducto();
            break;
        case 4:
            pagarCarrito();
            break;
        case 5:
            printf("\nBye\n");
            break;
        default:
            printf("\nIngresa una opcion entre 1 y 5\n");
            break;
        }
    }
    return 0;
}