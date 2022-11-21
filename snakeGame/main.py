import pygame
import sys
from pygame.locals import *
from enum import Enum
from copy import deepcopy , copy
from random import randint

WIDTH = 30
HEIGHT = 20
SIZE = 35

MOVE_AND_DRAW_ID = 25
MOVE_AND_DRAW_INTERVAL = 75

foodCoordinate = (randint(0,WIDTH) , randint(0,HEIGHT))
eatFood = False

class fieldCondition(Enum):
  EMPTY = 0
  PLAYER_BODY = 1
  PLAYER_TIP = 2
  FOOD = 3

def main():

  score = 0
  lastPushedKey = K_s
  playerCoordinateList = [[0,i] for i in range(3,0,-1)]
  field = [[0 for i in range(0,HEIGHT)] for j in range(0,WIDTH)]
  gameover = False
  foodCoordinate = [randint(0,WIDTH) , randint(0,HEIGHT)]

  pygame.init()
  screen = pygame.display.set_mode((WIDTH*SIZE , HEIGHT*SIZE))
  pygame.display.set_caption("Snake Game")

  scoreFont = pygame.font.Font(None,int(WIDTH*SIZE/20))
  describeFont = pygame.font.Font(None,int(WIDTH*SIZE/35))
  describeText = describeFont.render("enter right shift key to play again.",True,(255,255,255))

  pygame.time.set_timer(MOVE_AND_DRAW_ID , MOVE_AND_DRAW_INTERVAL)

  while True:
    screen.fill((0,0,0))
    global eatFood
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
        pygame.quit()
      if event.type == KEYDOWN:
        if event.key == K_w or event.key == K_s or event.key == K_a or event.key == K_d: 
          lastPushedKey = event.key
        if event.key == K_0:
          eatFood = True
        if event.key == K_RSHIFT:
          main()

      if event.type == MOVE_AND_DRAW_ID and not gameover:
        playerCoordinateListAfterMove = movePlayerCoordinate(lastPushedKey , playerCoordinateList)
        if isOutOfArea(playerCoordinateListAfterMove[0]) or isCollisionWithBody(playerCoordinateListAfterMove):
          gameover = True
          continue
        field = updateField(playerCoordinateListAfterMove)
        if eatFood:
          extendPlayer(playerCoordinateListAfterMove)
        playerCoordinateList = playerCoordinateListAfterMove
        score += len(playerCoordinateListAfterMove)
        drawField(field , screen)
        pygame.display.update()
      if event.type == MOVE_AND_DRAW_ID and gameover:
        scoreText = scoreFont.render(f"score: {score}",True,(255,255,255))
        screen.blit(scoreText,(WIDTH*SIZE/3,HEIGHT*SIZE/3))
        screen.blit(describeText,(WIDTH*SIZE/3,HEIGHT*SIZE/3+SIZE*HEIGHT/6))
        pygame.display.update()


          
def movePlayerCoordinate(lastPushedKey,playerCoordinateList):
  playerCoordinateListAfterMove = deepcopy(playerCoordinateList)

  for i in range(1 , len(playerCoordinateListAfterMove)):
    playerCoordinateListAfterMove[i] = playerCoordinateList[i-1]
  if lastPushedKey == K_w:
    playerCoordinateListAfterMove[0][1] -= 1
  elif lastPushedKey == K_s:
    playerCoordinateListAfterMove[0][1] += 1
  elif lastPushedKey == K_a:
    playerCoordinateListAfterMove[0][0] -= 1
  elif lastPushedKey == K_d:
    playerCoordinateListAfterMove[0][0] += 1
  
  return playerCoordinateListAfterMove



def isOutOfArea(playerTipCoordinate) -> bool:
  if playerTipCoordinate[0] < 0:
    return True
  if WIDTH-1 < playerTipCoordinate[0]:
    return True
  if playerTipCoordinate[1] < 0:
    return True
  if HEIGHT-1 < playerTipCoordinate[1]:
    return True
  
  return False



def isCollisionWithBody(playerCoordinatesAfterMove) -> bool:
  playerTipCoordinate = playerCoordinatesAfterMove[0]
  for i in range(1 , len(playerCoordinatesAfterMove)):
    if playerTipCoordinate[0] == playerCoordinatesAfterMove[i][0] and\
       playerTipCoordinate[1] == playerCoordinatesAfterMove[i][1]:
      return True

  return False



def updateField(playerCoordinateListAfterMove):
  global foodCoordinate
  global eatFood
  field = [[0 for i in range(0,HEIGHT)] for j in range(0,WIDTH)]
  field[foodCoordinate[0]][foodCoordinate[1]] = 3
  for i in playerCoordinateListAfterMove:
    if field[i[0]][i[1]] == 3:
      foodCoordinate = (randint(0,WIDTH-1) , randint(0,HEIGHT-1))
      eatFood = True
    field[i[0]][i[1]] = 1
  field[playerCoordinateListAfterMove[0][0]][playerCoordinateListAfterMove[0][1]] = 2

  return field


def  drawField(field , screen):
  for i in range(0,HEIGHT):
    for j in range(0,WIDTH):
      if field[j][i] == 0:
        pygame.draw.rect(screen,(0,0,0),(j*SIZE,i*SIZE,SIZE,SIZE))
      elif field[j][i] == 1:
        pygame.draw.rect(screen,(255,0,0),(j*SIZE,i*SIZE,SIZE,SIZE))
      elif field[j][i] == 2:
        pygame.draw.rect(screen,(0,255,0),(j*SIZE,i*SIZE,SIZE,SIZE))
      elif field[j][i] == 3:
        pygame.draw.rect(screen,(0,0,255),(j*SIZE,i*SIZE,SIZE,SIZE))



def extendPlayer(playerCoordinateListAfterMove):
  global eatFood
  playerCoordinateListAfterMove.append(copy(playerCoordinateListAfterMove[-1]))
  eatFood = False

if __name__ == "__main__":
  main()