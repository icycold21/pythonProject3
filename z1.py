import random
import time
import pickle
from guizero import App, Text, PushButton, Window, Box, Picture, TextBox, ListBox
app = App()
app.set_full_screen()
filename = "test2.pickle"
game_window = None
game_button = None
current_time2 = 0
window = None
instruction_window = None
listoftimes = []
leaderboard = 0
# Attempt to open and load the file
try:
    with open(filename, "rb") as infile:
        leaderboard = pickle.load(infile)
# If the file is empty, set leaderboard to an empty list
except EOFError:
    leaderboard = []

sorted_list = []
current_candidate = 0
trials = 0
difference = 0
user_name = ""
sorted_list = []
average_time = 0
age = ""
desiredage = ""
data_window = None
#Functions
def end_display_time():
    global window, game_window, instruction_window, age
    window.hide()
    game_window.hide()
    instruction_window.hide()


def instructions():
    global instruction_window, age
    instruction_window = Window(app, title="Instructions")
    instruction_window.set_full_screen()
    box9 = Box(instruction_window, height="200", width="fill")
    instruction_text = Text(instruction_window, text="Once you press the button OK, a new window will open \n with a singular button PRESS. Once \n the background of the window turns red, please \n press the button as quickly as you can. This will happen three times.", width="500")
    box10 = Box(instruction_window, height="150")
    ok_button = PushButton(instruction_window, image="button_ok.png", height="40")
    ok_button.when_clicked = game





def reset_game():
    global game_window, trials, age
    game_window.bg = "white"
    random_number = random.randint(1000,1200)
    game_window.after(random_number, red)
    box = Box(game_window, width="fill", height=300)
    trials += 1
    print(trials)
    if trials == 3:
        print("Changed")
        game_button.when_clicked = display_time
        game_window.update()
    else:
        game_button.when_clicked = display_time
        game_window.update()


def add_to_leaderboard():
    global listoftimes, current_candidate, leaderboard, sorted_list, user_name, difference, average_time, age
    current_candidate = (user_name.value, average_time, age.value)
    leaderboard.append(current_candidate)
    with open("test2.pickle", "wb") as outfile:
        pickle.dump(leaderboard, outfile)
    sorted_list = sorted(leaderboard, key=lambda t: t[1])
    print(sorted_list)
    current_candidate = 0
    difference = 0
    average_time = 0
    age = 0



def leaderboard_function():
    global listoftimes, current_candidate, leaderboard, sorted_list, age
    leaderboard_window = Window(app)
    leaderboard_window.set_full_screen()
    box9 = Box(leaderboard_window, height="200", width="fill")
    instruction_text = Text(leaderboard_window, text="This is the leaderboard. There are three columns: the first is the \n user's name, the second is the user's average reaction time, and the third is the user's age.", width="500")
    box10 = Box(leaderboard_window, height="200", width="fill")
    leaderboard_box = ListBox(leaderboard_window, items=sorted_list, scrollbar=True, width = "1000", height = "1500")
    sorted_list = []


def data_function():
    global listoftimes, current_candidate, leaderboard, user_name, difference, average_time, age, filtered_list, desiredage, data_window
    data_window = Window(app)
    data_window.set_full_screen()
    sorted_list = sorted(leaderboard, key=lambda t: t[1])
    if len(leaderboard) > 15 or len(leaderboard) == 15:
        del sorted_list[-1:]
    ageask  = Text(data_window, text="Enter the age for your desired data: ")
    desiredage = TextBox(data_window)
    desiredage.when_key_pressed = datadisplay


def datadisplay(event):
    global filtered_list, desiredage, data_window, age
    if event.key == "\r":
        filtered_list = [tuple for tuple in sorted_list if tuple[2] == desiredage.value]
        box10 = Box(data_window, height="200", width="fill")
        data_list = ListBox(data_window, items=filtered_list, scrollbar=True, width = "1000", height = "1500")




def game():
    global game_window, game_button, trials, age
    game_window = Window(app, bg="white")
    game_window.set_full_screen()
    box12 = Box(game_window, height="300")
    game_button = Picture(game_window, width = "50", image="filled-circle.png", height="50")
    reset_game()




def red():
    global game_window, current_time, age
    game_window.bg = "red"
    current_time = time.time()


def record_time():
    global game_window, current_time, current_time2, window, current_candidate, listoftimes, age
    current_time2 = time.time()
    difference = round((current_time2 - current_time), 2)
    listoftimes.append(difference)
    reset_game()

def enterKeyClicked(event):
    global age
    if event.key == "\r":
        add_to_leaderboard()

def display_time():
    global game_window, current_time, current_time2, window, current_candidate, listoftimes, trials, user_name, leaderboard, difference, average_time, age
    if trials == 3:
        current_time2 = time.time()
        trials = 0
        seconds_time = (current_time2 - current_time)
        difference = round((current_time2 - current_time), 2)
        window = Window(app, title="Second Window")
        window.set_full_screen()
        listoftimes.append(difference)
        average_time = round(sum(listoftimes) / len(listoftimes), 2)
        highest_time = round(max(listoftimes), 2)
        lowest_time = round(min(listoftimes), 2)
        listoftimes = []
        text = Text(window, text="Your average time was: \n" + str(average_time) + " seconds.")
        text = Text(window, text="Your highest time was: \n" + str(highest_time) + " seconds.")
        text = Text(window, text="Your lowest time was: \n" + str(lowest_time) + " seconds. Click OK to \n come back to the menu.")
        box11 = Box(window, height="100")
        nameorder = Text(window, text="Enter your name (with a capital letter)and press ENTER")
        user_name = TextBox(window)
        ageorder =  Text(window, text="Enter your age and press ENTER")
        age = TextBox(window)
        age.when_key_pressed = enterKeyClicked
        box14 = Box(window, height = "100")
        proceed_time = PushButton(window, image="button_ok.png", height="40")
        proceed_time.when_clicked = end_display_time




    else:
        record_time()



#The menu - all of the boxes are to create space between the different buttons
box1 = Box(app, width="fill", align="top", height="40")
box2 = Box(app, width="fill")
box3 = Box(app, width="fill", height="100")
box4 = Box(app, width="fill")
box5 = Box(app, width="fill", height="100")
box6 = Box(app, width="fill")
box7 = Box(app, width="fill", height="100")
box8 = Box(app, width="fill")
title_menu = Picture(box2, image="button_reaction-time.png", height = "50")
start_button = PushButton(box4, image="startbuttonrealfinal.png", height="40")
data_button = PushButton(box6, image="buttondatafinal.png", height="40")
leaderboard_button = PushButton(box8, image="buttonleaderboardfinal.png", height="40")
#what the buttons do
start_button.when_clicked = instructions
leaderboard_button.when_clicked = leaderboard_function
data_button.when_clicked = data_function






app.display()
