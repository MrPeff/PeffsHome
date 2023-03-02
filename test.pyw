
from tkinter import * # import all tkinter widget classes
import random
import threading

class MyWindow(Frame): # new class 'Window' inherits from tkinter class 'Frame'
   def __init__(self, parent): # define inherited-class window constructor
       Frame.__init__(self,parent,background="beige")
       self.parent=parent
       self.Interface()

   def Interface(self):
       self.parent.title("Button Test")
       self.pack(fill=BOTH,expand=1)
       lbl01=Label(self,
           text="Click either the green or blue button.",
           foreground="blue",background="beige")
       lbl01.place(x=10,y=10)
       exitbutton=Button(self,
           text="Exit Program",foreground="blue",background="red", command=self.quit)
       exitbutton.place(x=150,y=120)
       GetNumberBtn=Button(self,
           text="GetNumber",foreground="purple",background="green",
           command=self.GetNumberBtn)
       GetNumberBtn.place(x=10,y=40)
       blubtn=Button(self,
           text="BLUE",foreground="yellow",background="blue", command=self.blubtn)
       blubtn.place(x=10,y=80)
       clrlbls=Button(self, text="Reset",command=self.clrlbls)
       clrlbls.place(x=10, y=120)

   def clrlbls(self):
       print("You clicked the Reset button.")
       lbl02=Label(self, text="          ", background="beige")
       lbl02.place(x=80,y=40)
       lbl03=Label(self, text="          ", background="beige")
       lbl03.place(x=80,y=80)

   def GetNumberBtn(self):
       print("Thank you for clicking the GREEN button.")
       self.GetNumber()
       NumberStr = str(self.Number)
       lbl02=Label(self, text=NumberStr, foreground="blue",background="beige")
       lbl02.place(x=80,y=40)
       t = threading.Timer(5.0, self.ResetNumberText)
       t.start()

   def ResetNumberText(self):
       lbl02=Label(self, text="                  ",
           foreground="blue",background="beige")
       lbl02.place(x=80,y=40)

   def blubtn(self):
       print("Thank you for clicking the BLUE button.")
       lbl03=Label(self, text="You clicked the blue button.",
           foreground="blue",background="beige")
       lbl03.place(x=80,y=80)

   def GetNumber(self):
       self.Number = random.randint(100000,999999)

def main():
   root=Tk()
   root.geometry("275x160+500+300") # width, height, and x and y
   app=MyWindow(root)               # coordinates for window position
   root.mainloop() # wait for user to press a button
   root.destroy() # on exit, close window, but not IDE
if __name__=='__main__':
   main() # call main program
