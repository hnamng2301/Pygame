import pygame

pygame.init() # Initialize pygame

screen = pygame.display.set_mode((800,600)) # Create a screen

# Set name of game and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(".\\images\\ufo.png")
pygame.display.set_icon(icon)

playerImage = pygame.image.load(".\\images\\player.png") # Player
playerX = 370  # Toa do X của player
playerY = 470  # Toa do Y cua player

def player():
  screen.blit(playerImage, (playerX, playerY))

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
    screen.fill((0,0,0))
    player()
    pygame.display.update()
    
