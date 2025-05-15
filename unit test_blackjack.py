
from blackjack import Card, Hand, Deck, BettingSystem

def test_deck_has_52_cards():
    deck = Deck()
    assert len(deck.cards) == 52

def test_deck_deals_card():
    deck = Deck()
    card = deck.deal_card()
    assert isinstance(card, Card)
    assert len(deck.cards) == 51


def test_card_str():
    card = Card("hearts", "Ace")
    assert str(card) == "Ace of hearts"
    
def test_deck_has_52_cards():
    deck = Deck()
    assert len(deck.cards) == 52

def test_deck_deals_card():
    deck = Deck()
    card = deck.deal_card()
    assert isinstance(card, Card)
    assert len(deck.cards) == 51

def test_add_card_to_hand():
    hand = Hand()
    card = Card("spades", "5")
    hand.add_card(card)
    assert len(hand.cards) == 1
    assert hand.cards[0] == card

def test_hand_value_no_aces():
    hand = Hand()
    hand.add_card(Card("hearts", "10"))
    hand.add_card(Card("diamonds", "7"))
    assert hand.calculate_value() == 17

def test_hand_value_with_ace():
    hand = Hand()
    hand.add_card(Card("spades", "Ace"))
    hand.add_card(Card("clubs", "7"))
    assert hand.calculate_value() == 18

def test_hand_value_with_ace_adjustment():
    hand = Hand()
    hand.add_card(Card("hearts", "Ace"))
    hand.add_card(Card("diamonds", "King"))
    hand.add_card(Card("spades", "5"))
    assert hand.calculate_value() == 16 
    
def test_place_bet():
    system = BettingSystem(100)
    system.place_bet(30)
    assert system.get_balance() == 70
    assert system.current_bet == 30

def test_win_bet():
    system = BettingSystem(100)
    system.place_bet(20)
    system.win_bet()
    assert system.get_balance() == 120

def test_lose_bet():
    system = BettingSystem(100)
    system.place_bet(10)
    system.lose_bet()
    assert system.get_balance() == 90 

def test_push_bet():
    system = BettingSystem(100)
    system.place_bet(40)
    system.push_bet()
    assert system.get_balance() == 100

    
