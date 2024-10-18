#include <stdio.h>

float add(float a, float b) {
    return a + b;
}

float sub(float a, float b) {
    return a - b;
}

float mul(float a, float b) {
    return a * b;
}

float div(float a, float b) {
    if (b != 0) {
        return a / b;
    } else {
        printf("Division by zero is not allowed.\n");
        return 0; // Return 0 or handle error appropriately
    }
}
int main() {
    int choice;
    float num1, num2, result;

    while (1) {
        printf("Calculator Menu:\n");
        printf("1. Addition\n");
        printf("2. Multiplication\n");
        printf("3. Subtraction\n");
        printf("4. Division\n");
        printf("5. Quit\n");

        printf("Enter your choice (1-5): ");
        scanf("%d", &choice);

        if (choice == 5) {
            printf("Exiting the calculator. Goodbye!\n");
            break;
        }

        printf("Enter the first number: ");
        scanf("%f", &num1);
        printf("Enter the second number: ");
        scanf("%f", &num2);
        printf(".");

        switch (choice) {
            case 1:
                result = add(num1, num2);
                printf("Result: %.2f\n", result);
                break;
            case 2:
                result = mul(num1, num2);
                printf("Result: %.2f\n", result);
                break;
            case 3:
                result = sub(num1, num2);
                printf("Result: %.2f\n", result);
                break;
            case 4:
                result = div(num1, num2);
                // Note: Division by zero message is already printed in div function.
                break;
            default:
                printf("Please enter a valid number (1-5).\n");
                break;
        }
    }

    return 0;
}



