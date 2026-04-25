import random
import time
import os

cards1 = ["♠","♥","♦","♣"] #moznosti symbolov kariet (pre hratelnost nemaju vyznam, su tu cisto pre esteticke ucely)
cards2 = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]  #moznosti hodnot kariet (tie su pre hru dolezite, program z nich vyráta hodnotu kariet v ruke)

def sumCards(hand):
    total = 0
    for i in range (len(hand)):
        if hand[i] == "K" or hand[i] == "Q" or hand[i] == "J":
            total += 10
        elif hand[i] == "A":
            if (total + 11) > 21:
                total += 1
            else:
                total += 11
        else:
            total += int(hand[i])
    return total

def newCard(): #hrac si potiahne novu kartu s vlastnym symbolom a cislom, hodnota sa pricita k celkovej hodnote hracovych kariet
    global playerhand, playerhandS, playerhandVisible, playerTotal

    playerTotal = 0
    playerhand.append(random.choice(cards2))
    playerhandS.append(random.choice(cards1))
    playerTotal = sumCards(playerhand)
    playerhandVisible = []
    for i in range(len(playerhand)):
        playerhandVisible.append(str(playerhand[i]) + playerhandS[i])


def sumPlayer(): #kontrola hodnoty hracovych kariet bez tahania dalsej
    global playerhand, playerhandS, playerhandVisible, playerTotal

    playerTotal = 0
    playerTotal = sumCards(playerhand)
    print("Player: ", *playerhandVisible, " ", "Total:", playerTotal)
    return(playerTotal)


def newCardDealer(): #krupier si potiahne novu kartu, jej hodnota sa pricita k jeho celkovej hodnote
    global dealerhand, dealerhandS, dealerhandVisible, dealerTotal

    dealerTotal = 0
    dealerhand.append(random.choice(cards2))
    dealerhandS.append(random.choice(cards1))
    dealerTotal = sumCards(dealerhand) 
    dealerhandVisible = []
    for i in range(len(dealerhand)):
        dealerhandVisible.append(str(dealerhand[i]) + dealerhandS[i])
    time.sleep(0.7)

def sumDealer(): #kontrola hodnoty krupierovych kariet bez tahania dalsej
    global dealerhand, dealerhandS, dealerhandVisible, dealerTotal

    dealerTotal = 0
    dealerTotal = sumCards(dealerhand) 
    print("Dealer: ", *dealerhandVisible, " ", "Total:", dealerTotal)
    return(dealerTotal)

def rules(): #vycisti konzolu a napise pravidla pre zaciatocnikov
    clear()
    print("-----Welcome to playing blackjack!-----")
    print("1. You only play against the dealer")
    print("2. You can use commands 'hit' or 'stand' to either take another card or stop and let the dealer play,\n or on the first turn, you can double your bet and stop drawing cards")
    print("3. You need to have cards of a better value than the dealer, but not more than 21")
    print("4. 21 with only 2 cards is a blackjack! - and blackjack pays 3:2 (1.5x your bet)")
    print("5. Aces can have 2 values - 1 or 11, depending on what helps you more")
    print("6. Dealer only takes cards until 17 or more and doesn't take with a soft hand (when ace as a 1 would be better)")
    print("Press 'enter' to start the game...")

commands = ""
clear = lambda: os.system('cls' if os.name == "nt" else "clear") #vycistenie konzoly, funguje aj na windowse aj na linuxe alebo macu
print("-----WELCOME TO THE BLACKJACK TABLE-----\n")
print("-----Press 'enter' to start the game----\n")
print("-------Type 'rules' to learn more-------") #uvodny text, zaciatok hry po stlaceni tlacidla enter
commands = input()
if commands == "rules" or commands == "help": #prvy prikaz po zaciatku hry mozu byt pravidla
    rules()
    input()
    commands = ""
clear()

dealerwins = 0 #premenne pre statistiku na konci hry
playerwins = 0
push = 0

cash = float(input("Deposit cash to play: ")) #hrac musi hrat o (samozrejme virtualne) peniaze, tu ich musi vlozit
while cash <= 0:
    cash = float(input("Enter a valid amount of more than 0: ")) #poistenie vstupu
cash_before = cash


