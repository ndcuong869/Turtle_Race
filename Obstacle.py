import turtle


class Obstacle:
    Obstacle = 0
    padding_position_x = 0
    screen = 0

    def __init__(self, x_character, y_character, filename, name_object):
        self.Obstacle = turtle.Turtle()
        self.Obstacle.speed(0)
        self.Obstacle.hideturtle()

        self.screen = turtle.Screen()

        self.Obstacle.speed(0)
        self.set_padding(name_object)
        self.set_position(x_character, y_character, name_object)
        self.screen.addshape(filename)
        self.Obstacle.shape(filename)

    def set_position(self, x_position, y_postion, name_object):
        self.Obstacle.penup()
        self.set_padding(name_object)
        self.Obstacle.setposition(int(x_position + self.padding_position_x), int(y_postion))

    def set_padding(self, name_object):
        if name_object == "Light":
            self.padding_position_x = 60
        elif name_object == "Cage":
            self.padding_position_x = 0

    def hide_shape(self):
        self.Obstacle.hideturtle()

    def show_shape(self):
        self.Obstacle.showturtle()

