#########################################
# File Name: YeetPong_V4
# Description: PONG
# Author: Sunny, Michael, Justin
# Date: 10/29/18
#########################################

#
# V4
# SCORE AND SIDE BOUNCING
#

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
GREY  = (100,100,100)
outline = 0
timeDelay = 6
flagY = False
font = pygame.font.SysFont("Courier Regular",75)
gameEndFont = pygame.font.SysFont("Courier Regular",150)
MAX_SCORE = 7
mainMenu = True


#---------------------------------------#
# functions                             #
#---------------------------------------#
def drawMainMenu():
    print "test"

def drawGameOverBlock():
    gameWindow.fill(BLACK)
    pygame.draw.rect(gameWindow, WHITE, (WIDTH/2-250,HEIGHT/2-50, 500,80 ), 5)
    p1ScoreRender = gameEndFont.render(str(player1Score), 1, WHITE)
    p2ScoreRender = gameEndFont.render(str(player2Score), 1, WHITE)
    gameWindow.blit(p1ScoreRender,((WIDTH/2 + (WIDTH/2)/2),35))
    gameWindow.blit(p2ScoreRender,((WIDTH/2 - (WIDTH/2)/2),35))
    gameWindow.blit(winScreen,(WIDTH/2-170,HEIGHT/2-33))
    pygame.display.update()

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
#---------------------------------------#
# main program                          #
#---------------------------------------#

while mainMenu == True:
    pygame.event.clear()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        mainMenu = False
        print "YEET"
    elif keys[pygame.K_ESCAPE]:
        pygame.quit()
    
print "Hit ESC to end the program."

# players
player1Score = 0 # right side
player2Score = 0 # left side

# ball properties
ballR  = 15
ballX  =  WIDTH/2
ballY  =  HEIGHT/2
speedX =  1
speedY =  1
ballClr = WHITE
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

#####
inPlay = True
while inPlay:
    redrawGameWindow()
    pygame.time.delay(timeDelay)

    if player1Score == MAX_SCORE:
        print "p1 wins"
        inPlay = False
        speedX = 0
        speedY = 0
        closeGame = False
    elif player2Score == MAX_SCORE:
        print "p2 wins"
        inPlay = False
        speedX = 0
        speedY = 0
        closeGame = False

    # control inputs
    pygame.event.clear()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
        closeGame = True
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

    ##### bounce from paddles
    ##### paddle 1
    if ballY >= paddle1Y and ballY <= paddle1Y + paddleH and ballX + ballR == paddle1X:
        speedX = -speedX
    if ballX >= paddle1X and ballY + ballR >= paddle1Y and ballY + ballR <= paddle1Y + 60 or ballX >= paddle1X and ballY - ballR <= paddle1Y + paddleH and ballY - ballR >= paddle1Y + paddleH - 60:
        if flagY == False:
            speedY = -speedY
            flagY = True
        if flagY == True:
            speedY = speedY
    ##### increment score, reset ball (PADDLE 1)
    if ballX == WIDTH:
        player2Score += 1
        print "Player 1:",player1Score,"\nPlayer 2:",player2Score
        ballX = WIDTH/2
        ballY = HEIGHT/2
        flagY = False
        redrawGameWindow()
        pygame.time.delay(1000)
        
    ##### paddle 2
    if ballY >= paddle2Y and ballY <= paddle2Y + paddleH and ballX - ballR == paddle2X + paddleW:
        speedX = -speedX
    if ballX <= paddle2X + paddleW and ballY + ballR >= paddle2Y and ballY + ballR <= paddle2Y + 60 or ballX <= paddle2X + paddleW and ballY - ballR <= paddle2Y + paddleH and ballY - ballR >= paddle2Y + paddleH - 60:
        if flagY == False:
            speedY = -speedY
            flagY = True
        if flagY == True:
            speedY = speedY
    ##### increment score, reset ball (PADDLE 2)
    if ballX == 0:
        player1Score += 1
        print "Player 1:",player1Score,"\nPlayer 2:",player2Score
        ballX = WIDTH/2
        ballY = HEIGHT/2
        flagY = False
        redrawGameWindow()
        pygame.time.delay(1000)
        
    # move the ball
    ballX = ballX + speedX
    ballY = ballY + speedY 
    
    ##### testing keys
    if keys[pygame.K_q]:
        timeDelay = timeDelay + 2
    if keys[pygame.K_e]:
        timeDelay = timeDelay - 2
    if keys[pygame.K_p]:
        player1Score = MAX_SCORE

    
        

if closeGame == True:
    pygame.quit()

if closeGame == False:
    if player1Score == MAX_SCORE:
        winScreen = font.render(("Player 1 Wins"), 1, WHITE)
    else:
        winScreen = font.render(("Player 2 Wins"), 1, WHITE)
    drawGameOverBlock()
    
    



    

