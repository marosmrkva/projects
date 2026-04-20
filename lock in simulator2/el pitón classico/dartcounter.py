import tkinter as tk
import keyboard

m = tk.Tk()
m.title("Dartcounter")

globalfont = "calibri 25"
buttonfont = "calibri 17"

player1_name = tk.Entry(m, text="Hráč 1", font=globalfont, bd=5)
player1_name.grid(row=2, column=1)

player1_turn = tk.Label(m, text="", bg="lime", width=20, font=globalfont, bd=5)
player1_turn.grid(row=7, column=1)

player2_name = tk.Entry(m, text="Hráč 2", font=globalfont, bd=5)
player2_name.grid(row=2, column=3)

player2_turn = tk.Label(m, text="", bg="white", width=20, font=globalfont, bd=5)
player2_turn.grid(row=7, column=3)

player1_score = 0
player1_score_save = 0
player1_legs = 0
player1_sets = 0
player1_all = []
player1_avg = 0

player2_score = 0
player2_score_save = 0
player2_legs = 0
player2_sets = 0
player2_all = []
player2_avg = 0

legstarter = False
setstarter = False

turn = False
gametype = 0

def enter(event):
    global turn, player1_score, player1_score_save, player2_score, player2_score_save, player1_legs, player2_legs, player1_sets, player2_sets, player1_all, player2_all, player1_avg, player2_avg

    score_var = score.get()

    if score_var == "":
        match turn:
            case False:
                player1_all.append(0)
                passturn()
                return
            case True:
                player2_all.append(0)
                passturn()
                return

    score_var = int(score_var)
    score.delete(0,"end")
    

    match turn:
        case False:
            passturn()
            if score_var > player1_score: #bust
                player1_all.append(0)
                player1_avg = round(sum(player1_all)/len(player1_all), 2)
                return
            player1_all.append(score_var)
            player1_avg = round(sum(player1_all)/len(player1_all), 2)
            player1_score -= score_var
            
            if player1_score == 0: #koniec legu
                passleg()
                match legstarter:
                    case True:
                        turn = True
                        player1_turn.config(bg="white")
                        player2_turn.config(bg="lime")
                    case False:
                        turn = False
                        player1_turn.config(bg="lime")
                        player2_turn.config(bg="white")
                player1_legs += 1
                player1_score = gametype
                player2_score = gametype
                if player1_legs == 3: #koniec setu
                    passset()
                    match setstarter:
                        case True:
                            turn = True
                            player1_turn.config(bg="white")
                            player2_turn.config(bg="lime")
                        case False:
                            turn = False
                            player1_turn.config(bg="lime")
                            player2_turn.config(bg="white")
                    player1_legs = 0
                    player2_legs = 0
                    player1_sets += 1
                    if player1_sets == 3: #koniec hry
                        player1_score = gametype
                        player2_score = gametype
                        player1_legs = 0
                        player1_sets = 0
                        player2_legs = 0
                        player2_sets = 0

        case True:
            passturn()
            if score_var > player2_score: #bust
                player2_all.append(0)
                player2_avg = round(sum(player2_all)/len(player2_all), 2)
                return
            player2_all.append(score_var)
            player2_avg = round(sum(player2_all)/len(player2_all), 2)
            player2_score -= score_var
            
            if player2_score == 0: #koniec legu
                passleg()
                match legstarter:
                    case True:
                        turn = True
                        player1_turn.config(bg="white")
                        player2_turn.config(bg="lime")
                    case False:
                        turn = False
                        player1_turn.config(bg="lime")
                        player2_turn.config(bg="white")             
                player2_legs += 1
                player1_score = gametype
                player2_score = gametype
                if player2_legs == 3: #koniec setu
                    passset()
                    match setstarter:
                        case True:
                            turn = True
                            player1_turn.config(bg="white")
                            player2_turn.config(bg="lime")
                        case False:
                            turn = False
                            player1_turn.config(bg="lime")
                            player2_turn.config(bg="white")
                    player1_legs = 0
                    player2_legs = 0
                    player2_sets += 1
                    if player2_sets == 3: #koniec hry
                        player1_score = gametype
                        player2_score = gametype
                        player1_legs = 0
                        player1_sets = 0
                        player2_legs = 0
                        player2_sets = 0
            
    
    
    

    player1_score_label.config(text = player1_score)
    player2_score_label.config(text = player2_score)
    player1_legs_label.config(text = ("Legs:", player1_legs))
    player2_legs_label.config(text = ("Legs:", player2_legs))
    player1_sets_label.config(text = ("Sets:", player1_sets))
    player2_sets_label.config(text = ("Sets:", player2_sets))
    player1_avg_label.config(text = ("Avg:", player1_avg))
    player2_avg_label.config(text = ("Avg:", player2_avg))

    
