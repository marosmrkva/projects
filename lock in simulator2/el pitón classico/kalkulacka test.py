import tkinter as tk

m = tk.Tk() #vytvorime okno

window_str = "" #prazdne pole vstupu
cantypemarks = False #poistka proti dvom znamienkam za sebou

def type_1(): #napise 1 po stlaceni 1
    global window_str, cantypemarks
    
    cantypemarks = True
    window_str = window_str + "1"
    window.config(text = window_str)

def type_2(): #napise 2 po stlaceni 2
    global window_str, cantypemarks

    cantypemarks = True
    window_str = window_str + "2"
    window.config(text = window_str)

def type_3(): #napise 3 po stlaceni 3
    global window_str, cantypemarks
    
    cantypemarks = True
    window_str = window_str + "3"
    window.config(text = window_str)

def type_4(): #napise 4 po stlaceni 4
    global window_str, cantypemarks
    
    cantypemarks = True
    window_str = window_str + "4"
    window.config(text = window_str)

def type_5(): #napise 5 po stlaceni 5
    global window_str, cantypemarks
    
    cantypemarks = True
    window_str = window_str + "5"
    window.config(text = window_str)

def type_6(): #napise 6 po stlaceni 6
    global window_str, cantypemarks
    
    cantypemarks = True
    window_str = window_str + "6"
    window.config(text = window_str)

def type_7(): #napise 7 po stlaceni 7
    global window_str, cantypemarks
    
    cantypemarks = True
    window_str = window_str + "7"
    window.config(text = window_str)

def type_8(): #napise 8 po stlaceni 8
    global window_str, cantypemarks
    
    cantypemarks = True
    window_str = window_str + "8"
    window.config(text = window_str)

def type_9(): #napise 9 po stlaceni 9
    global window_str, cantypemarks
    
    cantypemarks = True
    window_str = window_str + "9"
    window.config(text = window_str)

def type_0(): #napise 0 po stlaceni 0
    global window_str, cantypemarks
    
    cantypemarks = True
    window_str = window_str + "0"
    window.config(text = window_str)

def type_plus(): #napise + po stlaceni +
    global window_str, cantypemarks
    
    if cantypemarks == True:
        window_str = window_str + "+"
        cantypemarks = False
        window.config(text = window_str)

def type_minus(): #napise - po stlaceni -
    global window_str, cantypemarks

    if cantypemarks == True:
        window_str = window_str + "-"
        cantypemarks = False
        window.config(text = window_str)

def type_multi(): #napise × po stlaceni ×
    global window_str, cantypemarks
    
    if cantypemarks == True:
        window_str = window_str + "×"
        cantypemarks = False
        window.config(text = window_str)

def type_div(): #napise ÷ po stlaceni ÷
    global window_str, cantypemarks
    
    if cantypemarks == True:
        window_str = window_str + "÷"
        cantypemarks = False
        window.config(text = window_str)

def type_dec(): #napise , po stlaceni ,
    global window_str, cantypemarks
    if cantypemarks == True:
        window_str = window_str + "."
        cantypemarks = False
        window.config(text = window_str)


#===========================================================================================================
#                                         PRE ZATVORKY TREBA DOPLNIT 
#===========================================================================================================

def type_bracket_open(): #napise ( po stlaceni ,
    global window_str, cantypemarks, openbrackets_count

    window_str = window_str + "("
    cantypemarks = False
    window.config(text = window_str)
    openbrackets_count += 1

def type_bracket_close(): #napise ) po stlaceni ,
    global window_str, cantypemarks, closebrackets_count

    window_str = window_str + ")"
    window.config(text = window_str)
    closebrackets_count += 1

#===========================================================================================================
#                                         PRE ZATVORKY TREBA DOPLNIT
#===========================================================================================================

