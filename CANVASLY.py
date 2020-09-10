from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, colorchooser, filedialog
from pygame import mixer
root = Tk()
root.geometry('1280x800')
root.iconbitmap('C:/Users/DEVANSH/Downloads/logo bitmap.ico')
root.title('CANVASLY')

color_bg = 'white'
color_fg = 'black'
old_x = None
old_y = None
v1 = DoubleVar()
v2 = DoubleVar()

c1=Canvas(root, width=1920, height=1080,bg='black')
t = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/img.png'))
c1.create_image(0,-5,anchor=NW,image=t)
c1.place(x=0, y=0)
c = Canvas(root, width=1000, height=500, bg=color_bg)
c.place(x=0, y=130)
gif1 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/gif1.png'))
gif2 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/gif2.png'))
t1 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/text.png'))
t2 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/pen.png'))
t3 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/erase.png'))
t4 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/clear_screen.png'))
t5 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/resize.png'))
t6 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/fill.png'))
t7 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/magni.png'))
t8 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/zoomin.png'))
t9 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/zoomout.png'))
t10 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/win_size.png'))
t11 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/color.png'))
t12 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/brush _color.png'))
t13 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/circle.png'))
t14 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/rect.png'))
t15 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/line.png'))
t16 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/square.png'))
t17 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/vet_line.png'))
t18 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/slash.png'))
t19 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/dash.png'))
t20 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/hor_dash.png'))
t21 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/r_triangle.png'))
t22 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Downloads/a_triangle.png'))
a = b = 1
width = 1000
height = 500


def text():
    c.bind('<Button-1>', text_1)
    global canvas, t1


def pen():
    c.bind('<B1-Motion>', paint)
    c.bind('<ButtonRelease-1>', reset)


def erase():
    try:
        c.bind('<B3-Motion>', erase_s)
        c.bind('<ButtonRelease-3>', reset_s)
        erase_s(e=None)

    except:
        print('ef')


def clear():
    c.delete('all')


def ok():
    n1 = e1.get()
    n1 = int(n1)
    n2 = e2.get()
    n2 = int(n2)
    c.configure(width=n1, height=n2)


def cancel():
    r1.destroy()


def resize():
    global e1, e2, r1
    r1 = Toplevel(root)
    r1.geometry('200x200')
    labelframe = LabelFrame(r1, text="RESIZE ")
    labelframe.pack(fill="both", expand="yes")
    L1 = Label(labelframe, text='Pixels')
    L1.pack()
    L2 = Label(labelframe, text='HORIZONTAL--:>')
    L2.place(x=0, y=30)
    e1 = Entry(labelframe, width=15)
    e1.place(x=100, y=30)
    L3 = Label(labelframe, text='   VERTICAL  ---:>')
    L3.place(x=0, y=60)
    e2 = Entry(labelframe, width=15)
    e2.place(x=100, y=60)
    b1 = Button(labelframe, text='OK', width=5, command=ok)
    b1.place(x=100, y=100)
    b2 = Button(labelframe, text='Cancel', command=cancel)
    b2.place(x=150, y=100)


def zoomin():
    global a, b
    xamount = 0.9
    yamount = 0.9
    i1 = xamount * a
    i1 = float(i1)
    i2 = yamount * b
    i2 = float(i2)
    while a != 6 and b != 6:
        m = c.scale(ALL, 200, 200, i1, i2)
        c.configure(m, width=width * a, height=height * b)
        show = Label(root, width=30, height=2, bg='grey', fg='white', font=('Times New Roman', 12))
        show.place(x=0, y=700, anchor=SW)
        show.configure(text='                                               ' \
                            'ZOOM IN --:>' + 'X:' + str(i1) + '       ' + 'Y:' + str(i2))
        show.update()
        break
    root.after(1000, show.place_forget())
    a = a + 1
    b = b + 1
    if a == 0 and b == 0:
        a = b = 0


