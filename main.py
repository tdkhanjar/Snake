import turtle
import random
import time

curr_score = 0
high_score = 0
delay = 0.1

window = turtle.Screen()
window.title("Snake Maze")
window.bgcolor("blue")
window.setup(width=600, height=600)

snake = turtle.Turtle()
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(0, 0)
snake.direction = "up"

food = turtle.Turtle()
shapes = random.choice(('triangle', 'circle'))
food.shape(shapes)
food.color("red")
food.speed(0)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Your Score: 0 Highest Score: 0", align="center")
font = ("Arial", 25, "normal")


def move_left():
    if snake.direction != "right":
        snake.direction = "left"


def move_right():
    if snake.direction != "left":
        snake.direction = "right"


def move_up():
    if snake.direction != "down":
        snake.direction = "up"


def move_down():
    if snake.direction != "up":
        snake.direction = "down"


def move():
    if snake.direction == "up":
        coord_y = snake.ycor()
        snake.sety(coord_y + 20)

    if snake.direction == "left":
        coord_x = snake.xcor()
        snake.setx(coord_x - 20)

    if snake.direction == "down":
        coord_y = snake.ycor()
        snake.sety(coord_y - 20)

    if snake.direction == "right":
        coord_x = snake.xcor()
        snake.setx(coord_x + 20)


window.listen()
window.onkeypress(move_left, 'a')
window.onkeypress(move_up, 'w')
window.onkeypress(move_down, 's')
window.onkeypress(move_right, 'd')

segments = []

while True:
    window.update()
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "Stop"
        snake.shape("square")
        snake.color("green")

        for segment in segments:
            segment.goto(1000, 1000)
            segments.clear()
            curr_score = 0
            delay = 0.1
            pen.clear()
            pen.write("Player's score: {} Highest score: {}".format(curr_score, high_score), align="center",
                      font=("Arial", 24, "normal"))

    if snake.distance(food) < 20:
        coord_x = random.randint(-270, 270)
        coord_y = random.randint(-270, 270)
        food.goto(coord_x, coord_x)

        added_segment = turtle.Turtle()
        added_segment.speed(0)
        added_segment.shape("square")
        added_segment.color("white")
        added_segment.penup()
        segments.append(added_segment)
        delay -= 0.001
        curr_score += 5

        if curr_score > high_score:
            high_score = curr_score
            pen.clear()
            pen.write("Player's score: {} Highest score: {}".format(curr_score, high_score), align="center",
                      font=("Arial", 24, "normal"))

    for i in range(len(segments) - 1, 0, -1):
        coord_x = segments[i - 1].xcor()
        coord_y = segments[i - 1].ycor()
        segments[i].goto(coord_x, coord_y)

    if len(segments) > 0:
        coord_x = snake.xcor()
        coord_y = snake.ycor()
        segments[0].goto(coord_x, coord_y)
    move()

    for segment in segments:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"
            snake.color("white")
            snake.shape("square")

            for segment in segments:
                segment.goto(1000, 1000)
                segment.clear
                curr_score = 0
                delay = 0.1
                pen.clear()
                pen.write("Player's score: {} Highest score: {}".format(curr_score, high_score), align="center",
                          font=("Arial", 24, "normal"))

    time.sleep(delay)

turtle.mainloop()


