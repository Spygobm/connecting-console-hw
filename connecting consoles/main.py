import pgzrun 
import random 

HEIGHT = 600
WIDTH = 800

consoles = []
number_of_consoles = 10
next_console = 0

def creating_console():
    global console
    for i in range (number_of_consoles):
        console = Actor("console")
        console.pos = (random.randint(20,WIDTH - 20),random.randint(20,HEIGHT - 20))
        consoles.append(console)



def draw():
    screen.clear()
    screen.blit("backround",(0,0))
    for item in consoles:
        item.draw()

creating_console()

pgzrun.go()