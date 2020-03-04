#include <bits/stdc++.h>
#ifdef __cplusplus
#define EXTERN_C extern "C" {
#define EXTERN_C_END }
#else
#define EXTERN_C
#define EXTERN_C_END
#endif
using namespace std;

class Cbacken {
public:
    Cbacken(char* message) {
        _message = string(message);
    }
    void my_sort(int *arr, int n);
    void my_sort2(int *arr, int n);
private:
    int _partition(int *, int, int);
    void _quick_sort(int *, int, int);
    string _message;
};

int Cbacken::_partition(int *arr, int front, int end) {
    int pivot = arr[end];
    int i = front - 1;
    for(int j = front; j < end; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i+1], arr[end]);
    return i + 1;
}

void Cbacken::_quick_sort(int *arr, int front, int end) {
    if (front >= end) return;
    int index = _partition(arr, front, end);
    _quick_sort(arr, front, index-1);
    _quick_sort(arr, index+1, end);
}

void Cbacken::my_sort(int *arr, int n) {
    this->_quick_sort(arr, 0, n - 1);
}

void Cbacken::my_sort2(int *arr, int n) {
    sort(arr, arr + n);
}

// 封装C接口
EXTERN_C
// 創建對象
Cbacken* cbacken_new(char* mes) {
    return new Cbacken(mes);
}
void cbacken_sort(Cbacken* cb, int *arr, int n){
    cb->my_sort(arr, n);
}
void cbacken_sort2(Cbacken* cb, int *arr, int n){
    cb->my_sort2(arr, n);
}
EXTERN_C_END