import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Soda vs Water"


class Water:
    def __init__(self):
        """"""
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.size = 0
        self.color = None


# class Soda:
#     def __init__(self):
#         """"""
#         self.x = random.randrange(self.size, SCREEN_WIDTH - self.size)
#         self.y = random.randrange(self.size, SCREEN_HEIGHT - self.size)
#         self.change_x = random.randrange(-1, 2)
#         self.change_y = random.randrange(-1, 2)
#         self.size = random.randrange(2, 5)
#         self.color = arcade.color.BROWN
#
#
# class Player:
#     def __init__(self):
#         """"""
#         self.x = SCREEN_WIDTH / 2
#         self.y = SCREEN_HEIGHT / 2
#         self.size = 6
#         self.color = arcade.color.RED

def make_water():
    water = Water()

    water.x = random.randrange(water.size, SCREEN_WIDTH - water.size)
    water.y = random.randrange(water.size, SCREEN_HEIGHT - water.size)
    water.change_x = random.randrange(-1, 2)
    water.change_y = random.randrange(-1, 2)
    water.size = random.randrange(2, 5)
    water.color = arcade.color.BLUE

    return water


class MyGame(arcade.Window):
    """"""

    def __int__(self):
        """"""
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.water_list = []
        # self.soda_list = []
        # self.player = Player()

        for i in range(10):
            water = make_water()
            self.water_list.append(water)
            # soda = Soda
            # self.soda_list.append(soda)

    def on_draw(self):
        """
        """
        arcade.start_render()

        # for water in self.water_list:
        #     arcade.draw_circle_filled(water.x, water.y, water.size, water.color)

        # for soda in self.sode_soda:
        #     arcade.draw_circle_filled(soda.x, soda.y, soda.size, soda.color)
        #
        # arcade.draw_circle_filled(self.player.x, self.player.y, self.player.size, self.player.color)
        arcade.finish_render()

    # def on_update(self, delta_time):
    #     for water in self.water_list:
    #         water.x += water.change_x
    #         water.y += water.change_y
    #
    #         if water.x < water.size:
    #             water.change_x *= -1
    #
    #         if water.y < water.size:
    #             water.change_y *= -1
    #
    #         if water.x > SCREEN_WIDTH - water.size:
    #             water.change_x *= -1
    #
    #         if water.y > SCREEN_HEIGHT - water.size:
    #             water.change_y *= -1

    # for soda in self.soda_list:
    #     soda.x += soda.change_x
    #     soda.y += soda.change_y
    #
    #     if soda.x < soda.size:
    #         soda.change_x *= -1
    #
    #     if soda.y < soda.size:
    #         soda.change_y *= -1
    #
    #     if soda.x > SCREEN_WIDTH - soda.size:
    #         soda.change_x *= -1
    #
    #     if soda.y > SCREEN_HEIGHT - soda.size:
    #         soda.change_y *= -1


def main():
    MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
