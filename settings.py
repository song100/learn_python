class Settings():
    """Store all setting classes of the alien invasion"""

    def __init__(self):
        """Initialize the game when start the game"""
        #  Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # attribute of ship
        self.ship_speed_factor = 1.5

        # attribute of bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (128,60,60)
        self.bullets_allowed =3

        # attributes of alien
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction 为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
