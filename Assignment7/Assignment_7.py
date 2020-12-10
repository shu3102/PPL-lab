from tkinter import *
from tkinter import ttk, colorchooser

class main:
    left_button = "up"
    x_position = None
    y_position = None
    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None 
    
    def __init__(self,master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.penwidth = 5
        self.drawWidgets()
        self.c.bind("<Motion>", self.motion)
        self.c.bind("<ButtonPress-1>", self.left_button_down)
        self.c.bind("<ButtonRelease-1>", self.left_button_up)
        self.drawing_tool = "pencil"

    def set_line_drawing_tool(self):
        self.drawing_tool = "line"

    def set_pencil_drawing_tool(self):
        self.drawing_tool = "pencil"
    
    def set_arc_drawing_tool(self):
        self.drawing_tool = "arc"
    
    def set_rectangle_drawing_tool(self):
        self.drawing_tool = "rectangle"
        
    def set_oval_drawing_tool(self):
        self.drawing_tool = "oval"
        
    def set_text_drawing_tool(self):
        self.drawing_tool = "oval"
        
    def left_button_down(self, event=None):
        self.left_button = "down"
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y
        
    def left_button_up(self, event=None):
        self.left_button = "up"
        self.x_position = None
        self.y_position = None
        
        self.x2_line_pt = event.x
        self.y2_line_pt = event.y
        
        if self.drawing_tool=="line":
            self.line_draw(event)
        if self.drawing_tool=="pencil":
            self.pencil_draw(event)
        if self.drawing_tool=="arc":
            self.arc_draw(event)
        if self.drawing_tool=="oval":
            self.oval_draw(event)
        if self.drawing_tool=="rectangle":
            self.rect_draw(event)
        if self.drawing_tool=="text":
            self.text_draw(event)
            
    def motion(self, event=None):
        if self.drawing_tool=="pencil":
            self.pencil_draw(event)
            
        self.x_position = event.x
        self.y_position = event.y
        
    def pencil_draw(self, event=None):
        if self.left_button =="down":
            if self.x_position is not None and self.y_position is not None:
                self.c.create_line(self.x_position, self.y_position, event.x, event.y, smooth=True, fill = self.color_fg, width = self.penwidth)
                
    def line_draw(self, event=None):
        if  None not in (self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):
            self.c.create_line(self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt, smooth=True, fill = self.color_fg, width = self.penwidth)
            
    def arc_draw(self, event=None):
        if  None not in (self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):
            coords = self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt
            
            self.c.create_arc(coords, start=0, extent=150, style=ARC, fill = self.color_fg, width = self.penwidth)
            
    def oval_draw(self, event=None):
        if  None not in (self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):
            self.c.create_oval(self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt,outline = self.color_fg, width = self.penwidth)
            
    def rect_draw(self, event=None):
        if  None not in (self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):
            self.c.create_rectangle(self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt,outline = self.color_fg, width = self.penwidth)
            self.c.create_text(self.x1_line_pt, self.y1_line_pt, fill="lightblue", font=text_font, text="helloooo!")
    

    def changeW(self,e): #change Width of pen through slider
        self.penwidth = e           

    def clear(self):
        self.c.delete(ALL)

    def change_fg(self):  #changing the pen color
        self.color_fg=colorchooser.askcolor(color=self.color_fg)[1]

    def change_bg(self):  #changing the background color canvas
        self.color_bg=colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg

    def drawWidgets(self):
        self.controls = Frame(self.master,padx = 5,pady = 5)
        Label(self.controls, text='Pen Width:',font=('arial 18')).grid(row=0,column=0)
        self.slider = ttk.Scale(self.controls,from_= 5, to = 100,command=self.changeW,orient=VERTICAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0,column=1,ipadx=30)
        self.controls.pack(side=LEFT)
        
        self.c = Canvas(self.master,width=500,height=400,bg=self.color_bg,)
        self.c.pack(fill=BOTH,expand=True)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu)
        colormenu = Menu(menu)
        toolsmenu = Menu(menu)
        menu.add_cascade(label='Colors',menu=colormenu)
        colormenu.add_command(label='Brush Color',command=self.change_fg)
        colormenu.add_command(label='Background Color',command=self.change_bg)
        optionmenu = Menu(menu)
        menu.add_cascade(label='Options',menu=optionmenu)
        optionmenu.add_command(label='Clear Canvas',command=self.clear)
        optionmenu.add_command(label='Exit',command=self.master.destroy) 
        menu.add_cascade(label='tools', menu=toolsmenu)
        toolsmenu.add_command(label='line', command= self.set_line_drawing_tool)
        toolsmenu.add_command(label='arc', command= self.set_arc_drawing_tool)
        toolsmenu.add_command(label='rectangle', command= self.set_rectangle_drawing_tool)
        toolsmenu.add_command(label='oval', command= self.set_oval_drawing_tool)
        toolsmenu.add_command(label='pencil', command= self.set_pencil_drawing_tool)
        


if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('Application')
    root.mainloop()