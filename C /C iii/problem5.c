#include <stdio.h>

int main() {
    int age, experience, dateOfBirth;

    printf("Yoshingizni kiriting: ");
    scanf("%d", &age);

    printf("Ish tajribangizni (yil) kiriting: ");
    scanf("%d", &experience);

    printf("Tug'ilgan yilingizni kiriting: ");
    scanf("%d", &dateOfBirth);

  
    printf("Mening ismim Kimdr. Men %d-yilda Qoqonda tug'ilganman. ", dateOfBirth);
    printf("Yoshim %dda. Hozirda %d yillik ish tajribasiga egaman.\n", age, experience);

    return 0;
}
