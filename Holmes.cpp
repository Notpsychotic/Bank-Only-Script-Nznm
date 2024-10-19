#include <iostream>
#include <cstdlib>
#include <ctime>

void playGame() {
    int playerMoney = 100;
    int bet;
    int guess;
    int dice;

    std::cout << "Welcome to Holmes Casino!\n";
    std::cout << "You have $" << playerMoney << " to start.\n";

    while (playerMoney > 0) {
        std::cout << "Enter your bet: ";
        std::cin >> bet;

        if (bet > playerMoney) {
            std::cout << "You don't have enough money to make that bet.\n";
            continue;
        }

        std::cout << "Guess the dice roll (1-6): ";
        std::cin >> guess;

        if (guess < 1 || guess > 6) {
            std::cout << "Invalid guess. Please guess a number between 1 and 6.\n";
            continue;
        }

        std::srand(std::time(0));
        dice = std::rand() % 6 + 1;

        if (guess == dice) {
            std::cout << "Congratulations! You guessed correctly. You win $" << bet * 2 << "!\n";
            playerMoney += bet * 2;
        } else {
            std::cout << "Sorry, you guessed wrong. The dice roll was " << dice << ". You lose $" << bet << ".\n";
            playerMoney -= bet;
        }

        std::cout << "You now have $" << playerMoney << ".\n";
    }

    std::cout << "Game over! You ran out of money.\n";
}

int main() {
    playGame();
    return 0;
}