def zoomout():
    global a, b
    xamount = 1.1
    yamount = 1.1
    i1 = xamount / a
    i1 = float(i1)
    i2 = yamount / b
    i2 = float(i2)
    while a != 5 and b != 5:
        m = c.scale(ALL, 200, 200, i1, i2)
        c.configure(m, width=(width / xamount), height=(height / yamount))
        show = Label(root, width=30, height=2, bg='grey', fg='white', font=('Times New Roman', 12))
        show.place(x=0, y=700, anchor=SW)
        show.configure(text='                                               ' \
                            'ZOOM OUT --:>' + 'X:' + str(i1) + '       ' + 'Y:' + str(i2))
        show.update()
        break
    a = a + 1
    b = b + 1
    if a == 0 and b == 0:
        a = b = 0


def win_reset():
    m = c.scale(ALL, 0, 0, 1, 1)
    c.configure(m, width=1000, height=500)


def fill():
    global X, Y, a, b
    xamount = 5.5
    yamount = 5.5
    i1 = xamount * a
    i1 = float(i1)
    i2 = yamount * b
    i2 = float(i2)
    while a != 6 and b != 6:
        m = c.scale(ALL, 200, 200, i1, i2)
        try:
            c.configure(m, width=X / 2 * 2000, height=Y / i2 * 2000)
        except:
            a = a + 1
            b = b + 1
    c.configure(bg=color_bg)


def magnify():
    global X, Y, a, b
    xamount = 5.5
    yamount = 5.5
    i1 = xamount * a
    i1 = float(i1)
    i2 = yamount * b
    i2 = float(i2)
    while a != 6 and b != 6:
        m = c.scale(ALL, 200, 200, i1, i2)
        try:
            c.configure(m, width=X / 2 * 2000, height=Y / i2 * 2000)
        except:
            a = a + 1
            b = b + 1
            if a == 0 and b == 0:
                a = b = 0
        break


def bg_color():
    global color_bg
    try:
        color_bg = colorchooser.askcolor(color=color_bg)[1]
    except:
        print('')


def fg_color():
    global color_fg
    try:
        color_fg = colorchooser.askcolor(color=color_fg)[1]
        c['fg'] = color_fg
    except:
        print('')

#-----------------------------------------------------------------------------
def circle():
    c.bind('<1>',select_circle)
    c.bind('<Shift-1>', make_circle)

    selected = None


def make_circle( event):
    radius=int(v1.get())
    x, y, r = event.x, event.y, radius
    c.create_oval(x - r, y - r, x + r, y + r, outline='black', fill=color_bg)


def select_circle(self, event):
    self.canvas.bind('<Motion>', self.move_circle)
    self.canvas.bind('<ButtonRelease-1>', self.deselect)

    self.canvas.addtag_withtag('selected',CURRENT)


def move_circle(self, event):
    x, y, r = event.x, event.y, self.radius
    self.canvas.coords('selected', x - r, y - r, x + r, y + r)


def deselect(self, event):
    self.canvas.dtag('selected')  # removes the 'selected' tag
    self.canvas.unbind('<Motion>')
    self.canvas.bind('<Shift-1>', self.make_circle)

#-------------------------------------------------------------------------------------
def rect():
    c.bind('<1>', select_rect)
    c.bind('<Shift-1>', make_rect)

    selected = None


def make_rect(event):
    width= int(v1.get())
    x, y, w = event.x, event.y, width
    c.create_rectangle(x+w, y+w, (x*w)/x,(y*w)/y, outline='black', fill=color_bg)


def select_rect(event):
    c.bind('<Motion>', move_rect)
    c.bind('<ButtonRelease-1>',deselect)
    c.addtag_withtag('selected', CURRENT)


def move_rect(event):
    width = int(v1.get())
    x, y, w = event.x, event.y, width
    c.coords('selected', x - w, y - w, x - w, y - w)


def deselect(event):
    c.dtag('selected')  # removes the 'selected' tag
    c.unbind('<Motion>')
    c.bind('<Shift-1>', make_rect)

# ----------------------------------------------------------------------------
def square():
    c.bind('<1>', select_square)
    c.bind('<Shift-1>', make_square)

    selected = None


def make_square(event):
    side = int(v1.get())
    x, y, r = event.x, event.y,side
    c.create_rectangle(x - r, y - r, x + r, y + r, outline='black', fill=color_bg)


def select_square(event):
    c.bind('<Motion>', move_square)
    c.bind('<ButtonRelease-1>', deselect)
    c.addtag_withtag('selected', CURRENT)


