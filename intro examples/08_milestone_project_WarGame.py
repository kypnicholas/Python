import random

# Global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card: 
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]  # map the rank to a value, for example, 'Two' is 2, 'Three' is 3, etc.

    def __str__(self):
        return f'{self.rank} of {self.suit}'

'''
two_hearts =Card('Hearts','Two')
print(two_hearts)
print(values[two_hearts.rank])
'''


class Deck: 
    
    def __init__(self):
        self.all_cards = [] # Not a class attribute, as we do not need to pass it. It is always the same. 

        for suit in suits: 
            for rank in ranks:
                # Create a card object and add it to the list of all_cards.
                card = Card(suit,rank)
                self.all_cards.append(card)
    

    def shuffle(self):         # Note this doesn't return anything. It does everything in place.
        random.shuffle(self.all_cards)

    def deal_one(self):        # Remove one card from the list of all_cards
        return self.all_cards.pop()    


mydeck = Deck()

'''
print('There is a total of:' + str(len(mydeck.all_cards)) + ' cards in every deck')
for card in mydeck.all_cards:
    print(card)


first_card = mydeck.all_cards[0]
print('First card BEFORE shuffling is: ' + str(first_card))
mydeck.shuffle()
first_card = mydeck.all_cards[0]
print('First card AFTER shuffling is: ' + str(first_card))


mydeck.shuffle()
my_card = mydeck.deal_one()             # pops one card from the deck, so lenght is going to be 51. 
print(my_card)
print(str(len(mydeck.all_cards)))   

my_card = mydeck.deal_one()             # pops ANOTHER card from the deck, so lenght is going to be 50.
print(my_card)
print(str(len(mydeck.all_cards)))
'''


class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []     # A new player starts with no cards.

    def remove_one(self):      
        return self.all_cards.pop(0)        # Remove the top card [0] from the top of the deck. Imagine [-1] is the bottom. 

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):             # If the player gets MANY cards (of type list) we use the extend() to add them to the end of the deck. 
            self.all_cards.extend(new_cards)
        else:                                       # OTHERWISE (only one card), we use append() to add it to the end of the deck. 
            self.all_cards.append(new_cards)       
    
    def __str__(self):
        return f'{self.name} has {len(self.all_cards)} cards.'
    
'''
new_player = Player('Jose')
print(new_player)

my_card = mydeck.deal_one() 

new_player.add_cards(my_card)
print(new_player)
print(new_player.all_cards[0])

new_player.add_cards(['Five of Hearts', 'Three of Clubs'])
print('Player is dealt with 2 new cards. His new deck includes: ')

for card in new_player.all_cards:
    print(card)
'''


# GAME SETUP

player_one = Player('Player One')
player_two = Player('Player Two')

new_deck = Deck()
new_deck.shuffle()

# Split the deck between the two players (assign one to each player x26 times)
for card in range(26): 
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")


    # Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break

    # Otherwise, the game is still on!
    
    # Start a new round and reset current cards. player_one_cards are the cards "on the table" (NOT the same as player_one.all_cards)
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:


        if player_one_cards[-1].value > player_two_cards[-1].value:

            # Player One gets the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            
            # No Longer at "war" , time for next round
            at_war = False
        
        # Player Two Has higher Card
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            # Player Two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            # No Longer at "war" , time for next round
            at_war = False

        else:
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.
            
            # First check to see if player has enough cards
            
            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
