# main miter >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
''' 1 miter = 39.37007874 inchi
    1 foot = 12 inchi
    1 cm = 0.03280839895 inchi
    1 inchi = 1 inchi
'''

class Oupt:
    def __init__(miter, num, froms ,tos):
        miter.num = num
        miter.froms = froms
        miter.tos = tos

    def conv_cm(miter): # conv Froms to inch
        if miter.froms == 'meter':
            main_num = miter.num * 39.37007874
            return main_num
        if miter.froms == 'foot':
            main_num = miter.num * 12
            return main_num
        if miter.froms == 'cm':
            main_num = miter.num * 0.03280839895
            return main_num
        if miter.froms == 'inchi':
            main_num = miter.num * 1
            return main_num

    def conv_tos(miter, main_num): # comv inch to Tos
        if miter.tos == 'meter':
            oupts = main_num / 39.37007874
            return oupts
        if miter.tos == 'foot':
            oupts = main_num / 12
            return oupts
        if miter.tos == 'cm':
            oupts = main_num / 0.03280839895
            return oupts
        if miter.tos == 'inchi':
            oupts = main_num / 1
            return oupts
# main miter <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  


# making main window >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

from tkinter import * # importing module
from tkinter.ttk import Combobox

win = Tk() # making window 
# designimg window >>>>>
win.title('Meter')
win.geometry('700x300')
win.attributes('-topmost',1)
win.configure(bg='SkyBlue')
win.resizable(0,0)
# designing window <<<<
# making From text
from_label = Label(win, text='From', font=('Arial',20),bg='SkyBlue', fg='red')
from_label.place(x=120,y=60)
# making To text
from_label = Label(win, text='To', font=('Arial',20),bg='SkyBlue', fg='red')# From text 
from_label.place(x=400,y=60)
# making from combobox >>>>
from_combo = Combobox(win, height=20,width=30)
from_combo['values']=('Meter','Feet','Centimetre','Inch')
from_combo.current(1)# set the selected items
from_combo['state']='readonly'
from_combo.place(x=120,y=100)

# making to combobox >>>>
from_combo = Combobox(win, height=20,width=30)
from_combo['values']=('Meter','Feet','Centimetre','Inch')
from_combo.current(1)# set the selected items
from_combo['state']='readonly'
from_combo.place(x=400,y=100)

# making to combobox >>>>
from_combo = Combobox(win, height=20,width=30)
from_combo['values']=('Meter','Feet','Centimetre','Inch')
from_combo.current(1)# set the selected items
from_combo['state']='readonly'
from_combo.place(x=120,y=100)

win.mainloop() # window mainloop
# making main window <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<