"""
def operation(op1, op2, eq): #prechadza zoznam, ak najde operaciu vykona ju a nahradi pouzite prvky vysledkom pre dalsie pocitanie
    eq_len = len(eq)
    pointer = 0
    while pointer != eq_len:
            if eq[pointer] in (op1, op2): #ak pointer ukazuje na znamienko
                match eq[pointer]: #najdeme danu operaciu a vykoname
                    case "×":
                        eq[pointer] = eq[pointer-1] * eq[pointer+1] #vynasobime
                    case "÷":
                        eq[pointer] = eq[pointer-1] / eq[pointer+1] #vydelime
                    case "+":
                        eq[pointer] = eq[pointer-1] + eq[pointer+1] #scitame
                    case "-":
                        eq[pointer] = eq[pointer-1] - eq[pointer+1] #odcitame
                eq.pop(pointer-1) #odstranime prvy prvok operacie
                eq.pop(pointer) #indexy sa posunuli
                eq_len = len(eq)
            else:
                pointer += 1 #inak posunieme pointer dalej na prehladavanie
    
    return eq #vrati rovnicu ako zoznam bez hladanych operacii (uz su vykonane)


def equals(): #spracuje zadanu rovnicu, zavola funkciu na vypocty (operations) a aktualizuje displej na vysledok s ktorym sa da dalej pocitat
    global window_str

    if not cantypemarks: #false znamena ze posledny znak je znamienko = error
        window_str = "Syntax error"
        window.config(text=window_str)
        return
    else:
        eq = window_str.split() #rozdeli rovnicu na cisla a znamienka
        for i in range(len(eq)): #prejdeme cely zoznam
            if eq[i] not in ("+", "-", "×", "÷"): #ak je to cislo (nie je znamienko)
                eq[i] = float(eq[i]) #zmenime na float keby sme mali desatinne cisla

        eq = operation("×", "÷", eq) #najprv prejde zadanu rovnicu a hlada nasobenie a delenie (priorita)  
        eq = operation("+", "-", eq) #druhy prechod hlada scitanie a odcitanie

        window_str = str(round(eq[0], 10)) #zaokruhli na 10 desatinnych miest (pre istotu)
        window.config(text=window_str) #aktualizuje displej na finalny vysledok
"""

#===========================================================================================================
#                                         Dvorakove funkcie
#===========================================================================================================


def operator(vyraz):
    """
    vrati vyraz s odstranenymi vnejsimi zavorkami
    a pozici operatoru, ktery bude aplikovan jako posledni
    ci None, pokud takovy neexistuje
    """
    aditOp, multiOp, pocetZavorek = 0, 0, 0

    for i in range(len(vyraz)):
        znak = vyraz[i]
        if znak == '(': pocetZavorek += 1
        if znak == ')': pocetZavorek -= 1
        if znak == '+' or znak == '-':        # aditivní operátor 
            if pocetZavorek == 0: aditOp = i  # mimo závorky
        if znak == '×' or znak == '÷':        # multiplikativní operátor
            if pocetZavorek == 0: multiOp = i # mimo závorky
            
    if aditOp > 0: return vyraz, aditOp
    if multiOp > 0: return vyraz, multiOp

    if vyraz[0] == '(':                       # vnejsi zavorky
        return operator(vyraz[1:-1])          # odstranime

    return vyraz, None                        # konstanta

def hodnota(vyraz):
    """ vrati hodnotu zadaneho vyrazu """   
    vyraz, posledni = operator(vyraz)
    if posledni == None: return float(vyraz)    # konstanta
    levy = vyraz[:posledni]
    pravy = vyraz[posledni+1:]
    if vyraz[posledni] == '+': return hodnota(levy) + hodnota(pravy)
    if vyraz[posledni] == '-': return hodnota(levy) - hodnota(pravy)
    if vyraz[posledni] == '×': return hodnota(levy) * hodnota(pravy)
    if vyraz[posledni] == '÷': return hodnota(levy) / hodnota(pravy)


def print_result():
    global window_str, cantypemarks, openbrackets_count, closebrackets_count

    if window_str[len(window_str)-1] == ")":
        cantypemarks = True

    if openbrackets_count != closebrackets_count or cantypemarks == False:
        window_str = "Syntax error"
        return

    openbrackets_count, closebrackets_count = 0, 0

    window_str = hodnota(window_str)
    window.config(text = window_str)



#===========================================================================================================
#                                      Dvorakove funkcie koniec
#===========================================================================================================


def clearinput(): #vycisti displej na ""
    global window_str, openbrackets_count, closebrackets_count

    openbrackets_count, closebrackets_count = 0, 0

    window_str = ""
    window.config(text=window_str)


