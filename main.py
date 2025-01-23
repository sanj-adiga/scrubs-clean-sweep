import pygame, titleScreen, mainMenu, slideShowIntro, dontDropTheSoap, grimeGrinder, minigameInstructions,rubbishMain

import boss_battle_main
import level_1_main, level_2_main, level_3_main
pygame.init()


titleScreen.run_title()
mainMenu.run_menu()
slideShowIntro.run_slideshow()


minigameInstructions.run_level_instructions()
level_1_main.run()
minigameInstructions.run_ddts_instructions()
dontDropTheSoap.run_minigame()
level_2_main.run()
minigameInstructions.run_ss_instructions()
grimeGrinder.run_minigame()
level_3_main.run()
minigameInstructions.run_rr_instructions()
rubbishMain.run_minigame()
minigameInstructions.run_boss_instructions()
boss_battle_main.run()
