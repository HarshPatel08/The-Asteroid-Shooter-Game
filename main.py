##########################################################Name: Harsh Patel
#Game Name: Astrofire
#Purpose: Shoot down dangers
#########################################################

from tkinter import *
from math import *
from time import*
from random import*

numastdiff = 8

astspeed1 = 1.9

astspeed2 = 2.9



#BACKGROUND
root = Tk()
screen = Canvas( root, width = 600, height = 600, background = "black" )
screen.pack()


#IMAGES
attackship = PhotoImage(file = "Attackship.gif")

bullet = PhotoImage(file = "BulletGIF.gif")

asteroid = PhotoImage(file = "ASTEROIDGIF.gif")

heart = PhotoImage(file = "HEARTGIF.gif")

space = PhotoImage(file = "SPACEGIFACTUAL.gif")

screen.create_image(300,300, image = space)

#CREATE INTRO SCREEN
def drawintro():
  global title, play, playbox
  
  title = screen.create_text( 300, 200, text= "ASTEROFIRE", font= "Times 40 bold", fill = "red")

  play = screen.create_text( 300, 300, text= "PLAY", font= "Times 40 bold", fill = "black")

  playbox = screen.create_rectangle(270, 270, 330, 330)

  

  

#CREATES ATTACK SHIP
def createattackship():
  global attackshipx, attackshipy, attackship, theattackship

  theattackship = screen.create_image(attackshipx, attackshipy, image = attackship)

#INITAL VALUES
def setinitalvalues():
  global attackshipx, attackshipy, attackspeedx, attackspeedy, maxspeed, bullets, bulletsx, bulletsy, bulletspeed, asteroids, asteroidsx, asteroidsy, asteroidspeed, asteroidnumber, lives, asteroiddestroyed, score, Qpressed, explosionhappenning, numparticles, temporary, hearts, heartsx, heartsynumastdiff, astspeed1, astspeed2, gamerunning



  explosionhappenning = False

  numparticles = 50

  temporary = 0


  attackshipx = 300
  attackshipy = 550

  lives = 3

  hearts = [0,0,0]
  heartsx = [50, 120, 190]
  
  score = 0
  Qpressed = False
  gamerunning = False
  
  attackspeedx = 0
  attackspeedy = 0

  maxspeed = 4.5

  bullets = []
  bulletsx = []
  bulletsy = []
  bulletspeed = 10

  asteroids = []
  asteroidsx = []
  asteroidsy = []
  asteroidspeed = []
  asteroidnumber = numastdiff


  
  for i in range(asteroidnumber):
    asteroidsx.append(randint(30,570))
    asteroidsy.append(randint(-10, -8))      
    # asteroidspeed.append(randint(1,2))
    asteroidspeed.append(uniform(0.9,1.9))
    asteroids.append(0)


#UPDATES AND CREATES EACH EXPLOSION PARTICLE
def updateexplosion():
  global numparticles, particlex, particley, particlespeedx, particlespeedy, particlesize, particlecolours,particles, explosionhappenning, temporary

  if explosionhappenning == True:

  
    for i in range( numparticles ):
      particles[i] = screen.create_oval( particlex[i],   particley[i], particlex[i] +particlesize[i],       particley[i] +particlesize[i], fill=particlecolours[i])
      
      particlex[i] = particlex[i] + particlespeedx[i]
      particley[i] = particley[i] + particlespeedy[i]

    temporary = temporary + 1

    if temporary > 7:
      explosionhappenning = False
      temporary = 7

    
    
#TAKES X AND Y OF ASTEROIDS AND STARTS SETTING VALUES FOR EACH EXPLOSION PARTICLE
def createexplosion(x,y):
  global numparticles, particlex, particley, particlespeedx, particlespeedy, particlesize, particlecolours,particles, explosionhappenning, temporary

  temporary = 0

  explosionhappenning = True

  numparticles = 20

  particlex = []
  particley = []
  particlespeedx = []
  particlespeedy = []
  particlesize = []
  particlecolours = []
  particles = []  


  for i in range( numparticles ):
    particlesize.append( randint(5, 10) )
    particlex.append( x )
    particley.append( y )
    particlespeedx.append( uniform(-8,8) ) 
    particlespeedy.append( uniform(-6,6) )
    particlecolours.append( choice(["orange", "red", "gray", "gray"])  )
    particles.append ( 0 )  
    

#DELETES THE EXPLOSION PARTICLES EACH TIME
def deleteexplosions():
  global numparticles, particles, explosionhappenning, temporary

  if explosionhappenning == True:
  
    for i in range( numparticles ):
      screen.delete( particles[i] )

#DELETES THE ENTIRE EXPLOSION
def eraseallexplosions():
  global numparticles, particles, explosionhappenning

  if temporary == 7:
    for i in range( numparticles ):
      screen.delete( particles[i] )