def move_square(event):
    side = int(v1.get())
    x, y, r = event.x, event.y, side
    c.coords('selected', x - r, y - r, x + r, y + r)


def deselect(event):
    c.dtag('selected')  # removes the 'selected' tag
    c.unbind('<Motion>')
    c.bind('<Shift-1>', make_square)
# ------------------------------------------------------------------------------------------------
def vert_line():
    c.bind('<1>', select_vert_line)
    c.bind('<Shift-1>', make_vert_line)

    selected = None


def make_vert_line(event):
    width= int(v1.get())
    x, y, w = event.x, event.y, width
    c.create_rectangle(x+w, y+w, x+w,60,  fill=color_bg)


def select_vert_line(event):
    c.bind('<Motion>', move_line)
    c.bind('<ButtonRelease-1>',deselect)
    c.addtag_withtag('selected', CURRENT)


def move_vert_line(event):
    width = int(v1.get())
    x, y, w = event.x, event.y, width
    c.coords('selected', x - w, y - w, x - w, y - w)


def deselect(event):
    c.dtag('selected')  # removes the 'selected' tag
    c.unbind('<Motion>')
    c.bind('<Shift-1>', make_line)
# --------------------------------------------------------------------------------------
def line():
    c.bind('<1>', select_line)
    c.bind('<Shift-1>', make_line)

    selected = None


def make_line(event):
    width= int(v1.get())
    x, y, w = event.x, event.y, width
    c.create_line(x+w, y+w, 200, y+w,  fill=color_bg)


def select_line(event):
    c.bind('<Motion>', move_line)
    c.bind('<ButtonRelease-1>',deselect)
    c.addtag_withtag('selected', CURRENT)


def move_line(event):
    width = int(v1.get())
    x, y, w = event.x, event.y, width
    c.coords('selected', x - w, y - w, x - w, y - w)


def deselect(event):
    c.dtag('selected')  # removes the 'selected' tag
    c.unbind('<Motion>')
    c.bind('<Shift-1>', make_line)
#---------------------------------------------------------------------------------------------
def slash():
    c.bind('<1>', select_slash)
    c.bind('<Shift-1>', make_slash)

    selected = None


def make_slash(event):
    width= int(v1.get())
    x, y, w = event.x, event.y, width
    c.create_line(x+w, 10, 200, y+w,  fill=color_bg)


def select_slash(event):
    c.bind('<Motion>', move_slash)
    c.bind('<ButtonRelease-1>',deselect)
    c.addtag_withtag('selected', CURRENT)


def move_slash(event):
    width = int(v1.get())
    x, y, w = event.x, event.y, width
    c.coords('selected', x - w, y - w, x - w, y - w)


def deselect(event):
    c.dtag('selected')  # removes the 'selected' tag
    c.unbind('<Motion>')
    c.bind('<Shift-1>', make_line)
#------------------------------------------------------------------------------------
def dot_line():
    c.bind('<1>', select_dot_line)
    c.bind('<Shift-1>', make_dot_line)

    selected = None


def make_dot_line(event):
    width= int(v1.get())
    x, y, w = event.x, event.y, width
    c.create_line(x+w, y+w, x+w,60,dash = (5, 2),)
def select_dot_line(event):
    c.bind('<Motion>', move_line)
    c.bind('<ButtonRelease-1>',deselect)
    c.addtag_withtag('selected', CURRENT)


def move_dot_line(event):
    width = int(v1.get())
    x, y, w = event.x, event.y, width
    c.coords('selected', x - w, y - w, x - w, y - w)


def deselect(event):
    c.dtag('selected')  # removes the 'selected' tag
    c.unbind('<Motion>')
    c.bind('<Shift-1>', make_line)
# --------------------------------------------------------------------------------
def dash_hor():
    c.bind('<1>', select_dash_hor)
    c.bind('<Shift-1>', make_dash_hor)

    selected = None


def make_dash_hor(event):
    width= int(v1.get())
    x, y, w = event.x, event.y, width
    c.create_line(60, y+w, x+w,y+w,dash = (5, 2),)
