###################################
from tkinter import * 
from PIL import Image, ImageTk ############### Import lib
import os                      ###############
import tkinter.messagebox
###################################

# config 
root = Tk() # root = tkinter()
root.geometry("600x500") # resize windows 600x500
root.title("Nvidia Installler") # title text program


root.resizable(width=False, height=False) #  not resize windows

######################################

def Cilck_exit(): # Funtion exit gui
	root.destroy()

def Cilck_next(): # Funtion exit gui and run hander.py
	root.destroy()
	os.system("python3 hander.py")
#####################################


#########################################  Backgournd image

img  = Image.open("n2.png") 

resize_image = img.resize((1000, 500)) # resize img to 600x500
#  ....
photo=ImageTk.PhotoImage(resize_image) # set resize
# show img in programe
lab=Label(image=photo) .pack()  # run image and iamge to center

##########################################
#           NVIDIA ISNTALLER V.2         #
##########################################

logo_img = Image.open("logo.png")
resize_logo = logo_img.resize((50, 50))  # Adjust size as needed
logo_photo = ImageTk.PhotoImage(resize_logo)
logo_label = Label(root, image=logo_photo)
logo_label.place(x=520, y=10)  # Adjust position as needed


#####################################################33
button_img = Image.open("next1.png")
resize_button_img = button_img.resize((150, 45))
button_photo = ImageTk.PhotoImage(resize_button_img)
######################################################

############################################ create frame gui
frame = Frame(root, bd=2, relief="groove")
frame.place(x=80, y=110)
#############################################

####################################################################################################  header text 
Head = Label(root,text="NVIDIA Graphics Driver",fg="green",font=("Helvetica", 12)) .place(x=5,y=5)    
lowHead = Label(root,text="Version Arch Linux ",fg="green",font=("Helvetica", 12)) .place(x=5,y=30)
####################################################################################################

############################################################################################################################################
TextFrame = Label(frame, text="Install NVIDIA Graphics Driver", fg="green", font=("Helvetica", 12)) # TEXT in frame 
TextFrame.pack(padx=30,pady=40)
TextFrame1 = Label(frame, text="Create By Nxz02 For Project Begin GUI Python \nFor Arch Linux for Version 340xx 390xx 470xx 525xx 535xx")
TextFrame1.pack(padx=30,pady=40)

#create_button = Button(root,text="HELLO") .place(x=90,y=60)
create_button = Button(root, image=button_photo,command=Cilck_next) .place(x=400,y=400) # Button next gui
create_exit = Button(root,text="EXIT",command=Cilck_exit) .place(x=300,y=425) # buuton exit gui

############################################################################################################################################


# end
root.mainloop()
#


############################# Help !

#  Run in Terminal {}
#  python3 Nvidiainstaller.py

#############################3