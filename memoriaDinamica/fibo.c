#define _POSIX_C_SOURCE 199309L
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

long long current_timestamp()
{
    struct timespec te;
    clock_gettime(CLOCK_REALTIME, &te);
    return te.tv_nsec;
}

//Por referencia
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
    
    long long begin = current_timestamp();

    int elementos;
    printf("\n\nFibonacci\n\n");
    printf("Ingresa el numero del elemento de la serie de fibonacci a mostrar: ");
    scanf("%i", &elementos);
    unsigned long long int fib[elementos], *apFib = &fib[0];
    //Por referencia
    fibonacci(apFib, elementos);
    printf("\nValor del elemento ingresado: %llu\n", fib[elementos - 1]);

    long long end = current_timestamp();
    double timeProceso = (end - begin) / 1000000000.0; // Convertir de nanosegundos a segundos
    printf("Tiempo que tarda la ejecucion: %lf\n", timeProceso);

    return 0;
}