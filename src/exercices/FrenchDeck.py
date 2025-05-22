class Cards:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"
    
class Frenchdeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    def __init__(self):
        self._cards = [Cards(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, card):
        self._cards[position] = card

deck = Frenchdeck()

print(len(deck))          
print(deck[0])            
print(deck[-1])           
print(deck[:5])          

    

    
