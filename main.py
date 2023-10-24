

import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Beginner's Maze")
wn.setup(700, 700)
wn.tracer(0)

#Register shapes
wn.register_shape("wizzr-1.gif")
wn.register_shape("wizzl-1.gif")
wn.register_shape("wall-1.gif")
wn.register_shape("loot-1.gif")
wn.register_shape("enemy.gif")


# def function

def game():
#Create Blocks
  class Blocks(turtle.Turtle):
      def __init__(self):
          turtle.Turtle.__init__(self)
          self.shape("wall-1.gif")
          self.shape("square")
          self.color("white")
          self.penup()
          self.speed(0)


  class Player(turtle.Turtle):
      def __init__(self):
          turtle.Turtle.__init__(self)
          self.shape("wizzr-1.gif")
          self.color("red")
          self.penup()
          self.speed(0)
          self.gold = 100

      def go_up(self):
            
          #Calculate the spot to move to
          move_to_x = player.xcor()
          move_to_y = player.ycor() + 24

        #Check if the space has a wall
          if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

      def go_down(self):
            
          #Calculate the spot to move to
          move_to_x = player.xcor()
          move_to_y = player.ycor() - 24

          #Check if the space has a wall
          if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)


      def go_left(self):
            
          #Calculate the spot to move to
          move_to_x = player.xcor() - 24
          move_to_y = player.ycor()

          self.shape("wizzl-1.gif")

          #Check if the space has a wall
          if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

      def go_right(self):
            
          #Calculate the spot has a wall
          move_to_x = player.xcor() + 24
          move_to_y = player.ycor()

          self.shape("wizzr-1.gif")

          #Check if the space has a wall
          if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

        
      def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b **2) )

        if distance <5:
          return True
        else:
          return False

  class Treasure(turtle.Turtle):
    def __init__(self, x, y):
      turtle.Turtle.__init__(self)
      self.shape("loot-1.gif")
      self.color("gold")
      self.penup()
      self.speed(0)
      self.gold = 0
      self.goto(x, y)

    def destroy(self):
      self.goto(2000,2000)
      self.hideturtle()

  class Enemy(turtle.Turtle):
      def __init__(self, x, y):
          turtle.Turtle.__init__(self)
          self.shape("enemy.gif")
          self.color("green")
          self.penup()
          self.speed(0)
          self.gold = 25
          self.goto(x, y)
          self.direction = random.choice(["up", "down", "left", "right"] )   
      def move(self):
          if self.direction == "up":
              dx = 0
              dy = 24
          elif self.direction == "down":
              dx = 0
              dy = -24
          elif self.direction == "left":
              dx = -24
              dy = 0
              self.shape("enemy.gif")
          elif self.direction == "right":
              dx = 24
              dy = 0

          else:
              dx = 0
              dy = 0

          #Check if player is close 
          #If so, follow the player
          if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

          #Calculate the spot to move to
          move_to_x = self.xcor() + dx
          move_to_y = self.ycor() + dy

          #Calculate if the space has a wall
          if (move_to_x, move_to_y) not in walls:
              self.goto(move_to_x, move_to_y)
          else:
              #Choose a different direction
              self.direction = random.choice(["up", "down", "left", "right"])

          #Set timer to move next time
          turtle.ontimer(self.move, t=random.randint(100, 300))

      def is_close(self, other):
          a = self.xcor()-other.xcor()
          b = self.ycor()-other.ycor()
          distance = math.sqrt((a ** 2) + (b ** 2))

          if distance < 75:
              return True
          else:
              return False

      def destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()
            

  #Create levels list
  levels = []

  #Define first level
  level_1 = [
      "XXXXXXXXXXXXXXXXXXXXXXXXX",
      "XP XXXXXXXE         XXXXX",
      "X  XXXXXXX  XXXXXX  XXXXX",
      "X       XX  XXXXXX  XXXXX",
      "X       XX  XXX       EXX",
      "XXXXXX  XX  XXX        XX",
      "XXXXXX  XX  XXXXXX  XXXXX",
      "XXXXXX  XX    XXXX  XXXXX",
      "X  XXX        XXXXT XXXXX",
      "X  XXX  XXXXXXXXXXXXXXXXX",
      "X         XXXXXXXXXXXXXXX",
      "X                XXXXXXXX",
      "XXXXXXXXXXXX     XXXXX  X",
      "XXXXXXXXXXXXXXX  XXXXX  X",
      "XXX  XXXXXXXXXX         X",
      "XXXE                    X",
      "XXX         XXXXXXXXXXXXX",
      "XXXXXXXXXX  XXXXXXXXXXXXX",
      "XXXXXXXXXX              X",
      "XXXXXXXXXX              X",
      "XXXXXXXXXXXXXXXXXX  XXXXX",
      "XXXXXXXXXXXXXXXXXX  XXXXX",
      "XXXXXXXXXXXXXXXXXXXXXXXXX",  
      ]

  level_4 = [
      "XXXXXXXXXXXXXXXXXXXXXXXXX",
      "X                       X",
      "X P                    TX",
      "XXXXXXXXXXXXXXXXXXXXXXXXX",
      ]

  level_3 = [
      "XXXXXXXXXXXXXXXXXXXXXXXXX",
      "X P                     X",
      "XXXXXXXXXXXXXXXXXXXXXX  X",
      "XXXXXXXXXXXXXXXXXXXXXX  X",
      "XXXXXXXXXXXXXXXXXXXXXX  X",
      "X                       X",
      "X XXXXXXXXXXXXXXXXXXXXXXX",
      "X                       X",
      "X                       X",
      "XXXXXXXXXXXXXXXXXXXXXX  X",
      "XXXXXXXXXXXXXXXXXXXXXX  X",
      "XXXXXXXXXXXXXXXXXXXXXX  X",
      "XT                      X",
      "XXXXXXXXXXXXXXXXXXXXXXXXX",
  ]

  level_2 = [
      "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
      "X                  E      X",
      "X X X X X X X X X X X X X X",
      "X                         X",
      "X X X X X X X X X X X X X X",
      "X                    E    X",
      "XPX X X X X X X X X X X X X",
      "X                         X",
      "X X X X X X XTX X X X X X X",
      "X                         X",
      "X X X X X X X X X X X X X X",
      "X              E          X",
      "X X X X X X X X X X X X X X",
      "X      E                  X",
      "X X X X X X X X X X X X X X",
      "X  E                 E    X",
      "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
   ]
  
