#include <stdio.h>
#include <stdlib.h>
//Por referencia
void fibonacci (int *a, int n)
{
    *a = 1;
    *(a + 1) = 1;
    for (int i = 0; i < n; i++)
    {
        if(i < n - 2)
            *(a + i + 2) = *(a + i) + *((a + i) + 1);
        printf("%i, ", *(a + i));
    }
}

int main(void)
{
    int elementos;
    system("cls");
    printf("\n\nFibonacci\n\n");
    printf("Ingresa el numero del elemento de la serie de fibonacci a mostrar: ");
    scanf("%i", &elementos);
    //*apFib = fib es lo mismo que *apFib = &fib[0]
    int fib[elementos];
    //Por referencia
    fibonacci(&fib[0], elementos);
    printf("\nValor del elemento ingresado: %i\n", fib[elementos - 1]);
    return 0;
}