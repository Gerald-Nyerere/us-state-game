import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image  = "blank_states_img.gif"
screen.addshape(image)
screen.setup(height=491, width=725)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
geussed_states = []
while len(geussed_states) < 50:
    answer_state = screen.textinput(title=f"{len(geussed_states)}/50 correct States", prompt="what's anoher States name? ").title()
    print(answer_state)

    if answer_state == "Exit":
        #missing_states = []
        #for state in all_states:
         #   if state not in geussed_states:
          #      missing_states.append(state)
        missing_states = [state for state in all_states if state != geussed_states]
       
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("state_to_learn.csv")

        break

    if answer_state in all_states:
        geussed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data= data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

#state_to_learn.csv

