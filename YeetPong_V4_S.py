#########################################
# File Name: YeetPong_V4_S
# Description: PONG
# Author: Sunny, Michael, Justin
# Date: 10/29/18
#########################################

#
# V4_S
# RANDOM VERTICAL DIRECTION, PROPER SERVING, MAIN MENU TEXT
#

import pygame
from random import randint
pygame.init()
WIDTH = 800
HEIGHT= 600
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

TOP    = 0  
BOTTOM = HEIGHT
LEFT   = 0     
RIGHT  = WIDTH 
GREEN = (  0,255,  0)
BLUE  = (  0,  0,128)
WHITE = (255,255,255)
BLACK = (  0,  0,  0)
GREY  = (100,100,100)
outline = 0
timeDelay = 3
flagY = False
font = pygame.font.SysFont("Courier Regular",75)
MAX_SCORE = 7
mainMenu = True

#---------------------------------------#
# functions                             #
#---------------------------------------#

def redrawGameWindow():
    gameWindow.fill(BLACK)
    pygame.draw.rect(gameWindow,GREY,(WIDTH/2-5,0,5,HEIGHT),outline)
    p1ScoreRender = font.render(str(player1Score), 1, WHITE)
    p2ScoreRender = font.render(str(player2Score), 1, WHITE)
    gameWindow.blit(p1ScoreRender,((WIDTH/2 + (WIDTH/2)/2),35))
    gameWindow.blit(p2ScoreRender,((WIDTH/2 - (WIDTH/2)/2),35))
    pygame.draw.circle(gameWindow, WHITE, (ballX, ballY), ballR, outline)
    pygame.draw.rect(gameWindow, WHITE, (paddle1X, paddle1Y, paddleW, paddleH), outline)
    pygame.draw.rect(gameWindow, WHITE, (paddle2X, paddle2Y, paddleW, paddleH), outline)
    pygame.display.update()

def redrawMainMenu():
    gameWindow.fill(BLACK)
    menuMessage = font.render("Press ENTER to start", 1,WHITE)
    gameWindow.blit(menuMessage,(1,1))
    pygame.display.update()

def randDirection():
    vertical = randint(0,1)
    if vertical == 0:
        return -1
    if vertical == 1:
        return 1
#---------------------------------------#
# main program                          #
#---------------------------------------#

# MAIN MENU

while mainMenu == True:
    redrawMainMenu()
    pygame.event.clear()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        mainMenu = False
        print "YEET"
    elif keys[pygame.K_ESCAPE]:
        pygame.quit()
    
print "Hit ESC to end the program."


# GAME INITIALIZATION

# players
player1Score = 0 # right side
player2Score = 0 # left side

# ball properties
ballR  = 15
ballX  =  WIDTH/2
ballY  =  HEIGHT/2
speedX =  1
speedY =  1

# paddle properties 
paddleW  = 20
paddleH  = 120
paddleShift = 2

# paddle 1
paddle1X = RIGHT - paddleW - 20
paddle1Y = (BOTTOM/2) - (paddleH/2)

# paddle 2
paddle2X = LEFT + 20
paddle2Y = (BOTTOM/2) - (paddleH/2)

# GAME LOOP

inPlay = True

redrawGameWindow()
pygame.time.delay(2000)

while inPlay:
    redrawGameWindow()
    pygame.time.delay(timeDelay)

    # ~~~~~~~~ USER INPUTS ~~~~~~~ #
    
    pygame.event.clear()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    if keys[pygame.K_a]:
        paddle2Y = paddle2Y - paddleShift
    if keys[pygame.K_d]:
        paddle2Y = paddle2Y + paddleShift
    if keys[pygame.K_LEFT]:
        paddle1Y = paddle1Y - paddleShift
    if keys[pygame.K_RIGHT]:
        paddle1Y = paddle1Y + paddleShift

    # ~~~~~~~ PREVENT PADDLES FROM GOING OFF-SCREEN ~~~~~~~ #

    if paddle1Y <= 0:
        paddle1Y = 0
    if paddle1Y >= BOTTOM - paddleH:
        paddle1Y = BOTTOM - paddleH

    if paddle2Y <= 0:
        paddle2Y = 0
    if paddle2Y >= BOTTOM - paddleH:
        paddle2Y = BOTTOM - paddleH

    # bounce from walls
    if ballY + ballR == BOTTOM:
        speedY = -speedY
    if ballY - ballR == TOP:
        speedY = -speedY

    # ~~~~~~~ BOUNCE FROM PADDLES ~~~~~~~ #

    # PADDLE 1
    if ballY >= paddle1Y and ballY <= paddle1Y + paddleH and ballX + ballR == paddle1X:
        speedX = -speedX
    if ballX >= paddle1X and ballY + ballR >= paddle1Y and ballY + ballR <= paddle1Y + 60 or ballX >= paddle1X and ballY - ballR <= paddle1Y + paddleH and ballY - ballR >= paddle1Y + paddleH - 60:
        if flagY == False:
            speedY = -speedY
            flagY = True
        if flagY == True:
            speedY = speedY
        
    #PADDLE 2
    if ballY >= paddle2Y and ballY <= paddle2Y + paddleH and ballX - ballR == paddle2X + paddleW:
        speedX = -speedX
    if ballX <= paddle2X + paddleW and ballY + ballR >= paddle2Y and ballY + ballR <= paddle2Y + 60 or ballX <= paddle2X + paddleW and ballY - ballR <= paddle2Y + paddleH and ballY - ballR >= paddle2Y + paddleH - 60:
        if flagY == False:
            speedY = -speedY
            flagY = True
        if flagY == True:
            speedY = speedY

    #  ~~~~~~~ INCREMENT SCORE ~~~~~~~ #
    
    # PADDLE 1
    if ballX == WIDTH:
        player2Score += 1
        print "Player 1:",player1Score,"\nPlayer 2:",player2Score
        ballX = WIDTH/2 + (WIDTH/2)/2
        ballY = HEIGHT/2
        flagY = False
        speedY = randDirection()
        speedX = -speedX
        redrawGameWindow()
        pygame.time.delay(1000)

    # PADDLE 2
    if ballX == 0:
        player1Score += 1
        print "Player 1:",player1Score,"\nPlayer 2:",player2Score
        ballX = WIDTH/2 - (WIDTH/2)/2
        ballY = HEIGHT/2
        flagY = False
        speedY = randDirection()
        speedX = -speedX
        redrawGameWindow()
        pygame.time.delay(1000)

    # ~~~~~~~ MOVE BALL ~~~~~~~ #
    
    ballX = ballX + speedX
    ballY = ballY + speedY 
    
    ##### testing keys
    if keys[pygame.K_q]:
        timeDelay = timeDelay + 2
    if keys[pygame.K_e]:
        timeDelay = timeDelay - 2

pygame.quit()