import random
from tkinter import *
import math
from random import *
from players_simple import Players
away = "Away"
home = "Home"

names_team1 = ["Nurbol", "Baibol", "Aibek", "Zhanserik", "Nurzhan", "Aimedet"]
names_team2 = ["Nurbol", "Baibol", "Aibek", "Zhanserik", "Nurzhan", "Aimedet"]

POSITIONS_team1 = ["ATTACKER", "DEFENDER", "MIDFIELDER"]
POSITIONS_team2 = ["ATTACKER", "DEFENDER", "MIDFIELDER"]

timer = None
FONT_NAME = "Courier"
reps = 0

ONE_TIME = 45
BREAK_MIN = 15

FILE_NAME = "pitch.png"
HEIGHT = 738
WIDTH = 1280


class GameMechanism:
    def __init__(self):
        super().__init__()
        self.player_1 = None
        self.break_sec = BREAK_MIN * 60
        self.time_sec = ONE_TIME * 60
        # creating window
        self.window = Tk()
        self.window.title("Football Match")
        self.window.config(padx=25, pady=50)
        #####################
        self.count_sec = None
        self.count_min = None
        # creating Timer text label
        self.Timer_lab = Label(text="FOOTBALL MATCH")
        self.Timer_lab.config(font=(FONT_NAME, 35))
        self.Timer_lab.grid(column=1, row=0)
        self.time_track = Label(text="00:00")
        self.time_track.config(font=(FONT_NAME, 35))
        self.time_track.grid(column=1, row=1)
        #######################
        self.home_score = 0
        self.away_score = 0
        # creating pitch canvas
        self.pitch = Canvas(width=WIDTH + 50, height=HEIGHT + 50, highlightthickness=0)
        self.pitch_image = PhotoImage(file=FILE_NAME)
        self.pitch.create_image(WIDTH / 2 + 25, 400, image=self.pitch_image)
        self.pitch.grid(column=1, row=2)
        ########
        # texts on the canvas pitch
        self.score_text = self.pitch.create_text(665, 80, text=f"{self.home_score} {self.away_score}",
                                                 font=(FONT_NAME, 40, "bold"), fill="black")
        self.home_team = self.pitch.create_text(365, 180, text="",
                                                font=(FONT_NAME, 15, "bold"), fill="black")
        self.away_team = self.pitch.create_text(965, 180, text="",
                                                font=(FONT_NAME, 15, "bold"), fill="black")
        # buttons
        self.start_button = Button(text="Start Football Match", command=self.start_game)
        self.start_button.grid(column=0, row=0)
        self.exit_button = Button(text="Exit", command=self.quit)
        self.exit_button.grid(column=0, row=1)

        self.window.mainloop()

    # button to start game and counter
    def start_game(self):
        global reps
        if reps == 0:
            self.count_down(self.time_sec)
            self.Timer_lab.config(text="1ST HALF")
            self.update_score()
        elif reps == 1:
            self.count_down(self.break_sec)
            self.Timer_lab.config(text="HT")
        elif reps == 2:
            self.count_down(self.time_sec)
            self.Timer_lab.config(text="2ND HALF")
            self.update_score()
        elif reps == 3:
            self.Timer_lab.config(text="FT")
        else:
            pass
        reps += 1

    # timer mechanism
    def count_down(self, count):
        self.count_min = math.floor(count / 60)
        self.count_sec = count % 60
        if self.count_sec < 10:
            self.count_sec = f"0{self.count_sec}"
        if self.count_min < 10:
            self.count_min = f"0{self.count_min}"
        self.time_track.config(text=f"{self.count_min}:{self.count_sec}")
        if count > 0:
            global timer
            self.window.after(1, self.count_down, count - 1)
        else:
            self.start_game()

    # updating score
    def update_score(self):
        for _ in range(0, 45):
            if randint(0, 60) == 1:
                self.away_score += 1
                scorer1 = choice(names_team2)
                self.pitch.itemconfig(self.away_team,
                                      text=(Players(scorer1, choice(POSITIONS_team2), away).name + " " +
                                            Players(scorer1, choice(POSITIONS_team2), away).position +
                                            " scores for " + away + " team"))
                names_team2.remove(scorer1)
                self.pitch.itemconfig(self.score_text, text=f"{self.home_score}:{self.away_score}")
            if randint(0, 60) == 1:
                self.home_score += 1
                scorer2 = choice(names_team1)
                self.pitch.itemconfig(self.home_team,
                                      text=(Players(scorer2, choice(POSITIONS_team1), home).name + " " +
                                            Players(scorer2, choice(POSITIONS_team1), home).position +
                                            " scores for " + home + " team"))
                names_team1.remove(scorer2)
                self.pitch.itemconfig(self.score_text, text=f"{self.home_score}:{self.away_score}")

    # exiting the game
    def quit(self):
        self.window.quit()
