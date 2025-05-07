import random

class Card:
    """Represents a one playing card out of a deck."""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """Represents a standard deck of 52 playing cards."""
    def __init__(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


class Hand:
    """Represents the hand that either the player or the dealer possesses."""
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        value = 0
        aces = 0
        for card in self.cards:
            if card.rank in ['Jack', 'Queen', 'King']:
                value += 10
            elif card.rank == 'Ace':
                value += 11
                aces += 1
            else:
                value += int(card.rank)

        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value

    def show_hand(self, show_all=True):
        if show_all:
            return ', '.join(str(card) for card in self.cards)
        else:
            return f"{self.cards[0]}, Hidden"


class BettingSystem:
    """Manages the player's betting and balance throughout the game session."""
    def __init__(self, starting_balance=100):
        self.balance = starting_balance
        self.current_bet = 0

    def place_bet(self, amount):
        if amount > self.balance:
            raise ValueError("Not enough money")
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
    """Simulates a game of single player Blackjack."""
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.betting_system = BettingSystem()

    def start(self):
        print("Welcome to Blackjack")
        while True:
            self.deck = Deck()
            self.deck.shuffle()
            self.player_hand = Hand()
            self.dealer_hand = Hand()
            self.take_bet()

            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())

            print("\nYour hand:", self.player_hand.show_hand())
            print("Dealer's hand:", self.dealer_hand.show_hand(show_all=False))

            player_value = self.player_hand.calculate_value()
            dealer_value = self.dealer_hand.calculate_value()

            if player_value == 21 and dealer_value != 21:
                print("\nYou have blackjack. You now win 1 and a half of your bet.")
                self.betting_system.balance += int(self.betting_system.current_bet * 2.5)
                self.betting_system.reset_bet()
            elif dealer_value == 21 and player_value != 21:
                print("\nDealer has Blackjack. You lose. (Womp womp)")
                print("Dealer's hand:", self.dealer_hand.show_hand(show_all=True))
                self.betting_system.lose_bet()
            elif player_value == 21 and dealer_value == 21:
                print("\nBoth you and the dealer have Blackjack. It is now a push.")
                print("Dealer's hand:", self.dealer_hand.show_hand(show_all=True))
                self.betting_system.push_bet()
            else:
                self.player_turn()

                if self.player_hand.calculate_value() <= 21:
                    self.dealer_turn()

                self.check_winner()

            if self.betting_system.get_balance() <= 0:
                print("You are now broke. Game over.")
                break

            if not self.play_again():
                print("Thats all folks!")
                break

    def take_bet(self):
        while True:
            try:
                bet = int(input(f"\nYour balance is ${self.betting_system.get_balance()}. Enter your bet: "))
                self.betting_system.place_bet(bet)
                break
            except ValueError as e:
                print(f"Error: {e}")

    def player_turn(self):
        while True:
            choice = input("\nDo you want to hit or stand? ").lower()
            if choice == 'hit':
                self.player_hand.add_card(self.deck.deal_card())
                print("Your hand:", self.player_hand.show_hand())
                if self.player_hand.calculate_value() > 21:
                    print("You busted!")
                    break
            elif choice == 'stand':
                break
            else:
                print("Invalid input. Please enter hit or stand.")

    def dealer_turn(self):
        print("\nDealer's hand is:", self.dealer_hand.show_hand())
        while self.dealer_hand.calculate_value() < 17:
            print("Dealer hits.")
            self.dealer_hand.add_card(self.deck.deal_card())
            print("Dealer's hand is:", self.dealer_hand.show_hand())

        if self.dealer_hand.calculate_value() > 21:
            print("Dealer busted.")

    def check_winner(self):
        player_value = self.player_hand.calculate_value()
        dealer_value = self.dealer_hand.calculate_value()

        print(f"\nYour final hand is {player_value}: {self.player_hand.show_hand()}")
        print(f"Dealer's final hand is {dealer_value}: {self.dealer_hand.show_hand()}")

        if player_value > 21:
            print("You lose (Womp womp)")
            self.betting_system.lose_bet()
        elif dealer_value > 21 or player_value > dealer_value:
            print("You win")
            self.betting_system.win_bet()
        elif player_value == dealer_value:
            print("Push. It is a tie.")
            self.betting_system.push_bet()
        else:
            print("You lose(Womp womp)")
            self.betting_system.lose_bet()

        print(f"Your new balance: ${self.betting_system.get_balance()}")

    def play_again(self):
        choice = input("\nPlay one more round? (y/n): ").lower()
        return choice == 'y'


def main():
    game = BlackjackGame()
    game.start()


if __name__ == "__main__":
    main()
