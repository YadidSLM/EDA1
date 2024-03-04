/*Equipo: Los algoritmólogos EDA 1
  Almacenamiento en tiempo de ejecución.
*/
#define _POSIX_C_SOURCE 199309L
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>
void fibonacci (unsigned long long int *a, int n)
{
  *a = 1;
  *(a + 1) = 1;
  for (unsigned long long int i = 0; i < n; i++)
  {
    if(i < n - 2)
      *(a + i + 2) = *(a + i) + *((a + i) + 1);
    printf("%llu, ", *(a + i));
  }
}
int main(void)
{
    /**************Programa fibonacci*******************/
    int elementos;
    printf("\n\nFibonacci\n\n");
    printf("Ingresa el numero del elemento de la serie de fibonacci a mostrar: ");
    scanf("%i", &elementos);

    //Forma 1
    clock_t ini, fin;
    double tiempo;
    ini = clock();
    unsigned long long int fib[elementos], *apFib = &fib[0];

    //Inicio 
    //Forma 3
    struct _FILETIME begin2, creation_time, kernel_time, exit_time;
    GetProcessTimes(GetCurrentProcess(), &creation_time, &exit_time, &kernel_time, &begin2);

    //Forma 2
    struct timespec begin;
    clock_gettime(CLOCK_REALTIME, &begin);

    //Por referencia
    fibonacci(apFib, elementos);
    printf("\nValor del elemento ingresado: %llu\n", fib[elementos - 1]);
    /**************Programa fibonacci*******************/

    //Fin
    //Forma 1
    fin = clock();
    tiempo = (double)(fin - ini) / CLOCKS_PER_SEC;
    printf("\n\nTiempo de ejecucion: %fs\n", tiempo);

    //Forma 2
    struct _FILETIME end2;
    GetProcessTimes(GetCurrentProcess(), &creation_time, &exit_time, &kernel_time, &end2);
    
    //Forma 3
    ULARGE_INTEGER ulBegin2;
    ulBegin2.LowPart = begin2.dwLowDateTime;
    ulBegin2.HighPart = begin2.dwHighDateTime;

    ULARGE_INTEGER ulEnd2;
    ulEnd2.LowPart = end2.dwLowDateTime;
    ulEnd2.HighPart = end2.dwHighDateTime;

    double time_spent2 = (ulEnd2.QuadPart - ulBegin2.QuadPart)/10000000000.0;
    /**********************/

    struct timespec end;
    clock_gettime(CLOCK_REALTIME, &end);
    double time_spent = (end.tv_sec - begin.tv_sec) + (end.tv_nsec - begin.tv_nsec)/1000000000.0;

    printf("\n\nEl tiempo que tardo la ejecucion fue de: %lf\n", time_spent);
    printf("\n\nEl tiempo que tardo la ejecucion en CPU fue de: %llf\n", time_spent2);

    return 0;
}