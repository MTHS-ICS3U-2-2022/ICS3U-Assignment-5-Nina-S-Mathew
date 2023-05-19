// Copyright (c) 2022 Nina Mathew All rights reserved
//
// Created by: Nina Mathew
// Created on: April 14, 2023
// This program does a for loop



#include <stdio.h>
#include <math.h>

int main() {
    int number;
    int power;
    int answer = 1;
    int loopCounter = 0;
    int ScanError = 0;

    // input
    printf("Enter a base number: ");
    ScanError = scanf("%d", &number);
    printf("Enter a power: ");
    ScanError = scanf("%d", &power);

    // process and output
    if (ScanError == 0) {
        printf("Invalid Input");
    } else {
        for (loopCounter = 0; loopCounter < power; loopCounter++) {
            answer = answer * number;
        }
        printf("%d to the power of %d is %d", number, power, answer);
    }
    printf("\nDone.\n");
    return 0;
}


