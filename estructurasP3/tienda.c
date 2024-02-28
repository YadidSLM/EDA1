#include <stdio.h>
struct producto{
    float precio;
    char nombre[50];
    char tipo[5];
    int cantidad;
};

void llenarCarrito(){
    /*Elige y escribe los productos a comprar*/
    struct producto product[10];
    char tipos[5][20] = {"Salud", "Bebidas", "Alimentos", "Electrodomesticos", "Limpieza"};
    int option = 0, numProd = 0;

    printf("\n\n1)Nuevo producto (10 max)\n2)Añadir otro producto existenete.\n3)Volver\n");
    scanf("%i", &option);

    if(option == 1){
        product[numProd].cantidad = 1;
        printf("\n\nTipo de producto:");
        printf("\na)Salud\nb)Bebidas\nc)Alimentos\nd)Electrodomesticos\ne)Limpieza\n");
        scanf("%c", product[numProd].tipo);
        if(product[numProd].tipo == 'a' || product[numProd].tipo == 'd')
        {
            product[numProd].precio = 387;
            printf("\nIngresa el nombre del producto: ");
            fgets(product[numProd].nombre, 50, stdin);
        }
        else if(product[numProd].tipo == 'b' || product[numProd].tipo == 'c')
        {
            product[numProd].precio = 70.5;
            printf("\nIngresa el nombre del producto: ");
            fgets(product[numProd].nombre, 50, stdin);
        }
        else if(product[numProd].tipo == 'e')
        {
            product[numProd].precio = 50;
            printf("\nIngresa el nombre del producto: ");
            fgets(product[numProd].nombre, 50, stdin);
        }
        else{
            printf("\nCaracter no valido.\n");
        }
        
    } else if (option == 2){
        printf("\nEilge el numero del producto a añadir cantidad: ");
        scanf("%i", &numProd);
        product[numProd].cantidad++;
    } else if(option == 3){
        printf("\nRegresando a menu principal.\n");
    }


}
void listarProductos(){
    /*Lista los productos a comprar*/
    printf("Listar productos");
}
void devolverProducto(){
    printf("Devolver producto");
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