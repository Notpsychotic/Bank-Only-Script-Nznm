# This script updates higher tier computers to a middle tier system

class Computer:
    def __init__(self, tier):
        self.tier = tier

    def update_tier(self):
        if self.tier == 'high':
            self.tier = 'middle'
            print('Computer tier updated to middle.')
        else:
            print('No update needed. Current tier:', self.tier)

# Example usage
if __name__ == '__main__':
    computer = Computer('high')
    print('Current tier:', computer.tier)
    computer.update_tier()
    print('Updated tier:', computer.tier)
