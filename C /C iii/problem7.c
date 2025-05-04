#include <stdio.h>

int main() {
    int a;
    int yuzlik, onlik, birlik;
    int teskari_son;

    printf("Uch xonali son kiriting: ");
    scanf("%d", &a);


    if (a < 100 || a > 999) {
        printf("Xatolik: Iltimos faqat uch xonali son kiriting.\n");
        return 1;
    }

    yuzlik = a / 100;
    onlik = (a / 10) % 10;
    birlik = a % 10;


    teskari_son = birlik * 100 + onlik * 10 + yuzlik;


    printf("Teskari yozilgan son: %d\n", teskari_son);

    return 0;
}
