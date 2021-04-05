#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

double* generate_matrix(int n) {
	int i, j;
	double *mat = (double *)malloc(n * n * sizeof(double));
	
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			mat[i * n + j] = (double)(rand() % 10000) / 100.0;
		}
	}

	return mat;
}

void display_matrix(double* mat, int n) {
	int i, j;
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			printf("%.2lf ", mat[i * n + j]);
		}
		printf("\n");
	}
}

double* multiply_slow(double *a, double *b, double *c, int n) {
	int i, j, k;

	for (i = 0; i < n; i++){
		for (j = 0; j < n; j++){
			double suma = 0.0;
			for (k = 0; k < n; k++) {
				suma += a[k + i * n] * b[j + k * n];
			}
			c[i + j * n] = suma;
		}
	}

	return c;
}

double* multiply(double *a, double *b, double *c, int n) {
	int i, j, k;

	for (i = 0; i < n; i++){
		for (k = 0; k < n; k++){
			for (j = 0; j < n; j++) {
				if (c[i + j * n])
					c[i + j * n] += a[k + i * n] * b[j + k * n];
				else 
					c[i + j * n] = a[k + i * n] * b[j + k * n];
			}
		}
	}

	return c;
}

int main() {
	time_t t;
	srand((unsigned) time(&t));
	struct timeval start_f, end_f, end_s;

	int n = 50;
	double *a, *b;
	double *c = (double *)malloc(n * n * sizeof(double));
	double *d = (double *)malloc(n * n * sizeof(double));
	a = generate_matrix(n);
	b = generate_matrix(n);

	display_matrix(a, n);
	printf("\n");
	display_matrix(b, n);
	printf("\n");

	gettimeofday(&start_f, NULL);
	c = multiply(a, b, c, n);
	gettimeofday(&end_f, NULL);

	d = multiply_slow(a, b, d, n);
	gettimeofday(&end_s, NULL);

	float elapsed_f = ((end_f.tv_sec - start_f.tv_sec) * 1000000.0
		+ end_f.tv_usec - start_f.tv_usec);
	float elapsed_s = ((end_s.tv_sec - end_f.tv_sec) * 1000000.0
		+ end_s.tv_usec - end_f.tv_usec);

	display_matrix(c, n);
	printf("\n");
	display_matrix(d, n);
	printf("\n");

	printf("slow(%f us) vs fast(%f us)\n", elapsed_s, elapsed_f);

	free(a);
	free(b);
	free(c);
}