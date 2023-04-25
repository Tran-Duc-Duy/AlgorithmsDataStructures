#include <stdio.h>

int main() {
    int n, src[100000], height[100000], maxHeight = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &src[i]);
        height[i] = 0;
    }
    for (int i = 0; i < n; i++) {
        int p = i;
        while (p != -1) {
            if (height[p] != 0) {
                height[i] += height[p];
                break;
            }
            height[i]++;
            p = src[p];
        }
        maxHeight=height[i] > maxHeight?height[i]:maxHeight;
    }
    printf("%d", maxHeight);
    return 0;
}