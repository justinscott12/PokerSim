from random import randrange

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
usedCards = []

def generateCard():
  global value
  value = str(randrange(13) + 1)
  suit = randrange(4)

  if value == '1':
    value = 'Ace'
  elif value == '11':
    value = 'Jack'
  elif value == '12':
    value = 'Queen'
  elif value == '13':
    value = 'King'

  generatedCard = value + ' of ' + suits[suit]

  if generatedCard in usedCards:
    return generateCard()

  usedCards.append(generatedCard)
  return generatedCard

def generateHand():
  card1 = generateCard()
  card2 = generateCard()
  return card1 + ', ' + card2

def rankHand(card1, card2, flop1, flop2, flop3, turn, river):
  global rank
  pairCounter = 0
  
  for i in len(locals()):
    if i.value == (i + 1).value:
      pairCounter += 1

  if pairCounter == 1:
    rank = 'Pair of ' + card1.value
  elif pairCounter == 2:
    # Add value of second pair
    rank = 'Two Pair, ' + card1.value + 's and '
  elif pairCounter == 3:
    rank = 'Three of a Kind of ' + card1.value
  
  return rank

#Execute

yourHand = generateCard() + ', ' + generateCard()
print('Your hand is ' + yourHand)

test = input('')
if test == '':
  flop = generateCard() + ', ' + generateCard() + ', ' + generateCard()
  print(flop)

test = input('')
if test == '':
  turn = generateCard()
  print(turn)

test = input('')
if test == '':
  river = generateCard()
  print(river)



#Prints one of every 52 cards (used for testing)
# x = 52;
# while x != 0:
#   x -= 1
#   generateCard()

# y = 0  
# for i in usedCards:
#   y += 1
#   print(str(y) + ' ' +  i)