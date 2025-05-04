#include <stdio.h>

int main() {
    int a, b;
    int count;


    printf("a ni kiriting: ");
    scanf("%d", &a);

    printf("b ni kiriting: ");
    scanf("%d", &b);


    if (a >= b) {
        printf("Xatolik: a soni b dan kichik bo'lishi kerak.\n");
        return 1;
    }

    count = b - a - 1;

    printf("%d dan %d ga qadar %d ta son bor\n", a, b, count);

    return 0;
}
