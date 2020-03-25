/** The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. */
/** Find the sum of all the primes below two million. */

#include <stdio.h>
#include <math.h>

long int main() {
  long int a = 2000000;
  long int s = 5;
  for (long int i = 5; i < a; i += 2 ) {
    int stat = 0;
    for (long int j = 3; j <= sqrt(i); j = j+2) {
      if (i % j == 0) {
        stat += 1;
        break;
      } else {
        continue;
      }
    }
    if (stat == 0) {
      printf("%ld\n", i);
      s += i;
      printf(" and sum: %ld\n", s);
    }
  }
  printf("Sum: %ld\n", s);
}
