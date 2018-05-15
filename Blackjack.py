import random

deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]
total_decks = 4

def total_cards():
    cards = deck*total_decks
    return cards

cards = total_cards()

def remove_card(string):
    return cards.remove(string)

def computerCards():
    card1 = cards.pop(cards.index(random.choice(cards)))
    card2 = cards.pop(cards.index(random.choice(cards)))
    return card1, card2, card1+card2

def userCards():
    u_card1 = cards.pop(cards.index(random.choice(cards)))
    u_card2 = cards.pop(cards.index(random.choice(cards)))
    return u_card1, u_card2, u_card1+u_card2

def extra_card():
    extra = random.choice(cards)
    remove_card(extra)
    return extra

c_cards = list(computerCards())
u_cards = list(userCards())
computer_stands = 16

def comp_show():
    print("Computer has {}".format(c_cards))

def user_show():
    print("User has {}".format(u_cards))

def bust():
    print("You lost the round, computer takes all the money")

def askAnother():
    answ = input("Computer stands on: {}. Do you want another cards".format(c_cards[len(c_cards)-1]))
    return answ


def userInitial():
    print("Your first card is {}, Computer's first card is {}".format(u_cards[0],c_cards[0]))
    print("Your second card is {}, Computer's second card is {}".format(u_cards[1],c_cards[1]))
    while u_cards[len(u_cards)-1]<=21:
        ans = askAnother().lower()
        if ans == 'yes':
            oneMore = extra_card()
            u_cards[len(u_cards)-1] += oneMore
            print("Your new card is {} and your total is {}".format(oneMore,u_cards[len(u_cards)-1]))
            u_cards.insert(len(u_cards)-1,oneMore)
        else:
            while c_cards[len(c_cards)-1]<computer_stands:
                cNewCard = extra_card()
                print("Computer has drawn {}".format(cNewCard))
                c_cards[len(c_cards)-1] += cNewCard
                c_cards.insert(len(c_cards)-1, cNewCard)

            else:
                if c_cards[len(c_cards)-1] <= 21:
                    if c_cards[len(c_cards)-1]<u_cards[len(u_cards)-1]:
                        print("Your total is {}".format(u_cards[len(u_cards)-1]))
                        print("Computer's total is {}".format(c_cards[len(c_cards)-1]))
                        print("Congrats!! you have won this round, take away all the money")
                        break
                    elif c_cards[len(c_cards)-1]>u_cards[len(u_cards)-1]:
                        print("Your total is {}".format(u_cards[len(u_cards)-1]))
                        print("Computer's total is {}".format(c_cards[len(c_cards)-1]))
                        print("You Lost!! computer takes away all the money")
                        break
                    else:
                        print("Your total is {}".format(u_cards[len(u_cards)-1]))
                        print("Computer's total is {}".format(c_cards[len(c_cards)-1]))
                        print("THIS IS A PUSH, well played both of you!")
                        break
                else:
                    print("Your total is {}".format(u_cards[len(u_cards)-1]))
                    print("Computer's total is {}".format(c_cards[len(c_cards)-1]))
                    print("Congrats!! you won this game, take away all the money")
                    break
    else:
        bust()
        user_show()
        comp_show()

userInitial() 
    
