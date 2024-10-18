#include <iostream>
#include <cmath>
using namespace std;

// Function to check if a number is Kaprekar in the given base
bool isKaprekarNumber(int n, int base) {
    // Square the number in the given base
    long long square = n * n;

    // Get the number of digits in n
    int numDigits = log(n) / log(base) + 1;

    // Generate parts L and R
    long long powerBase = pow(base, numDigits);
    long long rightPart = square % powerBase;
    long long leftPart = square / powerBase;

    // Check if n is a Kaprekar number
    return (rightPart + leftPart == n);
}

int main() {
    int number, base;
    
    // Input the number and the base
    cout << "Enter a number: ";
    cin >> number;
    
    cout << "Enter a base (>= 2): ";
    cin >> base;

    // Input validation
    if (number < 0 || base < 2) {
        cout << "Invalid input. Please enter a non-negative number and a base greater than or equal to 2." << endl;
        return 1;
    }

    // Check and display if the number is a Kaprekar number
    if (isKaprekarNumber(number, base)) {
        cout << number << " is a Kaprekar number in base " << base << "." << endl;
    } else {
        cout << number << " is not a Kaprekar number in base " << base << "." << endl;
    }

    return 0;
}
