import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()

    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)

def catSet(wind):
    tWind = float(wind)
    if 74 <= tWind <= 95:
        return "1"
    if 96 <= tWind <= 110:
        return "2"
    if 111 <= tWind <= 130:
        return "3"
    if 131 <= tWind <= 155:
        return "4"
    if tWind > 155:
        return "5"
    else:
        return ""


def colorSet(wind):
    tWind = float(wind)
    if 74 <= tWind <= 95:
        return "blue"
    if 96 <= tWind <= 110:
        return "green"
    if 111 <= tWind <= 130:
        return "yellow"
    if 131 <= tWind <= 155:
        return "orange"
    if tWind > 155:
        return "red"
    else:
        return "white"

def widthSet(wind):
    tWind = float(wind)
    if 74 <= tWind <= 95:
        return 3
    if 96 <= tWind <= 110:
        return 6
    if 111 <= tWind <= 130:
        return 9
    if 131 <= tWind <= 155:
        return 12
    if tWind > 155:
        return 15
    else:
        return 1

def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()

    # your code to animate Irma here
    file = open("data/Matthew.csv", "r")

    lines = file.readlines()

    print(len(lines))

    lst = lines[1].split(",")
    lon = lst[3]
    lat = lst[2]
    wind = lst[4]
    t.penup()
    t.goto(float(lon), float(lat))
    t.pendown()
    color = colorSet(wind)
    width = widthSet(wind)
    t.write("messi fan", font=("Arial", 16, "normal"))


    for x in range(2, len(lines)):
        lst = lines[x].split(",")
        lon = lst[3]
        lat = lst[2]
        wind = lst[4]
        color = colorSet(wind)
        t.pencolor(color)
        t.pensize(widthSet(wind))
        t.goto(float(lon), float(lat))
        t.write(catSet(wind), font=("Arial", 16, "normal"))

    turtle.done()


if __name__ == "__main__":
    irma()
