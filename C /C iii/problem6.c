#include <stdio.h>

int main() {
    float baholar[5];
    float summa = 0.0;
    float ortacha;
    int i;

    printf("Iltimos, 5 ta fandan olgan baholaringizni kiriting:\n");

    for(i = 0; i < 5; i++) {
        printf("%d-fan bahosi: ", i + 1);
        scanf("%f", &baholar[i]);
        summa += baholar[i];
    }

    ortacha = summa / 5;

    printf("\nSizning o'rtacha bahoyingiz: %.2f\n", ortacha);

    return 0;
}
