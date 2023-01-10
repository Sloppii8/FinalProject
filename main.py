import random
import sys
import time
import pygame

from guizero import App, Box, Text, PushButton, Window, TextBox

#globals + Lists + color
reaction_button = None
text_box_username = None
text_box_age = None
save_button = None
bottombox = None
continuebutton = None
start_text_1 = None
start_text_2 = None
start_text_3 = None
textbox_username_results = None
text_box_username_results = None
username_list = []
age_list =[]
results_list = []
big_list = []
little_list =[]
score_recorded = False
myblue = "#7180ac"

app = App(width=1080, height=720, bg="#7180ac")

#solid menu

def menu():
   space_box = Box(app, width="fill", height=30, align="top")
   space_box.bg = "#7180ac"
   title_box = Box(app, width=700, height=100, align="top")
   title = Text(title_box, text="Reaction Game", size=50, align="top")
   space_box_two = Box(app, width="fill", height=30, align="top")
   space_box_two.bg = "#7180ac"
   space_box_three = Box(app, width=150, height="fill", align="left")
   space_box_three.bg = "#7180ac"
   space_box_four = Box(app, width=100, height="fill", align="right")
   space_box_four.bg = "#7180ac"
   space_box_five = Box(app, width="fill", height=50, align="bottom")
   space_box_five.bg = "#7180ac"
   buttons_box = Box(app, width="fill", height="fill", align="top")
   box_space_box = Box(buttons_box, width=400, height=30, align="right")
   box_space_box.bg = "#7180ac"
   start_button = PushButton(buttons_box, width=40, height=5, text="Start", align="top", command=pregame)
   start_button.bg = "#2e294e"
   box_space_box_2 = Box(buttons_box, width=60, height=60, align="top")
   box_space_box_2.bg = "#7180ac"
   Teacher_button = PushButton(buttons_box, width=40, height=5, text="Teacher access", align="top", command=teacher_access_window)
   Teacher_button.bg = "#2e294e"
   box_space_box_3 = Box(buttons_box, width=60, height=60, align="top")
   box_space_box_3.bg = "#7180ac"
   results_button = PushButton(buttons_box, width=40, height=5, text="My Results", align="top", command=my_results_window)
   results_button.bg = "#2e294e"

#before game functions + game functions

def pregame():
   global reaction_button, text_box_username,text_box_age,save_button, bottombox, window_1
   window_1 = Window(app, title="Second window",width=1080, height=720)
   app.hide()
   topspace_box = Box(window_1, width="fill", height=200, align="top")
   topspace_box.bg = "#7180ac"
   age_text = Text(topspace_box, text="Enter Username: ", size = 30, align= "top")
   text_box_username = TextBox(topspace_box, width=30)
   username_text = Text(topspace_box, text="Enter Age: ", size = 30, align= "top")
   text_box_age = TextBox(topspace_box, width=30)
   space_betweensaveandtext = Box(window_1, width="fill", height=50, align="top")
   space_betweensaveandtext.bg = "#7180ac"
   save_button = PushButton(space_betweensaveandtext, width=5, height=1, text="save", align="bottom", command=stopusernameandage)
   bottombox = Box(window_1, width="fill", height = "fill", )
   bottombox.bg = "#7180ac"
   topspace_box_2 = Box(bottombox, width="fill", height= "30")
   topspace_box_2.bg = "#7180ac"
   information = TextBox(bottombox, width="100", height= "30", text="When done with the test, and seen results, close window, to come back to this screen", align="top")
   information.disable()


def stopusernameandage():
   global text_box_username, age_text,save_button, bottombox, start_text_1, start_text_2, start_text_3, little_list, big_list, continuebutton
   text_box_username.disable()
   text_box_age.disable()
   save_button.disable()
   little_list.append(text_box_username.value)
   little_list.append(text_box_age.value)
   start_text_1 = PushButton(bottombox, width=40, height=4, align="top", text="Test 1", command=reaction_game_window)
   start_text_2 = PushButton(bottombox, width=40, height=4, align="top", text="Test 2", command=reaction_game_window_1)
   start_text_3 = PushButton(bottombox, width=40, height=4, align="top", text="Test 3", command=reaction_game_window_3)
   continuebutton = PushButton(bottombox, width=40, height=4, align="top", text="CONTINUE", command=smt)
   continuebutton.disable()

