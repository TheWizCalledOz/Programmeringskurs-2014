import sys
import Tkinter
from Tkinter import *
root = Tk( )
labelfont = ('times', 50, 'italic')

widget= Label(root, text='SYNTHESIZER', font=labelfont)
widget.config(bg='black', fg='red')

widget.pack(expand=YES, fill=BOTH)
root.mainloop( )


