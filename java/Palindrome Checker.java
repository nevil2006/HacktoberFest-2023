import java.util.Scanner;

public class PalindromeChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Input string from the user
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();
        
        // Remove spaces and convert to lowercase for comparison
        String cleanedInput = input.replaceAll("[\\W]", "").toLowerCase();
        
        // Check if the cleaned input is a palindrome
        if (isPalindrome(cleanedInput)) {
            System.out.println("\"" + input + "\" is a palindrome.");
        } else {
            System.out.println("\"" + input + "\" is not a palindrome.");
        }
        
        scanner.close();
    }
    
    // Method to check if a string is a palindrome
    public static boolean isPalindrome(String str) {
        int left = 0;
        int right = str.length() - 1;
        
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false; // Not a palindrome
            }
            left++;
            right--;
        }
        return true; // It's a palindrome
    }
}