def smt():
   global window_1, app
   app.show()
   window_1.hide()

def stop_menu_window():
   app.hide()
   reaction_game_window()


def reaction_game_window():
   global little_list, big_list, score_recorded, continuebutton, myblue
   pygame.init()
   # Screen + Font
   screen = pygame.display.set_mode((1080, 720))
   pygame.display.set_caption("Reaction Time!")


   main_font = pygame.font.SysFont("Helvetica", 90)

   # Title
   title = main_font.render("Reaction Time Test", True, "black")
   title_rect = title.get_rect(center=(540, 50))

   # Click to Start
   click_to_start = main_font.render("Click to Start", True, "black")
   click_to_start_rect = click_to_start.get_rect(center=(540, 360))

   # Waiting
   waiting = main_font.render("Wait...", True, "black")
   waiting_rect = waiting.get_rect(center=(540, 360))

   # Click
   click = main_font.render("Click NOW!", True, "black")
   click_rect = click.get_rect(center=(540, 360))

   # Score
   score = main_font.render("Speed: 1000 ms", True, "red")
   score_rect = score.get_rect(center=(540, 360))

   # Game State
   game_state = "Click to Start"

   # Times
   start_time, end_time = 0, 0

   # Game Loop
   run = True
   while run:
      # Events and MOUSEBUTTONDOWN
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            run = False
         if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "Click to Start":
               game_state = "Waiting"
            elif game_state == "Test Starting":
               ending_time = time.time()
               score_recorded = False
               game_state = "Showing Results"

      if not run:
         break
      screen.fill(myblue)

      screen.blit(title, title_rect)

      # Game State Logics
      if game_state == "Click to Start":
         screen.blit(click_to_start, click_to_start_rect)
      elif game_state == "Waiting":
         screen.fill("yellow")

         screen.blit(waiting, waiting_rect)

         pygame.display.update()

         delay_time = random.uniform(1, 10)

         time.sleep(delay_time)

         game_state = "Test Starting"

         starting_time = time.time()

      elif game_state == "Test Starting":
         screen.fill("green")
         screen.blit(click, click_rect)
      elif game_state == "Showing Results":
         reaction_time = round((ending_time - starting_time) * 1000)
         score_text = main_font.render(f"Test Speed: {reaction_time} ms", True, "black")
         screen.blit(score_text, score_rect)
         start_text_1.disable()
         if not score_recorded:
            little_list.append(reaction_time)
            score_recorded = True
         if len(little_list) == 5:
            big_list.append(little_list.copy())
            little_list = []
            print(little_list)
            print(big_list)
            continuebutton.enable()

      # Update Display
      pygame.display.update()



def backtomenuteacher():
   global exit_teacher_button, window_2
   window_2.hide()
   app.show()


def backtomenuresults():
   global exit_results_button, window_3
   window_3.hide()
   app.show()


def reaction_game_window_1():
   global start_text_2
   reaction_game_window()
   start_text_2.disable()

def reaction_game_window_3():
   global start_text_3
   reaction_game_window()
   start_text_3.disable()

