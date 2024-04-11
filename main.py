import turtle
import pandas



def state_location(x,y,state_name):
    location=turtle.Turtle()
    location.hideturtle()
    location.penup()
    location.goto(x,y)
    location.write(f"{state_name}")



screen=turtle.Screen()
screen.setup(width=730,height=500)
screen.title("U.S State game")
image="us-states-game/image.gif"
screen.addshape(image)
turtle.shape(image)

game_on=True

data=pandas.read_csv("us-states-game/50_states.csv")

data_list=data.to_dict("records")
all_state=data.state.to_list()
correct_answer=0
#my version code here
while game_on:
    answer=screen.textinput(title=f"{correct_answer}/50 Guess a state",prompt="Guess a state of Us that you know ").title()
    if answer=="Exit":
        game_on=False
    else:
        for state in data_list:
            if state["state"]==answer:
                state_location(state["x"],state["y"],state["state"])  
                data_list.remove(state)
                correct_answer+=1
        
data_df=pandas.DataFrame(data_list)
data_df.state.to_csv("us-states-game/state_to_learn.csv")

    # answer=screen.textinput(title="Guess a state",prompt="Guess a state of Us that you know ").title()
    # for state in  all_state:
    #     if answer==state:
    #         state_data=data[data.state==state]
    #         x=float(state_data.x.iloc[0])
    #         y=float(state_data.y.iloc[0])
    #         state_location(x,y,state)
    #         correct_answer+=1
            
