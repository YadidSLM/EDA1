#include <stdio.h>

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
//Por valor
void factorial(int fac)
{
  int r = fac, i;
  for(i = (fac - 1); i > 0; i--)
    r = r * i;
  printf("\nEl factorial de %i es %i\n", fac, r);
}

int main(void)
{
  int elementos, opcion;
  while(opcion != 3)
  {
    printf("\n\n\nCalculadora de funciones: \n");
    printf(" 1) Fibonacci\n 2) Factorial\n 3) Salir\n\n\n");
    scanf("%i", &opcion);
    if(opcion == 1)
    {
      printf("Ingresa el numero del elemento de la serie de fibonacci a mostrar: ");
      scanf("%i", &elementos);
      int fib[elementos], *apFib = &fib[0];
      //Por referencia
      fibonacci(apFib, elementos);
      printf("\nValor del elemento ingresado: %i\n", fib[elementos - 1]);
    }
    else if(opcion == 2)
    {
      int fact;
      printf("Ingresa el numero del que desea sacar factorial: ");
      scanf("%i", &fact);
      //Por valor
      factorial(fact);
    }
    else if(opcion == 3)
    {
      printf("\nBye\n");
    }
    else if(opcion != 1 && opcion != 2 && opcion != 3)
    {
      printf("\nIngresa 1, 2 o 3\n");
    }
  }
  return 0;
}