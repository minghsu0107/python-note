#include <stdio.h>
#include <stdlib.h>
#ifdef __cplusplus
#define EXTERN_C extern "C" {
#define EXTERN_C_END }
#else
#define EXTERN_C
#define EXTERN_C_END
#endif

struct double_row_element_t {
    double value;
    int col_index;
    struct double_row_element_t * next_element;
};

typedef struct double_row_element_t double_row_element;

typedef struct {
    int nrows;
    int ncols;
    int nnz;
    double_row_element** rows;
} double_sparse_matrix;

EXTERN_C
double_sparse_matrix * initialize_matrix(int nrows, int ncols);
int free_matrix(double_sparse_matrix * matrix);
int set_value(double_sparse_matrix * matrix, int row, int col, double value);
double get_value(double_sparse_matrix* matrix, int row, int col);
EXTERN_C_END

double_sparse_matrix * initialize_matrix(int nrows, int ncols) {
    int i;
    double_sparse_matrix* new_matrix;
    new_matrix = (double_sparse_matrix *) malloc(sizeof(double_sparse_matrix));
    new_matrix->rows= (double_row_element **) malloc(sizeof(double_row_element *)*nrows);
    for (i = 0; i < nrows; i++) {
        (new_matrix->rows)[i]=(double_row_element *) malloc(sizeof(double_row_element));
        (new_matrix->rows)[i]->value = 0;
        (new_matrix->rows)[i]->col_index = 0;
        (new_matrix->rows)[i]->next_element = 0;
    }
    new_matrix->nrows = nrows;
    new_matrix->ncols = ncols;
    new_matrix->nnz = 0;
    return new_matrix;
}

int free_matrix(double_sparse_matrix * matrix) {
    int i;
    double_row_element* next_element;
    double_row_element* current_element;
    for (i = 0; i < matrix->nrows; i++) {
        current_element = (matrix->rows)[i];
        while (current_element->next_element != 0) {
            next_element = current_element->next_element;
            free(current_element);
            current_element = next_element;
        }
        free(current_element);
    }
    free(matrix->rows);
    free(matrix);
    return 1;
}

int set_value(double_sparse_matrix * matrix,int row, int col, double value) {
    int i;
    i = 0;
    double_row_element* current_element;
    double_row_element* new_element;

    if (row> matrix->nrows || col > matrix->ncols || row < 0 || col < 0)
        return 1;

    current_element = (matrix->rows)[row];
    while (1) {
        if (current_element->col_index == col) {
            current_element->value=value;
            return 0;
        }

        else if (current_element->next_element != 0) {
            if (current_element->next_element->col_index <= col)
                current_element = current_element->next_element;
            else {
                new_element = (double_row_element *) malloc(sizeof(double_row_element));
                new_element->value = value;
                new_element->col_index = col;
                new_element->next_element = current_element->next_element;
                current_element->next_element = new_element;
                return 0;
            }
        }
        else {
            new_element = (double_row_element *) malloc(sizeof(double_row_element));
            new_element->value = value;
            new_element->col_index = col;
            new_element->next_element = 0;
            current_element->next_element = new_element;
            break;
        }

    }
    return 0;
}

double get_value(double_sparse_matrix* matrix, int row, int col) {
    int i;
    double_row_element * current_element;
    if (row> matrix->nrows || col > matrix->ncols || row < 0 || col < 0)
        return 0.0;

    current_element = (matrix->rows)[row];
    while (1) {
        if (current_element->col_index == col) {
            return current_element->value;
        }
        else {
            if (current_element->col_index < col && current_element->next_element != 0)
                current_element = current_element->next_element;
            else
                return 0.0;
        }
    }
}
