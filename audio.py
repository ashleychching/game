from pygame import mixer
import pygame


def play_audio():
    mixer.init()
    mixer.music.load("audio/beginning and end.mp3")
    mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)


play_audio()
