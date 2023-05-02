// Copyright (c) 2022 Nina Mathew All rights reserved
//
// Created by: Nina Mathew
// Created on: April 14, 2023
// This program does a for loop

#include <stdio.h>

int main()
{

    // this function uses a while loop

    int base_Number;
    int power_Number;
    long long answer = 1;
    int ScanError = 0;

    // input

    printf("Enter a positive number: ");
    ScanError = scanf("%d", &power_Number);

    printf("Enter a positive number: ");
    ScanError = scanf("%d", &base_Number);

    // process

    if (ScanError == 1) {
        if (power_Number >= 0) {
            for (int base_number = 1; base_number <=
                power_Number; base_number++) {
                answer = answer * base_Number;
                printf("%d to the power of %d = %lld\n", base_number, power_Number, answer);
                break ;
            }
        } else {
            printf("Invalid input\n");
        }
    } else {
        printf("Invalid input\n");
    }
    printf("\nDone.\n");
    return 0;
}
