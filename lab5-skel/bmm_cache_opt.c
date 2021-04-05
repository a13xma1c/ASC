#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
 
void BMMultiply(int n, double* a, double* b, double* c)
{
    int bi=0;
    int bj=0;
    int bk=0;
    int i=0;
    int j=0;
    int k=0;
    int blockSize=64; 
 
    for(bi=0; bi<n; bi+=blockSize)
        for(bj=0; bj<n; bj+=blockSize)
            for(bk=0; bk<n; bk+=blockSize)
                for(i=0; i<blockSize; i++)
                    for(j=0; j<blockSize; j++)
                        for(k=0; k<blockSize; k++)
                            c[bi+i+n*(bj+j)] += a[bi+i+n*(bk+k)]*b[bk+k+n*(bj+j)];
}
 
int main(void)
{
    int n;
    int numreps = 10;
    int i=0;
    int j=0;
    struct timeval tv1, tv2;
    double elapsed;
    n = 500;
    // allocate memory for the matrices
    
    double *A = (double *)calloc(n * n, sizeof(double));
    double *B = (double *)calloc(n * n, sizeof(double));
    double *C = (double *)calloc(n * n, sizeof(double));
 
 
    // Initialize matrices A & B
    for(i=0; i<n; i++)
    {
        for(j=0; j<n; j++)
        {
            A[i + j * n] = 1;
            B[i + j * n] = 2;
        }
    }
 
    //multiply matrices
 
    printf("Multiply matrices %d times...\n", numreps);
    for (i=0; i<numreps; i++)
    {
        gettimeofday(&tv1, NULL);
        BMMultiply(n,A,B,C);
        gettimeofday(&tv2, NULL);
        elapsed += (double) (tv2.tv_sec-tv1.tv_sec) + (double) (tv2.tv_usec-tv1.tv_usec) * 1.e-6;
        memset(C, 0, n*n);
    }
    printf("Time = %lf \n",elapsed);
 
    //deallocate memory for matrices A, B & C
    // free(A);
    // free(B);
    // free(C);
    return 0;
}