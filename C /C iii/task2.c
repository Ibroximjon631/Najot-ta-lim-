#include <stdio.h>

int main() {
    int number, first_number, second_number, third_number;

    printf("Iltimos, uch xonali son kiriting: ");
    scanf("%d", &number);

    if (number < 100 || number > 999) {
        printf("Hatolik: Iltimos faqat 3 xonali musbat son kiriting.\n");
        return 1;
    }

    first_number = number / 100;         
    second_number = (number / 10) % 10;  
    third_number = number % 10;


    printf("Kiritilgan son: %d\n", number);
    printf("Birinchi raqam (Yuzlik): %d\n", first_number);
    printf("Ikkinchi raqam (O'nlik): %d\n", second_number);
    printf("Uchinchi raqam (Birlik): %d\n", third_number);

    return 0;
}