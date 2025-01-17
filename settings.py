class Settings():
    """Класс для хранения всекх настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана.
        self.screen_width = 1440
        self.screen_heigth = 800
        self.bg_color = (230, 230, 230)

        # Параметры снаряда.
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
        # Настройки корабля.
        self.ship_speed = 0.9
        self.ship_speeds = 0.9
