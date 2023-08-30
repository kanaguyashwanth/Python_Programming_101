# Day - 11: CAPSTONE PROJECT [BLACKJACK / 21]

'''
RULES:
 - Whoever manages to have cards which sum close to 21, wins.
 - If it crosses 21, then you lose immediately. It is also known as Bust.
 - cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
 - Cards are infinite in the DECK, once removed, there are still more cards.
 - Cards are not removed from the Deck when drawn.
 - EACH card has EQUAL chances of occurring.
 - The ACE can count as 1 or 11.
 - There are no JOKERS.

 - Cards with 2 to 10, count as their face value
 - J, Q, K - Count as 10 each
 - ACE - Can either count as 1 or as a 11
 - We DEAL till we get close to 21 or we can close the deal and the dealer reveals their cards.
 - If the dealer and you both end up in same score, then it is a DRAW!
 - If the dealer has 21 and we have less, then we LOSE!
 - If we have 21 and the dealer has less, then we WIN!


Your cards: [9, 10], current score: 19
Computer's first card: 8
Type 'y' to get another card, type 'n' to pass: n
Your final hand: [9, 10]
Computer's final hand: [8, 10]
You Win!

Do you want to play a game of Blackjack? Type 'y' or 'n': y

Your cards: [5, 10], current score: 15
Computer's first card: 10
Type 'y' to get another card, type 'n' to pass: y
Your final hand: [5, 10, 10], final score: 25
Computer's final hand: [10, 10], final score: 20
You went over. You lose.


'''

def blackjack ():
    
    
    from art import logo
    print (logo)
    
    
    import random
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_int = random.randint(0, 12)
    
    
    my_cards = []
    random_int = random.randint(0, 12)
    my_cards.append(cards[random_int])
    random_int = random.randint(0, 12)
    my_cards.append(cards[random_int])
    
    
    my_score = 0
    for n in range (len(my_cards)):
        my_score += my_cards[n]
    print(f'Your cards: {my_cards}, current score: {my_score}')
    

    
    comp_cards = []
    random_int = random.randint(0, 12)
    comp_cards.append(cards[random_int])
    print (f"Computer's first card: {comp_cards[0]}")
    
    
    comp_score = 0
    for n in range (len(comp_cards)):
        comp_score += comp_cards[n]

    
    should_continue = True
    
    
    choice = 'n'
    while should_continue:
        
        if my_score <= 21:

            if input("Type 'y' to get another card', type 'n' to pass: ") == 'y':
                random_int = random.randint(0, 12)
                my_cards.append(cards[random_int])
                my_score += my_cards[-1]
                print (f"Your final hand: {my_cards}, final score: {my_score}")
                
                random_int = random.randint(0, 12)
                comp_cards.append(cards[random_int])
                comp_score += comp_cards[-1]
                print (f"Computer's final hand: {comp_cards}, final score: {comp_score}")
            
            else:
                should_continue = False
                
                random_int = random.randint(0, 12)
                comp_cards.append(cards[random_int])
                comp_score += comp_cards[-1]
                print (f"Your final hand: {my_cards}, final score: {my_score}")
                print (f"Computer's final hand: {comp_cards}, final score: {comp_score}")
                
                if (my_score > comp_score) or (comp_score>21):
                    print ("You Win!")
                    blackjack()
                elif (my_score < comp_score) and (comp_score<=21):
                    print ("Computer wins.")
                    blackjack()
                elif my_score == comp_score:
                    print ("It's a draw.")
                    blackjack()
                
                blackjack()
            
        else:
            print("You went over. You lose.")
            blackjack()


blackjack()
