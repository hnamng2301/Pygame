import pygame
import random

# Initialize pygame
pygame.init() 

# Create a screen
screen = pygame.display.set_mode((1520,750), pygame.SCALED) 

# Set name of game and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(".\\images\\ufo.png")
pygame.display.set_icon(icon)

# Information for player
playerImage = pygame.image.load(".\\images\\player.png") # Player image
playerX = 760  # X root-coordinate of player
playerY = 650  # Y root-coordinate of player
playerChange = 0  # Change of player in loop

# Information for enemy
enemyImage = pygame.image.load(".\\images\\enemy.png") # Enemy image
enemyX = random.randint(0, 1400)  # X root-coordinate of enemy
enemyY = random.randint(50, 400)  # Y root-coordinate of enemy
enemyChangeX = 4
enemyChangeY = 0

# Information for attacking
bulletImage = pygame.image.load(".\images\\bullet.png")
bulletX = 0     # X root-coordinate of bullet
bulletY = 650   # Y root-coordinate of bullet
bulletXChange = 0
bulletYChange = 10
bulletState = 'ready'

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
running = True

while running:
  screen.fill((0,0,0)) # RGB : 0 , 0 , 0 -> Black
  screen.blit(background, (0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
    if event.type == pygame.KEYDOWN:
    #   print("Key pressed")
      if event.key == pygame.K_LEFT:
        playerChange -= 3
      elif event.key == pygame.K_RIGHT:
        playerChange += 3
      elif event.key == pygame.K_SPACE:
        if bulletState is 'ready':
          bulletX = playerX
          fire(bulletX, bulletY)
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        playerChange = 0

  playerX += playerChange

  if playerX <= 0:
    playerX = 0
  elif playerX >= 1460:
    playerX = 1460
    
  enemyX += enemyChangeX
  if enemyX <= 0:
    enemyChangeX = 4
  elif enemyX >= 1460:
    enemyChangeX = -4

  if bulletY <= 0:
    bulletY = 650
    bulletState = 'ready'

  if bulletState is 'fire':
    fire(playerX, bulletY)
    bulletY -= bulletYChange
    
  player(playerX, playerY)
  enemy(enemyX, enemyY)
  pygame.display.update()

