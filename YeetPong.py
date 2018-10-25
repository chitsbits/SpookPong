#########################################
# File Name: BrickBreakerStarter.py
# Description: Starter code for Brick Breaker game
# Author: ICS2O
# Date: 08/11/2017
#########################################
import pygame
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
outline = 0

#---------------------------------------#
# functions                             #
#---------------------------------------#
def redrawGameWindow():
    gameWindow.fill(BLACK)
    pygame.draw.circle(gameWindow, WHITE, (ballX, ballY), ballR, outline)
    pygame.draw.rect(gameWindow, GREEN, (paddle1X, paddle1Y, paddleW, paddleH), outline)
    pygame.draw.rect(gameWindow, GREEN, (paddle2X, paddle2Y, paddleW, paddleH), outline)
    pygame.display.update()
     
#---------------------------------------#
# main program                          #
#---------------------------------------#
print "Hit ESC to end the program."

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

inPlay = True
while inPlay:
    redrawGameWindow()
    pygame.time.delay(8)

    # control inputs
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

    # prevent paddles from going off-screen
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

    # bounce from paddles
    # paddle 1
    if ballY >= paddle1Y and ballY <= paddle1Y + paddleH and ballX + ballR == paddle1X:
        speedX = -speedX
    # paddle 2
    if ballY >= paddle2Y and ballY <= paddle2Y + paddleH and ballX - ballR == paddle2X + paddleW:
        speedX = -speedX
    # move the ball
    ballX = ballX + speedX
    ballY = ballY + speedY 
    
        

pygame.quit()
