import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс, представляющий одного прищельца."""

    def __init__(self, ai_game):
        """Инициализирует прищельца и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen

        # Загрузка изображения прищельца и назначение атрибута rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый прищелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции прещельца.
        self.x = float(self.rect.x)