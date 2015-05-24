from Tkinter import *
import random

#(197, 159)
root = Tk()
root.title('Behemoth!')

canvas = Canvas(root)
canvas.config(width=800,height=640,bg='dim gray')


istanbul = PhotoImage(file='Istanbul.gif')
playerimg = PhotoImage(file='airship-h.gif')
wallimg = PhotoImage(file='Wall.gif')
keyimg = PhotoImage(file='Key.gif')



global player
global has_key
global gravity
global speed

has_key = False
gravity = 1
speed = 1
player = canvas.create_image(110,550,image=playerimg)


canvas.create_image(400,320,image=istanbul)



def win():
    root.destroy()
    
    win = Tk()
    win.config(bg='gray')
    win.title('You\'ve won!')
    win.geometry("%dx%d%+d%+d" % (300, 200, 250, 125))
    
    winlabel = Label(win,text='You Win!',bg='gray').pack()
    
    
    win.mainloop()



def loss():
    losswindow = Toplevel(bg='gray')
    losswindow.title('You Lose!')


    losslabel = Label(losswindow,text="You Lose!",bg='gray').pack()
    
    losswindow.geometry("%dx%d%+d%+d" % (300, 200, 250, 125))
   
   
    losswindow.mainloop()
    


def playerloop():
    global player    
    global has_key
    global key
    global gravity
    global speed
    
    x,y = canvas.winfo_pointerxy()
    x = canvas.canvasx(x)
    y = canvas.canvasx(y)
    
    
    playerbbox = canvas.bbox(player)
    canvasarea = canvas.find_overlapping(*playerbbox)

    if len(canvasarea) < 100: 
        if canvas.coords(player)[0] < x-5:
            canvas.move(player,1,0)
            gravity = -.04
            speed = .5
            
            
            
        elif canvas.coords(player)[0] > x-5:
            canvas.move(player,-1,0)
            gravity = -.04
            speed = .5
            
            
        elif canvas.coords(player)[1] < y-50:
            canvas.move(player,0,gravity)
            gravity += .04
            speed = .5
       
        elif canvas.coords(player)[1] > y-50:
            canvas.move(player,0,speed)
            speed -= .04
            gravity = .5
    

    else:
        loss()

        
        
    
   
    if canvasarea == (1,2) and has_key == True:
        win()
    elif len(canvasarea) > 1 and canvasarea != (1,2792) and canvasarea != (1,2):
        loss()
        
    elif canvasarea == (1,2792):
        has_key = True
        canvas.delete(key)
    elif canvasarea == (1,2) and has_key == False:
        needkey= Toplevel(bg='gray')
        
        needkey.title('Oops!')


        losslabel = Label(needkey,text="You tried to enter without the key!",bg='gray').pack()
    
        needkey.geometry("%dx%d%+d%+d" % (300, 200, 250, 125))
   
   
        needkey.mainloop()
        
        
        
    root.after(1,playerloop)
    





def makewalls():   
    for num in range(0,620):
        canvas.create_image(800,num,image=wallimg)
        num += 75
    
    for num2 in range(0,620):
        canvas.create_image(0,num2,image=wallimg)
        num2 += 75
    
    for num3 in range(0,770):
        canvas.create_image(num3,640,image=wallimg)
        num3 += 75
    for num4 in range(0,770):
        canvas.create_image(num4,0,image=wallimg)
        num4 += 75

    


def printcoords(event):
    print canvas.coords(player)    
def makeobstacles():
    global key
    a = canvas.create_rectangle(25,500,400,530,fill='dark gray')
    b = canvas.create_rectangle(500,180,530,615,fill='dark gray')
    c = canvas.create_rectangle(120,400,530,430,fill='dark gray')
    d = canvas.create_rectangle(120,100,150,400,fill='dark gray')
    e = canvas.create_rectangle(120,100,640,130,fill='dark gray')
    f = canvas.create_rectangle(640,100,670,550,fill='dark gray')
    g = canvas.create_rectangle(380,130,410,200,fill='dark gray')
    h = canvas.create_rectangle(250,200,410,230,fill='dark gray')
    i = canvas.create_rectangle(250,270,500,300,fill='dark gray')
    
    key = canvas.create_image(350,170,image=keyimg)
    


makewalls() 
makeobstacles()
playerloop()



root.bind("<Return>",printcoords)
    
    

    
canvas.pack()
root.mainloop()