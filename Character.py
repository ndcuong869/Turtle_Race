import turtle
import random
import datetime


class Char:
    Character = "Object"

    light = "Light turn on when Object backward"
    cage = "Cage turn on when Object not moved"

    race_track_length = 0
    race_track_length_frame = 0

    Shape = "File name consist of image of character"

    status = 0
    win = 0

    start_time = 0
    end_time = 0
    dur_minute = 0
    dur_second = 0
    dur_microsecond = 0
    image_cur = 0
    name = 0

    def __init__(self, x_position, y_position, name_active, color):
        self.Character = turtle.Turtle()
        self.Character.speed(0)

        file_name = "Source/Image/" + name_active + "/" + color + "/1forward.gif"
        self.Character.shape(file_name)
        self.set_position(x_position, y_position)

    def set_position(self, x_position, y_position):
        self.Character.penup()
        self.Character.setposition(x_position, y_position)

    def set_value_race_track_length(self, start_ran, end_ran):
        self.race_track_length = random.randint(start_ran, end_ran)

    def set_value_race_track_length_frame(self, frame, length):
        self.race_track_length_frame = self.race_track_length / (frame * length)

    def set_status(self, start_ran, end_ran, x_lower_left, x_high_right):
        if self.status != 3:
            ran = random.randint(start_ran, end_ran)
        else:
            return 0
        if self.Character.xcor() < x_lower_left:
            self.status = 0
            return 1

        if ran < 2:
            self.status = 1
        elif ran < 9:
            self.status = 0
        else:
            self.status = 2

    def load_shape(self, file_name):
        self.Shape = file_name
        self.Character.shape(self.Shape)

    def move(self, track_length_frame):
        self.Character.forward(random.randint(1, 6))

    def move_forward(self, file_name, number_image):
        self.Character.penup()
        self.Character.setheading(0)
        self.Character.showturtle()
        self.load_shape(file_name)
        self.move(self.race_track_length_frame)

    def move_backward(self, x_lower_left, frame, file_name, number_image):

        if self.image_cur == 0:
           self.Character.setheading(180)

        if self.Character.xcor() < x_lower_left:
            self.status = 0
            self.light.hide_shape()
            return 0

        self.load_shape(file_name)
        self.move(self.race_track_length_frame)

    def move_win(self, x_lower_left, file_name):
        self.Character.setheading(180)
        self.load_shape(file_name)
        self.move(self.race_track_length_frame)

    def is_win(self, x_right_high):
        if self.Character.xcor() > x_right_high:
            self.win = 1
            self.status = 3
            return True

        return False

    def get_time_start(self):
        self.start_time = datetime.datetime.now()

    def get_time_end(self):
        self.end_time = datetime.datetime.now()

    def get_duration_time(self):
        total = (self.end_time.minute - self.start_time.minute) * 60 + self.end_time.second - self.start_time.second

        self.dur_minute = total // 60
        self.dur_second = total % 60
        self.dur_microsecond = (self.end_time.microsecond - self.start_time.microsecond) % 100
        print("Total")
        print(self.end_time)












