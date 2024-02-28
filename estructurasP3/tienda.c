#include <stdio.h>
struct producto{
    float precio;
    char nombre[50];
    char tipo[5][20];
};

void llenarCarrito(){
    /*Elige y escribe los productos a comprar*/
    printf("LLenar carrito");
}
void listarProductos(){
    /*Lista los productos a comprar*/
    printf("Listar productos");
}
void devolverProducto(){
    printf("Devolver carrito");
}
void pagarCarrito(){
    printf("Pagar carrito");
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