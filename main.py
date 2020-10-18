
import arcade
import random

# Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Water vs Soda"


class Water:
    def __init__(self):
        self.size = random.randrange(5, 11)
        self.x = random.randrange(self.size, SCREEN_WIDTH - self.size)
        self.y = random.randrange(self.size, SCREEN_HEIGHT - self.size)
        self.change_x = random.randrange(-1, 2)
        self.change_y = random.randrange(-1, 2)
        self.color = arcade.color.BLUE


class Soda:
    def __init__(self):
        self.size = random.randrange(5, 11)
        self.x = random.randrange(self.size, SCREEN_WIDTH - self.size)
        self.y = random.randrange(self.size, SCREEN_HEIGHT - self.size)
        self.change_x = random.randrange(-1, 2)
        self.change_y = random.randrange(-1, 2)
        self.color = arcade.color.BROWN


class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.change_x = 0
        self.change_y = 0
        self.size = 6
        self.color = arcade.color.GREEN


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.water_list = []
        self.soda_list = []
        self.player = Player()

        for i in range(10):
            water = Water()
            self.water_list.append(water)
            soda = Soda()
            self.soda_list.append(soda)

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        for i in self.water_list:
            arcade.draw_circle_filled(i.x, i.y, i.size, i.color)
        for i in self.soda_list:
            arcade.draw_circle_filled(i.x, i.y, i.size, i.color)
        arcade.draw_circle_filled(self.player.x, self.player.y, self.player.size, self.player.color)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player.change_y += .2
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x -= .2
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x += .2
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.change_y -= .2

    def on_update(self, delta_time):
        """ Movement and game logic """
        for i in self.water_list:
            i.x += i.change_x
            i.y += i.change_y

            if i.x < i.size:
                i.change_x *= -1

            if i.y < i.size:
                i.change_y *= -1

            if i.x > SCREEN_WIDTH - i.size:
                i.change_x *= -1

            if i.y > SCREEN_HEIGHT - i.size:
                i.change_y *= -1

            if i.y - i.size/2 - self.player.size/2 < self.player.y and self.player.y < i.y + i.size/2 + self.player.size/2 :
                if i.x - i.size/2 - self.player.size/2  < self.player.x and self.player.x < i.x + i.size/2 + self.player.size/2:
                    self.player.size += i.size
                    self.water_list.remove(i)

        for i in self.soda_list:
            i.x += i.change_x
            i.y += i.change_y

            if i.x < i.size:
                i.change_x *= -1

            if i.y < i.size:
                i.change_y *= -1

            if i.x > SCREEN_WIDTH - i.size:
                i.change_x *= -1

            if i.y > SCREEN_HEIGHT - i.size:
                i.change_y *= -1

            if i.y - i.size/2 - self.player.size/2 < self.player.y and self.player.y < i.y + i.size/2 + self.player.size/2 :
                if i.x - i.size/2 - self.player.size/2  < self.player.x and self.player.x < i.x + i.size/2 + self.player.size/2:
                    self.player.size -= i.size
                    self.soda_list.remove(i)

            self.player.x += self.player.change_x
            self.player.y += self.player.change_y

            if self.player.x < self.player.size:
                self.player.change_x *= -1

            if self.player.y < self.player.size:
                self.player.change_y *= -1

            if self.player.x > SCREEN_WIDTH - self.player.size:
                self.player.change_x *= -1

            if self.player.y > SCREEN_HEIGHT - self.player.size:
                self.player.change_y *= -1

            if self.player.size < 5:
                self.player.size = 0
                del self.player




def main():
    MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
