from tkinter import *

class MainApplication(Tk):
    def __init__(self, tanga, *args, **kwargs):
        Tk.__init__(self, *args, *kwargs)
        print(tanga)
        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (mainPage, secondPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.showFrame(mainPage)

    def showFrame(self, container):
        frame = self.frames[container]
        frame.tkraise()

class mainPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Label(self, text="GAGO", font=20).pack(padx=10, pady=10)
        button = Button(self, text="Fuckers", command=lambda: controller.showFrame(secondPage))
        button.pack()

        button2 = Button(self, text="ADD", command=self.doNothing)
        button2.pack()

    def doNothing(self):
        print("NOTHING")

class secondPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Label(self, text="POTA", font=20).pack(padx=10, pady=10)
        button = Button(self, text="gago", command=lambda: controller.showFrame(mainPage))
        button.pack()

tanga = "tanga"
app = MainApplication(tanga)
app.mainloop()