#################################
from tkinter import *
from PIL import Image, ImageTk # import lib 
import os
import tkinter.messagebox
################################

# config 
root = Tk()
# size windows
root.geometry("600x500")

# title
root.title("Nvidia Installler")

#  not resize windows
root.resizable(width=False, height=False)

################## # Funtion exit gui

def Cilck_exit():
	root.destroy()

####################
############### Backgournd image

img  = Image.open("n2.png") 
# resize img to 600x500
resize_image = img.resize((1000, 500))
#  ....
photo=ImageTk.PhotoImage(resize_image)
# show img in programe
lab=Label(image=photo) .pack()  # center 

############################
def install_pass():
    tkinter.messagebox.showinfo("Message","Install Finish \nreboot you computer ")
############################

logo_img = Image.open("logo.png")
resize_logo = logo_img.resize((50, 50))  # Adjust size as needed
logo_photo = ImageTk.PhotoImage(resize_logo)
logo_label = Label(root, image=logo_photo)
logo_label.place(x=520, y=10)  # Adjust position as needed


#######################################################
button_img = Image.open("next1.png")
resize_button_img = button_img.resize((150, 45))
button_photo = ImageTk.PhotoImage(resize_button_img)
###########################3#########################


########################################### create frame gui
frame = Frame(root, bd=2, relief="groove")
frame.place(x=80, y=110)
############################################

Head = Label(root,text="NVIDIA Graphics Driver",fg="green",font=("Helvetica", 12)) .place(x=5,y=5)
lowHead = Label(root,text="Version Arch Linux",fg="green",font=("Helvetica", 12)) .place(x=5,y=30)

TextFrame = Label(frame, text="LIST NVIDIA Graphics Driver", fg="green", font=("Helvetica", 12))
TextFrame.pack(padx=30,pady=40)

TextFrame1 = Label(frame, text="            ", fg="green", font=("Helvetica", 12))
TextFrame1.pack(padx=30,pady=80)

#create_button = Button(root,text="HELLO") .place(x=90,y=60)
#create_button = Button(root, image=button_photo) .place(x=400,y=400)
#create_exit = Button(root,text="EXIT",command=Cilck_exit) .place(x=300,y=425)


def show(): # funtion choice nvidia driver 
    r = brave.get()
    if r == 1:
        root.destroy()
        os.system("sudo pacman -S base-devel linux-headers git nano --needed --noconfirm")
        os.system("yay -S nvidia-340xx-dkms nvidia-340xx-utils lib32-nvidia-340xx-utils nvidia-settings --noconfirm")
        os.system("clear;echo reboot you computer;echo ")
        install_pass()
    elif r == 2:
        root.destroy()
        os.system("sudo pacman -S base-devel linux-headers git nano --needed --noconfirm")
        os.system("yay -S nvidia-390xx-dkms nvidia-390xx-utils lib32-nvidia-390xx-utils nvidia-settings --noconfirm")
        os.system("clear;echo reboot you computer;echo ")
        install_pass()
        
    elif r == 3:
        root.destroy()
        os.system("sudo pacman -S git")
        os.system("sudo pacman -S base-devel linux-headers git nano --needed --noconfirm")
        os.system("yay -S nvidia-470xx-dkms nvidia-470xx-utils lib32-nvidia-470xx-utils nvidia-settings --noconfirm")
        os.system("clear;echo reboot you computer;echo ")
        install_pass()
    elif r == 4:
        root.destroy()
        os.system("sudo pacman -S base-devel linux-headers git nano --needed --noconfirm")
        os.system("yay -S nvidia-525xx-dkms nvidia-525xx-utils lib32-nvidia-525xx-utils nvidia-settings --noconfirm")
        os.system("clear;echo reboot you computer;echo ")
        install_pass()
    elif r == 5:
        root.destroy()
        os.system("sudo pacman -S base-devel linux-headers git nano --needed --noconfirm")
        os.system("yay -S nvidia-535xx-dkms nvidia-535xx-utils lib32-nvidia-535xx-utils nvidia-settings --noconfirm")
        os.system("clear;echo reboot you computer;echo ")
        install_pass()
    else:
        exit()



brave = IntVar()

xin = 90 # x = 90


############################################ NXZ02 ###############################################
 #                                  
 #                                * NVIDIA GRAPHICS DRIVER   * 
 #
##################################################################################################
Radiobutton(text="Driver version : 340xx",variable=brave,value=1,command=show) .place(x=xin,y=200) # choice 1
Radiobutton(text="Driver version : 390xx",variable=brave,value=2,command=show) .place(x=xin,y=230) # choice 2
Radiobutton(text="Driver version : 470xx",variable=brave,value=3,command=show) .place(x=xin,y=260) # choice 3
Radiobutton(text="Driver version : 525xx",variable=brave,value=4,command=show) .place(x=xin,y=290) # choice 4
Radiobutton(text="Driver version : 535xx",variable=brave,value=5,command=show) .place(x=xin,y=320) # choice 5
##################################################################################################

##########################################   END #################################################




root.mainloop()