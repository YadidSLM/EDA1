#include <stdio.h>
#include <string.h>

struct producto {
    float precio;
    char nombre[50];
    char tipo[20];
};

void llenarCarrito(struct producto *product, const char *tipo, const char *nombre, float precio) {
    strcpy((*product).tipo, tipo);
    strcpy((*product).nombre, nombre);
    (*product).precio = precio;
}   

void listarProductos(struct producto *products, int numProductos) {
    printf("Sus productos son:\n\n");
    for (int i = 0; i < numProductos; i++) {
        printf("Nombre: %s\n", products[i].nombre);
        printf("Tipo: %s\n", products[i].tipo);
        printf("Precio: %.2f\n", products[i].precio);
        printf("\n");
    }
}

void devolverProducto() {
    printf("Devolver producto\n");
}

void pagarCarrito(struct producto *products, int numProductos) {
    printf("En total es:\n");
    float total = 0;
    for (int i = 0; i < numProductos; i++) {
        total += products[i].precio;
    }
    printf("Total: %.2f\n", total);
}

int main() {
    struct producto carrito[5];

    int opcion;
    int contadorProductos = 0;

    while (opcion != 5) {
        printf("\n\tTienda de productos en venta\n\n");
        printf(" 1) Llenar carrito\n 2) Listar productos\n 3) Devolver producto\n 4) Pagar carrito\n 5) Salir\n");
        printf("\nQue desea hacer: ");
        scanf("%i", &opcion);

        switch (opcion) {
            case 1:
                if (contadorProductos < 5) {
                    char tipo[20];
                    char nombre[50];
                    float precio;

                    printf("Ingrese el tipo: ");
                    scanf("%s", tipo);
                    printf("Ingrese el nombre: ");
                    scanf("%s", nombre);
                    printf("Ingrese el precio: ");
                    scanf("%f", &precio);

                    llenarCarrito(&carrito[contadorProductos], tipo, nombre, precio);
                    contadorProductos++;
                } else {
                    printf("El carrito está lleno.\n");
                }
                break;

            case 2:
                listarProductos(carrito, contadorProductos);
                break;

            case 3:
                devolverProducto();
                break;

            case 4:
                pagarCarrito(carrito, contadorProductos);
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