window = tk.Label(m, text=window_str, font="Calibri, 30", height=3, width=20, anchor="e") #displej (okno na vstup/vystup), anchor="e" - pripnute na "east" vychodny (pravy) okraj
window.grid(row=1, column=1, columnspan=4, sticky="ew") #sticky="ew" - eastwest, columnspan=4 - kolko stlpcov zaberie (teraz 4)

openbrackets_count = 0
closebrackets_count = 0

buttonfont = "comicsans 25"
buttonwidth = 5
buttonheight = 2


button_1 = tk.Button(m, text="1", font=buttonfont, width=buttonwidth, height=buttonheight, command=type_1) #tlacidlo 1
button_1.grid(row=4, column=1)
button_2 = tk.Button(m, text="2", font=buttonfont, width=buttonwidth, height=buttonheight, command=type_2) #tlacidlo 2
button_2.grid(row=4, column=2)
button_3 = tk.Button(m, text="3", font=buttonfont, width=buttonwidth, height=buttonheight, command=type_3) #tlacidlo 3
button_3.grid(row=4, column=3)

button_4 = tk.Button(m, text="4", font=buttonfont, width=buttonwidth, height=buttonheight, command=type_4) #tlacidlo 4
button_4.grid(row=3, column=1)
button_5 = tk.Button(m, text="5", font=buttonfont, width=buttonwidth, height=buttonheight, command=type_5) #tlacidlo 5
button_5.grid(row=3, column=2)
button_6 = tk.Button(m, text="6", font=buttonfont, width=buttonwidth, height=buttonheight, command=type_6) #tlacidlo 6
button_6.grid(row=3, column=3)

button_7 = tk.Button(m, text="7", font=buttonfont, width=buttonwidth, height=buttonheight, command=type_7) #tlacidlo 7
button_7.grid(row=2, column=1)
button_8 = tk.Button(m, text="8", font=buttonfont, width=buttonwidth, height=buttonheight, command=type_8) #tlacidlo 8
button_8.grid(row=2, column=2)
button_9 = tk.Button(m, text="9", font=buttonfont, width=buttonwidth, height=buttonheight, command=type_9) #tlacidlo 9
button_9.grid(row=2, column=3)

button_dec = tk.Button(m, text=".", font=buttonfont, width=buttonwidth, height=buttonheight, command=type_dec) #tlacidlo ,
button_dec.grid(row=5, column=1)
button_0 = tk.Button(m, text="0", font=buttonfont, width=buttonwidth, height=buttonheight, command=type_0) #tlacidlo 0
button_0.grid(row=5, column=2)
button_eq = tk.Button(m, text="=", font=buttonfont, width=buttonwidth, height=buttonheight, command=print_result) #tlacidlo =
button_eq.grid(row=5, column=3)

button_plus = tk.Button(m, text="+", font=buttonfont, width=buttonwidth, height=buttonheight, command=type_plus) #tlacidlo +
button_plus.grid(row=2, column=4)
button_minus = tk.Button(m, text="-", font=buttonfont, width=buttonwidth, height=buttonheight, command=type_minus) #tlacidlo -
button_minus.grid(row=3, column=4)
button_multi = tk.Button(m, text="×", font=buttonfont, width=buttonwidth, height=buttonheight, command=type_multi) #tlacidlo ×
button_multi.grid(row=4, column=4)
button_div= tk.Button(m, text="÷", font=buttonfont, width=buttonwidth, height=buttonheight, command=type_div) #tlacidlo ÷
button_div.grid(row=5, column=4)
button_open_bracket = tk.Button(m, text="(", font=buttonfont, width=buttonwidth, height=buttonheight, command=type_bracket_open) #tlacidlo (
button_open_bracket.grid(row=2, column=5)
button_close_bracket= tk.Button(m, text=")", font=buttonfont, width=buttonwidth, height=buttonheight, command=type_bracket_close) #tlacidlo )
button_close_bracket.grid(row=3, column=5)

clear_button = tk.Button(m, text="CLEAR", font=buttonfont, command=clearinput, width=29) #tlacidlo clear
clear_button.grid(row=6, column=1, columnspan=5)

m.mainloop()