#teacher window, unfinished
def teacher_access_window():
   global exit_teacher_button, window_2
   window_2 = Window(app, title="Teacher Access",width=1080, height=720, bg="#7180ac")
   app.hide()
   space_box = Box(window_2, width="fill", height=30, align="top")
   space_box.bg = "#7180ac"
   title_box = Box(window_2, width=700, height=100, align="top")
   title = Text(title_box, text="Teacher Access", size=50, align="top")
   space_box_two = Box(window_2, width="fill", height=30, align="top")
   space_box_two.bg = "#7180ac"
   space_box_three = Box(window_2, width=50, height="fill", align="left")
   space_box_three.bg = "#7180ac"
   space_box_four = Box(window_2, width=100, height="fill", align="right")
   space_box_four.bg = "#7180ac"
   space_box_five = Box(window_2, width="fill", height=2, align="bottom")
   space_box_five.bg = "#7180ac"
   buttons_box = Box(window_2, width="fill", height="fill", align="top")
   information = Text(buttons_box, text="Teacher Access: Here you can access the results for all of the class", size=10, width=50,height= 4, align="right")
   information.bg = "#2e294e"
   yseven_button = PushButton(buttons_box,width=30, height=3, text="Year 7", align="top")
   yseven_button.bg = "#2e294e"
   yeight_button = PushButton(buttons_box,width=30, height=3, text="Year 8", align="top")
   yeight_button.bg = "#2e294e"
   ynine_button = PushButton(buttons_box,width=30, height=3, text="Year 9", align="top")
   ynine_button.bg = "#2e294e"
   yten_button = PushButton(buttons_box,width=30, height=3, text="Year 10", align="top")
   yten_button.bg = "#2e294e"
   yeleven_button = PushButton(buttons_box,width=30, height=3, text="Year 11", align="top")
   yeleven_button.bg = "#2e294e"
   ytwelve_button = PushButton(buttons_box,width=30, height=3, text="Year 12", align="top")
   ytwelve_button.bg = "#2e294e"
   ythirteen_button = PushButton(buttons_box,width=30, height=3, text="Year 13", align="top",command=yearthirteen)
   ythirteen_button.bg = "#2e294e"
   exit_teacher_button = PushButton(buttons_box, width=5, height=1, align="top", text="EXIT", command=backtomenuteacher)

def yearthirteen():
   window_4 = Window(app,title="Year Thirteen")

#results function

def my_results_window():
   global text_box_age_results, text_box_username_results, avarage_score, window_3, avarageresultsbox, exit_results_button, window_3
   window_3 = Window(app, title="Results",width=1080, height=720, bg="#7180ac")
   app.hide()
   space_box = Box(window_3, width="fill", height=30, align="top")
   space_box.bg = "#7180ac"
   title_box = Box(window_3, width=700, height=100, align="top")
   title = Text(title_box, text="Your Results", size=50, align="top")
   space_box_two = Box(window_3, width="fill", height=30, align="top")
   space_box_two.bg = "#7180ac"
   space_box_three = Box(window_3, width=50, height="fill", align="left")
   space_box_three.bg = "#7180ac"
   space_box_four = Box(window_3, width=100, height="fill", align="right")
   space_box_four.bg = "#7180ac"
   space_box_five = Box(window_3, width="fill", height=50, align="bottom")
   space_box_five.bg = "#7180ac"
   buttons_box = Box(window_3, width="fill", height="fill", align="top")
   information = Text(buttons_box, text="Here are your results:", size=10, width=50,height= 4, align="top")
   information.bg = "#2e294e"
   age_text_results = Text(buttons_box, text="Enter Username: ", size = 30, align= "top")
   text_box_username_results = TextBox(buttons_box, width=30)
   username_text_results = Text(buttons_box, text="Enter Age: ", size = 30, align= "top")
   text_box_age_results = TextBox(buttons_box, width=30)
   avarageresultsbox = Box(buttons_box, width="fill", height=110, align="top")
   space_betweensaveandtext_results = Box(window_3, width="fill", height=30, align="top")
   space_betweensaveandtext_results.bg = "#7180ac"
   save_button_results = PushButton(buttons_box, width=5, height=1, text="save", align="top", command=stopusernameandage_results)
   exit_results_button = PushButton(space_betweensaveandtext_results, width=5, height=1, align="bottom", text="EXIT", command=backtomenuresults)

def stopusernameandage_results():
   global text_box_age_results, text_box_username_results, little_list, big_list,avarage_score, window_3, avarageresultsbox
   text_box_age_results.disable()
   text_box_username_results.disable()
   username = str(text_box_username_results.value)
   age = str(text_box_age_results.value)
   for user in big_list:
      if user[0] == username and user[1] == age:
         print("Works")
         avarage_score = (user[2] + user[3] + user[4])//3
         print(avarage_score)
         tempo_list = [user[2], user[3], user[4]]
         tempo_list.sort()
         print(tempo_list[0])
         print(tempo_list[2])
         lowest_score = (tempo_list[0])
         highest_score = (tempo_list[2])
         results_avarage = Text(avarageresultsbox,text="Average result:" + str(avarage_score), size= 15)
         results_highest = Text(avarageresultsbox,text="Highest result:" + str(highest_score), size= 15)
         results_lowest = Text(avarageresultsbox,text="Lowest result:" + str(lowest_score), size= 15)








menu()
app.display()
