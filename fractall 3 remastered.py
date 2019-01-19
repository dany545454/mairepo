from tkinter import *
from tkinter import Menu
import pygame, math
import os
res1 = 6
res2 = 23
res3 = 8
def rerun():
    window1 = Tk()
    window1.title("Fractal tree")
    window1.geometry('400x400')
    def res():
        window2 = Tk()
        window2.title("Resolution")
        window2.geometry('350x200')
    def clicked():
        pygame.init()
        window = pygame.display.set_mode((1530, 790))
        pygame.display.set_caption("Fractal Tree")
        screen = pygame.display.get_surface()
        #----------------------------------------------------
        def drawTree(x1, y1, angle, res3):
            if res3:
                x2 = x1 + int(math.cos(math.radians(angle)) * res3 * res1)
                y2 = y1 + int(math.sin(math.radians(angle)) * res3 * res1)
                pygame.draw.line(screen, (255,255,255), (x1, y1), (x2, y2), 2)
                drawTree(x2, y2, angle - res2, res3 - 1)
                drawTree(x2, y2, angle + res2, res3 - 1)
        #----------------------------------------------------
        def input(event):
            if event.type == pygame.QUIT:
                exit(0)
                sys.exit()
        #----------------------------------------------------
        drawTree(764, 790, -90, res3)
        pygame.display.flip()
        #----------------------------------------------------
        while True:
            input(pygame.event.wait())
    #---------------------------------------------
    def abt():
        window1.destroy()
        abilities = Tk()
        abilities.title("Abilities")
        abilities.geometry('350x200')
        #---------------------------------------------------
        lbl = Label(abilities, text="How big:")
        lbl.grid(column=0, row=0)
        #---------------------------------------------------
        lbl = Label(abilities, text="Angle:")
        lbl.grid(column=0, row=1)
        #---------------------------------------------------
        lbl = Label(abilities, text="Branches:")
        lbl.grid(column=0, row=2)
        #---------------------------------------------------
        lbl = Label(abilities, text="preferably 9")
        lbl.grid(column=2, row=0)
        #---------------------------------------------------
        lbl = Label(abilities, text="preferably 20")
        lbl.grid(column=2, row=1)
        #---------------------------------------------------
        txt = Entry(abilities,width=10)
        txt2 = Entry(abilities,width=10)
        txt3 = Entry(abilities,width=10)
        #---------------------------------------------------
        txt.grid(column=1, row=0)
        txt2.grid(column=1, row=1)
        txt3.grid(column=1, row=2)
        #---------------------------------------------------
        def fkinfunctions2():
            res1 =int(txt.get())
            res2 =int(txt2.get())
            res3 =int(txt3.get())
            print (res1)
            print (res2)
            print (res3)
            clicked()
            abilities.destroy()
        btn = Button(abilities, text="Back!", command=fkinfunctions2)
        btn.grid(column=0, row=5)
        abilities.mainloop()
        #---------------------------------------------------
    #btn2 = Button(window1, text="Run", command=clicked1)
    #btn2.grid(column=0, row=3)
        abilities.mainloop()
        #---------------------------------------------------
    main_menu = Menu(window1, tearoff=0)
    main_menu.add_command(label="Abt", command=abt)
    main_menu.add_command(label="Res", command=res)
    main_menu.add_command(label="Quit", command=window1.destroy)
    window1.config(menu=main_menu)
    #---------------------------------------------
    btn = Button(window1, text="Create tree", command=clicked)
    btn.grid(column=0, row=0)
    window1.mainloop()
    #---------------------------------------------
rerun()
        
