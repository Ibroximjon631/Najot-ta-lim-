#include <stdio.h>

int main() {
    int number;
    int onlik, birlik;

 
    printf("Iltimos, 2 xonali son kiriting: ");
    scanf("%d", &number);

    if (number < 10 || number > 99) {
        printf("Xatolik: Iltimos faqat 2 xonali son kiriting.\n");
        return 1;
    }


    onlik = number / 10;
    birlik = number % 10;


    number = birlik * 10 + onlik;


    printf("Natija: %d\n", number);

    return 0;
}
