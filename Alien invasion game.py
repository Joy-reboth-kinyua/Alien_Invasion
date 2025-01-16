import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
# Initialize game, settings, and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #set display mode first
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    bg_color = (230, 230, 230)#set the background color.

# Start the main loop for the game.
    while True:
        gf.check_events()

 # Watch for keyboard and mouse events.
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
           sys.exit()

       screen.fill(ai_settings.bg_color)
       ship.blitme()
    # Make the most recently drawn screen visible.
       pygame.display.flip()

run_game()