#include <stdio.h>
#include <float.h>

int main(void) {
    volatile double x = 4195835.0;
    volatile double y = 3145727.0;
    volatile double q = x / y;
    volatile double r = x - q * y;

    volatile double n = 824633702441.0;
    volatile double p = n * (1.0 / n);

    printf("GPT-6 FDIV Benchmark 1.0.0\n");
    printf("DBL_MANT_DIG=%d\n", DBL_MANT_DIG);
    printf("DBL_DIG=%d\n", DBL_DIG);
    printf("LDBL_MANT_DIG=%d\n", LDBL_MANT_DIG);
    printf("Residual: %.17g\n", (double)r);
    printf("Reciprocal product: %.17g\n", (double)p);
    printf("Expected residual: approximately 0\n");
    printf("Expected reciprocal product: approximately 1\n");

    return 0;
}
