
# coding: utf-8

# In[1]:


import random, os


# In[2]:


wins = ((1,2,3), (4,5,6), (7,8,9),
        (1,4,7), (2,5,8), (3,6,9),
        (1,5,9), (3,5,7))


# In[3]:


def print_board():
    print ("Pole gry: ")
    a = "[1] [2] [3]"
    b = "[4] [5] [6]"
    c = "[7] [8] [9]"
    
    print (a)
    print (b)
    print (c)

print_board()

pole_gry = ["/", "/", "/", "/", "/", "/", "/", "/", "/"]

def check(strzal):
    if pole_gry[strzal-1] == "O" or pole_gry[strzal-1] == "X":
        return False
    elif strzal > 9 or strzal < 1:
        print ("Nie trafiłeś w tarczę!")
    else:
        return True
    
ruchy_gracza = []
ruchy_cpu = []

def won(ruchy, gracz):
    for i in wins:
        if set(i).issubset(ruchy):
            win = 1
            os.system('clear')
            print ("Wygrał", gracz)
            print ("")
            plansza()
            return True

def rysuj_gracz(pole):
    if check(pole) == True:
        pole_gry[pole-1] = "X"
        ruchy_gracza.append(pole)
        #won(ruchy_gracza,gracz)
        return ruchy_gracza
    #won(ruchy_gracza)
    
def plansza():
    a = pole_gry[:3]
    b = pole_gry[3:6]
    c = pole_gry[6:]
    for i in a:
        print (i,"", end="")
    print ("")
    for i in b:
        print (i,"", end="")
    print ("")
    for i in c:
        print (i,"", end="")
    #print (a)
    #print (b)
    #print (c)    

def rysuj_cpu(pole):
    if check(pole) == True:
        pole_gry[pole-1] = "O"
        ruchy_cpu.append(pole)
        return ruchy_cpu
    #won(ruchy_cpu)


# In[4]:


gracz = input("Wprowadź imię: ")
win = 0
while win != 1:
    strzal_gracza = int(input("Gdzie stawiasz iks?"))
    if won(rysuj_gracz(strzal_gracza), gracz) == True:
        break
    strzal_cpu = random.randrange(1,10)
    while check(strzal_cpu) == False:
        strzal_cpu = random.randrange(1,10)
    if won (rysuj_cpu(strzal_cpu), "CPU") == True:
        break
    os.system('clear')
    plansza()
    print_board()

