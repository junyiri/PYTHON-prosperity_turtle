import turtle
wn = turtle.Screen()
jimmy = turtle.Turtle()

wn.screensize(600,600)
wn.bgcolor("#F8E392")

def smallline(a,b,c,d):
    jimmy.width(5)
    jimmy.pencolor("black")
    jimmy.speed(30)
    jimmy.up()
    jimmy.setpos(a,b)
    jimmy.down()
    jimmy.seth(c)
    jimmy.forward(d)

def largeline(a,b,c,d):
    jimmy.width(8)
    jimmy.pencolor("black")
    jimmy.speed(8)
    jimmy.up()
    jimmy.setpos(a,b)
    jimmy.down()
    jimmy.seth(c)
    jimmy.forward(d)

def line(a,b):
    jimmy.width(3)
    jimmy.pencolor("#F9D139")
    jimmy.up()
    jimmy.setpos(a,b)
    jimmy.down()
    jimmy.seth(0)
    jimmy.forward(520)

def xin():
    smallline(200,225,315,10) #dian
    smallline(185,210,0,40) #heng
    smallline(195,205,310,10) #dian
    smallline(215,205,245,15) #dian
    smallline(185,190,0,40) #heng
    smallline(190,180,0,30) #heng
    smallline(205,190,270,40) #shu
    smallline(205,150,135,10) #gou
    smallline(195,170,225,10) #dian
    smallline(215,170,315,10) #dian
    smallline(260,220,202.5,25) #pie
    smallline(235,208,262.5,55) #pie
    smallline(232,190,0,30) #heng
    smallline(250,190,270,45) #shu

def nian():
    smallline(200,105,240,25) #pie
    smallline(198,95,0,60) #heng
    smallline(210,68,0,40) #heng
    smallline(210,68,270,20) #shu
    smallline(190,48,0,70) #heng
    smallline(230,95,270,75) #shu

def kuai():
    smallline(193,-65,235,10) #dian
    smallline(197,-55,315,10) #dian 
    smallline(195,-30,270,80) #shu
    smallline(213,-55,0,40) #heng
    smallline(253,-55,270,22) #zhe
    smallline(210,-80,0,50) #heng
    smallline(233,-30,270,50) #pie1
    smallline(233,-80,245,35) #pie2
    smallline(233,-80,305,40) #na

def le():
    smallline(250,-155,195,50) #pie
    smallline(202,-167,270,28) #shu
    smallline(202,-195,0,50) #heng
    smallline(230,-175,270,65) #shu
    smallline(230,-240,145,10) #gou
    smallline(215,-210,225,20) #dian
    smallline(240,-210,315,20) #dian


def wan():
    smallline(-250,220,0,60) #heng
    smallline(-222,220,250,65) #pie
    smallline(-230,200,0,30) #heng
    smallline(-200,200,270,45) #zhe
    smallline(-200,155,135,10) #gou

def shi():
    smallline(-250,105,0,50) #heng
    smallline(-245,95,270,15) #shu
    smallline(-245,95,0,40) #heng
    smallline(-205,95,270,15) #zhe
    smallline(-245,80,0,40) #heng
    smallline(-245,70,0,40) #heng
    smallline(-205,70,270,20) #zhe
    smallline(-250,60,0,50) #heng
    smallline(-245,50,0,40) #heng
    smallline(-225,110,270,80) #shu
    smallline(-225,30,135,10) #gou

def ru():
    smallline(-235,-30,247.5,55) #pie
    smallline(-255,-82,315,25) #zhe
    smallline(-225,-50,247.5,55) #pie
    smallline(-255,-62,0,25) #heng
    jimmy.up()
    jimmy.setpos(-220,-70)
    jimmy.seth(0)
    jimmy.down()
    for x in range(0,4):
        jimmy.forward(20)
        jimmy.right(90) #kou

def yi():
    smallline(-233,-145,315,8) #dian
    smallline(-260,-155,0,60) #heng
    smallline(-243,-160,315,8) #dian
    smallline(-217,-160,225,8) #dian
    smallline(-260,-170,0,60) #heng
    jimmy.up()
    jimmy.setpos(-247.5,-177.5)
    jimmy.seth(0)
    jimmy.down()
    for x in range(0,2):
        jimmy.forward(35)
        jimmy.right(90)
        jimmy.forward(20)
        jimmy.right(90) #kou
    smallline(-245,-187.5,0,30) #heng
    smallline(-255,-210,225,8) #dian
    smallline(-205,-210,315,8) #dian
    smallline(-247.5,-210,270,15) #shu
    smallline(-247.5,-225,0,35) #zhe
    smallline(-212.5,-225,90,5) #gou
    smallline(-232,-207,315,8)


def square():
    jimmy.width(2)
    jimmy.speed(12)
    jimmy.color("red","red")
    jimmy.up()
    jimmy.setpos(0,150)
    jimmy.down()
    jimmy.seth(225)
    jimmy.begin_fill()
    for x in range(0,4):
        jimmy.forward(212.13)
        jimmy.left(90)
    jimmy.end_fill()

def sqwd():
    largeline(-50,70,0,100) #heng
    largeline(-30,43,0,60) #heng
    largeline(-55,16,0,110) #heng
    largeline(0,100,270,85) #pie1
    largeline(0,15,220,75) #pie2
    largeline(0,15,320,75) #na
    jimmy.up()
    jimmy.setpos(-25,-75)
    jimmy.down()
    jimmy.circle(40) #kou
    largeline(-38,-45,0,80)

def border():
    line(-260,250)
    line(-260,-270)

    
xin()
nian()
kuai()
le()

wan()
shi()
ru()
yi()

square()
sqwd()

border()



