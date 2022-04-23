import pygame

SZEROKOSC_EKRANU = 800
WYOKOSC_EKRANU = 600

obraz_tla = pygame.image.load('images/background.png')
obraz_bazy_postaci = pygame.image.load('images/base.png')

pygame.init()

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU,WYOKOSC_EKRANU])
zegar = pygame.time.Clock()


gra_dziala = True
while gra_dziala:
    for zdarzenie in pygame.event.get():
        print(zdarzenie)
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False


    ekran.blit(obraz_tla, (0,0))
    ekran.blit(obraz_bazy_postaci, (270, 130))

    pygame.display.flip()

    zegar.tick(30)

pygame.quit()