// Copyright (c) 2022 Nina Mathew All rights reserved
//
// Created by: Nina Mathew
// Created on: April 14, 2023
// This program does a for loop

#include <stdio.h>

int main() {
    // this function uses a while loop

    int base_Number;
    int power_Number;
    int answer = 1;
    int ScanError = 0;
    int positive_integer;

    // input

    printf("Enter a base number: ");
    ScanError = scanf("%d", &base_Number);

    printf("Enter a positive number: ");
    ScanError = scanf("%d", &power_Number);

    // process

    if (ScanError == 1) {
        if (power_Number >= 0) {
            for (int positive_integer = 1; positive_integer <=
                power_Number; positive_integer++) {
                answer = answer * base_Number;
                }
                printf("%d to the power of %d is %d\n",
                base_Number, power_Number, answer);

        } else {
            printf("Invalid input\n");
        }
    } else {
        printf("Invalid input\n");
    }
    printf("\nDone.\n");
    return 0;
}
