import turtle
import math
import winsound
import random

#Moving the Player
playerspeed = 15
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #Declare bulletstate as global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)

def inCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 20:
        return True
    else:
        return False

#Start Up Command
start = input("Welcome to Space Invaders! Press Enter to begin!")

#Setting Up Screen
screen = turtle.Screen()
screen.screensize(1000, 1000)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.bgpic("space_invaders_background.gif")

#Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")
turtle.register_shape("congrats.gif")

#WinningScene
congrats = turtle.Turtle()
congrats.hideturtle()
congrats.shape("congrats.gif")
congrats.shapesize(5, 5)

#Draw a Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
   border_pen.fd(600)
   border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
score_pen.hideturtle()

#Create Player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

#Choose a number of enemies
num_enemies = 5
#Create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(num_enemies):
    #Create the Enemy
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

#Create the player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.25, 0.25)
bullet.hideturtle()
bulletspeed = 20



#Define bullet state
bulletstate = "ready"
#ready - ready to fire
#fire - moving straight

#Check if bullet has reached the top
if bullet.ycor() > 275:
    bullet.hideturtle()
    bulletstate = "ready"


#Keyboard Bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Main Game Loop
while True:
    for enemy in enemies:
        #Moving the Enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Moving the Enemy side to side and down
        if enemy.xcor() > 280:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1
        if enemy.xcor() < -280:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1
        #Check for Collision
        if inCollision(bullet, enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #Update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))

        if inCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            print("Game Over")
            break
        if score >= 1000:
            congrats.showturtle()
            print("Congrats! You've defeated the Invaders!")
            break

    #Moving the Bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    #Check if bullet has reached the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"


turtle.mainloop()