#Add maze to mazes list
  levels.append(level_1)
  levels.append(level_2)
  levels.append(level_3)
  levels.append(level_4)
  #Add maze to treasures list
  treasures = []

  #Add enemies list
  enemies = []
  for enemy in enemies:
      turtle.ontimer(enemy.move, t=250)
  #Create Level Setup Function
  def setup_maze(level):
      for y in range(len(level)):
          for x in range(len(level[y])):
              #Get the character at each x,y coordinate
              #NOTE the order of y and x in the next line
              character = level[y][x]
              #Calculate the screen x, y coordinates
              screen_x = -300 + (x * 24)
              screen_y = 197 - (y * 24)
                

              #Check if it is an X (representing a wall)
              if character == "X":
                  blocks.goto(screen_x, screen_y)
                  blocks.shape("wall-1.gif")
                  blocks.stamp()
                  #Add coordinates to wall list
                  walls.append((screen_x, screen_y))
              #Check if it is a P (representing the player)
              elif character == "P":
                player.goto(screen_x, screen_y)
                
              #Check if it is a T (representing treasure)
              elif character == "T":
                treasures.append(Treasure(screen_x, screen_y))
              
              #Check if it is an E (representing Enemy)
              elif character == "E":
                enemies.append(Enemy(screen_x, screen_y))

  
  #Create class instances
  blocks = Blocks()
  player = Player()
  #Create wall coordinate list
  walls = []
  f=0
  #Set up the level
  setup_maze(levels[f]) 
  maze="level1"
  #Keyboard Binding
  turtle.onkey(player.go_left,"a")
  turtle.onkey(player.go_right,"d")
  turtle.onkey(player.go_up,"w")
  turtle.onkey(player.go_down,"s")
  wn.listen()

  #Turn off screen updates
  wn.tracer(0)
  
  
  #Start moving enemies
  #for enemy in enemies:
      #turtle.ontimer(enemy.move, t=250)

  
  #Main Game LookupError
  while True:
    #Check for player collision with treasure
    #Iterate through treasure list
    for treasure in treasures:
      if player.is_collision(treasure):
        #Add the treasure gold to the player gold
        player.gold += treasure.gold
        print("Player Gold: {}".format(player.gold))
        #Destroy the treasure
        for enemyz in enemies:
          enemyz.destroy()
        walls.clear()
        enemies.clear()
        treasure.destroy()
        #Remove the treasure from the treasures list
        treasures.remove(treasure)
        wn.clear()
        wn.bgcolor("black")
        player = Player()
        f= f + 1
        blocks.clear()
        setup_maze(levels[f])
        maze = "level2" 
                                  

    for treasure in treasures:
      if player.is_collision(treasure):
        #Add the treasure gold to the player gold
        player.gold += treasure.gold
        print("Player Gold: {}".format(player.gold))
        #Destroy the treasure
        for enemyz in enemies:
          enemyz.destroy()
        walls.clear()
        enemies.clear()
        treasure.destroy()
        #Remove the treasure from the treasures list
        treasures.remove(treasure)
        wn.clear()
        wn.bgcolor("black")
        player = Player()
        f= f + 1
        blocks.clear()
        setup_maze(levels[f])
        maze = "level3"
    

    for treasure in treasures:
      if player.is_collision(treasure):
        #Add the treasure gold to the player gold
        player.gold += treasure.gold
        print("Player Gold: {}".format(player.gold))
        
        #Destroy the treasure
        for enemyz in enemies:
          enemyz.destroy()
        walls.clear()
        enemies.clear()
        treasure.destroy()
        #Remove the treasure from the treasures list
        treasures.remove(treasure)
        wn.clear()
        wn.bgcolor("black")
        player = Player()
        f= f + 1
        blocks.clear()
        setup_maze(levels[f])
        maze = "level4"

      turtle.onkey(player.go_left,"a")
      turtle.onkey(player.go_right,"d")
      turtle.onkey(player.go_up,"w")
      turtle.onkey(player.go_down,"s")

      for enemy in enemies:
       #turtle.ontimer(enemy.move, t=250)
       turtle.onkey(player.go_left,"a")
       turtle.onkey(player.go_right,"d")
       turtle.onkey(player.go_up,"w")
       turtle.onkey(player.go_down,"s")
       wn.listen()
          
      #Iterate through enemy list to see if the player collides
    for enemy in enemies:
      if player.is_collision(enemy):
        print ("Player died!")
        wn.clear()
        wn.bgcolor("black")
        game()

        #walls.clear()
        #blocks.clear()
        for enemy in enemies:
          enemy.destroy(enemy)
        for treasure in treasures:
          treasure.destroy(treasure)
        

      else: 
        pass
        
    #Update screen
    wn.update()

game()