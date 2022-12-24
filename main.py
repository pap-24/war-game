# Βάλε ΟΛΗ την βιβλιοθήκη random
import random

# =========================================================================
# Βάλε ΟΛΗ την βιβλιοθήκη keyboard, η οποία επιτρέπει να χρησιμοποιήσουμε
# πλήκτρα για να ξεκινούν οι γύροι (rounds)
# =========================================================================
#import keyboard (soon)

# =================================================
# Λεξικό το οποίο χρησιμοποιείται για την σύγκριση
# και την μετάφραση των καρτών (π.χ. King > Two)
# =================================================
values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14,
}
# =================================================

# Σύμβολα καρτών (Tuple)
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# Αξία καρτών (Tuple) (π.χ. King, Jack)
ranks = (
    'Two', 
    'Three', 
    'Four', 
    'Five', 
    'Six', 
    'Seven', 
    'Eight', 
    'Nine', 
    'Ten', 
    'Jack', 
    'Queen', 
    'King', 
    'Ace'
)

# Δημιουργία κάρτας
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

# Δημιουργία τράπουλας
class Deck:

    def __init__(self):
        
        self.cards = []
        
        for suit in suits:
            for rank in ranks:
                # Βάλε την κάρτα στην λίστα που περιέχει την τράπουλα
                newCard = Card(suit, rank)
                self.cards.append(newCard)
     
    # Εκτύπωση της τράπουλας και όλων των καρτών
    def __str__(self):
        return f'The Deck has {len(self.cards)} cards.'

    # Εκτύπωση του μήκους της τράπουλας (το πόσα χαρτι΄ά έχει)
    def __len__(self):
        return len(self.cards)

    # Ανακάτεμα της τράπουλας (λίστας) με χρήση της βιβλιοθήκης "random"
    def shuffle(self):
        random.shuffle(self.cards)
        print('The Deck has been successfully shuffled.')

# Δημιουργία του παίχτη
class Player:
    
    def __init__(self, name):
        # Όρισε τα χαρτιά του παίχτη
        self.name = name
        # Όρισε τη λίστα που θα περιέχει τα χαρτιά του παίχτη
        self.playerCards = []
        
    # Εκτύπωση πληροφοριών του παίχτη
    def __str__(self):
        return f'The player {self.name} has {len(self.playerCards)} cards.'
        
    # Μέθοδος χρήσης κάρτας από τα χαρτιά του παίχτη
    def drawCard(self):
        if len(self.playerCards) > 0:
            return self.playerCards.pop(0)
    
    # ===============================================================
    # Μέθοδος που επιτρέπει τον παίχτη να παίρνει και να βάζει χαρτιά
    # στη λίστα του που περιέχει τα χαρτιά του
    # ===============================================================
    def collectCards(self, collectedCards):
        if type(collectedCards) is list: # List
            return self.playerCards.extend(collectedCards)
        
        else: # String
            return self.playerCards.append(collectedCards)
        
        # =============================================
        # 2ος τρόπος:
        # =============================================
        # type([]) = list
        # type('') = string
        # if type(collectedCards) == type([]): # List
        #      return self.playerCards.extend(collectedCards)
        # else: # String
        #      return self.playerCards.append(collectedCards)
        # =============================================


# GAME LOGIC & MAIN PROGRAM

# ============================================================
# SETUP GAME
# ============================================================

# 1) Δημιουργία των δύο (2) παιχτών (με ψευδώνυμα για παίχτες)
p1 = Player(input('Player 1, give yourself a nickname: '))
p2 = Player(input('Player 2, give yourself a nickname: '))

LINE = '---------------------------------------'

# 2) Δημιουργία και ανακάτεμα της τράπουλας
newDeck = Deck()
newDeck.shuffle()

# ----------------------------------------------
# 3) Μοίρασμα της τράπουλας στους δύο παίχτες 
# (βγάζοντας χαρτιά από την τράπουλα)
# len(newDeck) / 2 = πάντα σταθερό 26 φορές
# ----------------------------------------------
for i in range(26):
    # ------------------------------------------
    # Βγάζω δύο (2) χαρτιά από την τράπουλα και 
    # δίνω από ένα (1) σε κάθε παίχτη
    # ------------------------------------------
    card1 = newDeck.cards.pop(0)
    card2 = newDeck.cards.pop(0)
    
    p1.collectCards(card1)
    p2.collectCards(card2)
