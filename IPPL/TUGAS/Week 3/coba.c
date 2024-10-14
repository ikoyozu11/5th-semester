#include <stdio.h>

int main() {
    int computer_amount, peripheral_amount;
    float base_fee = 0, additional_fee = 0, total_fee = 0;
    char service_time, drop_pickup;

    // Input jumlah komputer dan periferal
    printf("Masukkan Jumlah Komputer: ");
    scanf("%d", &computer_amount);

    printf("Masukkan Jumlah Periferal: ");
    scanf("%d", &peripheral_amount);

    // Tentukan base fee dan additional fee berdasarkan jumlah komputer
    if (computer_amount == 1 || computer_amount == 2) {
        base_fee = 50;
        additional_fee = 0;
    } else if (computer_amount >= 3 && computer_amount <= 10) {
        base_fee = 100;
        additional_fee = 10 * peripheral_amount;
    } else if (computer_amount > 10) {
        base_fee = 500;
        additional_fee = 10 * peripheral_amount;
    }

    // Input apakah servis dilakukan di luar jam kerja
    printf("Apakah servis dilakukan di luar jam kerja? (Y/N): ");
    scanf(" %c", &service_time);

    // Jika di luar jam kerja, base fee digandakan
    if (service_time == 'Y' || service_time == 'y') {
        base_fee *= 2;
    }

    // Input apakah pelanggan bersedia antar-jemput
    printf("Is the customer willing to drop off and pick up? (Y/N): ");
    scanf(" %c", &drop_pickup);

    // Jika pelanggan bersedia antar-jemput, base fee dibagi dua
    if (drop_pickup == 'Y' || drop_pickup == 'y') {
        base_fee /= 2;
    }

    // Hitung total fee
    total_fee = base_fee + additional_fee;

    // Output total biaya
    printf("The total service fee is: $%.2f\n", total_fee);

    return 0;
}