
#include <stdio.h>

int sum(int digits){
    int k = digits;
    int totalsum =0;
    while(k>0){
        int d = k%10;
        totalsum += d;
        k = k/10;
    }
    return totalsum;
}
int swap(int *a, int *b){
   int t=*a;
    *a=*b;
    *b=t;
}
int divide(int arr[], int low,int high){
    int piv = sum(arr[high]);
    int i = low-1;
    for(int j=low;j<high;j++){
        if(sum(arr[j])<piv){
            i++;
            swap(&arr[i],&arr[j]);
        }
    }
    swap(&arr[i+1],&arr[high]);
    return i+1;
}
int quicksort(int arr[], int low, int high){
    if(low<high){
        int p = divide(arr,low,high);
        quicksort(arr,low,p-1);
        quicksort(arr,p+1,high);
    }
}
int main()
{
    int arr[]={129,990,856,738,11,222,409,177,363,600};
        int n = sizeof(arr)/sizeof(arr[0]);
    quicksort(arr,0,n-1);
    for(int i=0;i<10;i++){
        printf("%d\n",arr[i]);
    }

    return 0;
}
