import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Irish Counties Game")
image = "blank_counties_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("32_counties.csv")
all_counties = data.county.to_list()
guessed_counties = []

while len(guessed_counties) < 32:
    answer_county = screen.textinput(title=f"{len(guessed_counties)}/32 Counties Correct", prompt="What's another state's name?").title()

    if answer_county == "Exit":
        missing_counties = [county for county in all_counties if county not in guessed_counties]
        new_data = pd.DataFrame(missing_counties)
        new_data.to_csv("counties_to_learn.csv")
        break
    elif answer_county in all_counties:
        guessed_counties.append(answer_county)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        county_data = data[data.county == answer_county]
        t.goto(county_data.x.item(), county_data.y.item())
        t.write(answer_county)

screen.exitonclick()
#get position of click
def get_mouse_click_coor(x,y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