while commands == "":
    clear()

    bet = input("Enter your bet for this hand, press 'enter' to bet the same amount: ") #vstup pre zadanie stavky, pripadne enter pre zopakovanie predoslej
    if bet == "":
        bet = bet_before
    bet_before = bet
    bet = int(bet) #ulozi aktualnu stavku pre pripad opakovania

    playerhand = [random.choice(cards2)]
    playerhandS = [random.choice(cards1)] #rozdanie nahodnej prvej karty hracovi
    playerhandVisible = []
    playerTotal = 0

    dealerhand = [random.choice(cards2)]
    dealerhandS = [random.choice(cards1)]
    dealerhandVisible = [dealerhand[0]+dealerhandS[0]] #rozdanie nahodnej prvej karty krupierovi
    dealerTotal = 0

    newCard() #hrac potiahne druhu kartu, dealer ostava s jednou otocenou
    totalD = sumDealer()
    totalP = sumPlayer() #prva kontrola suctu

    gameover = False #trigger na ukoncenie hry ak hrac potiahne na 21

    if totalP == 21:
        print("You have a blackjack, you win!")
        cash += bet*1.5
        playerwins += 1
        print(f"Balance: {cash}€") #blackjack, hrac vyhrava, hra konci

    else:
        commands = "hit" #nastavene predpezne na hit aby program pokracoval

        while commands != "hit" and commands != "stand":
            print("Invalid command.")
            commands = input("Hit or stand? ") #osetrenie platneho vstupu

        while commands == "hit": #hrac nema blackjack, moze tahat dalej
            commands = input("Hit or stand? ")
            if commands == "double": #hrac potiahne jednu kartu, zdvojnasobi stavku a konci jeho tah
                bet = bet*2
                newCard()
                break
            if commands == "stand": #hrac stoji, jeho tah konci
                break
            newCard() #ak hrac taha kartu (hit), potiahne si dalsiu
            sumDealer() #kontrola suctu krupiera pre porovnanie a priebezny vypis stavu
            totalP = sumPlayer() #sucet hraca
            if totalP > 21: #hrac ma viac ako 21, prehral
                print("You bust, dealer wins!")
                cash -= bet
                dealerwins += 1
                print(f"Balance: {cash}€")
                gameover = True
                break
            elif totalP == 21: #hrac ma presne 21, dealer ho uz neprekona, vyhrava
                print("You won!")
                playerwins += 1
                cash += bet
                print(f"Balance: {cash}€")
                gameover = True
                break
            
        
        totalP = sumPlayer()
        totalD = sumDealer() #posledna kontrola pred uzavretim

        while totalD < 17 and gameover == False: #dealer taha po 17 podla pravidiel blackjacku
            newCardDealer()
            totalD = sumDealer()

        #zaverecne kontroly a pridelenie vyhry podla suctu
        if totalD > 21: #krupier ma vela, hrac vyhrava
            print("Dealer busts, you won!")
            cash += bet
            playerwins += 1
            print(f"Balance: {cash}€")
        elif totalD > totalP: #krupier ma viac ako hrac, hrac prehrava
            print("Dealer won!")
            cash -= bet
            dealerwins += 1
            print(f"Balance: {cash}€")
        elif totalD < totalP and totalP <= 21: #hrac ma viac ako krupier a menej ako 21, vyhrava
            print("You won!")
            cash += bet
            playerwins += 1
            print(f"Balance: {cash}€")
        elif totalD == totalP: #remiza, nikto nic nevyhral ani neprehral
            print("Push, nobody wins!")
            print(f"Balance: {cash}€")
            push += 1

    commands = input("Press enter to play again or type 'leave' to leave...") #opakovanie hry, pripadne koniec a zobrazenie statistik
    
    if commands == "rules" or commands == "help": #zobrazenie pravidiel uprostred hry
        clear()
        rules()
        commands = input()
        commands = ""

    if commands == "leave": #hrac ukoncil hru, zobrazia sa statistiky
        print("\n\n--Thank you for playing!--\n")
        time.sleep(1)
        print("--------Your stats--------\n")
        time.sleep(0.5)
        print("Wins:", playerwins) #pocet vyhier
        time.sleep(0.5)
        print("Losses:", dealerwins) #pocet prehier
        time.sleep(0.5)
        print("Draws:", push) #pocet remiz
        time.sleep(0.5)
        print(f"Money won: {cash-cash_before}€") #penazna vyhra/prehra
        time.sleep(0.5)
        print("\n---Press any key to quit--") #caka na vstup pre ukoncenie
        exit()
    clear()


