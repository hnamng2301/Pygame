import pygame
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init() 

# Create a screen
screen = pygame.display.set_mode((800,600)) 

# Set name of game and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(".\\images\\ufo.png")
pygame.display.set_icon(icon)

# Information for player
playerImage = pygame.image.load(".\\images\\player.png") # Player image
playerX = 370  # X root-coordinate of player
playerY = 480  # Y root-coordinate of player
playerChangeX = 0  # Change of player in loop
playerChangeY = 0
# Information for enemy
# enemyImage = pygame.image.load(".\\images\\enemy.png") # Enemy image
# enemyX = random.randint(0, 1000)  # X root-coordinate of enemy
# enemyY = random.randint(50, 300)  # Y root-coordinate of enemy
# enemyChangeX = 4
# enemyChangeY = 10
enemyImage = []
enemyX = []
enemyY = []
enemyChangeX = []
enemyChangeY = []
enemyNums = 5

for enemy in range(enemyNums):
  enemyImage.append(pygame.image.load(".\\images\\enemy.png"))
  enemyX.append(random.randint(0, 736))
  enemyY.append(random.randint(50, 150))
  enemyChangeX.append(2)
  enemyChangeY.append(40)

# Information for attacking
bulletImage = pygame.image.load(".\images\\bullet.png")
bulletX = 0     # X root-coordinate of bullet
bulletY = 480   # Y root-coordinate of bullet
bulletXChange = 0
bulletYChange = 10
bulletState = 'ready'

#Score
score = 0
# print(pygame.font.get_fonts())
scoreFont = pygame.font.SysFont('glasgow.ttf', 40)
gameOverFont = pygame.font.SysFont('microsquare.ttf', 60)
textX = 10
textY = 10
isOver = True

# Background
background = pygame.image.load(".\images\\background.jpg")

# Functions for game
def player(x, y): # Function for player change
  screen.blit(playerImage, (x, y))


def enemy(x, y, i): # Function for enemy change
  screen.blit(enemyImage[i], (x, y))


def fire(x, y): # Function for firing
  global bulletState
  bulletState = 'fire'
  screen.blit(bulletImage, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY): # Function for checking collision
  distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
  if distance < 27:
    return True
  return False

def randomAppear():
  x = random.randint(0, 736)  # X root-coordinate of enemy
  y = random.randint(50, 150)  # Y root-coordinate of enemy
  return x, y

def showScore(x, y): # Function for show score
  scoreText = scoreFont.render('Score: ' + str(score), True, (255, 255, 255))
  screen.blit(scoreText, (x, y))

def gameOver():
  gameOverText = gameOverFont.render('GAME OVER', True, (255, 255, 255))
  screen.blit(gameOverText, (250, 250))

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
        playerChangeX = -2
      elif event.key == pygame.K_RIGHT:
        playerChangeX = 2
      elif event.key == pygame.K_DOWN:
        playerChangeY = 2
      elif event.key == pygame.K_UP:
        playerChangeY = -2
      elif event.key == pygame.K_SPACE:
        if bulletState == 'ready':
          bulletSound = mixer.Sound('.\images\\laser.wav')
          bulletSound.play()
          bulletX = playerX
          fire(bulletX, bulletY)

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        playerChangeX = 0
      elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        playerChangeY = 0

  playerX += playerChangeX
  playerY += playerChangeY

  if playerX <= 0:
    playerX = 0
  elif playerX >= 736:
    playerX = 736
    
  if playerY <= 0:
    playerY = 0
  elif playerY >= 480:
    playerY = 480

  # Enemy movement
  for i in range(enemyNums):

    # Game over when enemy collide with spaceship
    if enemyY[i] >= playerY - 40:
      if (enemyX[i] >= playerX - 16 and enemyX[i] <= playerX) or (enemyX[i] <= playerX + 16 and enemyX[i] >= playerX):
        print(playerX, enemyX[i])
        for j in range(enemyNums):
          enemyY[j] = 3000
        gameOver()
        break

    enemyX[i] += enemyChangeX[i]
    if enemyX[i] <= 0:
      enemyChangeX[i] = 1
      enemyY[i] += enemyChangeY[i]
    elif enemyX[i] >= 736:
      enemyChangeX[i] = -1
      enemyY[i] += enemyChangeY[i]
  
    collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
    if collision:
      explosionSound = mixer.Sound(".\images\\explosion.wav")
      explosionSound.play()
      bulletY = 480
      bulletState = 'ready'
      score += 1
      # print(score)
      enemyX[i], enemyY[i] = randomAppear()
      
    enemy(enemyX[i], enemyY[i], i)

  if bulletY <= 0:
    bulletY = 480
    bulletState = 'ready'

  if bulletState == 'fire':
    fire(bulletX, bulletY)
    bulletY -= bulletYChange

  player(playerX, playerY)
  showScore(textX, textY)
  pygame.display.update()