#RESETS ASTEROID IF DESTROYED OR OUT OF SCREEN
def resetasteroid():
  global asteroidsx, asteroidsy, asteroidspeed, asteroids

  asteroidsx.append(randint(30,570))
  asteroidsy.append(randint(-10, -5))
  asteroidspeed.append(randint(1,1))
  asteroids.append(0)


#"DELETES" ASTEROIDS OUT OF SCREEN
def outofscreenasteroids():
  global asteroidsx, asteroidsy, asteroidspeed, asteroids

  for t in range(len(asteroidsy)):
    if 600 <= asteroidsy[t-1]:
      asteroidsx.pop(t-1)
      asteroidsy.pop(t-1)
      asteroids.pop(t-1)

      

      resetasteroid()


#UPDATES SCORE
def updatescoreasteroid():
  global score

  
  score = score + 1

#DRAWS SCORE
def createscore():
  global score, newscore, scoreword, scorenumber

  newscore = str(score)

  scoreword = screen.create_text(510, 590, text = "Score:" , font = "Arial 18 bold", fill = "black")

  scorenumber = screen.create_text(580, 590, text = newscore , font = "Arial 18 bold", fill = "black")


#DELETES SCORE EACH FRAME
def deletescore():
  global score, newscore, scoreword, scorenumber

  screen.delete(scoreword)
  screen.delete(scorenumber)

      
#SUBTRACTS LIVES WHEN ATTACKSHIP HIT
def updatelives():
  global lives, lifenumber, livesword, hearts, heartsx
  
  lives = lives -1

  index = len(heartsx) - 1

  
  heartsx.pop(index)
  
  

  if lives <= 0:

    

    stopGame()

#DRAWS LIVES COUNTER
def createlivescounter():
  global lives, lifenumber, livesword, hearts, heartsx

  
  for i in range(len(heartsx)):
    hearts[i] = screen.create_image(heartsx[i], 575, image = heart)
  

#DELETES LIVES COUNTER EACH FRAME
def deletelivescounter():
  global lifenumber, lives, livesword, hearts, heartsx

  for i in range(len(heartsx)):
    screen.delete(hearts[i])
    


#CHECKS FOR ASTEROID COLLISION WITH ATTACKSHIP
def checkattackshipcollision():
  global asteroids, asteroidsx, asteroidsy, asteroidnumber, theattackship, attackshipx, attackshipy

  for i in range(len(asteroids)):
    distX = asteroidsx[i-1] - attackshipx
    distY = asteroidsy[i-1] - attackshipy
    totaldistance = sqrt(distX **2 + distY **2)

    inputofx = asteroidsx[i-1]
    inputofy = asteroidsy[i-1]

    if totaldistance < 50:
      asteroids.pop(i-1)
      asteroidsx.pop(i-1)
      asteroidsy.pop(i-1)

      resetasteroid()

      createexplosion(inputofx, inputofy)

      updatescoreasteroid()
      
      updatelives()
  

#CHECKS FOR BULLET COLLISION WITH ASTEROIDS
def checkbulletcollision():
  global asteroids, asteroidsx, asteroidsy, asteroidnumber, bullets, bulletsx, bulletsy, distance

  for i in range(len(asteroidsy)):
    for t in range(len(bulletsy)):


      disX = asteroidsx[i-1] - bulletsx[t-1]
      disY = asteroidsy[i-1] - bulletsy[t-1]
      distance = sqrt(disX **2 + disY **2)

      

      if distance < 30:
        inputx = asteroidsx[i-1]
        inputy = asteroidsy[i-1]
        
        bulletsy.pop(t-1)
        bulletsx.pop(t-1)
        bullets.pop(t-1)
        asteroids.pop(i-1)
        asteroidsx.pop(i-1)
        asteroidsy.pop(i-1)

        createexplosion(inputx, inputy)

        
        resetasteroid()

        updatescoreasteroid()
        
        print(inputx)
        print(asteroidsx[i])
        
                           
                           
#UPDATES ALL ASTERIOD POSITIONS
def updateasteriods():
  global asteroids, asteroidsx, asteroidsy, asteroidspeed, asdteroidnumber

  

  for i in range(len(asteroidsy)):
    asteroidsy[i] = asteroidsy[i] + asteroidspeed[i]
    outofscreenasteroids()

#DRAWS ALL ASTERIODS
def drawasteroids():
  global asteroids, asteroidsx, asteroidsy, asteroidspeed, asteroidnumber

  for i in range(len(asteroidsy)):
    asteroids[i] = screen.create_image(asteroidsx[i], asteroidsy[i], image = asteroid)

