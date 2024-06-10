import java.util.Random;
import java.util.Scanner;

public class GuessTheNumber {
    public static void main(String[] args) {
        // Create a random number generator
        Random random = new Random();
        int numberToGuess = random.nextInt(100) + 1; // Random number between 1 and 100
        int numberOfAttempts = 10; // Set the number of attempts
        int attempts = 0;
        boolean hasWon = false;

        System.out.println("Welcome to Guess the Number Game!");
        System.out.println("I have randomly chosen a number between 1 and 100.");
        System.out.println("You have " + numberOfAttempts + " attempts to guess it.");

        // Use try-with-resources to manage the Scanner resource
        try (Scanner scanner = new Scanner(System.in)) {
            // Loop for the number of attempts
            while (attempts < numberOfAttempts) {
                System.out.print("Enter your guess: ");
                int playerGuess = scanner.nextInt();
                attempts++;

                if (playerGuess < numberToGuess) {
                    System.out.println("It's higher than " + playerGuess + ".");
                } else if (playerGuess > numberToGuess) {
                    System.out.println("It's lower than " + playerGuess + ".");
                } else {
                    hasWon = true;
                    break;
                }
            }
        }

        // Output the result
        if (hasWon) {
            System.out.println("Congratulations! You've guessed the number " + numberToGuess + " in " + attempts + " attempts.");
        } else {
            System.out.println("Sorry, you've used all " + numberOfAttempts + " attempts. The number was " + numberToGuess + ".");
        }
    }
}