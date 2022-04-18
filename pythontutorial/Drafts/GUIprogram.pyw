from tkinter import *


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        Label(self, text="Choose your favorite movie types").grid(row=0, column=0, sticky=W)
        Label(self, text="Select all that apply:").grid(row=1, column=0, sticky=W)

        self.likeComedy = BooleanVar()
        self.likeDrama = BooleanVar()
        self.likeRomantic = BooleanVar()
        Checkbutton (self, text="Comedy", variable=self.likeComedy, command=self.updateText).grid(row=2, column=0, sticky=W)
        Checkbutton (self, text="Drama", variable=self.likeDrama, command=self.updateText).grid(row=3, column=0, sticky=W)
        Checkbutton (self, text="Romantic", variable=self.likeRomantic, command=self.updateText).grid(row=4, column=0, sticky=W)

        self.resultTxt = Text(self, width=40, height=5, wrap=WORD)
        self.resultTxt.grid(row=5, column=0, columnspan=3)

    def updateText(self):
        likes = ""

        if self.likeComedy.get():
            likes += "You like comedic movies!\n"

        if self.likeDrama.get():
            likes += "You like dramatic movies!\n"

        if self.likeRomantic.get():
            likes += "You like romantic movies!\n"

        self.resultTxt.delete(0.0, END)
        self.resultTxt.insert(0.0, likes)



root = Tk()
root.title("My Simple GUI")
root.geometry("300x200")

mainFrame = App(root)

root.mainloop()