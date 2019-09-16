import turtle
import matplotlib.pyplot as plt
import numpy as np
import winsound
import datetime
from Application import main_game


class FunctionMenu:
    """Menu load successful"""

    brush = 0
    screen = 0
    back_active = 0
    arr_active = [1, 0, 0]
    screen_text = []
    scene_active = [0, 0, 0, 0]
    screen_size = [1, 0, 0]
    char_active = [1, 0, 0, 0, 0]
    img = 0
    end_game = 0
    size_screen = 0
    name_player = 0
    point_char = [0, 0, 0, 0, 0]
    point_cur = []
    winner = 0
    name_char = []
    choose_index = 0
    point_player = []

    def __init__(self, width_screen, height_screen):
        self.brush = turtle.Turtle()
        self.brush.hideturtle()
        self.brush.speed(0)
        self.brush._tracer(0, 0)

        self.load_file_screen("Source/Screen/Text/Screen_Eng.txt")

        self.scene_active = [0, 0, 0, 1]
        self.img = "Dragon"

        self.screen = turtle.Screen()
        self.screen.setup(width_screen, height_screen)

        self.screen.title("BEST CHOICE")
    def set_defaul(self):
        self.brush.speed(0)
        self.brush._tracer(0, 0)

        self.load_file_screen("Source/Screen/Text/Screen_Eng.txt")
        self.img = self.screen_text[3]

    def load_file_screen(self, file_name):
        screen_file = open(file_name)

        for line in screen_file:
            self.screen_text.append(line)

        self.screen_text = [x.strip() for x in self.screen_text]

    def load_file_player(self, file_name):
        file = open(file_name, "r")

        self.point_player = []

        for line in file:
            self.point_player.append(int(line))

        self.point_player[0] += 1

        if int(self.choose_index) == self.point_cur[1] + 1:
            self.point_player[1] += 1

        file.close()

        file = open(file_name, "w")

        for line in range(2):
            file.write(str(self.point_player[line]))
            file.write("\n")

    def load_sound_status(self, file_name, duration):
        winsound.PlaySound(file_name, winsound.SND_ASYNC)

        start = datetime.datetime.now()

        while datetime.datetime.now().second - start.second < duration:
            i = 1

    def load_file_point_char(self, file_total, file_cur):
        point_file = open(file_total, "r")
        point_cur = open(file_cur, "r")

        self.point_cur.clear()

        for line in point_cur:
            self.point_cur.append(int(line))

        self.winner = self.point_cur[1]


        self.point_char.clear()
        for line in point_file:
            self.point_char.append(int(line))

        point_cur.close()
        point_file.close()

        for i in range(len(self.point_char)):
            self.point_char[self.point_cur[i + 1]] = self.point_char[self.point_cur[i + 1]] + (5 - i)

        point_file = open(file_total, "w")
        for i in range(5):
            point_file.write(str(self.point_char[i]))
            point_file.write("\n")

    def load_file_name_char(self, file_name):
        file = open(file_name)

        self.name_char.clear()
        for line in file:
            self.name_char.append(line)

        file.close()

    def set_position_button(self, x_position, y_position):
        self.brush.penup()
        self.brush.setposition(x_position, y_position)
        self.brush.pendown()

    def print_text(self, text, x_position, y_position, color, size):
        self.set_position_button(x_position, y_position)
        self.brush.color(color)
        self.brush.write(text, font=("Arial", size, "normal"))
        self.brush.color("black")

    def get_name_img(self):
        return self.img

    def load_sound(self, file_name):
        winsound.PlaySound(file_name, winsound.SND_ASYNC + winsound.SND_LOOP)

    def stop_sound(self):
        winsound.PlaySound(None, winsound.SND_ASYNC + winsound.SND_LOOP)

    def create_button(self, x_position, y_position, width, height, name_button, size_text):
        self.set_position_button(x_position, y_position)
        self.brush.penup()

        for step in range(2):
            self.brush.forward(width)
            self.brush.right(90)
            self.brush.forward(height)
            self.brush.right(90)

        self.set_position_button(x_position + width / 2,
                                 y_position - height / 2 - 15)
        self.brush.write(name_button, align="center", font=("Arial", size_text, "normal"))

    @staticmethod
    def location_mouse(x_location, y_location, x_max, x_min, y_max, y_min):
        if (x_min < x_location < x_max) and (y_min < y_location < y_max):
            return True

        return False

    def create_choose_circle(self, x_position, y_position, radian, text, size, index, arr=[]):
        self.brush.pendown()
        self.set_position_button(x_position, y_position)

        if arr[index] == 1:
            self.brush.color("black", "black")
        else:
            self.brush.color("black", "white")

        self.brush.begin_fill()
        self.brush.circle(radian)
        self.brush.end_fill()

        x, y = self.brush.position()

        self.set_position_button(x, y - radian)

        self.brush.circle(radian + 5)

        self.set_position_button(x_position + 50, y_position)
        self.brush.write(text, font=("Arial", size, "normal"))

    @staticmethod
    def turn_active(index, arr=[]):
        for i in range(len(arr)):
            if i != index:
                arr[i] = 0

        arr[index] = 1

    def onclick_setting(self, x_position, y_position):
        if self.location_mouse(x_position, y_position, -240, -260, 15, -5) and self.scene_active[1] == 1:
            self.size_screen = 0
            self.turn_active(0, self.screen_size)
            print("Small Screen was chosen.")

        if self.location_mouse(x_position, y_position, -240, -260, -35, -55) and self.scene_active[1] == 1:
            self.size_screen = 1
            self.turn_active(1, self.screen_size)
            print("Medium Screen was chosen.")

        if self.location_mouse(x_position, y_position, -240, -260, -85, -105) and self.scene_active[1] == 1:
            self.size_screen = 2
            self.turn_active(2, self.screen_size)
            print("Large Screen was chosen.")

        if self.location_mouse(x_position, y_position, 60, 40, 15, 5) and self.scene_active[1] == 1:
            self.turn_active(0, self.char_active)
            self.img = self.screen_text[3]
            print("Character 1 was chosen.")

        if self.location_mouse(x_position, y_position, 60, 40, -15, -35) and self.scene_active[1] == 1:
            self.turn_active(1, self.char_active)
            self.img = self.screen_text[4]
            print("Character 2 was chosen.")

        if self.location_mouse(x_position, y_position, 60, 40, -45, -65) and self.scene_active[1] == 1:
            self.turn_active(2, self.char_active)
            self.img = self.screen_text[5]
            print("Character 3 was chosen.")

        if self.location_mouse(x_position, y_position, 60, 40, -75, -95) and self.scene_active[1] == 1:
            self.turn_active(3, self.char_active)
            self.img = self.screen_text[6]
            print("Character 4 was chosen.")

        if self.location_mouse(x_position, y_position, 60, 40, -105, -125) and self.scene_active[1] == 1:
            self.turn_active(4, self.char_active)
            self.img = self.screen_text[7]
            print("Character 5 was chosen.")

        if self.location_mouse(x_position, y_position, 50, -50, -170, -200) and self.scene_active[1] == 1:
            self.back_active = 1
            self.turn_active(0, self.arr_active)
            print("From Option to Menu")

    def setting(self):
        self.brush.clear()
        self.screen.bgpic("Source/Image/Background/option_bg.png")

        self.create_button(-300, 230, 600, 50, "Options", 30)
        self.back_active = 0

        #   Write title
        self.set_position_button(-270, 55)
        self.brush.write(self.screen_text[8], font=("Arial", 15, "normal"))

        self.set_position_button(0, 55)
        self.brush.write(self.screen_text[9], font=("Arial", 15, "normal"))

        while self.back_active == 0:
            self.create_choose_circle(-250, 0, 5, self.screen_text[10], 10, 0, self.screen_size)
            self.create_choose_circle(-250, -50, 5, self.screen_text[11], 10, 1, self.screen_size)
            self.create_choose_circle(-250, -100, 5, self.screen_text[12], 10, 2, self.screen_size)

            self.create_choose_circle(50, 0, 5, self.screen_text[3], 10, 0, self.char_active)
            self.create_choose_circle(50, -30, 5, self.screen_text[4], 10, 1, self.char_active)
            self.create_choose_circle(50, -60, 5, self.screen_text[5], 10, 2, self.char_active)
            self.create_choose_circle(50, -90, 5, self.screen_text[6], 10, 3, self.char_active)
            self.create_choose_circle(50, -120, 5, self.screen_text[7], 10, 4, self.char_active)

            self.create_button(-50, -170, 100, 50, self.screen_text[13], 20)

            print(self.img)

            self.brush.screen.onclick(self.onclick_setting)

        self.brush.clear()
        self.turn_active(0, self.scene_active)
        self.menu()

    def onclick_info(self, x_position, y_position):
        if self.location_mouse(x_position, y_position, -305, -360, -190, -265) and self.scene_active[2] == 1:
            self.back_active = 1
            self.turn_active(0, self.scene_active)
            print("From info to Menu")

    def info(self):
        self.brush.clear()
        self.screen.bgpic("Source/Image/Background/info_bg.png")
        self.print_text("Team 8 - 17CLC1", -100, 250, "white", 20)

        self.print_text("Nguyễn Duy Cường", -80, 145, "blue", 15)
        self.print_text("Mai Thanh Bình", -80, 50, "blue", 15)
        self.print_text("Đinh Nguyễn Hạnh Dung", -80, -45, "blue", 15)
        self.print_text("Võ Trần Chí Hưng", -80, -135, "blue", 15)
        self.print_text("Nguyễn Trần Tuấn Anh", -80, -235, "blue", 15)

        self.create_button(-360, -190, 55, 75, "", 0)
        self.back_active = 0
        while self.back_active == 0:
            self.create_button(-360, -190, 55, 75, "", 0)
            self.brush.screen.onclick(self.onclick_info)

        self.brush.clear()
        self.turn_active(0, self.scene_active)
        self.menu()

    def onclick_menu(self, x_position, y_position):
        if self.location_mouse(x_position, y_position, 100, -100, -15, -65) and self.scene_active[0] == 1:
            self.turn_active(1, self.scene_active)
            self.brush.screen.clearscreen()

            file_name = "Source/Screen/Text/" + str(self.img) + ".txt"
            self.load_file_name_char(file_name)
            self.enter_name_player()
            #self.screen.clear()
            #self.menu()

        if self.location_mouse(x_position, y_position, 100, -100, -90, -140) and self.scene_active[0] == 1:
            self.turn_active(1, self.scene_active)
            self.setting()

        if self.location_mouse(x_position, y_position, 100, -100, -160, -210) and self.scene_active[0] == 1:
            self.turn_active(2, self.scene_active)
            self.info()

    def menu(self):

        print("Menu is active")
        self.screen.bgpic("Source/Image/Background/menu_bg.png")

        #self.create_button(-250, 250, 500, 250, "Best choice", 40)

        self.create_button(-100, -15, 200, 50, self.screen_text[0], 20)

        self.create_button(-100, -90, 200, 50, self.screen_text[1], 20)

        self.create_button(-100, -160, 200, 50, self.screen_text[2], 20)

        self.brush.screen.onclick(self.onclick_menu)
        turtle.done()

    def set_language_vie(self):
        self.screen_text[0] = "Chơi game"
        self.screen_text[1] = "Cài đặt"
        self.screen_text[2] = "Thông tin"
        self.screen_text[3] = "Dragon"
        self.screen_text[4] = "Dog"
        self.screen_text[5] = "Ninja"
        self.screen_text[6] = "Racoon"
        self.screen_text[7] = "Robot"
        self.screen_text[8] = "Chọn kích thước màn hình"
        self.screen_text[9] = "Chọn bộ nhân vật"
        self.screen_text[10] = "Nhỏ"
        self.screen_text[11] = "Trung bình"
        self.screen_text[12] = "Lớn"
        self.screen_text[13] = "Quay lại"
        self.screen_text[14] = "Điền tên người chơi"

    def set_language_jap(self):
        self.screen_text[0] = "遊びます"
        self.screen_text[1] = "オプション"
        self.screen_text[2] = "情報"
        self.screen_text[3] = "Dragon"
        self.screen_text[4] = "Dog"
        self.screen_text[5] = "Ninja"
        self.screen_text[6] = "Racoon"
        self.screen_text[7] = "Robot"
        self.screen_text[8] = "画面サイズを選択してください"
        self.screen_text[9] = "文字を選択してくださいt"
        self.screen_text[10] = "小さい"
        self.screen_text[11] = "中"
        self.screen_text[12] = "大"
        self.screen_text[13] = "バック"
        self.screen_text[14] = "あなたの名前を記入してください"

    def onclick_language(self, x_position, y_position):
        if self.location_mouse(x_position, y_position, 100, -100, -20, -70) and self.scene_active[3] == 1:
            self.load_file_screen("Source/Screen/Text/Screen_Eng.txt")
            self.brush.clear()
            self.turn_active(0, self.scene_active)
            self.menu()

        if self.location_mouse(x_position, y_position, 100, -100, -90, -140) and self.scene_active[3] == 1:
            self.set_language_vie()
            self.brush.clear()
            self.turn_active(0, self.scene_active)
            self.menu()

        if self.location_mouse(x_position, y_position, 100, -100, -160, -210) and self.scene_active[3] == 1:
            self.set_language_jap()
            self.brush.clear()
            self.turn_active(0, self.scene_active)
            self.menu()

    def choose_language(self):
        self.load_sound("Source/Screen/Sound/Menu_song.wav")
        self.screen.bgpic("Source/Image/Background/language_bg.png")
        self.create_button(-100, -20, 200, 50, "English", 20)
        self.create_button(-100, -90, 200, 50, "Vietnamese", 20)
        self.create_button(-100, -160, 200, 50, "Japanese", 20)

        self.brush.screen.onclick(self.onclick_language)
        turtle.done()

    def enter_name_player(self):
        file_name = "Source/Screen/Text/" + self.img + ".txt"
        self.load_file_name_char(file_name)
        name_player = self.screen.textinput(self.screen_text[16], self.screen_text[14])

        while name_player == "":
            name_player = self.screen.textinput(self.screen_text[16], self.screen_text[14])

        string = "1. Race 1\n2. Race 2\n3. Race 3\n4. Race 4\n5. Race 5"

        self.choose_index = self.screen.textinput(self.screen_text[15], string)

        while self.choose_index == "" or (self.choose_index != "1" and self.choose_index != "2" and self.choose_index != "3") \
                and self.choose_index != "4" and self.choose_index != "5":
            self.choose_index = self.screen.textinput(self.screen_text[15], string)

        self.load_sound("Source/Screen/Sound/playgame.wav")
        main_game(self.img, self.size_screen, self.choose_index, name_player)
        self.load_sound("Source/Screen/Sound/awesomeness.wav")
        file_name_point = "Source/Output/" + self.img + ".txt"
        self.load_file_point_char(file_name_point, "Source/Output/Output.txt")
        self.load_file_player("Source/Output/Player.txt")
        self.end_game.end()

        self.screen.clear()

        turtle.done()