# ============================================================

# ============================================================
# PLAY GAME
# ============================================================
WAR_CARDS_AMOUNT = int(input('Give the amount of cards for WAR: '))
gameOn = True
warOn = True # Έστω ότι τα πρώτα χαρτιά καταλήγουν σε πόλεμο (WAR)
Round = 0

while gameOn: # Όσο το παιχνίδι παίζει (gameOn == True)
    
    # ---------------------------------------------------
    # Ελέγχω αν τελείωσαν τα χαρτιά σε κάποιον παίχτη
    # έτσι ώστε το παιχνίδι να τελείωσει κάποια
    # στιγμή. Χρησιμοποιώ break αντί για gameOn = False
    # για να σταματήσω την while από το να συνεχίσει.
    # ---------------------------------------------------
    if len(p1.playerCards) == 0: # Player 2 wins
        print('\n') # Νέα γραμμή (new line)
        print(f'{p1.name} does not have any more cards!')
        print(f'Congratulations, {p2.name}, you won the game!')
        break

    if len(p2.playerCards) == 0: # Player 1 wins
        print('\n') # Νέα γραμμή (new line)
        print(f'{p2.name} does not have any more cards!')
        print(f'Congratulations, {p1.name}, you won the game!')
        break
    # ---------------------------------------------------
    
    # Γύρος (Round)
    Round += 1
    print(f'\n{LINE}')
    print(f'ROUND {Round} - PLAY')
    
    # Player 1
    p1Cards = []
    # --------------------------------
    # Βάλε στην λίστα το πρώτο χαρτί
    # από τη λίστα του παίχτη 1
    # -------------------------------
    p1Cards.append(p1.drawCard())
    print(f'{p1.name} got a {p1Cards[-1]} ({p1Cards[-1].value})!')

    # Player 2
    p2Cards = []
    # --------------------------------
    # Βάλε στην λίστα το πρώτο χαρτί
    # από τη λίστα του παίχτη 2
    # -------------------------------
    p2Cards.append(p2.drawCard())
    print(f'{p2.name} got a {p2Cards[-1]} ({p2Cards[-1].value})!')
    warOn = True
    
    while warOn: # Όσο υπάρχει πόλεμος (WAR) (warOn == True)
        
        # ---------------------------------------------------
        # Ελέγχω ξανά αν τελείωσαν τα χαρτιά σε κάποιον παίχτη
        # έτσι ώστε να καταλήξουν σε πόλεμο
        # στιγμή. Χρησιμοποιώ break αντί για warOn = False
        # για να σταματήσω την while από το να συνεχίσει.
        # ---------------------------------------------------
        if len(p1Cards) == 0: # Player 2 wins
            print('\n') # Νέα γραμμή (new line)
            print(f'{p1.name} does not have any more cards!')
            print(f'Congratulations, {p2.name}, you won the game!')
            break
    
        if len(p2Cards) == 0: # Player 1 wins
            print('\n') # Νέα γραμμή (new line)
            print(f'{p2.name} does not have any more cards!')
            print(f'Congratulations, {p1.name}, you won the game!')
            break
        # ---------------------------------------------------
    
        if p1Cards[-1].value > p2Cards[-1].value:
            # Player 1 wins the draw
            print(f'\n{p1.name} won this round!')
            print(LINE)
            p1.collectCards(p1Cards)
            p1.collectCards(p2Cards)
            warOn = False
    
        elif p1Cards[-1].value < p2Cards[-1].value:
            # Player 2 wins the draw.
            print(f'\n{p2.name} won this round!')
            print(LINE)
            p2.collectCards(p2Cards)
            p2.collectCards(p1Cards)
            warOn = False
    
        else:
            # WAR Συνεχίζει (ξανατράβα χαρτιά από τους παίχτες)
            print(f'\nWAR! Both {p1.name} and {p2.name} got the same card!')
            for i in range(WAR_CARDS_AMOUNT):
                p1Cards.append(p1.drawCard())
                p2Cards.append(p2.drawCard())
            
            # Εκτύπωσε τα χαρτιά του πρώτου παίχτη στο WAR
            print(f'\n{p1.name} has: ')
            for card in p1Cards:
                print(f'- {card}')
                
            # Εκτύπωσε τα χαρτιά του δεύτερου παίχτη στο WAR
            print(f'\n{p2.name} has: ')
            for card in p2Cards:
                print(f'- {card}')
# ============================================================
