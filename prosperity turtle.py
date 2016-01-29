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
    smallline(230,-235,145,10) #gou
    smallline(215,-210,225,20) #dian
    smallline(240,-210,315,20) #dian

def wan():
    smallline(-250,220,0,60) #heng
    smallline(-222,220,250,65) #pie
    smallline(-230,200,0,30) #heng
    smallline(-200,200,270,45) #zhe
    smallline(-200,155,135,10) #gou

def square():
    jimmy.width(2)
    jimmy.speed(10)
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
    




xin()
nian()
kuai()
le()

wan()

square()
sqwd()

'''jimmy.up()
jimmy.setpos(200,-150)
jimmy.down()
jimmy.pencolor("red")
jimmy.stamp()'''

