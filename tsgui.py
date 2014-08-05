# tsgui.py
#
# GUI for a solution to travelling salesman problem

from Tkinter import *
from Dialog import Dialog

#/////////////////////////////////////////////////////////////////////

class TSSWindowGui(Frame):

   def  __init__(self, parent=None):
      Frame.__init__(self, parent)
      self.pack()
      #self.createMenuBar()
      self.createGUI()
      self.master.title("Solution")
      self.master.iconname("self")
 
   def createMenuBar(self):
      self.menubar = Frame(self, relief=RAISED, bd=2)
      self.menubar.pack(side=TOP, fill=X)

      #----- menu "File"
      mbutton = Menubutton(self.menubar, text='File', underline=0)
      mbutton.pack(side=LEFT)
      menu = Menu(mbutton, tearoff=N)
      menu.add_command(label='New', command=self.New_pressed)
      menu.add_command(label='Open...', command=self.Open_pressed)
      menu.add_command(label='Save', command=self.Save_pressed)
      menu.add_command(label='Save as...', command=self.SaveAs_pressed)
      menu.add_command(label='Exit', command=self.Exit_pressed)
      mbutton['menu'] = menu

      #----- menu "Edit"
      mbutton = Menubutton(self.menubar, text='Edit', underline=0)
      mbutton.pack(side=LEFT)
      menu = Menu(mbutton, tearoff=N)
      menu.add_command(label='Copy', command=self.Copy_pressed)
      menu.add_command(label='Cut', command=self.Cut_pressed)
      menu.add_command(label='Paste', command=self.Paste_pressed)
      mbutton['menu'] = menu

      #----- menu "Help"
      mbutton = Menubutton(self.menubar, text='Help', underline=0)
      mbutton.pack(side=LEFT)
      menu = Menu(mbutton, tearoff=N)
      menu.add_command(label='About...', command=self.About_pressed)
      menu.add_command(label='Getting started', command=self.GettingStarted_pressed)
      menu.add_command(label='Reference manual', command=self.Reference_pressed)
      mbutton['menu'] = menu

   def createGUI(self):
      par_colLayout1 = Frame(self)
      par_rowLayout2 = Frame(par_colLayout1, bd=4, relief=RIDGE, bg='#44ccff')
      self.label3 = par_label3 = Label(par_rowLayout2, text="At the top!")
      par_label3.pack(side=LEFT, anchor=NW)
      #par_button4 = Button(par_rowLayout2, text="press me")
      #par_button4.pack(side=LEFT, anchor=NW)
      #par_button5 = Button(par_rowLayout2, text="and me")
      #par_button5.pack(side=LEFT, anchor=NW)
      par_rowLayout2.pack(side=TOP, anchor=NW)
      
      self.canvas = c = Canvas(par_colLayout1, height=300, 
         width=300, bg='#ffffff')
      c.pack(side=TOP, anchor=NW) 
      
      par_colLayout1.pack(side=TOP, anchor=NW)

#***** methods to be redefined

   def New_pressed(self):
      print '[MyWindow New_pressed]'      

   def Open_pressed(self):
      print '[MyWindow Open_pressed]'      

   def Save_pressed(self):
      print '[MyWindow Save_pressed]'      

   def SaveAs_pressed(self):
      print '[MyWindow SaveAs_pressed]'      

   def Exit_pressed(self):
      print '[MyWindow Exit_pressed]'      

   def Copy_pressed(self):
      print '[MyWindow Copy_pressed]'      

   def Cut_pressed(self):
      print '[MyWindow Cut_pressed]'      

   def Paste_pressed(self):
      print '[MyWindow Paste_pressed]'      

   def About_pressed(self):
      print '[MyWindow About_pressed]'      

   def GettingStarted_pressed(self):
      print '[MyWindow GettingStarted_pressed]'      

   def Reference_pressed(self):
      print '[MyWindow Reference_pressed]'      

#***** end of methods to be redefined

#/////////////////////////////////////////////////////////////////////

if __name__=='__main__':
   TSSWindowGui().mainloop()

#/////////////////////////////////////////////////////////////////////

#(end genetic.py)
