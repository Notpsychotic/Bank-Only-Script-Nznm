#include <stdio.h>

// Function to display spaceship details
void displaySpaceshipDetails(const char* name, const char* owner) {
    printf("Spaceship Name: %s\n", name);
    printf("Owned by: %s\n", owner);
}

int main() {
    // Example spaceship details
    const char* spaceshipName = "Galactic Cruiser";
    const char* ownerName = "Media Corp X";
    
    // Display the spaceship details
    displaySpaceshipDetails(spaceshipName, ownerName);
    
    return 0;
}
