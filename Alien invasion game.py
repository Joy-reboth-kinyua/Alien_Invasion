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
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)



run_game()