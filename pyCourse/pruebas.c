#include <stdio.h>

int main()
{
    char contA[5] = {'a', 'm', 'o', 'r', '!'}, contE[5] = {'c', 'l', 'o', 'r', '!'};
    char *arr[2] = {&contA[0], &contE[0]};
    //Compara lo que hay dentro de la primera localidad del arreglo
    char pL = contA[0] /* *contA = contA[0]*/, pLB = contE[2];
    int bool = *contA == *contE;
    printf("%i, %c, %c\n", bool, pL, pLB);
    printf("%s", arr[1]);
    return 0;
}