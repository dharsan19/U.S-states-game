import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "assets/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="what's the states name?").title()

    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_state]
        # missing_state = []
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        df = pandas.DataFrame(missing_state)
        df.to_csv("missing_states.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        state_date = data[data["state"] == answer_state]
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(state_date.x.item(), state_date.y.item())
        t.write(answer_state)