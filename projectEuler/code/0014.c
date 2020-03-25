#include <stdio.h>
#include <math.h>
#include <omp.h>

/** Longest Collatz sequence */
/** The following iterative sequence is defined for the set of positive integers: */
/** n → n/2 (n is even) */
/** n → 3n + 1 (n is odd) */
/** Using the rule above and starting with 13, we generate the following sequence: */
/** 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 */
/** It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1. */
/** Which starting number, under one million, produces the longest chain? */
/** NOTE: Once the chain starts the terms are allowed to go above one million. */

int main () {
  long int n;
  long int rc = 1;
  long int rn = 1;
  #pragma omp parallel for shared(n)
  for (n = 3; n < 1000000; n++) {
    long int nb = n;
    /** printf("%ld ", nb); */
    long int c = 0;
    while (nb > 1) {
      if (nb % 2 == 0) {
        nb = nb/2; c += 1; 
        /** printf("(%ld)-> %ld", c, nb); */
      } else {
        nb = 3*nb + 1; c += 1; 
        /** printf("(%ld)-> %ld", c, nb); */
      }
    }
    /** printf("%ld", c); */
    printf("\n");
    if (c > rc) {
      rc = c;
      rn = n;
      /** printf("new record: %ld with chain length: %ld", rn, rc); */
    }
  }
  printf("FINAL: %ld with %ld\n", rn, rc);
}
