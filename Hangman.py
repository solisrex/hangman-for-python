import pygame, sys, math, ctypes, string, random
from pygame.locals import *

pygame.init()
length = 750
DISPLAYSURF = pygame.display.set_mode((length,length))
pygame.display.set_caption("Hangman")
WHITE = (255,255,255)
LITEGREY = (200, 200, 200)
GREY = (130, 130, 130)
BLACK = (  0, 0,   0)
DISPLAYSURF.fill(GREY)
fontObj = pygame.font.SysFont('calibri', 32)
text = fontObj.render("TYPE A WORD", True, WHITE)
w,h = text.get_width(), text.get_height()
DISPLAYSURF.blit(text,(length/2-w/2,h/2))
colors = []
def draw_screen(counter):
    global colors
    colors+=[(random.randint(0,255),random.randint(0,255),random.randint(0,255),255)]
    for i in range(counter):
        s = pygame.Surface((length/3,length/3), pygame.SRCALPHA)    # per-pixel alpha
        s.fill(colors[i])                                                   # notice the alpha value in the color
        DISPLAYSURF.blit(s, (length/3*(i%3),length/3*(i//3)))

def reveal(secret,revealedstring,letter):
    if len(secret)==len(revealedstring):
        out = ""
        for checkletter in range(len(revealedstring)):
            if letter == secret[checkletter]:
                out += letter
            else:
                out += revealedstring[checkletter]
        return out
    else:
        return None

def main():
    global colors
    word = ""
    hanging = False
    counter = 0
    gameover = False
    revealed = None
    secret = None
    font = "calibri"
    while True:
        global letters
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.unicode in string.ascii_letters:
                    if hanging == False and gameover == False:
                        word+=event.unicode.upper()
                        DISPLAYSURF.fill(GREY)
                        fontObj = pygame.font.SysFont(font, 32)
                        text = fontObj.render(" ".join(word), True, WHITE)
                        w,h = text.get_width(), text.get_height()
                        DISPLAYSURF.blit(text,(length/2-w/2,length/2-h/2))
                        text = fontObj.render("TYPE A WORD", True, WHITE)
                        w,h = text.get_width(), text.get_height()
                        DISPLAYSURF.blit(text,(length/2-w/2,h/2))
                    elif hanging == True and gameover == False:
                        if reveal(secret,revealed,event.unicode.upper()) == revealed:
                            counter+=1;
                            DISPLAYSURF.fill(GREY)
                            draw_screen(counter)
                            fontObj = pygame.font.SysFont(font, 32)
                            text = fontObj.render(" ".join(revealed), True, WHITE)
                            w,h = text.get_width(), text.get_height()
                            DISPLAYSURF.blit(text,(length/2-w/2,length/2-h/2))
                            text = fontObj.render("GUESS THE WORD", True, WHITE)
                            w,h = text.get_width(), text.get_height()
                            DISPLAYSURF.blit(text,(length/2-w/2,h/2))
                        else:
                            revealed = reveal(secret,revealed,event.unicode.upper())
                            DISPLAYSURF.fill(GREY)
                            draw_screen(counter)
                            fontObj = pygame.font.SysFont(font, 32)
                            text = fontObj.render(" ".join(revealed), True, WHITE)
                            w,h = text.get_width(), text.get_height()
                            DISPLAYSURF.blit(text,(length/2-w/2,length/2-h/2))
                            text = fontObj.render("GUESS THE WORD", True, WHITE)
                            w,h = text.get_width(), text.get_height()
                            DISPLAYSURF.blit(text,(length/2-w/2,h/2))
                elif event.key == 8 and gameover == False and hanging == False:
                    word = word[:-1]
                    DISPLAYSURF.fill(GREY)
                    fontObj = pygame.font.SysFont(font, 32)
                    text = fontObj.render(" ".join(word), True, WHITE)
                    w,h = text.get_width(), text.get_height()
                    DISPLAYSURF.blit(text,(length/2-w/2,length/2-h/2))
                    text = fontObj.render("TYPE A WORD", True, WHITE)
                    w,h = text.get_width(), text.get_height()
                    DISPLAYSURF.blit(text,(length/2-w/2,h/2))
                elif event.key == 13 and gameover == False:
                    hanging = True
                    secret = word
                    revealed="_"*len(secret)
                    DISPLAYSURF.fill(GREY)
                    fontObj = pygame.font.SysFont(font, 32)
                    text = fontObj.render(" ".join(revealed), True, WHITE)
                    w,h = text.get_width(), text.get_height()
                    DISPLAYSURF.blit(text,(length/2-w/2,length/2-h/2))
                    text = fontObj.render("GUESS THE WORD", True, WHITE)
                    w,h = text.get_width(), text.get_height()
                    DISPLAYSURF.blit(text,(length/2-w/2,h/2))
                elif event.key == 13 and gameover == True:
                    colors =[]
                    word = ""
                    hanging = False
                    counter = 0
                    gameover = False
                    revealed = None
                    secret = None
                    DISPLAYSURF.fill(GREY)
                    fontObj = pygame.font.SysFont(font, 32)
                    text = fontObj.render("TYPE A WORD", True, WHITE)
                    w,h = text.get_width(), text.get_height()
                    DISPLAYSURF.blit(text,(length/2-w/2,h/2))
                elif event.key == 27:
                    pygame.quit()
                    sys.exit()
        if counter > 8:
            gameover = True
            DISPLAYSURF.fill(GREY)
            draw_screen(counter)
            counter=0
            colors=[]
            fontObj = pygame.font.SysFont(font, 32)
            text = fontObj.render(" ".join(word), True, WHITE)
            w,h = text.get_width(), text.get_height()
            DISPLAYSURF.blit(text,(length/2-w/2,length/2-h/2))
            text = fontObj.render("GAME OVER", True, WHITE)
            w,h = text.get_width(), text.get_height()
            DISPLAYSURF.blit(text,(length/2-w/2,h/2))
            fontObj = pygame.font.SysFont(font, 12)
            text = fontObj.render("Press enter to restart.", True, WHITE)
            w,h = text.get_width(), text.get_height()
            DISPLAYSURF.blit(text,(length/2-w/2,5*h))
        if secret == revealed and (secret and revealed) != None:
            gameover = True
            DISPLAYSURF.fill(GREY)
            draw_screen(counter)
            counter= 0
            colors = []
            fontObj = pygame.font.SysFont(font, 32)
            text = fontObj.render(" ".join(word), True, WHITE)
            w,h = text.get_width(), text.get_height()
            DISPLAYSURF.blit(text,(length/2-w/2,length/2-h/2))
            text = fontObj.render("YOU WIN", True, WHITE)
            w,h = text.get_width(), text.get_height()
            DISPLAYSURF.blit(text,(length/2-w/2,h/2))
            fontObj = pygame.font.SysFont(font, 12)
            text = fontObj.render("Press enter to restart.", True, WHITE)
            w,h = text.get_width(), text.get_height()
            DISPLAYSURF.blit(text,(length/2-w/2,5*h))
        pygame.display.update()
main()
