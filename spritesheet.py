from Pygame_functions import*

screenSize(800,800)
setBackgroundColour("dark green")
testSprite = makeSprite("assets\Warrior\SpriteSheet\Warrior_SheetnoEffect.png",6)

moveSprite(testSprite,300,300,True)
showSprite(testSprite)


nextFrame = clock()

frame=0

while True:
    if clock() > nextFrame:
        frame = (frame+1)%6
        nextFrame += 120     # vitesse d'animation

    if keyPressed("right"):
        changeSpriteImage(testSprite, 0*8+frame)

    tick(60)

endWait()
