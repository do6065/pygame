import pygame
import sys
import random
import time

pygame.init()

# 게임화면
Color = (255,255,255)
BLACK = (0,0,0)
size  = [600,400]
screen= pygame.display.set_mode(size)

#게임이름
pygame.display.set_caption("Memory")

done = False
clock = pygame.time.Clock()

#사용할 폰트
game_font = pygame.font.Font(None, 80)
click_font = pygame.font.Font(None, 40)


#게임 작동 부분
def run_game():
    global done, ques, ans

    ques=[]
    ans=[]

    i=1
    time=1000
    score=0

    left= game_font.render("Left",0,(0,0,0))
    right= game_font.render("Right",0,(0,0,0))

    while not done:
        clock.tick(10)
        screen.fill(Color)
        pic= random.randint(0,1)
        if pic == 0:
            screen.blit(left,(220,150))
            ques.append(0)
        else:
            screen.blit(right,(220,150))
            ques.append(1)

        if i==4:
            done=True
        i+=1
        pygame.display.update()


#게임 시작화면
def game_start():
    global done
    start_text= game_font.render("Memory",  0, (0,0,0))
    start_txt= click_font.render("Click...",  0, (0,0,0))
    start= game_font.render("start",  0, (0,0,0))

    while not done:
        screen.fill(Color)
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                t=time.time()
                start_text= game_font.render("Memory",  0, Color)
                start_txt= click_font.render("Click...",  0, Color)
                pygame.time.wait(1000)
                run_game()

        screen.blit(start_text,(190,100))
        screen.blit(start_txt, (250,300))
        pygame.display.update()
        pygame.time.wait(1000)



game_start()
pygame.quit()



