def passturn():
    global turn

    match turn:
        case True:
            player1_turn.config(bg="lime")
            player2_turn.config(bg="white")
            turn = False
            return
        case False:
            player1_turn.config(bg="white")
            player2_turn.config(bg="lime")
            turn = True
            return

def passleg():
    global legstarter

    match legstarter:
        case True:
            legstarter = False
            return
        case False:
            legstarter = True
            return
        
def passset():
    global setstarter

    match setstarter:
        case True:
            setstarter = False
            return
        case False:
            setstarter = True
            return


def play_301():
    global player1_score, player2_score, player1_legs, player2_legs, player1_sets, player2_sets, gametype, player1_all, player2_all, player1_avg, player2_avg

    gametype = 301

    player1_score = 301
    player2_score = 301
    player1_legs = 0
    player2_legs = 0
    player1_sets = 0
    player2_sets = 0
    player1_all = []
    player2_all = []
    player1_avg = 0
    player2_avg = 0

    player1_score_label.config(text = player1_score)
    player2_score_label.config(text = player2_score)
    player1_legs_label.config(text = ("Legs:", player1_legs))
    player2_legs_label.config(text = ("Legs:", player2_legs))
    player1_sets_label.config(text = ("Sets:", player1_sets))
    player2_sets_label.config(text = ("Sets:", player2_sets))
    player1_avg_label.config(text = ("Avg:", player1_avg))
    player2_avg_label.config(text = ("Avg:", player2_avg))


def play_501():
    global player1_score, player2_score, player1_legs, player2_legs, player1_sets, player2_sets, gametype, player1_all, player2_all, player1_avg, player2_avg

    gametype = 501

    player1_score = 501
    player2_score = 501
    player1_legs = 0
    player2_legs = 0
    player1_sets = 0
    player2_sets = 0
    player1_all = []
    player2_all = []
    player1_avg = 0
    player2_avg = 0

    player1_score_label.config(text = player1_score)
    player2_score_label.config(text = player2_score)
    player1_legs_label.config(text = ("Legs:", player1_legs))
    player2_legs_label.config(text = ("Legs:", player2_legs))
    player1_sets_label.config(text = ("Sets:", player1_sets))
    player2_sets_label.config(text = ("Sets:", player2_sets))
    player1_avg_label.config(text = ("Avg:", player1_avg))
    player2_avg_label.config(text = ("Avg:", player2_avg))



pickscore_301 = tk.Button(m, text="New 301", width=25, height=1, command=play_301, font=buttonfont, bd=5)
pickscore_301.grid(row=5, column=2)
pickscore_501 = tk.Button(m, text="New 501", width=25, height=1, command=play_501, font=buttonfont, bd=5)
pickscore_501.grid(row=6, column=2)
exitbutton = tk.Button(m, text="Quit", width=25, height=1, command=exit, font=buttonfont, bg="red", bd=5)
exitbutton.grid(row=7, column=2)

player1_score_label = tk.Label(m, text = player1_score, font=globalfont, height=2)
player1_score_label.grid(row=3, column=1)
player2_score_label = tk.Label(m, text = player2_score, font=globalfont, height=2)
player2_score_label.grid(row=3, column=3)

player1_legs_label = tk.Label(m, text = ("Legs:", player1_score), font=globalfont, height=2)
player1_legs_label.grid(row=4, column=1)
player2_legs_label = tk.Label(m, text = ("Legs:", player2_score), font=globalfont, height=2)
player2_legs_label.grid(row=4, column=3)

player1_sets_label = tk.Label(m, text = ("Sets:", player1_score), font=globalfont, height=2)
player1_sets_label.grid(row=5, column=1)
player2_sets_label = tk.Label(m, text = ("Sets:", player2_score), font=globalfont, height=2)
player2_sets_label.grid(row=5, column=3)

player1_avg_label = tk.Label(m, text = ("Avg:", player1_avg), font=globalfont, height=2)
player1_avg_label.grid(row=6, column=1)
player2_avg_label = tk.Label(m, text = ("Avg:", player2_avg), font=globalfont, height=2)
player2_avg_label.grid(row=6, column=3,)

score = tk.Entry(m, font=globalfont)
score.grid(row=2, column=2)
score.bind("<Return>", enter)

m.mainloop()