#DELETES ALL ASTERIODS 
def deleteasteroids():
  global asteroids, asteroidsx, asteroidsy, asteroidspeed, asteroidnumber

  for i in range(len(asteroidsy)):
    screen.delete(asteroids[i])
    
#MOUSE CLICK HANDLER
def mouseClickHandler( event ):
  spawnnewbullet()

#FINDS X AND Y FOR BULLETS 
def spawnnewbullet():
  
  global bullets, bulletsx, bulletsy, attackshipx, attackshipy

  bulletsx.append(attackshipx)
  bulletsy.append(attackshipy)
  bullets.append(0)

#UPDATES THE BULLETS POSITION EACH FRAME
def updateBulletposition():
  global bullets, bulletsx, bulletsy, bulletspeed

  for i in range(len(bullets)):
    bulletsy[i-1] = bulletsy[i-1] - bulletspeed
    offscreenbullets()

#DELETES BULLETS OFF SCREEN
def offscreenbullets():
  global bullets, bulletsx, bulletsy
  
  for t in range(len(bulletsy)):
    if 0 >= bulletsy[t-1]:
      bulletsy.pop(t-1)
      bulletsx.pop(t-1)
      bullets.pop(t-1)

      print("Deleted Bullet")

      
#CHECKS IF ATTACK SHIP IS OUT OF BOUNDS
def checkbounds():
  global attackshipx, attackshipy, attackspeedx, attacksppedy

  if attackshipx <= 30:
    attackshipx = 30

  elif attackshipx >= 570:
    attackshipx = 570


  if attackshipy <= 30:
    attackshipy = 30

  elif attackshipy >= 570:
    attackshipy = 570
    
      
#DRAWS BULLETS
def drawBullets():
  global bullets, bulletsx, bulletsy

  for x in range (len(bulletsy)):
    bullets[x] = screen.create_image(bulletsx[x], bulletsy[x] - 20, image = bullet)

#DELETES THE BULLETS
def deleteBullets():
  global bullets, bulletsx, bulletsy
  
  for c in range(len(bulletsy)):
    screen.delete(bullets[c])


#KEY HANDLER
def keyDownHandler( event ):
  global attackspeedx, attackspeedy, maxspeed, Qpressed
  
  if event.keysym == "Left":     
    attackspeedx = -1 * maxspeed
      
  elif event.keysym == "Right":  
    attackspeedx = maxspeed

  elif event.keysym == "Up":     
    attackspeedy = -1 * maxspeed

  elif event.keysym == "Down":   
    attackspeedy = maxspeed

  elif event.keysym == "space":   
    spawnnewbullet()

  elif event.keysym == "q" or event.keysym == "Q":
    Qpressed = True

  else:
    print("Nothing happens")

    
#KEYUP HANDLER
def keyUpHandler( event ):
  global attackspeedx, attackspeedy

  if event.keysym in ["Left", "Right"]:
    attackspeedx = 0

  elif event.keysym in ["Up", "Down"]:
    attackspeedy = 0


#UPDATE ATTACKSHIP POSITION
def updateattackship():
  global attackspeedx, attackspeedy, attackshipx, attackshipy

  
  attackshipy = attackshipy + attackspeedy
  attackshipx = attackshipx + attackspeedx

  checkbounds()

#STOPS THE GAME AND CHECKS THE SCORE
def stopGame():
    screen.delete(theattackship)
    deleteBullets()
    deletescore()
    deleteasteroids()
    deletelivescounter()
    screen.create_text( 300, 300, text= "YOU'RE DONE!", font= "Times 40", fill = "black")
  
    screen.create_text(290, 350, text = "Score:" , font = "Arial 30", fill = "black")

    screen.create_text(390, 350, text = newscore , font = "Arial 30", fill = "black")
    screen.update()
    sleep(2)
    root.destroy()


  
#RUN GAME DEF (RUNS THE ENTIRE GAME WITH FUNCTIONS MADE)
def runGame():

  setinitalvalues()
  while Qpressed == False:
    updateattackship()
    updateBulletposition()
    updateasteriods()
    checkbulletcollision()
    checkattackshipcollision()
    createattackship()
    drawBullets()
    drawasteroids()
    createlivescounter()
    createscore()
    updateexplosion()
    screen.update()
    sleep(0.01)
    screen.delete(theattackship)
    deleteBullets()
    deletescore()
    deleteasteroids()
    deletelivescounter()
    deleteexplosions()
    eraseallexplosions()

  stopGame()

#ACTUALLY RUNS THE GAME
root.after( 0, runGame )

#BINDS THE BUTTONS
screen.bind("<Button-1>", mouseClickHandler)
screen.bind( "<Key>", keyDownHandler )
screen.bind( "<KeyRelease>", keyUpHandler )

screen.pack()
screen.focus_set()
root.mainloop()
  