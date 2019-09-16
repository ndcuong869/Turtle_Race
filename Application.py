import turtle
import Character
from Obstacle import Obstacle
import random


def set_position(char, x_position, y_position):
    char.penup()
    char.setposition(x_position, y_position)
    char.pendown()


def draw_line_square(brush, x_position, y_position, width, height):
    set_position(brush, x_position, y_position)
    brush.penup()
    for step in range(2):
        brush.forward(width)
        brush.right(90)
        brush.forward(height)
        brush.right(90)


def draw_line_race(brush, x_position, y_position, width, height):
    for i in range(y_position - 4 * height, y_position + height, height):
        draw_line_square(brush, x_position, i, width, height)

        x_lower_left = x_position
        x_high_right = x_position + width

    return x_lower_left,  x_high_right


def load_image(name_images, screen, number_image, image_color=[], statusImage=[]):
    for k in range(5):
        for i in range(2):
            for j in range(number_image):
                file_name = "Source/Image/" + name_images + "/" + \
                            image_color[k] + "/" + str(j + 1) + statusImage[i] + ".gif"
                screen.addshape(file_name)


def update_rank(brush, characters=[]):
    arr = characters[0].Character.ycor()
    brush.clear()
    for i in range(4):
        for j in range(i + 1, 5, 1):
            if (characters[i].Character.xcor() < characters[j].Character.xcor()):
                arr = characters[j].Character.ycor() 
    print("TEst")

    for i in range(5):
        if characters[i].Character.ycor() == arr:
            set_position(brush, -250, 200)
            brush.write(characters[i].name, font=("Arial", 20, "normal"))



def is_win(char, x_high_right):
    char.is_win(x_high_right)


def is_completed(char=[]):
    for i in range(5):
        if char[i].win == 0:
            return False

    return True


def arrange_char(characters=[], char_arrange=[], char_num_defaul=[], char_temp=[]):
    for i in range(4):
        for j in range(i + 1, 5, 1):
            if characters[return_index(characters[i].Character.ycor())].Character.xcor() < characters[return_index(characters[j].Character.ycor())].Character.xcor():
                char_temp[return_index(characters[i].Character.ycor())], char_temp[return_index(characters[j].Character.ycor())] = \
                    char_temp[return_index(characters[j].Character.ycor())], char_temp[return_index(characters[i].Character.ycor())]

    signal = []
    for i in range(len(char_arrange)):
        signal.append(0)

    for i in range(5):
        for j in range(len(char_arrange)):
            if (char_arrange[j] == i) and (signal[j] == 0):
                char_arrange[j] = char_temp[i]
                signal[j] = 1

    char_arr = [0, 0, 0, 0, 0]
    for i in range(len(char_temp)):
        char_arr[i] = char_num_defaul[char_temp[i]]

    return char_arr


def return_index(y_position):
    if y_position == 120:
        return 0
    elif y_position == 40:
        return 1
    elif y_position == -40:
        return 2
    elif y_position == -120:
        return 3
    else:
        return 4

def main_loop(brush, x_lower_left, x_high_right, frame, number_image, characters=[], char_arrange=[], char_num_defaul=[],
              char_temp=[], image_active=[], image_color=[], statusImage=[], char_num_frame=[], char_win=[], y_pos = [], index_win=[]):
    # Set value of track_race
    for i in range(5):
        characters[i].set_value_race_track_length(50, 100)

    # Set status of chars
    for i in range(5):
        characters[i].set_status(1, 10, x_lower_left, x_high_right)

    #   Arrange character
    char_num_frame = arrange_char(characters, char_arrange, char_num_defaul, char_temp)

    #  Create track length each frame
    for i in range(5):
        characters[i].set_value_race_track_length_frame(frame, char_num_frame[i])

    #   Set light show
    for i in range(5):
        if characters[i].status == 1:
            characters[i].light.set_position(characters[i].Character.xcor(), characters[i].Character.ycor(), "Light")
            characters[i].light.show_shape()

        if characters[i].status == 2:
            characters[i].cage.set_position(characters[i].Character.xcor(), characters[i].Character.ycor(), "Cage")
            characters[i].cage.show_shape()

    for i in range(frame):
        for j in range(len(char_arrange)):

            index = char_arrange[j]
            status_cur = characters[index].status

            #   Set defaul when current index over 5
            if characters[index].image_cur > number_image - 1:
                characters[index].image_cur = 0

            if status_cur < 2:
                file_name = "Source/Image/" + image_active + "/" + image_color[index] + "/" + \
                            str(characters[index].image_cur + 1) + \
                            statusImage[status_cur] + ".gif"

            if status_cur == 0:
                characters[index].move_forward(file_name, number_image)
            elif status_cur == 1:
                characters[index].move_backward(x_lower_left, frame, file_name, number_image)

            characters[index].image_cur += 1

            if characters[index].Character.xcor() > x_high_right and characters[index].win != 1:
                if characters[index].win != 1:
                    char_win.append(return_index(characters[index].Character.ycor()))
                if index_win[0] == 0:
                    index_win[0] = characters[index].Character.ycor()
                characters[index].win = 1
                characters[index].status = 3
                characters[index].get_time_end()

        #   Set light hide
    for i in range(5):
        if characters[i].status == 1:
            characters[i].light.hide_shape()

        if characters[i].status == 2:
            characters[i].cage.hide_shape()