class EndGame:
    brush = turtle.Turtle()
    brush.hideturtle()
    name_char = "1"
    screen = turtle.Screen()

    def chart_characters(self, char1, char2, char3, char4, char5):
        objects = (menu.name_char[0], menu.name_char[1], menu.name_char[2], menu.name_char[3], menu.name_char[4])
        performance = [char1, char2, char3, char4, char5]
        y_pos = np.arange(len(objects))
        plt.figure('Character Rating')  # change name of the chart screen
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Score')
        plt.title('Winning Score')
        plt.show()

    def chart_player(self, percent):
        labels = 'WIN', 'LOSE'
        sizes = [percent, 100 - percent]
        colors = ['lightskyblue', 'lightcoral']
        explode = [0, 0.1]
        plt.figure('Winning Percent')  # change name of the chart screen
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=166)
        plt.axis('equal')
        plt.show()

    def set_position(self, xPosition, yPosition):
        self.brush.penup()
        self.brush.setposition(xPosition, yPosition)
        self.brush.pendown()

    def draw_button(self, x, y, width, heigh, nameButton, size):
        self.brush._tracer(0, 0)
        self.set_position( x, y)
        self.brush.penup()
        for step in range(2):
            self.brush.forward(width)
            self.brush.right(90)
            self.brush.forward(heigh)
            self.brush.right(90)

        self.set_position(x + width / 2, y - heigh / 2 - 15)
        self.brush.write(nameButton, align="center", font=("Arial", size, "normal"))

    def is_location(self, xLocation, yLocation, xMax, xMin, yMax, yMin):
        if (xMin < xLocation < xMax) and (yMin < yLocation < yMax):
            return True

        return False

    def event_onclick_end_game(self, xPosition, yPosition):
        #   Chart player button
        if self.is_location(xPosition, yPosition, -130, -250, -50, -170):
            self.chart_player(menu.point_player[1] / menu.point_player[0] * 100)

        #   Chart Characters button
        if self.is_location(xPosition, yPosition, 270, 150, -50, -170):
            self.chart_characters(menu.point_char[0], menu.point_char[1], menu.point_char[2], menu.point_char[3], menu.point_char[4])

        #   Replay button
        if self.is_location(xPosition, yPosition, 70, -50, -50, -170):
            print("Alright")
            self.brush.screen.clearscreen()
            menu.set_defaul()
            menu.turn_active(0, menu.scene_active)
            menu.load_sound("Source/Screen/Sound/Menu_song.wav")
            menu.menu()


    def end(self):

        self.brush.speed(0)
        self.brush.hideturtle()
        self.brush._tracer(0, 0)
        self.screen.bgpic("Source/Image/Background/end_bg.png")

        duration = 5
        print("Winner = ")
        print(menu.winner)

        if menu.winner == int(menu.choose_index) - 1:
            self.draw_button(-90, 90, 200, 50, "YOU WIN", 20)

        else:
            self.draw_button(-90, 90, 200, 50, "YOU LOSE", 20)


        self.draw_button(-250, -50, 120, 120, "Winning Percent", 15)
        self.draw_button(-50, -50, 120, 120, "Replay", 20)
        self.draw_button(150, -50, 120, 120, "Rating", 15)

        if menu.winner == int(menu.choose_index) - 1:
            file_name = "Source/Screen/Sound/win.wav"
        else:
            file_name = "Source/Screen/Sound/Lose.wav"

        start = datetime.datetime.now()
        winsound.PlaySound(file_name, winsound.SND_ASYNC)

        while  datetime.datetime.now().second - start.second < duration:
            i = 1

        menu.load_sound("Source/Screen/Sound/awesomeness.wav")
        self.brush.screen.onclick(self.event_onclick_end_game)
        turtle.done()

menu = FunctionMenu(800, 600)
menu.end_game = EndGame()

menu.choose_language()
menu.menu()