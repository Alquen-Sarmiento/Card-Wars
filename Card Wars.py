from random import shuffle

class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    
    numbers = [None, None,"2", "3", "4", "5", "6", "7", "8", 
              "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    #Not considering draw for now because cards are unique
    def __gt__(self, other):
        if self.number > other.number:
            return True
        if self.number == other.number:
            if self.suit > other.suit:
                return True
        return False

    def __lt__(self, other):
        if self.number < other.number:
            return True
        if self.number == other.number:
            if self.suit < other.suit:
                return True
        return False

    def __repr__(self):
        return ('{n} of {s}'.format(n=self.numbers[self.number], s=self.suits[self.suit]))

class Deck:
    def __init__(self, numRange, suitRange):
        self.cards = []
        for n in numRange:
            for s in suitRange:
                self.cards.append(Card(n, s))
        shuffle(self.cards)

    def get_card(self):
        if len(self.cards) > 2:
            return self.cards.pop()


class Player:
    def __init__(self, name):
        self.winCount = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        p1 = input('Player 1 Name? ')
        p2 = input('Player 2 Name? ')
        self.p1 = Player(p1)
        self.p2 = Player(p2)
        self.deck = Deck(range(2, 13 + 2), range(4))

    def round_check(self):
        print("Player 1: {} \nPlayer 2: {}".format(self.p1.card, self.p2.card))
        if self.p1.card > self.p2.card:
            self.p1.winCount += 1
            print("Player 1 Wins")
        elif self.p1.card < self.p2.card:
            self.p2.winCount += 1
            print("Player 2 Wins")
        else:
            print('Draw')

    def game_check(self):
        if self.p1.winCount > self.p2.winCount:
            print('\nPlayer 1 wins with score: {}'.format(self.p1.winCount))
        else:
            print('\nPlayer 2 wins with score: {}'.format(self.p2.winCount))

    def start_game(self):
        i = None
        #Give cards to player until nothing left or quit
        while len(self.deck.cards) > 2 and i != 'q':
            i = input('\nPress any key to continue. Press "q" to quit')
            self.p1.card = self.deck.get_card()
            self.p2.card = self.deck.get_card()
            self.round_check()
        self.game_check()
        
        
game = Game()
game.start_game()