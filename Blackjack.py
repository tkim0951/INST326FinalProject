import random

class Card:
    """Represents a one playing card out of a deck."""
    def __init__(self, suit, rank):
        pass


class Deck:
    """Represents a standard deck of 52 playing cards."""
    def __init__(self):
        pass

    def shuffle(self):
        pass

    def deal_card(self):
        pass

class Hand:
    """Represents the hand that either the player or the dealer possesses."""
    def __init__(self):
        pass

    def add_card(self, card):
        pass

    def calculate_value(self):
        pass

    def show_hand(self, show_all=True):
        pass

class BettingSystem:
    """Manages the player's betting and balance throughout the game session. Shows the amount of betting that the player has undertaken in the session, also is where the bet interface takes place"""
    def __init__(self, starting_balance=100):
        self.balance = starting_balance
        self.current_bet = 0

    def place_bet(self, amount):
        if amount > self.balance:
            raise ValueError("Not enough balance")
        self.current_bet = amount
        self.balance -= amount

    def win_bet(self):
        self.balance += self.current_bet * 2
        self.reset_bet()

    def push_bet(self):
        self.balance += self.current_bet
        self.reset_bet()

    def lose_bet(self):
        self.reset_bet()

    def get_balance(self):
        return self.balance

    def reset_bet(self):
        self.current_bet = 0

class BlackjackGame:
    """ Simulates a game of single player Blackjack. """
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.betting_system = BettingSystem()

    def start(self):
        pass

    def take_bet(self):
        pass

    def player_turn(self):
        pass

    def dealer_turn(self):
        pass

    def check_winner(self):
        pass

    def play_again(self):
        pass

def main():
    game = BlackjackGame()
    game.start()


if __name__ == "__main__":
    main()
