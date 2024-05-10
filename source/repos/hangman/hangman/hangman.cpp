#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

// Function to check if a character is present in the secret word
bool isLetterInWord(char letter, const string& word) {
    for (char c : word) {
        if (c == letter) {
            return true;
        }
    }
    return false;
}

// Function to display the current state of the guessed word
void displayWord(const string& word, const vector<char>& guessedLetters) {
    for (char c : word) {
        if (find(guessedLetters.begin(), guessedLetters.end(), c) != guessedLetters.end()) {
            cout << c << " ";
        }
        else {
            cout << "_ ";
        }
    }
    cout << endl;
}

int main() {
    vector<string> words = { "hangman", "programming", "computer", "science", "algorithm", "cplusplus" };

    srand(static_cast<unsigned int>(time(0)));
    int randomIndex = rand() % words.size();
    string secretWord = words[randomIndex];

    int maxAttempts = 7;
    int attemptsLeft = maxAttempts;
    vector<char> guessedLetters;

    cout << "Welcome to Hangman!" << endl;

    while (attemptsLeft > 0) {
        cout << "Attempts left: " << attemptsLeft << endl;
        displayWord(secretWord, guessedLetters);

        char guess;
        cout << "Enter a letter guess: ";
        cin >> guess;

        if (isLetterInWord(guess, secretWord)) {
            cout << "Correct guess!" << endl;
            guessedLetters.push_back(guess);
        }
        else {
            cout << "Incorrect guess!" << endl;
            attemptsLeft--;
        }

        bool allLettersGuessed = true;
        for (char c : secretWord) {
            if (find(guessedLetters.begin(), guessedLetters.end(), c) == guessedLetters.end()) {
                allLettersGuessed = false;
                break;
            }
        }

        if (allLettersGuessed) {
            cout << "Congratulations! You guessed the word: " << secretWord << endl;
            break;
        }
    }

    if (attemptsLeft == 0) {
        cout << "You ran out of attempts. The word was: " << secretWord << endl;
    }

    return 0;
}

