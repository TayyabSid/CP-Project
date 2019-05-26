import contextlib
with contextlib.redirect_stdout(None):
    from pygame import mixer
    import time
    
import tkinter
from tkinter import *



def fetch():
    return (hour.get(),minute.get(),second.get(),task.get())
def sound():
	mixer.init()
	mixer.music.load("D:\marimba.mp3")

def alarm(hor,minn,secn,task):
        zone = v.get()
        n = 5
        print("Alarm is set for "+str(hor)+"H-"+str(minn)+"M-"+str(secn)+"S")
        
        if zone == 1:
	
            while True:
                    if(time.localtime().tm_hour==int(hor) and time.localtime().tm_min==int(minn) and time.localtime().tm_sec==int(secn)):
                            print("Time for your task ("+task+") ")
                            break
            sound()
            while(n>0):
                    mixer.music.play()
                    time.sleep(1)
                    n=n-1

            #exit()
        elif zone == 2:
            while True:
                    if((time.localtime().tm_hour-12)==int(hor) and time.localtime().tm_min==int(minn) and time.localtime().tm_sec==int(secn)):
                            print("Time for your task ("+task+") ")
                            break
            sound()
            while(n>0):
                    mixer.music.play()
                    time.sleep(1)
                    n=n-1
            #exit()
        


def click():
    data = fetch()
    alarm(data[0],data[1],data[2],data[3])

def stop():
    exit()



root = Tk()

root.title('ReminderBot')

Label(text='Name of your task').pack(side=TOP,padx=10,pady=10)

task = Entry(root, width=10)
task.pack(side=TOP,padx=10,pady=10)

Label(text='Hour').pack(side=TOP,padx=10,pady=10)

hour = Entry(root, width=10)
hour.pack(side=TOP,padx=10,pady=10)

Label(text='Minute').pack(side=TOP,padx=10,pady=10)

minute = Entry(root, width=10)
minute.pack(side=TOP,padx=10,pady=10)

Label(text='Second').pack(side=TOP,padx=10,pady=10)

second = Entry(root, width=10)
second.pack(side=TOP,padx=10,pady=10)

v = IntVar()

Label(root, 
        text="""Choose a 
timezone:""",
        justify = LEFT,
        padx = 20).pack()
Radiobutton(root, 
              text="AM",
              padx = 20, 
              variable=v, 
              value=1).pack(anchor=W)
Radiobutton(root, 
              text="PM",
              padx = 20, 
              variable=v, 
              value=2).pack(anchor=W)



Button(root, text='Set', command=click).pack(side=LEFT)
Button(root, text='Exit', command=click).pack(side=RIGHT)

root.mainloop()
