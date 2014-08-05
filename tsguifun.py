# tsimp.py
#
# functionality for GUI for travelling salesman problem

from Tkinter import *
from Dialog import Dialog

from tsgui import TSSWindowGui
import ts


#/////////////////////////////////////////////////////////////////////

def scale(x):
   return 5 + x*2.9

class TSSGuiFun(TSSWindowGui):

   def  __init__(self, parent=None):
      TSSWindowGui.__init__(self, parent)
      self.pack()

   def writeSolution(self, tss):
      l = self.label3
      l.config(text=tss.__str__())
   
      c = self.canvas
        
      #draw something on it:
      oldCoords = None
      for letter in tss.solution:
         coords = tss.getCoords(letter)
         x = coords[0]
         y = coords[1]
         xs = 5 + x*2.9
         ys = 5 + y*2.9
         c.create_oval(xs-4,ys-4,xs+4,ys+4)
         if oldCoords:
            #c.config(highlightcolor='#880000')
            c.create_line(xs, ys, oxs, oys, fill='#880000')
            
         c.create_text(xs+8, ys+8, text=letter, fill='#003388')
         oldCoords = coords
         oxs = xs
         oys = ys
            


#/////////////////////////////////////////////////////////////////////

#end
