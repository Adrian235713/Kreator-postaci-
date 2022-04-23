import pygame

class Obraz(pygame.sprite.Sprite):
    def __init__(self, sciezka):
        super(Obraz, self).__init__()
        self.obraz = pygame.image.load(sciezka)


class Element():
    def __init__(self,type):
        self.wybrany = 0
        self.lista_obrazow = []

        for i in range(1,4):
            sciezka = f'images/{type}{i}.png'
            wczytany_obraz = Obraz(sciezka)
            self.lista_obrazow.append(wczytany_obraz)

    def wybierzNastepny(self):
        self.wybrany += 1
        if self.wybrany > 2:
            self.wybrany = 0

    def wybranyObraz(self):
        return self.lista_obrazow[self.wybrany].obraz

# --------------------------------------------------------

class NakrycieGlowy(Element):
    def __init__(self):
        super().__init__('head')

class UbranieElement(Element):
    def __init__(self):
        super().__init__('body')

class OczyElement(Element):
    def __init__(self):
        super().__init__('eye')
        
class BronElement(Element):
    def __init__(self):
        super().__init__('weapon')