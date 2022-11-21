import pygame as pg
import sys
from pygame.locals import *
import math

SCREEN_SIZE = (600, 800)
WHITE = (255,255,255)
BLACK = (0,0,0)


class Player:
  viewRange = 40.0
  visionL = 0
  visionR = 0
  rotation = 0.0
  x = 0
  y = 0
  def __init__(self,x,y,rotation):
    self.x = x
    self.y = y
    self.rotation = rotation
    self.calcVision()
    
  def getRotation(self):
    return math.radians(self.rotation)

  def moveRight(self):
    self.x+=5

  def moveLeft(self):
    self.x-=5

  def moveUp(self):
    self.y-=5

  def moveDown(self):
    self.y+=5

  def rotateRight(self):
    self.rotation-=5.0

  def rotateLeft(self):
    self.rotation+=5.0

  def calcVision(self):
    radianL = math.radians(self.rotation+self.viewRange)
    radianR = math.radians(self.rotation-self.viewRange)
    self.visionL = vec2(math.cos(radianL),math.sin(radianL))
    self.visionR = vec2(math.cos(radianR),math.sin(radianR))

  def getSVector(self,h,v):
    x = (1-h)*0.1/(v-1.01)*self.visionL.x + h*0.1/(v-1.01)*self.visionR.x
    y = (1-h)*0.1/(v-1.01)*self.visionL.y + h*0.1/(v-1.01)*self.visionR.y

    return vec2(x,y)
    


class vec2:
  x = 0
  y = 0

  def __init__(self,x,y):
    self.x = x
    self.y = y

  def add(self,x):
    return vec2(self.x+x , self.y+x)

  def add(self,x,y):
    return vec2(self.x+x,self.y+y)

  def mult(self,x):
    return vec2(self.x*x,self.y*x)

  @staticmethod
  def getPVector(h,v):
    p = vec2(0,0)

    p.x = h*SCREEN_SIZE[0]
    p.y = v*SCREEN_SIZE[1]/2

    return p




def main():
  pg.init()
  screen = pg.display.set_mode(SCREEN_SIZE)
  pg.display.set_caption("pseudo 3D")
  fpsClock = pg.time.Clock()
  pg.key.set_repeat(1,50)
  #30*20
  field = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
    [0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0],
    [0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0],
    [0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0],
    [0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0],
    [0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0],
    [0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0],
    [0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0],
    [0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  ]
  player = Player(200,200,50)

  while True:
    for event in pg.event.get():
      if event.type == QUIT:
        pg.quit()
        sys.exit()
      if event.type == KEYDOWN:
        if event.key == K_a:
          player.moveLeft()
        if event.key == K_d:
          player.moveRight()
        if event.key == K_w:
          player.moveUp()
        if event.key == K_s:
          player.moveDown()
        if event.key == K_i:
          player.rotateRight()
        if event.key == K_p:
          player.rotateLeft()

    player.calcVision()

    screen.fill(BLACK)

    for i in range(0, 20):
      for j in range(0, 30):
        if field[i][j] == 1:
          pg.draw.rect(screen, WHITE, (j*20, i*20, 20, 20))

    """
    for v in range(0,21):
      pos1 = player.getSVector(0,v/20).mult(200).add(player.x,player.y)
      pos2 = player.getSVector(1,v/20).mult(200).add(player.x,player.y)
      pg.draw.line(screen,(255,0,0),(pos1.x , pos1.y),(pos2.x , pos2.y))
    
    for h in range(0,21):
      pos1 = player.getSVector(h/20,0).mult(200).add(player.x,player.y)
      pos2 = player.getSVector(h/20,1).mult(200).add(player.x,player.y)
      pg.draw.line(screen,(255,0,0),(pos1.x,pos1.y),(pos2.x,pos2.y))
    """

    for v in range(0,51):
      for h in range(0,51):
        pos = player.getSVector(h/50,v/50).mult(200).add(player.x,player.y)

        if SCREEN_SIZE[0] <= pos.x or SCREEN_SIZE[1] <= pos.y:
          continue
        if pos.x <= 0 or pos.y <= 0:
          continue

        color = screen.get_at((int(pos.x),int(pos.y)))
        if color.r == 255 and color.g == 255 and color.b == 255:
          pos2 = vec2.getPVector(h/50,v/50)
          print(f"pos2( {pos2.x} , {pos2.y} )")
          pg.draw.rect(screen,(255,255,255),(SCREEN_SIZE[0]-pos2.x,SCREEN_SIZE[1]-pos2.y,int(SCREEN_SIZE[0]/50),int(SCREEN_SIZE[1]/50)))


        pg.draw.circle(screen,(255,0,0),(pos.x,pos.y),1.0)

    pg.draw.circle(screen,(0,255,0),(player.x,player.y),10.0)


    pg.display.update()
    fpsClock.tick(10)


  



if __name__ == "__main__":
  main()