#include <stdio.h>

int main() {
    int number;
    int a, b, c, d; 
    int result;

    printf("Iltimos, to'rt xonali son kiriting: ");
    scanf("%d", &number);


    if (number < 1000 || number > 9999) {
        printf("Xatolik: Iltimos faqat 4 xonali musbat son kiriting.\n");
        return 1;
    }

    a = number / 1000;           
    b = (number / 100) % 10;   
    c = (number / 10) % 10;     
    d = number % 10;             


    result = (a + d) - (b + c);

   
    printf("Natija: (%d + %d) - (%d + %d) = %d\n", a, d, b, c, result);

    return 0;
}
