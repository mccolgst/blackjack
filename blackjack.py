import random
import os


#card and deck are from wikipedia

def keyprompt():
        char = 0
        print "press any key to continue..."
        while not  char:
                char=msvcrt.getch()
class Card:
        suit_names=['Clubs','Diamonds','Hearts','Spades']
        numbers=[None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        def __init__(self,suit=0,number=2):
                self.suit=suit
                self.number=number
        def __str__(self):
                return '%s of %s' % (Card.numbers[self.number],Card.suit_names[self.suit])
        def calcScore(self): #my little addition
                score=0
                if(self.number==11 or self.number==12 or self.number==13):
                        score=10
                else:
                        score=self.number
                return score
class Deck:
        def __init__(self):
                self.cards = []
                for suit in range(4):
                        for number in range(1,14):
                                card=Card(suit,number)
                                self.cards.append(card)
        def __str__(self):
                for suit in self.cards:
                        print suit
        def pop(self):
                return self.cards.pop()
        def shuffle(self):
                random.shuffle(self.cards)
        def reset(self):
                self.__init__()#play a new game of cards
class Player:
        def __init__(self):
                self.score=0
                self.hand=[]#cards that the player currently holds
                self.money=100
        def bet(self,bet):
                self.money-=bet
                return self.money
        def winHand(self,winnings):
                self.money+=winnings
                return self.money
        def draw(self,card):
                self.hand.append(card)
        def showHand(self):# a method really just for testing calcHand
                for h in self.hand:
                        print h
        def calcHand(self):
                self.score=0
                ace=0
                for h in self.hand: #for each card the player has
                        thing=h.calcScore()
                        if(thing==1):
                                ace=1
                        else:
                                self.score+=thing
                if(ace==1):
                        if(self.score+11<=21):
                                self.score+=11
                        else:
                                self.score+=1
                return self.score
        def reset(self): #reset the player's hand
                self.score=0
                self.hand=[]
class Game:
        def __init__(self):
                '''Create a deck, shuffle it, create two players, deal them each two cards,
                   the set what players are playing'''
                d1 = Deck()
                d1.shuffle()
                self.dealer = Player()
                self.pl = Player()
                self.dealer.draw(d1.pop())
                self.pl.draw(d1.pop())
                self.dealer.draw(d1.pop())
                self.pl.draw(d1.pop())
                self.deck=d1
                self.playDealer()
        def playDealer(self):
                done=0
                while not done:
                        dscore=self.dealer.calcHand()
                        #print "Dealer hand: ",self.dealer.showHand(),dscore
                        if(dscore>21):
                                done=1
                        else:
                                if(dscore>=17):
                                        done=1
                                else:
                                        self.dealer.draw(self.deck.pop())
        def compareScore(self):
                '''For each player, determine how much score they have, determine if they have over 21
                (auto lose), then determine which of those has the highest of the scores, it also
                keeps track of which player had that score, with the player variable'''
                bestscore=0
                if(self.pl.calcHand()<=21):
                         bestscore=self.pl.calcHand()
                if(self.dealer.calcHand()<=21 and self.dealer.calcHand()>bestscore):
                        print "Dealer wins with",self.dealer.calcHand()
                elif(bestscore==0):
                        print "No winners"
                else:
			os.system('clear')
                        print "Congrats, you win with",bestscore
                        self.pl.winHand(self.bet*2)
			print "Current money:$",self.pl.bet(0)
                return bestscore
	def play(self):
		print "You have $%s" %self.pl.bet(0)
		self.bet=int(raw_input("How much do you wish to bet?"))
		while(self.bet>self.pl.bet(0) or self.bet<=0):
			self.bet=int(raw_input("Sorry, you can't bet more than you have. \nHow much do you wish to bet?"))
		self.pl.bet(self.bet)
 		done=0
		while not done:
			os.system('clear')
			print "Current money:$%s" %self.pl.bet(0)
			print "Your hand:"
			self.pl.showHand()
			#print self.pl.calcHand()
			if(self.pl.calcHand()>21):
				print "BUST!!"
				done=1
			else:
				choice = raw_input("Hit or Stay (H/S)?")
				if choice.upper()=="H":
					self.pl.draw(self.deck.pop())
				else:
					done=1
                self.compareScore()
	def end(self):
		print "Thanks for playing"
        def reset(self):
                d1 = Deck()
                d1.shuffle()
                self.pl.reset()
                self.dealer.draw(d1.pop())
                self.pl.draw(d1.pop())
                self.dealer.draw(d1.pop())
                self.pl.draw(d1.pop())
                self.playDealer()
                
game=Game()
game.play()
again=raw_input("Play again?")
os.system('clear')
while(again.upper()=="Y"):
	game.reset()
	game.play()
	again=raw_input("Play again?")
	os.system('clear')
game.end()
