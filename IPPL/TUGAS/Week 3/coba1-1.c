#include <stdio.h>

void determine_triangle(int a, int b, int c) {
    // Jika ada sisi yang negatif atau 0, tidak bisa membentuk segitiga
    if (a <= 0 || b <= 0 || c <= 0) {
        printf("Tidak ada segitiga dapat dibangun.\n");
        return;
    }

    // Temukan sisi terbesar
    int max = a;
    if (b > max) max = b;
    if (c > max) max = c;

    int sum_of_two = a + b + c - max; // Penjumlahan dua sisi lainnya

    // Jika sisi terbesar lebih besar atau sama dengan penjumlahan dua sisi lainnya
    if (max >= sum_of_two) {
        printf("Tidak ada segitiga dapat dibangun.\n");
        return;
    }

    // Jika semua sisi sama, segitiga sama sisi
    if (a == b && b == c) {
        printf("Segitiga sama sisi (Equilateral).\n");
    }
    // Jika hanya dua sisi yang sama, segitiga sama kaki
    else if (a == b || b == c || a == c) {
        printf("Segitiga sama kaki (Isosceles).\n");
    }
    // Jika kuadrat sisi terbesar = penjumlahan kuadrat dua sisi lainnya, segitiga siku-siku
    else if (max * max == (sum_of_two - max) * (sum_of_two - max) + (a * a + b * b + c * c - max * max)) {
        printf("Segitiga siku-siku (Right triangle).\n");
    }
    // Jika tidak memenuhi syarat di atas, segitiga sembarang
    else {
        printf("Segitiga sembarang (Scalene).\n");
    }
}

int main() {
    int a, b, c;
    printf("Masukkan tiga bilangan bulat a, b, c: ");
    scanf("%d %d %d", &a, &b, &c);

    determine_triangle(a, b, c);
    
    return 0;
}
