from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.title("HTML Editor v 1.0 by ModernShrub")
root.minsize(650,650)

openimg = ImageTk.PhotoImage(Image.open("open.png"))
saveimg = ImageTk.PhotoImage(Image.open("save.png"))
runimg = ImageTk.PhotoImage(Image.open("run.png"))

labelfilename = Label(root, text="Filename")
labelfilename.place(relx=0.28,rely=0.03,anchor=CENTER)

inputfilename = Entry(root)
inputfilename.place(relx=0.46, rely=0.03,anchor=CENTER)

textspace = Text(root,height=35,width=80, bg="gray13", fg="white")
textspace.place(relx=0.5,rely=0.55,anchor=CENTER)

def openfile():
    global name
    textspace.delete(1.0, END)
    inputfilename.delete(0,END)
    htmfile = filedialog.askopenfilename(title="Open File",
                                         filetypes=(("HTML Files", "*.html *.htm"),))
    
    print(htmfile)
    name=os.path.basename(htmfile)
    formattedname=name.split('.')[0]
    inputfilename.insert(END,formattedname)
    root.title(formattedname)
    htmfile =open(name,'r')
    para=htmfile.read()
    textspace.insert(END,para)
    htmfile.close()

openbtn = Button(root, image=openimg, text="Open File",command=openfile)
openbtn.place(relx=0.05,rely=0.03,anchor=CENTER)
save_button=Button(root, image=saveimg,text="Save File")
save_button.place(relx=0.11,rely=0.03,anchor= CENTER)
run_button=Button(root,image=runimg,text="Run File")
run_button.place(relx=0.17,rely=0.03,anchor= CENTER)


root.mainloop()