def load_file_name_char(file_name, name_char=[]):
    file = open(file_name)

    name_char.clear()
    for line in file:
        name_char.append(line)

    file.close()

    name_char = [x.strip() for x in name_char]


def write_file(file_name, char_win = []):

    file_open = open(file_name, "r")

    array = []
    for line in file_open:
        array.append(line)

    n = int(array[0])
    print(n)
    n += 1
    print("n = ")
    print(n)

    file_open.close()

    file = open(file_name, "w")
    file.write(str(n))
    file.write("\n")
    for i in range(len(char_win)):
        file.write(str(char_win[i]))
        file.write("\n")

    file.close()


def main_game(img, screen_size, index_char, player_name):
    brush = turtle.Turtle()
    screen = turtle.Screen()

    char_name = []
    #   Set background
    if screen_size == 0:
        screen.bgpic("Source/Image/Background/gameplay_small.png")
    elif screen_size == 1:
        screen.bgpic("Source/Image/Background/gameplay_medium.png")
    elif screen_size == 2:
        screen.bgpic("Source/Image/Background/gameplay_large.png")

    file_name_char = "Source/Screen/Text/" + img + ".txt"
    load_file_name_char(file_name_char, char_name)

    #   Create array
    image_color = ["blue", "brown", "green", "red", "orange"]
    statusImage = ["forward", "backward"]
    image_active = img
    char_arrange = [0, 1, 0, 2, 0, 1, 0, 2, 1, 4, 2, 3, 4, 3]
    #char_arrange = [0, 1, 4, 0, 3, 2, 4, 1, 3, 4, 0, 2, 1, 0, 3, 1, 2, 0, 1, 3, 0, 2, 0, 4, 3, 1, 2, 3, 0, 4, 1, 3, 2, 0, 4]
    char_arrange = [0, 1, 2, 0, 3, 0, 1, 0, 1, 3, 1, 0, 2, 4, 2, 0, 3, 1, 3, 4, 2, 4]
    char_temp = [0, 1, 2, 3, 4]
    char_num_defaul = [5, 4, 4, 3, 3]
    char_num_frame = [0, 0, 0, 0, 0]
    frame = 3
    width = 500
    height = 80
    char_win = []
    y_pos = [120, 40, -40, -120, -200]
    y_signal = [0, 0, 0, 0, 0]
    index_win = [0]
    brush_temp = turtle.Turtle()

    brush_temp.hideturtle()
    brush_temp.speed(0)

    #   Set width
    if screen_size == 0:
        width = 350
    elif screen_size == 1:
        width = 450

    if image_active != "Dragon":
        number_image = 4
    else:
        number_image = 4

    #   Set up brush
    brush.hideturtle()
    brush.speed(0)
    #brush._tracer(1, 0)

    #   Set up height and width of screen
    screen.setup(800, 600)

    #   Draw line race
    x_lower_left, x_high_right = draw_line_race(brush, -200, 160, width, height)

    # Load image from file
    load_image("Dragon", screen, 4, image_color, statusImage)
    load_image("Dog", screen, number_image, image_color, statusImage)
    load_image("Ninja", screen, number_image, image_color, statusImage)
    load_image("Robot", screen, number_image, image_color, statusImage)
    load_image("Racoon", screen, number_image, image_color, statusImage)

    #   Create characters
    i = random.randint(0, 4)
    while y_signal[i] == 1:
        i = random.randint(0, 4)
    red = Character.Char(-250, y_pos[i], image_active, image_color[0])
    y_signal[i] = 1

    i = random.randint(0, 4)
    while y_signal[i] == 1:
        i = random.randint(0, 4)
    blue = Character.Char(-250, y_pos[i], image_active, image_color[1])
    y_signal[i] = 1

    i = random.randint(0, 4)
    while y_signal[i] == 1:
        i = random.randint(0, 4)
    brown = Character.Char(-250, y_pos[i], image_active, image_color[2])
    y_signal[i] = 1

    i = random.randint(0, 4)
    while y_signal[i] == 1:
        i = random.randint(0, 4)
    orange = Character.Char(-250, y_pos[i], image_active, image_color[3])
    y_signal[i] = 1

    i = random.randint(0, 4)
    while y_signal[i] == 1:
        i = random.randint(0, 4)
    yellow = Character.Char(-250, y_pos[i], image_active, image_color[4])
    y_signal[i] = 1

    characters = [red, blue, brown, orange, yellow]

    for i in range(5):
        characters[i].name = char_name[i]

    for i in range(5):
        if (characters[i].Character.ycor() == y_pos[int(index_char) - 1]):
            characters[i].name = player_name

    brush.color("#999999")
    for i in range(4):
        if (characters[i].Character.ycor() == y_pos[int(index_char) - 1]):
            set_position(brush, -380, characters[i].Character.ycor() - 20)
            brush.write(characters[i].name, font=("Arial", 25, "bold"))
        else:
            set_position(brush, -380, characters[i].Character.ycor() - 50)
            brush.write(characters[i].name, font=("Arial", 25, "bold"))

    set_position(brush, -380, characters[4].Character.ycor() - 10)
    brush.write(characters[4].name, font=("Arial", 25, "bold"))

    brush.color("black")

    #   Create light
    for i in range(5):
        file_name_light = "Source/Image/" + image_active + "/" + image_color[i] + "/light.gif"
        characters[i].light = Obstacle(characters[i].Character.xcor(), characters[i].Character.ycor(),
                                       file_name_light, "Light")

    #   Create cage
    for i in range(5):
        file_name_cage = "Source/Image/" + image_active + "/" + image_color[i] + "/cage.gif"
        characters[i].cage = Obstacle(characters[i].Character.xcor(), characters[i].Character.ycor(),
                                       file_name_cage, "Cage")
    #   Calculator time start
    for i in range(5):
        characters[i].get_time_start()

    #   Main Loop
    while not is_completed(characters):
        main_loop(brush_temp, x_lower_left, x_high_right, frame, number_image, characters, char_arrange,
                  char_num_defaul, char_temp, image_active, image_color, statusImage, char_num_frame, char_win, y_pos, index_win)
        print("Char temp = ")
        print(char_temp)
    for i in range(5):
        if characters[i].Character.xcor() > x_high_right and characters[i].win != 1:
            char_win.append(return_index(characters[i].Character.ycor()))
    #   Calculator time end
    for i in range(5):
        characters[i].get_duration_time()

    print("Char win = ")
    print(char_win)

    write_file("Source/Output/Output.txt", char_win)

    for i in range(5):
        set_position(brush, characters[i].Character.xcor() - 150, characters[i].Character.ycor())
        brush.write(str(characters[i].dur_minute) + ":", font=("Arial", 20, "normal"))
        set_position(brush, characters[i].Character.xcor() - 120, characters[i].Character.ycor())
        brush.write(str(characters[i].dur_second) + ":", font=("Arial", 20, "normal"))
        set_position(brush, characters[i].Character.xcor() - 80, characters[i].Character.ycor())
        brush.write(characters[i].dur_microsecond, font=("Arial", 20, "normal"))

    #while characters[char_win[0]].Character.xcor() > 50:
    for i in range(5):
        if characters[i].Character.ycor() == index_win[0]:
            index = i
    while characters[index].Character.xcor() > x_lower_left:
        for i in range(number_image):
            file_name_win = "Source/Image/" + img + "/" + image_color[index] + "/" + str(i + 1) + "backward.gif"
            characters[index].move_win(50, file_name_win)




    brush.screen.clear()


