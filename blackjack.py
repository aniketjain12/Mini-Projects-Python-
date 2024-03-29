import random
suits =('Hearts','Diamonds','Spades','Clubs')
ranks =('Two','Three','Four','Five','Six','Seven',
	    'Eight','Nine','Ten','Jack','Queen','King','Ace')
values ={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,
         'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True


class Card:

	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank+ " of " +self.suit

class Deck:
  def __init__(self):
    self.deck = [] #start with an empty list
    for suit in suits:
      for rank in ranks:
        self.deck.append(Card(suit,rank))
        
  def __str__(self):
    deck_comp = ''
    for card in self.deck:
      deck_comp += '\n'+ card.__str__()
    return "The deck has: "+deck_comp
    
  def shuffle(self):
    random.shuffle(self.deck)
    
  def deal(self):
    single_card = self.deck.pop()
    return single_card

class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0 

	def add_card(self,card):
		#card passed in
		#from Deck.deal()
		self.cards.append(card)
		self.value += values[card.rank]	   	

		if card.rank == 'Ace':
			self.aces +=1
    
  def adjust_for_ace(self):
    while self.value > 21 and self.aces > 0:
        self.value -=10
        self.aces -= 1

    while self.value > 21 amd self.aces > 0:
        self.value -=10
    		self.aces -= 1
    	
class Chips:
	def __init__(self,total=100):
		self.total = total
		self.bet = 0

	def win_bet(self):
		self.total += self.bet
	

	def lose_bet(self):
		self.total -= self.bet


def take_bet(chips):
	while True:
		try:
			chips.bet = int(input("How many chips would you like to bet?: "))
		except:
			print("Sorry please provide an integer")
		else:
			if chips.bet > chips.total:
				print("Sorry, you do not have enough chips! You have: {}".format(chips.total))
			else:
				break

def hit(deck,hand):
	single_card = deck.deal()
	hand.add_card(single_card)
	hand.adjust_for_ace()

def hit_or_stand(deck,hand):
	global playing

	while True:
		x = input('Hot or Stand? Enter h or s ')

		if x[0].lower() == 'h':
			hit(deck,hand)

		elif x[0].lower() == 's':
			print("Player Stands Dealer's Turn")
			playing = False

		else:
			print("Sorry, I don't understand that please enter h or s only!")
			continue
		break						

def show_some(player,dealer):
	print("\n Dealer's Hand: ")
	print("First card hidden!")
	print(dealer.cards[1])
	
	print("\n Player's Hand")
	for card in player.cards:
		print(card)


def show_all(player,dealer):
	print("\n Dealer's Hand")
	for card in dealer.cards:
		print(card)

	print("\n Dealer's Hand: ",*dealer.cards,sep='\n').
	print("Value of Dealer's Hand is: {}".format(dealer.value))


	print("\n Player's Hand")
	for card in player.cards:
		print(card)
	print("Value of Player's Hand is: {}".format(player.value))	




