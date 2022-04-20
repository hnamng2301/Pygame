import pygame
import random
import math

# Initialize pygame
pygame.init() 

# Create a screen
screen = pygame.display.set_mode((1000,600)) 

# Set name of game and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(".\\images\\ufo.png")
pygame.display.set_icon(icon)

# Information for player
playerImage = pygame.image.load(".\\images\\player.png") # Player image
playerX = 500  # X root-coordinate of player
playerY = 480  # Y root-coordinate of player
playerChange = 0  # Change of player in loop

# Information for enemy
enemyImage = pygame.image.load(".\\images\\enemy.png") # Enemy image
enemyX = random.randint(0, 1000)  # X root-coordinate of enemy
enemyY = random.randint(50, 300)  # Y root-coordinate of enemy
enemyChangeX = 4
enemyChangeY = 10

# Information for attacking
bulletImage = pygame.image.load(".\images\\bullet.png")
bulletX = 0     # X root-coordinate of bullet
bulletY = 480   # Y root-coordinate of bullet
bulletXChange = 0
bulletYChange = 10
bulletState = 'ready'

#Score
score = 0

# Background
background = pygame.image.load(".\images\\background.jpg")

# Functions for game
def player(x, y): # Function for player change
  screen.blit(playerImage, (x, y))


def enemy(x,y): # Function for enemy change
  screen.blit(enemyImage, (x, y))


def fire(x, y): # Function for firing
  global bulletState
  bulletState = 'fire'
  screen.blit(bulletImage, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY): # Function for checking collision
  distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
  if distance <= 27:
    return True
  return False

def randomAppear():
  x = random.randint(0, 1000)  # X root-coordinate of enemy
  y = random.randint(50, 300)  # Y root-coordinate of enemy
  return x, y

##############
running = True
while running:

  screen.fill((0,0,0)) # RGB : 0 , 0 , 0 -> Black
  screen.blit(background, (0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        playerChange -= 1
      elif event.key == pygame.K_RIGHT:
        playerChange += 1
      elif event.key == pygame.K_SPACE:
        if bulletState == 'ready':
          bulletX = playerX
          fire(bulletX, bulletY)

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        playerChange = 0

  playerX += playerChange

  if playerX <= 0:
    playerX = 0
  elif playerX >= 940:
    playerX = 940
    
  enemyX += enemyChangeX
  if enemyX <= 0:
    enemyChangeX = 1
    enemyY += enemyChangeY
  elif enemyX >= 940:
    enemyChangeX = -1
    enemyY += enemyChangeY
    
  if bulletY <= 0:
    bulletY = 480
    bulletState = 'ready'

  if bulletState == 'fire':
    fire(playerX, bulletY)
    bulletY -= bulletYChange
    
  collision = isCollision(enemyX, enemyY, bulletX, bulletY)
  if collision is True:
    bulletY = 480
    bulletState = 'ready'
    score += 1
    print(score)
    enemyX, enemyY = randomAppear()

  player(playerX, playerY)
  enemy(enemyX, enemyY)
  pygame.display.update()

