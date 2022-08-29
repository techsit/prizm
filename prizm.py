# -*- coding: utf-8 -*-
import sys
import pygame
from button import Button

pygame.init()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

background = pygame.image.load("assets/Background.png")
bob_surface = pygame.image.load("assets/bob.png")

sound_thisisbob = pygame.mixer.Sound("assets/audio/thisisbob.mp3")
sound_shoot = pygame.mixer.Sound("assets/audio/pewpew.mp3")

MUSIC_MAINMENU = "assets/audio/song.mp3"
MUSIC_LEVEL1 = None

BACKGROUND_MENU = "black"
BACKGROUND_GAME = "white"
BACKGROUND_SETTINGS = "lightblue"


def get_font(size):  # Returns Font in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def play():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(sound_thisisbob)

    x_position = 640
    y_position = 360
    x_increment = 1
    y_increment = 1

    while True:
        screen.fill(BACKGROUND_GAME)

        for event in pygame.event.get():
            pass

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.mixer.music.play()
            return

        # movement
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            x_position = x_position + x_increment
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            x_position = x_position - x_increment
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            y_position = y_position - y_increment
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            y_position = y_position + y_increment

        # shoot
        if keys[pygame.K_SPACE]:
            pygame.mixer.Sound.play(sound_shoot)
        

        screen.fill((255, 255, 255))
        screen.blit(bob_surface, (x_position, y_position))
        pygame.display.update()


def settings():

    while True:
        screen.fill(BACKGROUND_SETTINGS)
        mouse_pos = pygame.mouse.get_pos()

        RETURN_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="DONE", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        for button in [RETURN_BUTTON]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN_BUTTON.checkForInput(mouse_pos):
                    return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return

        pygame.display.update()


def main_menu():
    pygame.mixer.music.load(MUSIC_MAINMENU)
    pygame.mixer.music.play()

    while True:
        screen.fill(BACKGROUND_MENU)
        # screen.blit(background, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("PRIZM", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        SETTINGS_BUTTON = Button(image=pygame.image.load("assets/Settings Rect.png"), pos=(640, 400),
                                 text_input="SETTINGS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, SETTINGS_BUTTON, QUIT_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse_pos):
                    play()
                if SETTINGS_BUTTON.checkForInput(mouse_pos):
                    settings()
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