def select_dash_hor(event):
    c.bind('<Motion>', move_line)
    c.bind('<ButtonRelease-1>',deselect)
    c.addtag_withtag('selected', CURRENT)


def move_dash_hor(event):
    width = int(v1.get())
    x, y, w = event.x, event.y, width
    c.coords('selected', x - w, y - w, x - w, y - w)


def deselect(event):
    c.dtag('selected')  # removes the 'selected' tag
    c.unbind('<Motion>')
    c.bind('<Shift-1>', make_line)
# ----------------------------------------------------------------------------------
def triangle1():
    c.bind('<1>', select_triangle1)
    c.bind('<Shift-1>', make_triangle1)

    selected = None


def make_triangle1(event):
    width= int(v1.get())
    x, y, w = event.x, event.y, width
    c.create_line((85, 55, 180, 180,85, 180, 85, 55),fill=color_bg,)
# 85, 55, 180, 180,85, 180, 25, 55
# 55, 85, 180, 85,180, 180, 55, 85
def select_triangle1(event):
    c.bind('<Motion>', move_triangle1)
    c.bind('<ButtonRelease-1>',deselect)
    c.addtag_withtag('selected', CURRENT)


def move_triangle1(event):
    width = int(v1.get())
    x, y, w = event.x, event.y, width
    c.coords('selected', x - w, y - w, x - w, y - w)


def deselect(event):
    c.dtag('selected')  # removes the 'selected' tag
    c.unbind('<Motion>')
    c.bind('<Shift-1>', make_line)
# ---------------------------------------------------------------------------------
def triangle2():
    c.bind('<1>', select_triangle2)
    c.bind('<Shift-1>', make_triangle2)

    selected = None


def make_triangle2(event):
    width= int(v1.get())
    x, y, w = event.x, event.y, width
    c.create_line((55, 85, 155, 85, 105, 180, 55, 85),fill=color_bg)
# 85, 55, 180, 180,85, 180, 25, 55
# 55, 85, 180, 85,180, 180, 55, 85
def select_triangle2(event):
    c.bind('<Motion>', move_triangle1)
    c.bind('<ButtonRelease-1>',deselect)
    c.addtag_withtag('selected', CURRENT)


def move_triangle2(event):
    width = int(v1.get())
    x, y, w = event.x, event.y, width
    c.coords('selected', x - w, y - w, x - w, y - w)


def deselect(event):
    c.dtag('selected')  # removes the 'selected' tag
    c.unbind('<Motion>')
    c.bind('<Shift-1>', make_line)


F = Frame(root, width=760, height=120, bg='black')
f1 = LabelFrame(F, text='TOOLS', width=250, height=117, bg='black',font=('Times New Roman',10),fg='light blue')
b1 = Button(f1, image=t1, command=text, width=32,bg='#90F5CC')
b1.place(x=5, y=0)
b2 = Button(f1, image=t2, command=pen, width=40,bg='#90F5CC')
b2.place(x=45, y=0)
b3 = Button(f1, image=t3, command=erase, width=40,bg='#90F5CC')
b3.place(x=93, y=0)
b4 = Button(f1, image=t4, command=clear, height=50,bg='#90F5CC')
b4.place(x=5, y=40)
b5 = Button(f1, image=t5, command=resize, width=55, height=90,bg='#90F5CC')
b5.place(x=140, y=0)
b6 = Button(f1, image=t6, command=fill, width=32,bg='#90F5CC' )
b6.place(x=203, y=0)
b7 = Button(f1, image=t7, command=magnify, width=32, height=50,bg='#90F5CC')
b7.place(x=203, y=40)
f1.place(x=10, y=0)

f2 = LabelFrame(F, text='ZOOM',font=('Times New Roman',10),fg='light blue' ,width=100, height=118,bg='black' )
b8 = Button(f2, image=t8, command=zoomin, width=32,bg='#90F5CC')
b8.place(x=5, y=0)
b9 = Button(f2, image=t9, command=zoomout, width=40,bg='#90F5CC')
b9.place(x=45, y=0)
b10 = Button(f2, image=t10, command=win_reset, width=83, height=50,bg='#90F5CC')
b10.place(x=5, y=40)
f2.place(x=275, y=0)

