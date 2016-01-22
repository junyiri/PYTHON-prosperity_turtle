import turtle
wn = turtle.Screen()
jimmy = turtle.Turtle()

wn.screensize(600,600)

def smallline(a,b,c,d):
    jimmy.width(5)
    jimmy.up()
    jimmy.setpos(a,b)
    jimmy.down()
    jimmy.seth(c)
    jimmy.forward(d)

def xin():
    smallline(200,230,315,10) #dian
    smallline(185,215,0,40) #heng
    smallline(195,210,310,10) #dian
    smallline(215,210,245,15) #dian
    smallline(185,195,0,40) #heng
    smallline(190,185,0,30) #heng
    smallline(205,195,270,40) #shu
    smallline(205,155,135,10) #gou
    smallline(195,175,225,10) #dian
    smallline(215,175,315,10) #dian
    smallline(260,225,202.5,25) #pie
    smallline(235,213,262.5,55) #pie
    smallline(232,195,0,30) #heng
    smallline(250,195,270,45)
    
xin()
