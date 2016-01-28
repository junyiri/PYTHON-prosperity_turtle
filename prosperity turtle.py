import turtle
wn = turtle.Screen()
jimmy = turtle.Turtle()

wn.screensize(600,600)
wn.bgcolor("#F8E392")

jimmy.speed(20)

def smallline(a,b,c,d):
    jimmy.width(5)
    jimmy.pencolor("black")
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
    
xin()
nian()
kuai()
le()