f3 = LabelFrame(F, text='COLOR', width=100, height=118,bg='black',font=('Times New Roman',10),fg='light blue')
b11 = Button(f3, image=t11, command=bg_color, width=35, height=90,bg='#F3F2B0')
b11.place(x=5, y=0)
b12 = Button(f3, image=t12, command=fg_color, width=35, height=90,bg='#F3F2B0')
b12.place(x=50, y=0)
f3.place(x=390, y=0)

f4 = LabelFrame(F, text='SHAPES', width=210, height=118, bg='black',font=('Times New Roman',10),fg='light blue')
b13 = Button(f4, image=t13, command=circle, width=32,bg='#FA9496')
b13.place(x=5, y=0)
b14 = Button(f4, image=t14, command=rect, width=32,bg='#FA9496')
b14.place(x=45, y=0)
b15 = Button(f4, image=t15, command=line, width=32,bg='#FA9496')
b15.place(x=85, y=0)
b16 = Button(f4, image=t16, command=square, width=32,bg='#FA9496')
b16.place(x=125, y=0)
b17 = Button(f4,image=t17,command=vert_line,width=32,bg='#FA9496')
b17.place(x=165,y=0)
b18 = Button(f4,image=t18,command=slash,width=32,bg='#FA9496')
b18.place(x=5,y=50)
b19 = Button(f4,image=t19,command=dot_line,width=32,bg='#FA9496')
b19.place(x=45,y=50)
b20 = Button(f4,image=t20,command=dash_hor,width=32,height=32,bg='#FA9496')
b20.place(x=85,y=50)
b21 = Button(f4,image=t21,command=triangle1,width=32,height=32,bg='#FA9496')
b21.place(x=125,y=50)
b22 = Button(f4,image=t22,command=triangle2,width=32,height=32,bg='#FA9496')
b22.place(x=165,y=50)
f4.place(x=500, y=0)

F.place(x=565, y=2)


def paint(e):
    global old_y, old_x
    if old_x and old_y:
        c.create_line(old_x, old_y, e.x, e.y, width=str(v1.get()), fill=color_fg, capstyle=ROUND)
    old_x = e.x
    old_y = e.y


def reset(e):
    global old_y, old_x
    old_y = None
    old_x = None


def text_1(event):
    T1 = event.x
    T2 = event.y
    t1 = Text(c, width=10, height=2)
    try:
        t1.place_configure(x=T1, y=T2)
        text()
    except:
        print('fs')


def erase_s(e):
    global old_y, old_x
    if old_x and old_y:
        c.create_line(old_x, old_y, e.x, e.y, width=str(v2.get()), fill='White', capstyle=ROUND)
    old_x = e.x
    old_y = e.y


def reset_s(e):
    global old_y, old_x
    old_y = None
    old_x = None


def fill_c(e):
    c['bg'] = color_bg
    c.configure(bg=color_bg)


def magni_1(e):
    global X, Y, a, b
    X = e.x
    Y = e.y




# --------------------------------------------------------------------------------


s1 = Scale(root, variable=v1, from_=-0.9, to=100,
           orient=VERTICAL, sliderlength=10, length=51,bg='#90F5CC')
s1.place(x=622, y=58)

s2 = Scale(root, variable=v2, from_=1, to=100,
           orient=VERTICAL, sliderlength=10, length=51,bg='#90F5CC')
s2.place(x=670, y=58)
k1 = b2.bind('<B1-Motion>', paint)
k2 = b2.bind('<ButtonRelease-1>', reset)
e1 = b3.bind('<B3-Motion>', erase_s)
e2 = b3.bind('<ButtonRelease-3>', reset_s)
k = b1.bind('<Button-1>', text_1)
f1 = c.bind('<Button-1>', fill_c)
m1 = b7.bind('<Button-1>', magni_1)
k1=Label(root)
k1.pack()
mixer.init()
mixer.music.load("C:/Users/DEVANSH/Downloads/canvasly.mp3")

def animation():
    k1.configure(image=gif1)
    root.update()
    root.after(500, None)
    mixer.music.play()
    k1.configure(image=gif2)
    root.update()
    root.after(3500, k1.pack_forget())

animation()
root.mainloop()
