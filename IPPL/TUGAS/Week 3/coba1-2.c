#include <stdio.h>
#include <math.h>

int is_equal_with_tolerance(float x, float y) {
    return fabs(x - y) <= 0.01 * fmax(x, y); // Ketelitian 1%
}

void determine_triangle_float(float a, float b, float c) {
    // Jika ada sisi yang negatif atau 0, tidak bisa membentuk segitiga
    if (a <= 0 || b <= 0 || c <= 0) {
        printf("Tidak ada segitiga dapat dibangun.\n");
        return;
    }

    // Temukan sisi terbesar
    float max = a;
    if (b > max) max = b;
    if (c > max) max = c;

    float sum_of_two = a + b + c - max; // Penjumlahan dua sisi lainnya

    // Jika sisi terbesar lebih besar atau sama dengan penjumlahan dua sisi lainnya
    if (max >= sum_of_two) {
        printf("Tidak ada segitiga dapat dibangun.\n");
        return;
    }

    // Jika semua sisi hampir sama, segitiga sama sisi
    if (is_equal_with_tolerance(a, b) && is_equal_with_tolerance(b, c)) {
        printf("Segitiga sama sisi (Equilateral).\n");
    }
    // Jika hanya dua sisi hampir sama, segitiga sama kaki
    else if (is_equal_with_tolerance(a, b) || is_equal_with_tolerance(b, c) || is_equal_with_tolerance(a, c)) {
        printf("Segitiga sama kaki (Isosceles).\n");
    }
    // Jika kuadrat sisi terbesar = penjumlahan kuadrat dua sisi lainnya, segitiga siku-siku
    else if (is_equal_with_tolerance(max * max, a * a + b * b + c * c - max * max)) {
        printf("Segitiga siku-siku (Right triangle).\n");
    }
    // Jika tidak memenuhi syarat di atas, segitiga sembarang
    else {
        printf("Segitiga sembarang (Scalene).\n");
    }
}

int main() {
    float a, b, c;
    printf("Masukkan tiga bilangan pecahan a, b, c: ");
    scanf("%f %f %f", &a, &b, &c);

    determine_triangle_float(a, b, c);
    
    return 0;
}
